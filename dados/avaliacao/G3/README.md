# Dados brutos do objetivo G3 (manutenibilidade)

Cada métrica de G3 tem uma pasta própria, com o ID da métrica como nome. A ficha de cada uma está em [Especificação das métricas](../../../docs/fase-2/especificacao-das-metricas.md), e o passo a passo da coleta está no [Método do G3](../../../docs/fase-3/metodo-g3.md). Esta pasta só recebe dados reais de coleta; nada aqui é simulado. Todos os arquivos das pastas `M3.x.y/` saem da execução de `coletar.sh`, sem edição à mão.

## Código avaliado

| Item | Valor |
|------|-------|
| Repositório | Fork privado `LucasAvelar2711/Vicky` |
| Commit | `c2ae5704b9770fbc33156fb3f457c4e8c63e5007` (`c2ae570`), de 29/09/2026 20:51 (horário de Brasília) |
| Escopo | `src/vicky/` (38 arquivos `.py`) e `tests/` |

## Scripts

| Arquivo | Função |
|---------|--------|
| `coletar.sh` | Exporta o commit para uma pasta temporária, cria os ambientes, roda as ferramentas, grava as saídas brutas e chama `calcular.py` |
| `extrair.py` | Extração por AST, sem executar o código: imports internos (M3.1.1) e inventário das funções de `pipeline.py` (M3.2.3) |
| `calcular.py` | Lê só as saídas brutas e gera `resultado.md` em cada pasta e `resultados.csv` |
| `ferramentas.in` e `ferramentas.lock` | Versões de radon, flake8 e pylint, com hash |
| `testes.in` e `testes.lock` | Versões de pytest e pytest-cov, com hash, compatíveis com o `requirements.lock` do VICKY |

## Conteúdo das pastas

Toda pasta tem `ambiente.txt` (data e hora da coleta, commit, sistema, versões de Python e das ferramentas) e `resultado.md` (valor, A, B e nível pela Fase 2).

| Pasta | Saídas brutas |
|-------|---------------|
| `M3.1.1/` | `arquivos-py.txt` (lista dos arquivos, denominador) e `imports.csv` (um import interno por linha: arquivo, linha, texto do import e módulo de destino) |
| `M3.1.2/` | `radon-cc.txt` (saída do comando da Fase 2) e `radon-cc.json` (mesma análise em JSON, usada no cálculo) |
| `M3.2.1/` | `arquivos-py.txt`, `flake8-statistics.txt` (comando da Fase 2) e `flake8-violacoes.txt` (uma violação por linha, usada para contar os arquivos) |
| `M3.2.2/` | `pylint-duplicate-code.txt` (trechos duplicados), `radon-raw.txt` e `radon-raw.json` (linhas por arquivo) |
| `M3.2.3/` | `funcoes.csv` (inventário das funções de `pipeline.py` com os critérios de função crítica e as chamadas de registro) e `grep-logging.txt` (busca por `import logging` e `getLogger` no pacote; vazio quando não há ocorrência) e `inspecao.md` (conferência humana do inventário) |
| `M3.3.1/` | `pytest-cov.txt` (saída completa do pytest com o relatório de cobertura), `coverage.json` (cobertura por arquivo) e `junit.xml` (resultado de cada teste) |

O arquivo `resultados.csv`, nesta pasta, junta o valor e o nível das seis métricas.

## Como repetir

```bash
git clone https://github.com/LucasAvelar2711/Vicky.git ~/vicky-fork
dados/avaliacao/G3/coletar.sh ~/vicky-fork
git diff --stat dados/avaliacao/G3/
```

A repetição só confirma a coleta se `resultados.csv` não mudar além da coluna de data. Os arquivos de saída bruta mudam em data, hora, caminho da pasta temporária, tempo de execução e ordem das chaves em `radon-cc.json`, e isso é esperado. Detalhes, pré-requisitos e tratamento de divergência estão no [Método do G3](../../../docs/fase-3/metodo-g3.md).
