#!/usr/bin/env bash
# Coleta das métricas do G3 (M3.1.1 a M3.3.1). Método: docs/fase-3/metodo-g3.md
#
# Uso:
#   dados/avaliacao/G3/coletar.sh <clone do fork LucasAvelar2711/Vicky>
#
# O clone não é alterado: o commit avaliado é exportado com `git archive` para
# uma pasta de trabalho temporária, e todas as ferramentas rodam nessa cópia.
# As saídas brutas vão para dados/avaliacao/G3/M3.x.y/ e o cálculo é feito por
# calcular.py, que só lê essas saídas.
set -euo pipefail

COMMIT="${COMMIT:-c2ae5704b9770fbc33156fb3f457c4e8c63e5007}"
PYTHON_VERSAO="3.12"

REPO_VICKY="$(cd "${1:?informe o caminho do clone do fork Vicky}" && pwd)"
AQUI="$(cd "$(dirname "$0")" && pwd)"
TRAB="${TRAB:-$(mktemp -d "${TMPDIR:-/tmp}/vicky-g3.XXXXXX")}"
CODIGO="$TRAB/codigo"

echo "Commit avaliado: $COMMIT"
echo "Pasta de trabalho: $TRAB"

# 1. Cópia do commit, sem .git e sem nenhum arquivo local do clone
git -C "$REPO_VICKY" cat-file -e "${COMMIT}^{commit}"
rm -rf "$CODIGO" && mkdir -p "$CODIGO"
git -C "$REPO_VICKY" archive "$COMMIT" | tar -x -C "$CODIGO"

# 2. Ambientes isolados, instalados de lockfile com hash
uv venv -q --python "$PYTHON_VERSAO" "$TRAB/venv-ferramentas"
uv pip install -q --python "$TRAB/venv-ferramentas/bin/python" --require-hashes -r "$AQUI/ferramentas.lock"
uv venv -q --python "$PYTHON_VERSAO" "$TRAB/venv-testes"
uv pip install -q --python "$TRAB/venv-testes/bin/python" --require-hashes -r "$CODIGO/requirements.lock"
uv pip install -q --python "$TRAB/venv-testes/bin/python" --require-hashes -r "$AQUI/testes.lock"

F="$TRAB/venv-ferramentas/bin"
T="$TRAB/venv-testes/bin"
cd "$CODIGO"

# 3. Registro do ambiente (vai para cada pasta de métrica)
{
  echo "data_coleta=$(TZ=America/Sao_Paulo date '+%Y-%m-%d %H:%M %z')"
  echo "commit_vicky=$COMMIT"
  echo "data_commit=$(git -C "$REPO_VICKY" log -1 --format=%cd --date=iso "$COMMIT")"
  echo "so=$(uname -srm)"
  if command -v sw_vers >/dev/null; then echo "macos=$(sw_vers -productVersion)"; fi
  echo "uv=$(uv --version)"
  echo "python=$("$F/python" --version 2>&1)"
  echo "radon=$("$F/radon" --version)"
  echo "flake8=$("$F/flake8" --version | head -1)"
  echo "pylint=$("$F/pylint" --version | head -1)"
  echo "pytest=$("$T/python" -m pytest --version 2>&1 | head -1)"
  echo "pytest-cov=$("$T/python" -c 'import importlib.metadata as m; print(m.version("pytest-cov"))')"
  echo "coverage=$("$T/python" -c 'import coverage; print(coverage.__version__)')"
} > "$TRAB/ambiente.txt"
for m in M3.1.1 M3.1.2 M3.2.1 M3.2.2 M3.2.3 M3.3.1; do
  mkdir -p "$AQUI/$m"
  cp "$TRAB/ambiente.txt" "$AQUI/$m/ambiente.txt"
done

# Lista única de arquivos .py do pacote: denominador de M3.1.1 e M3.2.1
find src/vicky -name '*.py' -type f | LC_ALL=C sort > "$AQUI/M3.1.1/arquivos-py.txt"
cp "$AQUI/M3.1.1/arquivos-py.txt" "$AQUI/M3.2.1/arquivos-py.txt"

# M3.1.1 - imports internos (AST)
"$F/python" -I "$AQUI/extrair.py" imports src vicky > "$AQUI/M3.1.1/imports.csv"

# M3.1.2 - complexidade ciclomática do orquestrador
"$F/radon" cc src/vicky/pipeline.py -s -a > "$AQUI/M3.1.2/radon-cc.txt"
"$F/radon" cc src/vicky/pipeline.py -s -j > "$AQUI/M3.1.2/radon-cc.json"

# M3.2.1 - PEP 8 com a configuração padrão (--isolated ignora qualquer arquivo de configuração)
# flake8 sai com código 1 quando encontra violação; isso é resultado, não erro.
"$F/flake8" --isolated src/vicky/ --count --statistics > "$AQUI/M3.2.1/flake8-statistics.txt" || true
"$F/flake8" --isolated src/vicky/ > "$AQUI/M3.2.1/flake8-violacoes.txt" || true

# M3.2.2 - código duplicado (pylint, configuração padrão) e total de linhas (radon raw)
VAZIO="$TRAB/pylintrc-vazio"; : > "$VAZIO"
"$F/pylint" --rcfile="$VAZIO" --disable=all --enable=duplicate-code src/vicky/ \
  > "$AQUI/M3.2.2/pylint-duplicate-code.txt" || true
"$F/radon" raw src/vicky -s > "$AQUI/M3.2.2/radon-raw.txt"
"$F/radon" raw src/vicky -j > "$AQUI/M3.2.2/radon-raw.json"

# M3.2.3 - inventário das funções do orquestrador para a inspeção de logs
"$F/python" -I "$AQUI/extrair.py" funcoes src/vicky/pipeline.py > "$AQUI/M3.2.3/funcoes.csv"
grep -rn -E 'import logging|getLogger' src/vicky > "$AQUI/M3.2.3/grep-logging.txt" || true
# A ficha de inspeção é criada uma vez e nunca sobrescrita (é preenchida por A1 e A2)
if [ ! -f "$AQUI/M3.2.3/inspecao.md" ]; then
  "$F/python" -I "$AQUI/extrair.py" ficha "$AQUI/M3.2.3/funcoes.csv" > "$AQUI/M3.2.3/inspecao.md"
fi

# M3.3.1 - cobertura de linhas da suíte offline (a mesma do `make test` do VICKY)
# DATABASE_URL vazia: o conftest monta SQLite descartável e bloqueia rede.
set +e
DATABASE_URL= "$T/python" -m pytest --cov=src/vicky/ tests/ -p no:cacheprovider -rfEs \
  --junitxml="$AQUI/M3.3.1/junit.xml" \
  --cov-report=term --cov-report=json:"$AQUI/M3.3.1/coverage.json" \
  > "$AQUI/M3.3.1/pytest-cov.txt" 2>&1
echo "codigo_saida_pytest=$?" >> "$AQUI/M3.3.1/ambiente.txt"
set -e

# 4. Cálculo
"$F/python" -I "$AQUI/calcular.py" "$AQUI"
echo "Coleta concluída. Resultados em $AQUI/resultados.csv"
