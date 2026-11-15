"""Extração por AST para as métricas do G3 que não têm ferramenta pronta.

Só usa a biblioteca padrão. Lê o código, não o executa.

Uso:
    python extrair.py imports <pasta src> <pacote>       > M3.1.1/imports.csv
    python extrair.py funcoes <arquivo pipeline.py>      > M3.2.3/funcoes.csv
    python extrair.py ficha <M3.2.3/funcoes.csv>         > M3.2.3/inspecao.md

imports: uma linha por import interno (arquivo, linha, texto, módulo de destino).
funcoes: uma linha por função de nível de módulo ou método de classe do arquivo,
com os critérios de função crítica e as chamadas de registro encontradas.
"""

from __future__ import annotations

import ast
import csv
import sys
from pathlib import Path


# ---------------------------------------------------------------- M3.1.1

def nome_do_modulo(arquivo: Path, raiz_src: Path) -> str:
    partes = list(arquivo.relative_to(raiz_src).with_suffix("").parts)
    if partes[-1] == "__init__":
        partes.pop()
    return ".".join(partes)


def eh_pacote(arquivo: Path) -> bool:
    return arquivo.name == "__init__.py"


def resolver_relativo(modulo_atual: str, pacote_atual: bool, nivel: int, alvo: str | None) -> str:
    # O pacote de referência de um módulo comum é o pai; de um __init__ é ele mesmo.
    base = modulo_atual.split(".")
    if not pacote_atual:
        base = base[:-1]
    if nivel > 1:
        base = base[: len(base) - (nivel - 1)]
    if alvo:
        base = base + alvo.split(".")
    return ".".join(base)


def modulos_existentes(raiz_src: Path, pacote: str) -> set[str]:
    return {nome_do_modulo(p, raiz_src) for p in (raiz_src / pacote).rglob("*.py")}


def listar_imports(raiz_src: Path, pacote: str) -> None:
    existentes = modulos_existentes(raiz_src, pacote)
    saida = csv.writer(sys.stdout, lineterminator="\n")
    saida.writerow(["arquivo", "linha", "import", "modulo_destino"])
    for arquivo in sorted((raiz_src / pacote).rglob("*.py")):
        atual = nome_do_modulo(arquivo, raiz_src)
        arvore = ast.parse(arquivo.read_text(encoding="utf-8"), filename=str(arquivo))
        for no in ast.walk(arvore):
            destinos: list[str] = []
            if isinstance(no, ast.Import):
                for alias in no.names:
                    destinos.append(alias.name)
            elif isinstance(no, ast.ImportFrom):
                if no.level:
                    base = resolver_relativo(atual, eh_pacote(arquivo), no.level, no.module)
                else:
                    base = no.module or ""
                for alias in no.names:
                    candidato = f"{base}.{alias.name}" if base else alias.name
                    # `from pacote import modulo` aponta para o módulo; `from modulo import nome`, para o módulo.
                    destinos.append(candidato if candidato in existentes else base)
            else:
                continue
            for destino in destinos:
                if destino == pacote or destino.startswith(pacote + "."):
                    rel = arquivo.relative_to(raiz_src.parent).as_posix()
                    saida.writerow([rel, no.lineno, ast.unparse(no), destino])


# ---------------------------------------------------------------- M3.2.3

# Módulos do pacote (caminho relativo a vicky) que caracterizam função crítica.
# Integração externa: LLM, buscas nas bases, scraping e custo do OpenRouter.
MODULOS_INTEGRACAO = {"llm", "discovery", "sources", "openrouter_cost", "scraper", "acesso_aberto"}
# Banco de dados: camada de acesso (storage, db) e os CRUD de projetos e workspaces.
MODULOS_BANCO = {"storage", "db", "web.projects", "web.workspaces", "web.queries"}
NOMES_LOGGER = {"logging", "logger", "log", "_log", "LOGGER", "_logger"}


def nomes_importados(nos: list[ast.stmt] | ast.AST) -> dict[str, str]:
    """Nome local -> módulo de origem (relativo a vicky), para imports internos relativos.

    `from .storage import connect` -> connect: storage
    `from .web import projects as projects_module` -> projects_module: web.projects
    """
    mapa: dict[str, str] = {}
    for no in ast.walk(nos) if isinstance(nos, ast.AST) else nos:
        if isinstance(no, ast.ImportFrom) and no.level:
            base = no.module or ""
            for alias in no.names:
                submodulo = f"{base}.{alias.name}" if base else alias.name
                origem = submodulo if submodulo in SUBMODULOS else base
                mapa[alias.asname or alias.name] = origem
    return mapa


# Submódulos que podem aparecer em `from .pacote import submodulo`.
SUBMODULOS = {"web.projects", "web.workspaces", "web.queries", "web.users", "web.app",
              "sources.pubmed", "sources.scielo", "sources.scholar"}


def funcoes_de_topo(arvore: ast.Module):
    for no in arvore.body:
        if isinstance(no, (ast.FunctionDef, ast.AsyncFunctionDef)):
            yield no.name, no
        elif isinstance(no, ast.ClassDef):
            for filho in no.body:
                if isinstance(filho, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    yield f"{no.name}.{filho.name}", filho


def nome_chamado(chamada: ast.Call) -> str:
    f = chamada.func
    if isinstance(f, ast.Name):
        return f.id
    if isinstance(f, ast.Attribute):
        partes = [f.attr]
        v = f.value
        while isinstance(v, ast.Attribute):
            partes.append(v.attr)
            v = v.value
        if isinstance(v, ast.Name):
            partes.append(v.id)
        return ".".join(reversed(partes))
    return ""


def listar_funcoes(arquivo: Path) -> None:
    arvore = ast.parse(arquivo.read_text(encoding="utf-8"), filename=str(arquivo))
    modulo_map = nomes_importados(arvore.body)
    saida = csv.writer(sys.stdout, lineterminator="\n")
    saida.writerow([
        "funcao", "linha", "async", "criterio_integracao", "criterio_banco", "criterio_orquestracao",
        "critica", "chamadas_logging", "blocos_except", "chamadas_print", "traceback_print_exc",
        "registro_em_job",
    ])
    for nome, no in funcoes_de_topo(arvore):
        mapa = dict(modulo_map)
        mapa.update(nomes_importados(no))  # imports feitos dentro da função
        usados = {n.id for n in ast.walk(no) if isinstance(n, ast.Name)}
        origens = {mapa[u] for u in usados if u in mapa}
        integracao = sorted(o for o in origens if o.split(".")[0] in MODULOS_INTEGRACAO)
        banco = sorted(origens & MODULOS_BANCO)
        simples = nome.split(".")[-1]
        orquestracao = simples.startswith(("run_", "schedule_", "_step_"))
        critica = bool(integracao or banco or orquestracao)
        chamadas = [nome_chamado(c) for c in ast.walk(no) if isinstance(c, ast.Call)]
        logging_ = [c for c in chamadas if c.split(".")[0] in NOMES_LOGGER and "." in c]
        excepts = sum(isinstance(n, ast.ExceptHandler) for n in ast.walk(no))
        prints = sum(c == "print" for c in chamadas)
        tb = sum(c == "traceback.print_exc" for c in chamadas)
        job = sum(c in {"_job_fail", "_job_update", "_job_done", "_fail_project", "update_job"} for c in chamadas)
        saida.writerow([
            nome, no.lineno, isinstance(no, ast.AsyncFunctionDef), ";".join(integracao), ";".join(banco),
            orquestracao, critica, len(logging_), excepts, prints, tb, job,
        ])


# ---------------------------------------------------------------- ficha de inspeção

def ficha_inspecao(funcoes_csv: Path) -> None:
    linhas = list(csv.DictReader(funcoes_csv.open(encoding="utf-8")))
    print("# M3.2.3 - Inspeção do inventário de funções\n")
    print("Ficha da inspeção da seção 4.6 do [Método do G3](../../../../docs/fase-3/metodo-g3.md). "
          "Criada por `extrair.py ficha` a partir de `funcoes.csv` e nunca sobrescrita pelo script. "
          "Cada avaliador preenche só a própria coluna com `ok` ou com o erro encontrado "
          "(crítica indevida, crítica não marcada, chamada a `logging` não contada), sem ver a coluna do outro.\n")
    print("| Avaliador | Data | Sistema |\n|-----------|------|---------|\n| A1 | | |\n| A2 | | |\n")
    print("| Função | Linha | Crítica no inventário | Chamadas a `logging` | A1 | A2 | consenso | decidido_por |")
    print("|--------|------:|:---------------------:|:--------------------:|----|----|----------|--------------|")
    for l in linhas:
        critica = "sim" if l["critica"] == "True" else "não"
        print(f"| `{l['funcao']}` | {l['linha']} | {critica} | {l['chamadas_logging']} | | | | |")


if __name__ == "__main__":
    modo = sys.argv[1]
    if modo == "imports":
        listar_imports(Path(sys.argv[2]), sys.argv[3])
    elif modo == "funcoes":
        listar_funcoes(Path(sys.argv[2]))
    elif modo == "ficha":
        ficha_inspecao(Path(sys.argv[2]))
    else:
        sys.exit(f"modo desconhecido: {modo}")
