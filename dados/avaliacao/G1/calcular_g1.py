#!/usr/bin/env python3
"""Cálculo das métricas do G1 (adequação funcional) a partir das planilhas de coleta.

Método: docs/fase-3/metodo-g1.md. Fórmulas e níveis: docs/fase-2/especificacao-das-metricas.md
e docs/fase-2/niveis-e-julgamento.md.

Só usa a biblioteca padrão do Python (3.9 ou superior). Lê os CSV com os nomes fixos definidos
no método, dentro de dados/avaliacao/G1/. Arquivo ausente faz a métrica (ou o tema) aparecer
como "não coletado"; nenhum valor é estimado.

Uso, a partir da raiz do repositório:

    python3 dados/avaliacao/G1/calcular_g1.py calcular
    python3 dados/avaliacao/G1/calcular_g1.py calcular --saida dados/avaliacao/G1/resultados.csv
    python3 dados/avaliacao/G1/calcular_g1.py ficha-cega --tema T1
    python3 dados/avaliacao/G1/calcular_g1.py ficha-cega --tema T1 --rodada 2
    python3 dados/avaliacao/G1/calcular_g1.py amostra --tema T1

A opção --pasta aponta para outra pasta com a mesma estrutura (usada para testar o script
fora do repositório).
"""

from __future__ import annotations

import argparse
import csv
import math
import random
import re
import sys
import unicodedata
from pathlib import Path

PASTA_PADRAO = Path(__file__).resolve().parent
TEMAS = ["T1", "T2", "T3", "T4"]
TEMAS_M141 = ["T1", "T2"]
SEMENTE_BASE = 20261114  # semente da ficha cega: SEMENTE_BASE + número do tema

# Níveis da Fase 2 (niveis-e-julgamento.md). Cada faixa inclui o limite inferior.
# Lista de (piso, nível) do maior para o menor; valores em proporção (0 a 1).
NIVEIS = {
    "M1.1.1": [(0.80, "Excelente"), (0.60, "Bom"), (0.40, "Aceitável")],
    "M1.1.2": [(0.90, "Excelente"), (0.70, "Bom"), (0.50, "Aceitável")],
    "M1.2.1": [(0.95, "Excelente"), (0.85, "Bom"), (0.70, "Aceitável")],
    "M1.3.1": [(0.85, "Excelente"), (0.70, "Bom"), (0.50, "Aceitável")],
    "M1.3.2": [(0.98, "Excelente"), (0.90, "Bom"), (0.80, "Aceitável")],
    "M1.4.1": [(0.70, "Excelente"), (0.50, "Bom"), (0.36, "Aceitável")],
    "M1.5.1": [(1.00, "Excelente"), (0.93, "Bom"), (0.80, "Aceitável")],
    "M1.5.2": [(0.85, "Excelente"), (0.70, "Bom"), (0.50, "Aceitável")],
}
KAPPA_MINIMO = 0.61


# ---------------------------------------------------------------- leitura e normalização

def ler_csv(caminho: Path) -> list[dict[str, str]] | None:
    """Lê um CSV com cabeçalho (vírgula ou ponto e vírgula). Devolve None se não existir."""
    if not caminho.exists():
        return None
    with caminho.open(encoding="utf-8-sig", newline="") as f:
        amostra = f.read(4096)
        f.seek(0)
        delimitador = ";" if amostra.count(";") > amostra.count(",") else ","
        leitor = csv.DictReader(f, delimiter=delimitador)
        linhas = []
        for linha in leitor:
            limpa = {(k or "").strip(): (v or "").strip() for k, v in linha.items()}
            if any(limpa.values()):
                linhas.append(limpa)
        return linhas


def sim(valor: str) -> bool:
    return normalizar_texto(valor) in {"sim", "s", "1", "true", "x"}


def normalizar_doi(doi: str) -> str:
    doi = (doi or "").strip().lower()
    doi = re.sub(r"^(https?://)?(dx\.)?doi\.org/", "", doi)
    doi = re.sub(r"^doi:\s*", "", doi)
    return doi.rstrip(".")


def normalizar_texto(texto: str) -> str:
    texto = unicodedata.normalize("NFKD", texto or "")
    texto = "".join(c for c in texto if not unicodedata.combining(c)).lower()
    texto = re.sub(r"[^a-z0-9]+", " ", texto)
    return texto.strip()


def chaves_artigo(linha: dict[str, str]) -> set[str]:
    """Chaves de identidade de um artigo: DOI, PMID e título normalizado com ano."""
    chaves = set()
    doi = normalizar_doi(linha.get("doi", ""))
    if doi:
        chaves.add("doi:" + doi)
    pmid = re.sub(r"\D", "", linha.get("pmid", ""))
    if pmid:
        chaves.add("pmid:" + pmid)
    titulo = normalizar_texto(linha.get("titulo", ""))
    ano = re.sub(r"\D", "", linha.get("ano", ""))[:4]
    if titulo:
        chaves.add(f"titulo:{titulo}|{ano}")
    return chaves


def mesmo_artigo(a: dict[str, str], b: dict[str, str]) -> bool:
    """Regra do método: mesmo DOI; sem DOI em um dos lados, mesmo PMID; sem os dois, título e ano."""
    doi_a, doi_b = normalizar_doi(a.get("doi", "")), normalizar_doi(b.get("doi", ""))
    if doi_a and doi_b:
        return doi_a == doi_b
    pm_a = re.sub(r"\D", "", a.get("pmid", ""))
    pm_b = re.sub(r"\D", "", b.get("pmid", ""))
    if pm_a and pm_b:
        return pm_a == pm_b
    ca = {c for c in chaves_artigo(a) if c.startswith("titulo:")}
    cb = {c for c in chaves_artigo(b) if c.startswith("titulo:")}
    return bool(ca & cb)


# ---------------------------------------------------------------- estatística

def cohen_kappa(r1: list[str], r2: list[str]) -> tuple[float | None, float]:
    """Kappa de Cohen para duas classificações nominais. Devolve (kappa, concordância bruta).

    Se a concordância esperada for 1 (os dois usaram uma única e mesma categoria), o kappa é
    indefinido e a função devolve None.
    """
    if len(r1) != len(r2) or not r1:
        raise ValueError("as duas classificações precisam ter o mesmo número de itens, maior que zero")
    n = len(r1)
    categorias = sorted(set(r1) | set(r2))
    po = sum(1 for a, b in zip(r1, r2) if a == b) / n
    pe = sum((r1.count(c) / n) * (r2.count(c) / n) for c in categorias)
    if math.isclose(pe, 1.0):
        return None, po
    return (po - pe) / (1 - pe), po


def postos(valores: list[float]) -> list[float]:
    """Postos com empate resolvido pela média dos postos (posto 1 = menor valor)."""
    ordem = sorted(range(len(valores)), key=lambda i: valores[i])
    resultado = [0.0] * len(valores)
    i = 0
    while i < len(ordem):
        j = i
        while j + 1 < len(ordem) and valores[ordem[j + 1]] == valores[ordem[i]]:
            j += 1
        media = (i + j) / 2 + 1
        for k in range(i, j + 1):
            resultado[ordem[k]] = media
        i = j + 1
    return resultado


def spearman(x: list[float], y: list[float]) -> float | None:
    """Rho de Spearman como correlação de Pearson entre os postos (trata empates)."""
    if len(x) != len(y) or len(x) < 3:
        return None
    rx, ry = postos(x), postos(y)
    mx, my = sum(rx) / len(rx), sum(ry) / len(ry)
    sxy = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    sxx = sum((a - mx) ** 2 for a in rx)
    syy = sum((b - my) ** 2 for b in ry)
    if sxx == 0 or syy == 0:
        return None
    return sxy / math.sqrt(sxx * syy)


def jaccard(a: list[dict[str, str]], b: list[dict[str, str]]) -> tuple[float | None, int, int]:
    """Índice de Jaccard entre duas listas de artigos. Devolve (J, interseção, união)."""
    pares = 0
    usados_b: set[int] = set()
    for item in a:
        for j, outro in enumerate(b):
            if j not in usados_b and mesmo_artigo(item, outro):
                usados_b.add(j)
                pares += 1
                break
    uniao = len(a) + len(b) - pares
    if uniao == 0:
        return None, 0, 0
    return pares / uniao, pares, uniao


def nivel(metrica: str, valor: float | None) -> str:
    if valor is None:
        return "não coletado"
    for piso, nome in NIVEIS[metrica]:
        if valor >= piso - 1e-12:
            return nome
    return "Insatisfatório"


def media(valores: list[float]) -> float | None:
    return sum(valores) / len(valores) if valores else None


def fmt(valor: float | None, casas: int = 3) -> str:
    return "-" if valor is None else f"{valor:.{casas}f}".replace(".", ",")


# ---------------------------------------------------------------- métricas

def top30(pasta: Path, tema: str) -> list[dict[str, str]] | None:
    linhas = ler_csv(pasta / "M1.1.1" / f"top30_{tema}.csv")
    if linhas is None:
        return None
    return sorted(linhas, key=lambda l: int(l.get("posicao") or 0))


def recuperados(pasta: Path, tema: str, ref: list[dict[str, str]], top: list[dict[str, str]]) -> set[str]:
    """Estudos (estudo_id) da referência com ao menos um relato no Top 30."""
    achados = set()
    for relato in ref:
        if any(mesmo_artigo(relato, item) for item in top):
            achados.add(relato["estudo_id"])
    manual = ler_csv(pasta / "M1.1.1" / f"correspondencia_manual_{tema}.csv") or []
    por_relato = {r.get("relato_id"): r.get("estudo_id") for r in ref}
    for linha in manual:
        estudo = por_relato.get(linha.get("relato_id"))
        if estudo:
            achados.add(estudo)
    return achados


def referencia_valida(pasta: Path, tema: str) -> list[dict[str, str]] | None:
    """Relatos da revisão de referência publicados e indexados até a data da coleta."""
    ref = ler_csv(pasta / "M1.1.1" / f"referencia_{tema}.csv")
    if ref is None:
        return None
    return [r for r in ref if sim(r.get("publicado_ate_coleta", ""))]


def m111_m112(pasta: Path, resultados: list[dict], detalhe: list[str]) -> None:
    r_temas, rr_temas = [], []
    for tema in TEMAS:
        ref, top = referencia_valida(pasta, tema), top30(pasta, tema)
        if ref is None or top is None:
            detalhe.append(f"M1.1.1 {tema}: não coletado (falta referencia_{tema}.csv ou top30_{tema}.csv)")
            continue
        estudos = {r["estudo_id"] for r in ref}
        achados = recuperados(pasta, tema, ref, top)
        if not estudos:
            detalhe.append(f"M1.1.1 {tema}: referência vazia, tema não calculado")
            continue
        r = len(achados & estudos) / min(len(estudos), 30)
        r_temas.append(r)
        detalhe.append(f"M1.1.1 {tema}: {len(achados & estudos)} de {len(estudos)} estudos; "
                       f"denominador {min(len(estudos), 30)}; R = {fmt(r)}")

        consulta = ler_csv(pasta / "M1.1.2" / f"consulta_fontes_{tema}.csv")
        if consulta is None:
            detalhe.append(f"M1.1.2 {tema}: não coletado (falta consulta_fontes_{tema}.csv)")
            continue
        indexados_relatos = {c["relato_id"] for c in consulta
                             if sim(c.get("pubmed", "")) or sim(c.get("scielo", "")) or sim(c.get("scholar", ""))}
        estudos_idx = {r["estudo_id"] for r in ref if r.get("relato_id") in indexados_relatos}
        if not estudos_idx:
            detalhe.append(f"M1.1.2 {tema}: nenhum estudo indexado nas três fontes; tema não calculado")
            continue
        rr = len(achados & estudos_idx) / min(len(estudos_idx), 30)
        rr_temas.append(rr)
        detalhe.append(f"M1.1.2 {tema}: {len(achados & estudos_idx)} de {len(estudos_idx)} estudos indexados; "
                       f"Rr = {fmt(rr)}")
    for metrica, valores in (("M1.1.1", r_temas), ("M1.1.2", rr_temas)):
        v = media(valores)
        resultados.append({"metrica": metrica, "valor": v, "nivel": nivel(metrica, v),
                           "base": f"{len(valores)} de 4 temas"})


def m121(pasta: Path, resultados: list[dict], detalhe: list[str]) -> None:
    linhas = ler_csv(pasta / "M1.2.1" / "casos_funcoes.csv")
    if linhas is None:
        resultados.append({"metrica": "M1.2.1", "valor": None, "nivel": "não coletado", "base": "-"})
        return
    operantes = sum(1 for l in linhas if normalizar_texto(l.get("classificacao_final", "")) == "operante")
    parciais = sum(1 for l in linhas if normalizar_texto(l.get("classificacao_final", "")) == "parcial")
    declaradas = 9
    c = (operantes + 0.5 * parciais) / declaradas
    detalhe.append(f"M1.2.1: {operantes} operantes, {parciais} parciais, {len(linhas)} funções registradas "
                   f"de {declaradas} declaradas; C = {fmt(c)}")
    if len(linhas) != declaradas:
        detalhe.append("M1.2.1: ATENÇÃO, o arquivo não tem exatamente nove funções")
    resultados.append({"metrica": "M1.2.1", "valor": c, "nivel": nivel("M1.2.1", c), "base": "9 funções"})


def m131(pasta: Path, resultados: list[dict], detalhe: list[str]) -> None:
    p_validos = []
    for tema in TEMAS:
        a1 = ler_csv(pasta / "M1.3.1" / f"julgamento_A1_{tema}.csv")
        a2 = ler_csv(pasta / "M1.3.1" / f"julgamento_A2_{tema}.csv")
        cons = ler_csv(pasta / "M1.3.1" / f"consolidado_{tema}.csv")
        if a1 is None or a2 is None:
            detalhe.append(f"M1.3.1 {tema}: não coletado")
            continue
        # Se houve rejulgamento (kappa abaixo de 0,61), vale o segundo par de fichas.
        a1r = ler_csv(pasta / "M1.3.1" / f"julgamento_A1_{tema}_rodada2.csv")
        a2r = ler_csv(pasta / "M1.3.1" / f"julgamento_A2_{tema}_rodada2.csv")
        rodada = 1
        if a1r is not None and a2r is not None:
            k1, _ = kappa_fichas(a1, a2)
            detalhe.append(f"M1.3.1 {tema}: rodada 1 com kappa = {fmt(k1)}")
            a1, a2, rodada = a1r, a2r, 2
        k, po = kappa_fichas(a1, a2)
        valido = k is not None and k >= KAPPA_MINIMO - 1e-12
        if k is None and po == 1.0:
            valido = True
        if cons is None:
            detalhe.append(f"M1.3.1 {tema}: kappa = {fmt(k)} (rodada {rodada}); falta consolidado_{tema}.csv")
            continue
        relevantes = sum(1 for l in cons if sim(l.get("final", "")))
        p = relevantes / len(cons) if cons else None
        estado = "válido" if valido else "INVÁLIDO, fora da média"
        k_txt = "indefinido (concordância total)" if k is None and po == 1.0 else fmt(k)
        detalhe.append(f"M1.3.1 {tema}: kappa = {k_txt} (rodada {rodada}, concordância bruta {fmt(po)}); "
                       f"{relevantes} de {len(cons)} relevantes; P = {fmt(p)}; {estado}")
        if valido and p is not None:
            p_validos.append(p)
    v = media(p_validos) if len(p_validos) >= 3 else None
    if 0 < len(p_validos) < 3:
        detalhe.append("M1.3.1: menos de três temas válidos; métrica declarada não aplicável")
    resultados.append({"metrica": "M1.3.1", "valor": v,
                       "nivel": nivel("M1.3.1", v) if v is not None else "não aplicável" if p_validos else "não coletado",
                       "base": f"{len(p_validos)} de 4 temas válidos"})


def kappa_fichas(a1: list[dict[str, str]], a2: list[dict[str, str]]) -> tuple[float | None, float]:
    j1 = {l["item"]: normalizar_texto(l.get("relevante", "")) for l in a1}
    j2 = {l["item"]: normalizar_texto(l.get("relevante", "")) for l in a2}
    itens = sorted(set(j1) & set(j2))
    if set(j1) != set(j2):
        print(f"aviso: fichas com itens diferentes; usando os {len(itens)} itens em comum", file=sys.stderr)
    return cohen_kappa([j1[i] for i in itens], [j2[i] for i in itens])


def m132(pasta: Path, resultados: list[dict], detalhe: list[str]) -> None:
    corretos = verificados = 0
    temas = 0
    for tema in TEMAS:
        linhas = ler_csv(pasta / "M1.3.2" / f"conferencia_{tema}.csv")
        if linhas is None:
            detalhe.append(f"M1.3.2 {tema}: não coletado")
            continue
        campos = ["titulo_ok", "autores_ok", "ano_ok", "periodico_ok", "link_ok"]
        ok = sum(1 for l in linhas if all(sim(l.get(c, "")) for c in campos))
        corretos += ok
        verificados += len(linhas)
        temas += 1
        detalhe.append(f"M1.3.2 {tema}: {ok} de {len(linhas)} itens corretos")
    k = corretos / verificados if verificados else None
    resultados.append({"metrica": "M1.3.2", "valor": k, "nivel": nivel("M1.3.2", k),
                       "base": f"{verificados} itens em {temas} temas"})


def m141(pasta: Path, resultados: list[dict], detalhe: list[str]) -> None:
    rhos = []
    for tema in TEMAS_M141:
        top = top30(pasta, tema)
        chave = ler_csv(pasta / "M1.3.1" / f"chave_{tema}.csv")
        n1 = ler_csv(pasta / "M1.4.1" / f"rubrica_A1_{tema}.csv")
        n2 = ler_csv(pasta / "M1.4.1" / f"rubrica_A2_{tema}.csv")
        if None in (top, chave, n1, n2):
            detalhe.append(f"M1.4.1 {tema}: não coletado")
            continue
        posicao_do_item = {c["item"]: c["posicao"] for c in chave}
        score = {l["posicao"]: float(l["quality_score"].replace(",", ".")) for l in top}
        nota1 = {l["item"]: nota_rubrica(l) for l in n1}
        nota2 = {l["item"]: nota_rubrica(l) for l in n2}
        itens = sorted(set(nota1) & set(nota2) & set(posicao_do_item))
        x = [score[posicao_do_item[i]] for i in itens]
        y = [(nota1[i] + nota2[i]) / 2 for i in itens]
        rho = spearman(x, y)
        entre = spearman([nota1[i] for i in itens], [nota2[i] for i in itens])
        detalhe.append(f"M1.4.1 {tema}: {len(itens)} artigos; rho = {fmt(rho)} "
                       f"(informativo: rho entre as notas de A1 e A2 = {fmt(entre)})")
        if rho is not None:
            rhos.append(rho)
    v = media(rhos)
    resultados.append({"metrica": "M1.4.1", "valor": v, "nivel": nivel("M1.4.1", v),
                       "base": f"{len(rhos)} de 2 temas"})


def nota_rubrica(linha: dict[str, str]) -> float:
    limites = {"desenho": 4, "amostra": 3, "comparador": 2, "revisao_pares": 1}
    total = 0.0
    for campo, maximo in limites.items():
        valor = float((linha.get(campo) or "0").replace(",", "."))
        if not 0 <= valor <= maximo:
            raise ValueError(f"item {linha.get('item')}: {campo} = {valor} fora de 0 a {maximo}")
        total += valor
    return total


def m151(pasta: Path, resultados: list[dict], detalhe: list[str]) -> None:
    conformes = avaliados = 0
    execucoes = sorted((pasta / "M1.5.1").glob("conferencia_E*.csv")) if (pasta / "M1.5.1").exists() else []
    for arquivo in execucoes:
        linhas = ler_csv(arquivo) or []
        ok = sum(1 for l in linhas if sim(l.get("ano_ok", "")) and sim(l.get("tipo_ok", "")) and sim(l.get("fonte_ok", "")))
        conformes += ok
        avaliados += len(linhas)
        detalhe.append(f"M1.5.1 {arquivo.stem.replace('conferencia_', '')}: {ok} de {len(linhas)} itens conformes")
    f = conformes / avaliados if avaliados else None
    resultados.append({"metrica": "M1.5.1", "valor": f, "nivel": nivel("M1.5.1", f),
                       "base": f"{avaliados} itens em {len(execucoes)} execuções"})


def m152(pasta: Path, resultados: list[dict], detalhe: list[str]) -> None:
    js = []
    for tema in TEMAS:
        b = ler_csv(pasta / "M1.5.2" / f"top30_{tema}-B.csv")
        if b is None:
            continue
        a = top30(pasta, tema)
        if a is None:
            detalhe.append(f"M1.5.2 {tema}: existe a execução B, mas falta a A (M1.1.1/top30_{tema}.csv)")
            continue
        j, inter, uniao = jaccard(a, b)
        detalhe.append(f"M1.5.2 {tema}: {inter} artigos em comum, união de {uniao}; J = {fmt(j)}")
        if j is not None:
            js.append(j)
    v = media(js)
    resultados.append({"metrica": "M1.5.2", "valor": v, "nivel": nivel("M1.5.2", v),
                       "base": f"{len(js)} temas repetidos"})


# ---------------------------------------------------------------- comandos

PONTOS = {"Insatisfatório": 0, "Aceitável": 1, "Bom": 2, "Excelente": 3}
QUESTOES = {"Q1.1": ["M1.1.1", "M1.1.2"], "Q1.2": ["M1.2.1"], "Q1.3": ["M1.3.1", "M1.3.2"],
            "Q1.4": ["M1.4.1"], "Q1.5": ["M1.5.1", "M1.5.2"]}
CRITICAS = {"Q1.1": "M1.1.1", "Q1.3": "M1.3.1"}


def classe_pontuacao(p: float) -> str:
    if p < 1.0:
        return "Insatisfatório"
    if p < 1.75:
        return "Aceitável"
    if p < 2.5:
        return "Bom"
    return "Excelente"


def agregar(resultados: list[dict]) -> list[str]:
    """Regras do G1 em niveis-e-julgamento.md, seção 2."""
    por_metrica = {r["metrica"]: r["nivel"] for r in resultados}
    linhas, pontuacoes, alguma_insat = [], [], False
    for q, metricas in QUESTOES.items():
        pts = [PONTOS[por_metrica[m]] for m in metricas if por_metrica.get(m) in PONTOS]
        if not pts:
            linhas.append(f"{q}: sem métrica medida")
            continue
        p = sum(pts) / len(pts)
        cl = classe_pontuacao(p)
        critica = CRITICAS.get(q)
        if critica and por_metrica.get(critica) == "Insatisfatório" and cl in ("Bom", "Excelente"):
            cl = "Aceitável"
        alguma_insat |= cl == "Insatisfatório"
        pontuacoes.append(p)
        linhas.append(f"{q}: {fmt(p, 2)} pontos, {cl} ({len(pts)} de {len(metricas)} métricas medidas)")
    if pontuacoes:
        g = sum(pontuacoes) / len(pontuacoes)
        cl = classe_pontuacao(g)
        if alguma_insat and cl == "Excelente":
            cl = "Bom"
        julgamento = {"Excelente": "Atende", "Bom": "Atende", "Aceitável": "Atende parcialmente",
                      "Insatisfatório": "Não atende"}[cl]
        medidas = sum(1 for r in resultados if r["nivel"] in PONTOS)
        linhas.append(f"G1: {fmt(g, 2)} pontos, {cl}; julgamento: {julgamento} "
                      f"({medidas} de 8 métricas medidas, {len(pontuacoes)} de 5 questões)")
    return linhas


def cmd_calcular(pasta: Path, saida: Path | None) -> int:
    resultados: list[dict] = []
    detalhe: list[str] = []
    for funcao in (m111_m112, m121, m131, m132, m141, m151, m152):
        funcao(pasta, resultados, detalhe)
    print("Detalhe por tema")
    for linha in detalhe:
        print("  " + linha)
    print("\nMétrica   Valor   Nível            Base")
    for r in resultados:
        print(f"{r['metrica']:<9} {fmt(r['valor']):>6}  {r['nivel']:<16} {r['base']}")
    print("\nAgregação (Fase 2, níveis e julgamento)")
    for linha in agregar(resultados):
        print("  " + linha)
    if saida:
        with saida.open("w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(["metrica", "valor", "nivel", "base"])
            for r in resultados:
                w.writerow([r["metrica"], "" if r["valor"] is None else f"{r['valor']:.4f}", r["nivel"], r["base"]])
        print(f"\nResultados gravados em {saida}")
    return 0


def cmd_ficha_cega(pasta: Path, tema: str) -> int:
    top = top30(pasta, tema)
    if top is None:
        print(f"falta M1.1.1/top30_{tema}.csv", file=sys.stderr)
        return 1
    semente = SEMENTE_BASE + int(tema[1:])
    ordem = list(range(len(top)))
    random.Random(semente).shuffle(ordem)
    destino = pasta / "M1.3.1"
    destino.mkdir(exist_ok=True)
    ficha, chave = destino / f"ficha_cega_{tema}.csv", destino / f"chave_{tema}.csv"
    for arquivo in (ficha, chave):
        if arquivo.exists():
            print(f"{arquivo} já existe; apague-o antes de gerar de novo", file=sys.stderr)
            return 1
    with ficha.open("w", encoding="utf-8", newline="") as f1, chave.open("w", encoding="utf-8", newline="") as f2:
        w1, w2 = csv.writer(f1), csv.writer(f2)
        w1.writerow(["item", "titulo", "resumo", "ano", "periodico", "doi"])
        w2.writerow(["item", "posicao"])
        for n, i in enumerate(ordem, start=1):
            item = f"{tema}-{n:02d}"
            l = top[i]
            w1.writerow([item, l.get("titulo", ""), l.get("resumo", ""), l.get("ano", ""), l.get("periodico", ""), l.get("doi", "")])
            w2.writerow([item, l.get("posicao", "")])
    print(f"Gerados {ficha} e {chave} com a semente {semente}")
    return 0


def cmd_ficha_rodada2(pasta: Path, tema: str) -> int:
    """Rejulgamento (kappa abaixo de 0,61): mesma ficha e mesmos códigos de item, em nova ordem."""
    origem = pasta / "M1.3.1" / f"ficha_cega_{tema}.csv"
    destino = pasta / "M1.3.1" / f"ficha_cega_{tema}_rodada2.csv"
    linhas = ler_csv(origem)
    if linhas is None:
        print(f"falta {origem}", file=sys.stderr)
        return 1
    if destino.exists():
        print(f"{destino} já existe; apague-o antes de gerar de novo", file=sys.stderr)
        return 1
    semente = SEMENTE_BASE + int(tema[1:]) + 100
    random.Random(semente).shuffle(linhas)
    with destino.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0].keys()))
        w.writeheader()
        w.writerows(linhas)
    print(f"Gerado {destino} com a semente {semente}")
    return 0


def posicoes_amostra(n: int) -> list[int]:
    """Amostra sistemática de M1.3.2: posições round(i * n / 10), i = 1..10; todas se n <= 10."""
    if n <= 10:
        return list(range(1, n + 1))
    return sorted({max(1, round(i * n / 10)) for i in range(1, 11)})


def cmd_amostra(pasta: Path, tema: str) -> int:
    top = top30(pasta, tema)
    if top is None:
        print(f"falta M1.1.1/top30_{tema}.csv", file=sys.stderr)
        return 1
    print(f"{tema}: lista com {len(top)} itens; posições da amostra de M1.3.2: "
          + ", ".join(str(p) for p in posicoes_amostra(len(top))))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Cálculo das métricas do G1 a partir das planilhas de coleta.")
    parser.add_argument("--pasta", type=Path, default=PASTA_PADRAO, help="pasta com M1.1.1/ a M1.5.2/")
    sub = parser.add_subparsers(dest="comando", required=True)
    c = sub.add_parser("calcular", help="calcula todas as métricas disponíveis")
    c.add_argument("--saida", type=Path, help="grava o resumo em CSV")
    f = sub.add_parser("ficha-cega", help="gera a ficha cega e a chave de M1.3.1 e M1.4.1")
    f.add_argument("--tema", choices=TEMAS, required=True)
    f.add_argument("--rodada", type=int, choices=[1, 2], default=1,
                   help="2 gera a ficha do rejulgamento, com os mesmos itens em nova ordem")
    a = sub.add_parser("amostra", help="mostra as posições da amostra de M1.3.2")
    a.add_argument("--tema", choices=TEMAS, required=True)
    args = parser.parse_args(argv)
    if args.comando == "calcular":
        return cmd_calcular(args.pasta, args.saida)
    if args.comando == "ficha-cega":
        if args.rodada == 2:
            return cmd_ficha_rodada2(args.pasta, args.tema)
        return cmd_ficha_cega(args.pasta, args.tema)
    return cmd_amostra(args.pasta, args.tema)


if __name__ == "__main__":
    sys.exit(main())
