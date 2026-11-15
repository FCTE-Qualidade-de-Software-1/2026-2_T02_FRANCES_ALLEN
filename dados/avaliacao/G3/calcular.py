"""Cálculo das métricas do G3 a partir das saídas brutas de coletar.sh.

Uso:
    python calcular.py <pasta dados/avaliacao/G3>

Só lê os arquivos brutos de cada pasta M3.x.y/ e escreve:
    M3.x.y/resultado.md   valor, contagens e nível de cada métrica
    resultados.csv        uma linha por métrica

Fórmulas: docs/fase-2/especificacao-das-metricas.md (fichas M3.1.1 a M3.3.1).
Níveis: docs/fase-2/niveis-e-julgamento.md (tabela da seção 1).
Regras de contagem: docs/fase-3/metodo-g3.md (seção 4).
Só usa a biblioteca padrão.
"""

from __future__ import annotations

import csv
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def ler_ambiente(pasta: Path) -> dict[str, str]:
    amb = {}
    for linha in (pasta / "ambiente.txt").read_text(encoding="utf-8").splitlines():
        chave, _, valor = linha.partition("=")
        amb[chave] = valor
    return amb


def br(numero: float, casas: int = 2) -> str:
    return f"{numero:.{casas}f}".replace(".", ",")


# --------------------------------------------------------------- níveis
# Faixas da Fase 2 (niveis-e-julgamento.md, seção 1).

def nivel_m311(x: float) -> str:  # quanto menor, melhor
    if x < 5:
        return "Excelente"
    if x < 10:
        return "Bom"
    if x <= 15:
        return "Aceitável"
    return "Insatisfatório"


def nivel_crescente(x: float, aceitavel: float, bom: float, excelente: float) -> str:
    if x >= excelente:
        return "Excelente"
    if x >= bom:
        return "Bom"
    if x >= aceitavel:
        return "Aceitável"
    return "Insatisfatório"


def nivel_m322(x: float) -> str:  # quanto menor, melhor, em %
    if x < 2:
        return "Excelente"
    if x <= 5:
        return "Bom"
    if x <= 10:
        return "Aceitável"
    return "Insatisfatório"


# --------------------------------------------------------------- métricas

def m311(pasta: Path) -> dict:
    arquivos = [l for l in (pasta / "arquivos-py.txt").read_text(encoding="utf-8").splitlines() if l]
    linhas = list(csv.DictReader((pasta / "imports.csv").open(encoding="utf-8")))
    arestas = {(l["arquivo"], l["modulo_destino"]) for l in linhas}
    declaracoes = {(l["arquivo"], l["linha"]) for l in linhas}
    por_modulo: dict[str, int] = {}
    for origem, _ in arestas:
        por_modulo[origem] = por_modulo.get(origem, 0) + 1
    a, b = len(arestas), len(arquivos)
    x = a / b
    maiores = sorted(por_modulo.items(), key=lambda kv: (-kv[1], kv[0]))[:5]
    detalhe = [
        f"- A (dependências internas distintas, par arquivo de origem e módulo de destino): {a}",
        f"- B (arquivos `.py` em `src/vicky/`): {b}",
        f"- Declarações de import interno (informativo, não entra no cálculo): {len(declaracoes)}",
        "- Módulos com mais dependências internas: "
        + ", ".join(f"`{m}` ({n})" for m, n in maiores),
    ]
    return {"valor": x, "texto": br(x), "a": a, "b": b, "nivel": nivel_m311(x), "detalhe": detalhe}


def m312(pasta: Path) -> dict:
    dados = json.loads((pasta / "radon-cc.json").read_text(encoding="utf-8"))
    blocos = dados["src/vicky/pipeline.py"]
    funcoes = [bl for bl in blocos if bl["type"] in ("function", "method")]
    acima = sorted((bl for bl in funcoes if bl["complexity"] > 10), key=lambda bl: -bl["complexity"])
    a, b = len(acima), len(funcoes)
    x = 1 - a / b
    detalhe = [
        f"- A (funções e métodos com CC > 10, notas C a F): {a}",
        f"- B (funções e métodos de `pipeline.py`; a linha de classe do radon não entra): {b}",
        "- Funções acima do limiar: "
        + ", ".join(f"`{bl['name']}` ({bl['complexity']}, {bl['rank']})" for bl in acima),
    ]
    return {"valor": x, "texto": f"{br(100 * x, 1)}%", "a": a, "b": b,
            "nivel": nivel_crescente(100 * x, 70, 85, 95), "detalhe": detalhe}


def m321(pasta: Path) -> dict:
    arquivos = {l for l in (pasta / "arquivos-py.txt").read_text(encoding="utf-8").splitlines() if l}
    com_violacao = set()
    total = 0
    for linha in (pasta / "flake8-violacoes.txt").read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(.+?\.py):\d+:\d+: ", linha)
        if m:
            com_violacao.add(m.group(1))
            total += 1
    fora = com_violacao - arquivos
    if fora:
        raise SystemExit(f"M3.2.1: arquivos com violação fora da lista: {sorted(fora)}")
    b = len(arquivos)
    a = b - len(com_violacao)
    x = a / b
    conformes = sorted(arquivos - com_violacao)
    detalhe = [
        f"- B (arquivos `.py` analisados): {b}",
        f"- Arquivos com pelo menos uma violação: {len(com_violacao)}",
        f"- A (arquivos sem violação): {a} ({', '.join(f'`{c}`' for c in conformes)})",
        f"- Total de violações apontadas: {total}",
    ]
    return {"valor": x, "texto": f"{br(100 * x, 1)}%", "a": a, "b": b,
            "nivel": nivel_crescente(100 * x, 75, 90, 100), "detalhe": detalhe}


def m322(pasta: Path) -> dict:
    texto = (pasta / "pylint-duplicate-code.txt").read_text(encoding="utf-8")
    # pylint escreve "==modulo:[inicio:fim]", com início contado a partir de 0 e fim exclusivo:
    # o trecho ocupa as linhas inicio+1 a fim do arquivo (fim - inicio linhas).
    linhas_dup: set[tuple[str, int]] = set()
    blocos = 0
    for modulo, ini, fim in re.findall(r"^==([\w.]+):\[(\d+):(\d+)\]", texto, flags=re.M):
        blocos += 1
        for n in range(int(ini) + 1, int(fim) + 1):
            linhas_dup.add((modulo, n))
    raw = json.loads((pasta / "radon-raw.json").read_text(encoding="utf-8"))
    loc = sum(v["loc"] for v in raw.values())
    sloc = sum(v["sloc"] for v in raw.values())
    a = len(linhas_dup)
    x = 100 * a / loc
    detalhe = [
        f"- Ocorrências de trecho duplicado no relatório do pylint (R0801): {blocos}",
        f"- Linhas duplicadas (união das linhas de todas as ocorrências): {a}",
        f"- Total de linhas avaliadas (LOC do `radon raw`, {len(raw)} arquivos): {loc}",
        f"- Com SLOC ({sloc}) no denominador, informativo: {br(100 * a / sloc, 2)}%",
    ]
    return {"valor": x, "texto": f"{br(x, 2)}%", "a": a, "b": loc,
            "nivel": nivel_m322(x), "detalhe": detalhe}


def m323(pasta: Path) -> dict:
    linhas = list(csv.DictReader((pasta / "funcoes.csv").open(encoding="utf-8")))
    criticas = [l for l in linhas if l["critica"] == "True"]
    com_log = [l for l in criticas if int(l["chamadas_logging"]) > 0]
    grep = (pasta / "grep-logging.txt").read_text(encoding="utf-8").strip()
    a, b = len(com_log), len(criticas)
    x = a / b
    com_print = sum(int(l["chamadas_print"]) > 0 or int(l["traceback_print_exc"]) > 0 for l in criticas)
    com_job = sum(int(l["registro_em_job"]) > 0 for l in criticas)
    detalhe = [
        f"- Funções e métodos de `pipeline.py` inventariados: {len(linhas)}",
        f"- B (funções críticas pela regra do método): {b}",
        f"- A (funções críticas com chamada à biblioteca `logging`): {a}",
        "- `import logging` ou `getLogger` em `src/vicky/`: "
        + ("nenhuma ocorrência" if not grep else f"{len(grep.splitlines())} ocorrências"),
        f"- Informativo, fora da fórmula: funções críticas com `print` ou `traceback.print_exc`: {com_print}; "
        f"com registro de status em `job` no banco: {com_job}",
    ]
    return {"valor": x, "texto": f"{br(100 * x, 1)}%", "a": a, "b": b,
            "nivel": nivel_crescente(100 * x, 50, 75, 90), "detalhe": detalhe}


def m331(pasta: Path) -> dict:
    amb = ler_ambiente(pasta)
    raiz = ET.parse(pasta / "junit.xml").getroot()
    ts = raiz if raiz.tag == "testsuite" else raiz.find("testsuite")
    total = int(ts.get("tests"))
    falhas = int(ts.get("failures"))
    erros = int(ts.get("errors"))
    pulados = int(ts.get("skipped"))
    xfail = 0
    for tc in ts.iter("testcase"):
        s = tc.find("skipped")
        if s is not None and s.get("type") == "pytest.xfail":
            xfail += 1
    cobertura = json.loads((pasta / "coverage.json").read_text(encoding="utf-8"))["totals"]
    detalhe = [
        f"- Código de saída do pytest: {amb.get('codigo_saida_pytest')}",
        f"- Testes coletados: {total}; falhas: {falhas}; erros: {erros}; "
        f"pulados: {pulados - xfail}; falha esperada (xfail): {xfail}",
        f"- A (linhas executáveis executadas, `covered_lines`): {cobertura['covered_lines']}",
        f"- B (linhas executáveis de `src/vicky/`, `num_statements`): {cobertura['num_statements']}",
    ]
    if falhas or erros:
        # Regra do método (seção 7): com falha ou erro a coleta não vale.
        return {"valor": None, "texto": "não medida", "a": cobertura["covered_lines"],
                "b": cobertura["num_statements"], "nivel": "não aplicável",
                "detalhe": detalhe + ["- Coleta inválida: há teste com falha ou erro (ver pytest-cov.txt)"]}
    x = 100 * cobertura["covered_lines"] / cobertura["num_statements"]
    return {"valor": x, "texto": f"{br(x, 2)}%", "a": cobertura["covered_lines"],
            "b": cobertura["num_statements"], "nivel": nivel_crescente(x, 50, 70, 90), "detalhe": detalhe}


METRICAS = {
    "M3.1.1": ("Acoplamento de componentes", m311),
    "M3.1.2": ("Adequação da complexidade ciclomática", m312),
    "M3.2.1": ("Conformidade de estilo PEP 8", m321),
    "M3.2.2": ("Densidade de código duplicado", m322),
    "M3.2.3": ("Completude de logs do sistema", m323),
    "M3.3.1": ("Completude de testes automatizados", m331),
}


def main(raiz: Path) -> None:
    linhas_csv = []
    for mid, (nome, func) in METRICAS.items():
        pasta = raiz / mid
        amb = ler_ambiente(pasta)
        r = func(pasta)
        md = [
            f"# {mid} - {nome}",
            "",
            "Arquivo gerado por `calcular.py` a partir das saídas brutas desta pasta. Não editar à mão.",
            "",
            "| Campo | Valor |",
            "|-------|-------|",
            f"| Data da coleta | {amb['data_coleta']} |",
            f"| Commit avaliado | `{amb['commit_vicky']}` ({amb['data_commit']}) |",
            f"| Valor | {r['texto']} |",
            f"| A | {r['a']} |",
            f"| B | {r['b']} |",
            f"| Nível pela Fase 2 | {r['nivel']} |",
            "",
            "## Contagens",
            "",
            *r["detalhe"],
            "",
        ]
        (pasta / "resultado.md").write_text("\n".join(md), encoding="utf-8")
        linhas_csv.append([mid, nome, r["texto"], r["a"], r["b"], r["nivel"],
                           amb["commit_vicky"][:7], amb["data_coleta"]])
        print(f"{mid}: {r['texto']} ({r['nivel']})")
    with (raiz / "resultados.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["metrica", "nome", "valor", "A", "B", "nivel", "commit", "data_coleta"])
        w.writerows(linhas_csv)


if __name__ == "__main__":
    main(Path(sys.argv[1]))
