#!/usr/bin/env python3
"""Etapa 7 do G2 por inspeção: compara as fichas de A1 e A2, monta o consolidado e calcula as métricas.

Método: docs/fase-3/metodo-g2-inspecao.md (seções 5 e 6). Fórmulas e níveis: docs/fase-2/especificacao-das-metricas.md
e docs/fase-2/niveis-e-julgamento.md.

Só usa a biblioteca padrão do Python (3.9 ou superior). Lê as fichas `A1.md` e `A2.md` de cada pasta. Se A2 tiver
preenchido a planilha antiga (`A2.csv`, do modelo de 17/11), ela é lida no lugar de `A2.md`.

Uso, a partir da raiz do repositório:

    python3 dados/avaliacao/G2/calcular_g2_inspecao.py comparar
    python3 dados/avaliacao/G2/calcular_g2_inspecao.py calcular

`comparar` preenche, em cada `consolidado.md`, as colunas `item`, `valor_a1` e `valor_a2`; nas linhas iguais, também
`valor_final` e `decidido_por = consenso`. Linhas já decididas não são apagadas, então dá para rodar de novo. Linhas
acrescentadas na consolidação, que nenhuma ficha tem, ficam como estão e não entram na concordância. Mostra as
divergências e a concordância bruta, que vai para `coleta.md`.

`calcular` lê só a coluna `valor_final` do consolidado, como manda o método, e escreve a tabela "Resultado" de cada
métrica. Item com `valor_final` vazio interrompe o cálculo daquela métrica. Valores que tiram o item de B:
`nao_coletado`, `fora_de_B` e, na M2.4.2, `nao_se_aplica`.

A opção --pasta aponta para outra pasta com a mesma estrutura (usada para testar o script).
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from fractions import Fraction

SEP = re.compile(r"(?<!\\)\|")
FORA_DE_B = {"nao_coletado", "fora_de_b", "nao_se_aplica"}
NIVEIS = ["Insatisfatório", "Aceitável", "Bom", "Excelente"]

# métrica: (coluna da chave, colunas do valor, coluna da chave no A2.csv antigo, colunas no A2.csv antigo)
METRICAS = {
    "M2.1.1": ("item", ["descrito"], "item", ["descrito"]),
    "M2.2.1": ("funcao", ["diz_como_executar"], "funcao", ["diz_como_executar"]),
    "M2.2.2": ("id_inventario", ["tem_causa", "tem_solucao"], "id", ["tem_causa", "tem_solucao"]),
    "M2.3.1": ("padrao", ["consistente"], "padrao", ["consistente"]),
    "M2.3.2": ("id_inventario", ["clara"], "id", ["clara"]),
    "M2.4.1": ("id", ["protegida"], "acao", ["protegida"]),
    "M2.4.2": ("id", ["detectado", "sugeriu_valor"], "id", ["detectado", "sugeriu_valor"]),
    "M2.7.1": ("id", ["explica_proposito"], "item", ["explica_proposito"]),
}

# limites inferiores de Aceitável, Bom e Excelente (Fase 2, níveis de pontuação)
LIMIARES = {
    "M2.1.1": (Fraction(70, 100), Fraction(90, 100), Fraction(1)),
    "M2.2.1": (Fraction(70, 100), Fraction(88, 100), Fraction(1)),
    "M2.2.2": (Fraction(50, 100), Fraction(75, 100), Fraction(90, 100)),
    "M2.3.1": (Fraction(70, 100), Fraction(80, 100), Fraction(90, 100)),
    "M2.3.2": (Fraction(70, 100), Fraction(85, 100), Fraction(95, 100)),
    "M2.4.1": (Fraction(70, 100), Fraction(85, 100), Fraction(1)),
    "M2.4.2": (Fraction(40, 100), Fraction(60, 100), Fraction(80, 100)),
}


def normal(v: str) -> str:
    v = v.strip().strip("`").lower()
    return {"não": "nao", "s": "sim", "n": "nao", "fora de b": "fora_de_b"}.get(v, v)


def tabelas_md(caminho: str):
    """Devolve as tabelas de um arquivo Markdown como listas de dicionários."""
    if not os.path.isfile(caminho):
        return []
    saida, cab, linhas = [], None, []
    for l in open(caminho, encoding="utf-8").read().split("\n") + [""]:
        if l.startswith("|"):
            cels = [c.strip() for c in SEP.split(l.strip())[1:-1]]
            if cab is None:
                cab = cels
            elif not set(l.replace("|", "").strip()) <= set("-: "):
                linhas.append(dict(zip(cab, cels)))
        elif cab is not None:
            saida.append((cab, linhas))
            cab, linhas = None, []
    return saida


def ler_ficha(pasta: str, metrica: str, avaliador: str):
    """{item: valor} da ficha do avaliador; None se a ficha não existe ou está vazia."""
    chave, cols, chave_csv, cols_csv = METRICAS[metrica]
    csv_antigo = os.path.join(pasta, metrica, f"{avaliador}.csv")
    valores = {}
    if avaliador == "A2" and os.path.isfile(csv_antigo):
        with open(csv_antigo, encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                item = (r.get(chave_csv) or "").strip()
                if item:
                    valores[item] = "/".join(normal(r.get(c) or "") for c in cols_csv)
    else:
        for cab, linhas in tabelas_md(os.path.join(pasta, metrica, f"{avaliador}.md")):
            if chave in cab and all(c in cab for c in cols):
                for r in linhas:
                    item = r[chave].strip().strip("`")
                    if item:
                        valores[item] = "/".join(normal(r[c]) for c in cols)
    preenchidos = {k: v for k, v in valores.items() if v.replace("/", "").strip()}
    return preenchidos or None


def item_ordem(item: str):
    m = re.match(r"([A-Z]+)(\d+)(.*)", item)
    return (m.group(1), int(m.group(2)), m.group(3)) if m else (item, 0, "")


def ler_consolidado(caminho: str):
    for cab, linhas in tabelas_md(caminho):
        if cab[:2] == ["item", "valor_a1"]:
            return {r["item"].strip(): r for r in linhas if r["item"].strip()}
    return {}


def reescrever_tabela(caminho: str, cab_inicio: list, novas_linhas: list):
    texto = open(caminho, encoding="utf-8").read().split("\n")
    ini = next(i for i, l in enumerate(texto)
               if l.startswith("|") and [c.strip() for c in SEP.split(l.strip())[1:-1]][:len(cab_inicio)] == cab_inicio)
    fim = ini
    while fim < len(texto) and texto[fim].startswith("|"):
        fim += 1
    cab = [c.strip() for c in SEP.split(texto[ini].strip())[1:-1]]
    corpo = ["| " + " | ".join(cab) + " |", "|" + "---|" * len(cab)]
    corpo += ["| " + " | ".join(l) + " |" for l in novas_linhas]
    texto[ini:fim] = corpo
    open(caminho, "w", encoding="utf-8", newline="\n").write("\n".join(texto))


def comparar(pasta: str):
    for m in METRICAS:
        a1, a2 = ler_ficha(pasta, m, "A1"), ler_ficha(pasta, m, "A2")
        if not a1 or not a2:
            print(f"{m}: falta {'A1' if not a1 else 'A2'} preenchida; nada a comparar.")
            continue
        cons = ler_consolidado(os.path.join(pasta, m, "consolidado.md"))
        itens = sorted(set(a1) | set(a2) | set(cons), key=item_ordem)
        linhas, iguais, divergentes = [], 0, []
        for it in itens:
            ant = cons.get(it, {})
            final, just, dec = ant.get("valor_final", ""), ant.get("justificativa", ""), ant.get("decidido_por", "")
            if it not in a1 and it not in a2:
                # item acrescentado na consolidação (nenhuma ficha o tem): a linha fica como está
                linhas.append([it, "ausente", "ausente", final, just, dec])
                if not final:
                    divergentes.append((it, "ausente", "ausente"))
                continue
            v1, v2 = a1.get(it, "ausente"), a2.get(it, "ausente")
            if v1 != v2 and dec == "consenso" and ant.get("valor_a1") == ant.get("valor_a2"):
                final, dec = "", ""  # a ficha mudou depois da última comparação: a divergência volta a ser decidida
            if v1 == v2:
                iguais += 1
                final, dec = final or v1, dec or "consenso"
            elif not final:
                divergentes.append((it, v1, v2))
            linhas.append([it, v1, v2, final, just, dec])
        reescrever_tabela(os.path.join(pasta, m, "consolidado.md"), ["item", "valor_a1"], linhas)
        comp = sum(1 for it in itens if it in a1 and it in a2)
        print(f"{m}: {comp} itens comparados, {iguais} iguais, concordância bruta {iguais / comp:.0%}"
              if comp else f"{m}: nenhum item em comum")
        for it, v1, v2 in divergentes:
            print(f"    divergência sem decisão: {it}  A1={v1}  A2={v2}")


def nivel(m: str, a: int, b: int, credito_desprotegido: bool = False) -> str:
    if b == 0:
        return "não coletado"
    if m == "M2.7.1":
        return NIVEIS[max(0, min(3, a - 1))] if b == 4 else f"{a} de {b} (B menor que 4: ver o método)"
    x = Fraction(a, b)
    lim = LIMIARES[m]
    n = sum(1 for l in lim if x >= l)
    if m == "M2.4.1" and credito_desprotegido:
        n = 0
    return NIVEIS[n]


def acoes_pagas(pasta: str):
    pagas = set()
    for cab, linhas in tabelas_md(os.path.join(pasta, "M2.4.1", "A1.md")):
        if "consome_credito" in cab:
            pagas |= {r["id"] for r in linhas if normal(r["consome_credito"]).startswith("sim")}
    return pagas or {"A01"}


def calcular(pasta: str):
    resultado = {}
    for m in METRICAS:
        cons = ler_consolidado(os.path.join(pasta, m, "consolidado.md"))
        if not cons or any(not r.get("valor_final", "").strip() for r in cons.values()):
            vazios = [k for k, r in cons.items() if not r.get("valor_final", "").strip()]
            print(f"{m}: consolidado incompleto ({len(vazios)} itens sem valor_final); não calculado.")
            continue
        finais = {k: normal(r["valor_final"]) for k, r in cons.items()}
        fora = [k for k, v in finais.items() if v.split("/")[0] in FORA_DE_B or v in FORA_DE_B]
        dentro = {k: v for k, v in finais.items() if k not in fora}
        credito = False
        if m == "M2.2.2":
            a = sum(1 for v in dentro.values() if v == "sim/sim")
        elif m == "M2.3.1":
            a = sum(1 for v in dentro.values() if v == "nao")
        elif m == "M2.4.2":
            dentro = {k: v for k, v in dentro.items() if v.split("/")[0] == "sim"}
            fora = [k for k in finais if k not in dentro]
            a = sum(1 for v in dentro.values() if v.endswith("/sim"))
        else:
            a = sum(1 for v in dentro.values() if v == "sim")
        b = len(dentro)
        if m == "M2.4.1":
            credito = any(finais.get(k) == "nao" for k in acoes_pagas(pasta))
        if m == "M2.3.1":
            x = 1 - Fraction(a, b) if b else None
            nv = nivel_m231(x)
        else:
            x = Fraction(a, b) if b else None
            nv = nivel(m, a, b, credito)
        resultado[m] = (a, b, x, nv, fora, credito)
        valor = "-" if x is None else (f"{a} de {b}" if m == "M2.7.1" else f"{float(x):.3f}".replace(".", ","))
        linhas = [f"{a}", f"{b}", valor]
        if m == "M2.4.1":
            linhas.append("Sim" if credito else "Não")
        linhas += [nv, ", ".join(fora) + " (motivo na justificativa de cada item)" if fora else "nenhum"]
        escrever_resultado(os.path.join(pasta, m, "consolidado.md"), linhas)
        print(f"{m}: A={a} B={b} valor={valor} nível={nv}" + (" (ação paga sem proteção)" if credito else ""))
    if resultado:
        questoes(resultado)


def nivel_m231(x):
    if x is None:
        return "não coletado"
    lim = LIMIARES["M2.3.1"]
    return NIVEIS[sum(1 for l in lim if x >= l)]


def escrever_resultado(caminho: str, valores: list):
    texto = open(caminho, encoding="utf-8").read().split("\n")
    ini = next(i for i, l in enumerate(texto) if l.strip() == "## Resultado")
    linhas = [i for i in range(ini, len(texto)) if texto[i].startswith("| ") and not texto[i].startswith("| Campo")]
    for i, v in zip(linhas, valores):
        campo = SEP.split(texto[i].strip())[1].strip()
        texto[i] = f"| {campo} | {v} |"
    open(caminho, "w", encoding="utf-8", newline="\n").write("\n".join(texto))


def questoes(r: dict):
    idx = {n: i for i, n in enumerate(NIVEIS)}

    def nv(m):
        return r[m][3] if m in r and r[m][3] in idx else None

    def desce(n):
        return NIVEIS[max(0, idx[n] - 1)]

    print("\nQuestões (seção 3 de níveis e julgamento):")
    if nv("M2.1.1"):
        print(f"  Q2.1: {nv('M2.1.1')}")
    if nv("M2.2.1"):
        q = nv("M2.2.1")
        print(f"  Q2.2: {desce(q) if nv('M2.2.2') == 'Insatisfatório' else q}")
    if nv("M2.3.1") and nv("M2.3.2"):
        print(f"  Q2.3: {min(nv('M2.3.1'), nv('M2.3.2'), key=lambda n: idx[n])}")
    if nv("M2.4.1"):
        q = nv("M2.4.1")
        if r["M2.4.1"][5]:
            q = "Insatisfatório (ação que consome crédito sem proteção)"
        elif nv("M2.4.2") == "Insatisfatório":
            q = desce(q)
        print(f"  Q2.4: {q}")
    if nv("M2.7.1"):
        print(f"  Q2.7: depende de M2.7.2 (#28); M2.7.1 = {nv('M2.7.1')}"
              + (" (rebaixa Q2.7 em um nível)" if nv("M2.7.1") == "Insatisfatório" else ""))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("comando", choices=["comparar", "calcular"])
    ap.add_argument("--pasta", default=os.path.dirname(os.path.abspath(__file__)))
    a = ap.parse_args()
    (comparar if a.comando == "comparar" else calcular)(a.pasta)


if __name__ == "__main__":
    sys.exit(main())
