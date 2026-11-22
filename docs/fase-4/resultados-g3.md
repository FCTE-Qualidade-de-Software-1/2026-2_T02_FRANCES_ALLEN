# Resultados do G3 (manutenibilidade)

Esta página reúne o resultado das seis métricas do G3 coletadas no código-fonte do VICKY, conforme o [Método do G3](../fase-3/metodo-g3.md). Os níveis, as regras de agregação e o julgamento seguem [níveis e julgamento](../fase-2/niveis-e-julgamento.md), fixados antes da coleta.

## 1. Execução da coleta

| Campo | Valor |
|-------|-------|
| Período | Coleta principal (A1) em 14/11/2026; repetição independente (A2) em 18/11/2026 |
| Código avaliado | Fork privado `LucasAvelar2711/Vicky`, commit `c2ae5704b9770fbc33156fb3f457c4e8c63e5007` (`c2ae570`), de 29/09/2026 |
| Escopo medido | `src/vicky/` (38 arquivos `.py`) e `tests/` (1.034 testes) |
| Ferramentas | Python 3.12.13, `radon` 6.0.1, `flake8` 7.5.0, `pylint` 4.1.4, `pytest` 9.2.0, `pytest-cov` 7.1.0 (`coverage` 7.17.3), fixados por lockfile com hash |
| Avaliadores | A1 Lucas Avelar; A2 Guilherme Moura |
| Repetição independente | Confirmada em 18/11/2026 por A2 em outra máquina e outro sistema operacional (Linux vs. macOS): todas as seis métricas reproduziram exatamente os mesmos valores de A, B e nível ([`repeticao.md`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/blob/main/dados/avaliacao/G3/repeticao.md)) |
| Inspeção de M3.2.3 | Conferência das 47 funções de `pipeline.py` em [`inspecao.md`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/blob/main/dados/avaliacao/G3/M3.2.3/inspecao.md): 100% de concordância com o inventário automatizado (33 críticas, 0 chamadas a `logging`) |
| Itens não coletados | Nenhum (6 de 6 métricas medidas) |
| Desvios do método | Nenhum |

## 2. Valores medidos

| Métrica | Medida (ISO/IEC 25023:2016) | A | B | Valor | Nível | Pontos | Dados brutos |
|---------|-----------------------------|:-:|:-:|:-----:|:-----:|:------:|--------------|
| M3.1.1 | Adaptada de MMo-1-G | 78 | 38 | 2,05 | Excelente | 3 | [M3.1.1/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G3/M3.1.1) |
| M3.1.2 | MMo-2-S | 11 | 47 | 76,6% | Aceitável | 1 | [M3.1.2/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G3/M3.1.2) |
| M3.2.1 | Medida adicional | 2 | 38 | 5,3% | Insatisfatório | 0 | [M3.2.1/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G3/M3.2.1) |
| M3.2.2 | Medida adicional | 28 | 18.927 | 0,15% | Excelente | 3 | [M3.2.2/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G3/M3.2.2) |
| M3.2.3 | Adaptada de MAn-1-G | 0 | 33 | 0,0% | Insatisfatório | 0 | [M3.2.3/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G3/M3.2.3) |
| M3.3.1 | Adaptada de MTe-1-G | 4.750 | 7.519 | 63,17% | Aceitável | 1 | [M3.3.1/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G3/M3.3.1) |

## 3. Principais achados

| Métrica | Achado | Evidência |
|---------|--------|-----------|
| M3.1.1 | Baixo acoplamento entre arquivos: média de 2,05 dependências internas distintas por módulo, indicando boa separação estrutural entre os 38 arquivos do pacote. | `M3.1.1/imports.csv`, `M3.1.1/resultado.md` |
| M3.1.2 | 11 de 47 funções de `pipeline.py` (23,4%) excedem CC > 10. O problema se concentra em cinco funções acima de CC 30, com pico crítico em `run_full_pipeline` (**CC = 84**, nota F), seguida por `_step_rotate_terms` (45), `_build_expansion_queries` (40), `_step_verify_bloqueante` (38) e `_step_search` (31). | `M3.1.2/radon-cc.txt`, `M3.1.2/radon-cc.json` |
| M3.2.1 | Apenas 2 dos 38 arquivos passam sem violações (`src/vicky/__init__.py` e `src/vicky/web/__init__.py`). Das 1.916 violações totais, **1.777 (92,7%)** são linhas acima de 79 caracteres (`E501`), 117 (6,1%) são outras regras de estilo/formatação (`E701`, `E702`, `E127`, `E402`, entre outras) e **22 (1,1%)** são alertas do `pyflakes` (12 imports sem uso `F401`, 5 redefinições de `re` `F811` em `pipeline.py`, 3 variáveis atribuídas sem uso `F841` e 2 f-strings sem placeholder `F541`). | `M3.2.1/flake8-statistics.txt`, `M3.2.1/flake8-violacoes.txt` |
| M3.2.2 | Duplicação residual: apenas 28 linhas em 18.927 LOC (0,15%), restritas a dois blocos `R0801` — mapeamento de 8 campos de artigos entre `web/app.py` e `xlsx_report.py` e 6 linhas de estilo de tabela do ReportLab entre `pdf_report.py` e `pdf_resumo.py`. | `M3.2.2/pylint-duplicate-code.txt`, `M3.2.2/radon-raw.txt` |
| M3.2.3 | Ausência total da biblioteca `logging` em todo o pacote `src/vicky/` (`grep-logging.txt` vazio). Nenhuma das 33 funções críticas de `pipeline.py` registra sucesso ou exceção via `logging`; a rastreabilidade depende de chamadas ad hoc a `print` (21 só em `run_full_pipeline`), `traceback.print_exc()` (2 em `run_full_pipeline`) e atualizações de status na tabela `jobs`. | `M3.2.3/funcoes.csv`, `M3.2.3/grep-logging.txt`, `M3.2.3/inspecao.md` |
| M3.3.1 | Suíte offline íntegra (1.002 aprovados, 0 falhas, 27 pulados por dependência externa, 5 `xfail`), porém com forte desequilíbrio entre camadas: `src/vicky/web/` atinge **87,8%** de cobertura (3.075/3.503 comandos), enquanto o núcleo do produto cai para **41,7%** (1.675/4.016). Sozinho, `pipeline.py` tem **24% de cobertura** e responde por **905 das 2.769 linhas não cobertas (32,7% do déficit total)**, seguido por `cli.py` (19%), `sources/scholar.py` (13%), `discovery.py` (25%) e `scraper.py` (20%). | `M3.3.1/pytest-cov.txt`, `M3.3.1/coverage.json` |

### Síntese diagnóstica

Os dados apontam que a dívida técnica do backend do VICKY não está espalhada de forma homogênea, mas **converge no orquestrador `src/vicky/pipeline.py`**. Enquanto a camada web (rotas, autenticação, créditos e cobrança) possui alta cobertura de testes e o pacote mantém baixo acoplamento e duplicação quase nula, o orquestrador reúne simultaneamente os três maiores riscos de manutenção identificados: complexidade ciclomática extrema (`run_full_pipeline` em CC 84), ausência completa de `logging` estruturado (0/33 funções críticas) e cobertura de testes de apenas 24%.

## 4. Hipóteses

Uma hipótese é confirmada quando o valor medido coincide com a previsão formulada na Fase 2. O resultado não altera o julgamento do objetivo, mas verifica a acurácia da leitura preliminar da equipe.

| Hipótese | Previsão (Fase 2) | Medido | Resultado |
|----------|-------------------|--------|-----------|
| H3.1 | Acoplamento moderado e porção significativa das funções centrais de orquestração excedendo o limite de complexidade ciclomática. | M3.1.1 = 2,05 (Excelente, abaixo do esperado para "moderado"); M3.1.2 = 76,6% (11 de 47 funções com CC > 10, Aceitável). | **Parcialmente confirmada** (acoplamento melhor que o previsto; concentração de complexidade confirmada). |
| H3.2 | Sem duplicação estrutural significativa, conformidade PEP 8 na maior parte do pacote e baixa completude de logs nas integrações principais. | M3.2.2 = 0,15% (Excelente); M3.2.1 = 5,3% (Insatisfatório); M3.2.3 = 0,0% (Insatisfatório). | **Parcialmente confirmada** (duplicação e logs confirmados; previsão sobre PEP 8 **refutada**). |
| H3.3 | Cobertura de testes automatizados de 70% ou mais das linhas testáveis de `src/vicky/`. | M3.3.1 = 63,17% (4.750 de 7.519 linhas executáveis, Aceitável). | **Refutada** (6,83 p.p. abaixo do piso de 70%). |

## 5. Respostas às questões e julgamento do G3

As regras são as da seção 4 de [níveis e julgamento](../fase-2/niveis-e-julgamento.md#4-regras-do-g3-manutenibilidade): cada questão recebe a média dos pontos (0 a 3) de suas métricas — Insatisfatório (0,00 a < 1,00), Aceitável (1,00 a < 1,75), Bom (1,75 a < 2,50) e Excelente (2,50 a 3,00). M3.1.2 limita Q3.1 a Aceitável se ficar em Insatisfatório, e Q3.3 limita G3 a Aceitável se ficar em Insatisfatório.

| Questão | Métricas e cálculo | Pontuação | Nível | Resposta |
|---------|--------------------|:---------:|:-----:|----------|
| Q3.1 — Modularidade | M3.1.1 (3) e M3.1.2 (1) → média `(3 + 1) / 2`. Regra bloqueadora de M3.1.2 não acionada (nível Aceitável). | 2,00 | **Bom** | O acoplamento entre arquivos é baixo (2,05 imports internos/módulo), preservando a separação entre componentes. Contudo, a complexidade estrutural do orquestrador `pipeline.py` é apenas aceitável (76,6% adequadas), com 11 funções acima de CC 10 e gargalo severo em `run_full_pipeline` (CC 84). |
| Q3.2 — Analisabilidade | M3.2.1 (0), M3.2.2 (3) e M3.2.3 (0) → média `(0 + 3 + 0) / 3`. | 1,00 | **Aceitável** | A densidade de código duplicado é excelente (0,15%), mas a analisabilidade fica comprometida pela ausência completa de `logging` estruturado nas 33 funções críticas (0,0%) e pela baixa conformidade ao PEP 8 padrão (5,3%, dominada por linhas > 79 caracteres). |
| Q3.3 — Testabilidade | M3.3.1 (1) → métrica única. | 1,00 | **Aceitável** | A suíte executa 1.002 testes sem falhas, mas cobre 63,17% das linhas executáveis — abaixo da meta de 70% (H3.3). A cobertura é alta na camada web (87,8%), mas insuficiente no núcleo de orquestração (`pipeline.py` com 24%) e nas fontes de busca, elevando o risco de regressão em refatorações. |

### Julgamento do objetivo G3

- **Métricas medidas:** 6 de 6.
- **Perfil das questões:** Q3.1 **Bom (2,00)** · Q3.2 **Aceitável (1,00)** · Q3.3 **Aceitável (1,00)**.
- **Pontuação global de G3:** `(2,00 + 1,00 + 1,00) / 3 = 1,33` → **Aceitável** (regra de limitação de Q3.3 não acionada).
- **Julgamento do produto em Manutenibilidade (G3):** **Atende parcialmente**.

## 6. Limitações

- **Testes pulados por dependência externa (M3.3.1):** 27 dos 1.034 testes foram pulados de forma controlada (20 de Postgres local, 6 de integração real da Stripe e 1 dependente de arquivo externo). As linhas exercitadas exclusivamente por esses testes contam como não cobertas, afetando parcialmente `db.py` (51%) e `storage.py` (62%), mas não explicam o déficit principal de `pipeline.py` (24%).
- **Cobertura de linhas vs. cobertura de ramos (M3.3.1):** A medição segue a ficha da Fase 2 (cobertura de linhas). Desvios condicionais não exercitados em ambos os ramos (`True`/`False`) não são capturados.
- **Granularidade por arquivo no PEP 8 (M3.2.1):** A fórmula binária por arquivo penaliza igualmente um módulo com uma única linha de 80 caracteres e outro com dezenas de violações. Ainda assim, a análise por código em `flake8-statistics.txt` mostra que 92,7% das violações decorrem do limite de 79 caracteres (`E501`) e apenas 1,1% são alertas lógicos (`F`).
- **Fotografia estática:** Todos os valores refletem o commit `c2ae570` (29/09/2026), escolhido para manter consistência com as hipóteses do G3 e a inspeção do G2.

## 7. Sugestão de ação de melhoria (candidata do G3)

Esta seção registra a proposta de melhoria derivada exclusivamente dos resultados do G3. A decisão final sobre qual intervenção executar deve considerar também as candidatas levantadas nas avaliações de G1 e G2.

### Alvo e justificativa

Os dados da Fase 4 mostram que a dívida técnica de manutenibilidade do backend não está distribuída de forma uniforme, mas converge em `src/vicky/pipeline.py`. O módulo concentra simultaneamente:

- **Maior gargalo de complexidade (M3.1.2):** 11 das 47 funções excedem CC 10, com pico extremo em `run_full_pipeline` (**CC = 84**, nota F no `radon`).
- **Ausência total de observabilidade estruturada (M3.2.3):** 0 de 33 funções críticas utilizam `logging`; o diagnóstico depende de chamadas ad hoc a `print` (21 apenas em `run_full_pipeline`) e `traceback.print_exc()`.
- **Maior déficit de cobertura de testes (M3.3.1):** enquanto a camada web (`src/vicky/web/`) atinge 87,8% de cobertura, `pipeline.py` cobre apenas **24%**, respondendo sozinho por 905 das 2.769 linhas não cobertas do backend (32,7% do déficit total).

A outra métrica classificada como Insatisfatória, conformidade ao PEP 8 (**M3.2.1 = 5,3%**), foi mantida como recomendação secundária de processo: 92,7% das violações (1.777 de 1.916) correspondem apenas ao limite de 79 caracteres (`E501`), resolvíveis pela adoção de um formatador/linter automatizado na esteira de desenvolvimento, sem ganho estrutural na arquitetura do orquestrador.

### Escopo proposto

A intervenção recomendada sobre o commit `c2ae570` combina três frentes integradas em `src/vicky/pipeline.py`:

1. **Decomposição de `run_full_pipeline` (foco em M3.1.2):** extrair o estado do loop e os blocos lógicos da orquestração (fases iniciais, tratamento de estagnação, análise em lotes, rebalanceamento e expansão) para funções auxiliares menores com CC ≤ 10, reduzindo o maior ponto de fragilidade estrutural do backend.
2. **Instrumentação com `logging` nas funções críticas (foco em M3.2.3):** substituir `print` e `traceback.print_exc()` por chamadas estruturadas do módulo `logging` (`logger.info`, `logger.warning`, `logger.exception`), cobrindo tanto `run_full_pipeline` quanto as demais funções críticas de `pipeline.py` que já possuem tratamento de exceção (17 de 33 funções críticas possuem blocos `try/except`).
3. **Testes unitários para as funções extraídas (foco em M3.3.1):** cobrir os novos auxiliares de orquestração na suíte offline (`tests/`), mitigando o risco de regressão imposto pela cobertura atual de 24% em `pipeline.py`.

### Impacto esperado e verificação (antes e depois)

Caso esta candidata seja selecionada pela equipe, a verificação segue exatamente o [Método do G3](../fase-3/metodo-g3.md), executando `dados/avaliacao/G3/coletar.sh` sobre o novo commit da refatoração para comparar os valores de forma reprodutível:

| Métrica | Antes (`c2ae570`) | Impacto esperado |
|---------|-------------------|------------------|
| M3.1.2 (Complexidade) | 76,6% (Aceitável; máx. CC = 84) | Queda da complexidade máxima de `run_full_pipeline` de 84 para ≤ 10 e aumento da proporção de funções adequadas (acima de 80%). |
| M3.2.3 (Logs) | 0,0% (0/33, Insatisfatório) | Elevação para ≥ 50% ao instrumentar as 17 funções críticas com tratamento de exceção (saindo de Insatisfatório para Aceitável, ou Bom se estendida a ≥ 25 críticas). |
| M3.3.1 (Cobertura) | 63,17% geral / 24% em `pipeline.py` | Aumento da cobertura de `pipeline.py` e da cobertura global, sem regressão nos 1.002 testes aprovados da suíte offline. |

Como ação complementar de baixo custo (sem alterar a prioridade acima), recomenda-se corrigir os 22 alertas lógicos do `pyflakes` (imports e variáveis não usadas em `flake8-statistics.txt`) e adotar verificação automática de estilo no fluxo de *pull requests*.

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 20/11/2026 | Resultados consolidados do G3, análise dos achados, confronto de hipóteses, respostas de Q3.1 a Q3.3 e julgamento formal | Guilherme Moura | - |