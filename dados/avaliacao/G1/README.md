# Dados brutos do objetivo G1 (adequação funcional)

Cada métrica de G1 tem uma pasta própria, com o ID da métrica como nome. A ficha de cada uma está em [Especificação das métricas](../../../docs/fase-2/especificacao-das-metricas.md), e o passo a passo de coleta, com o nome e as colunas de cada planilha, está no [Método do G1](../../../docs/fase-3/metodo-g1.md). Esta pasta só recebe dados reais de coleta; nada aqui é simulado.

| Pasta ou arquivo | Conteúdo esperado |
|------------------|-------------------|
| `execucoes.csv` | Uma linha por triagem (T1 a T4, E1, E2, T1-B, T3-B), inclusive as que falharam: configuração, data e hora, créditos antes e depois, versão dos Termos |
| `M1.1.1/` | Top 30 de cada tema (T1 a T4), lista de estudos incluídos da revisão de referência, PICO gerado, exportação original do VICKY e correspondências manuais |
| `M1.1.2/` | Resultado da consulta de cada estudo da revisão de referência no PubMed, SciELO e Google Acadêmico |
| `M1.2.1/` | Caso de teste e captura de tela de cada função (F01 a F09), com a classificação em operante, parcial ou ausente |
| `M1.3.1/` | Ficha cega e chave de cada tema, piloto de calibração, fichas de julgamento de relevância dos dois avaliadores, consolidado e registro do kappa |
| `M1.3.2/` | Planilha de conferência dos 10 itens por tema contra a página oficial de cada artigo |
| `M1.4.1/` | Notas da rubrica dos dois avaliadores em T1 e T2 (o Quality Score vem do Top 30 em `M1.1.1/`) |
| `M1.5.1/` | Lista de cada execução com filtros (E1 e E2), PICO gerado e a conferência item a item |
| `M1.5.2/` | Segundo Top 30 (B) de cada tema repetido; o primeiro (A) é o de `M1.1.1/` |
| `modelos/` | Cabeçalho de cada planilha, sem dado. Copiar para a pasta da métrica com o nome indicado no método |
| `calcular_g1.py` | Script de cálculo de todas as métricas, dos níveis e da agregação do G1 |
| `referencias/referencias.md` | Título, DOI, PMID, PMCID, link e número de incluídos de cada revisão de referência e das reservas, conferidos em 14/11/2026 |

## Cálculo

A partir da raiz do repositório, com Python 3.9 ou superior e sem dependência externa:

```bash
python3 dados/avaliacao/G1/calcular_g1.py calcular --saida dados/avaliacao/G1/resultados.csv
python3 dados/avaliacao/G1/calcular_g1.py ficha-cega --tema T1    # ficha cega de M1.3.1 e M1.4.1
python3 dados/avaliacao/G1/calcular_g1.py amostra --tema T1       # posições da amostra de M1.3.2
```

Arquivo ausente deixa a métrica como "não coletado"; o script não estima valores. Para testar o script, use uma pasta fora do repositório com a opção `--pasta`, que vem **antes** do subcomando:

```bash
python3 dados/avaliacao/G1/calcular_g1.py --pasta /caminho/da/pasta-de-teste calcular
python3 dados/avaliacao/G1/calcular_g1.py --pasta /caminho/da/pasta-de-teste ficha-cega --tema T1
```

A pasta de teste precisa ter a mesma estrutura (`M1.1.1/` a `M1.5.2/`). Dado de teste não entra aqui.

O G1 não tem participantes externos. Os avaliadores são integrantes da equipe e aparecem nas planilhas pelo papel (C, A1, A2, A3); a relação entre papel e integrante, com o nome, fica em `M1.3.1/coleta.md`, como descreve o [README da pasta de dados](../../README.md). Registre a data da coleta e a versão do VICKY em produção em `execucoes.csv`.
