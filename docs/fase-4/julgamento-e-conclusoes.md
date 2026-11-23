# Julgamento e conclusões

## 1. Introdução e escopo da consolidação

Esta página reúne o julgamento consolidado da qualidade do **VICKY** (<https://vicky.synaptha.com/>) na **Fase 4** a partir das três características adaptadas da **ISO/IEC 25010:2023** e do método **GQM**:

- **G1 - Adequação funcional** (perspectiva dos estudantes de medicina; foco em completude, correção e pertinência funcional).
- **G2 - Capacidade de interação** (perspectiva dos estudantes de medicina; foco em reconhecimento da adequação, facilidade de aprendizado, operabilidade, proteção contra erro do usuário, engajamento do usuário, assistência ao usuário e autodescritividade).
- **G3 - Manutenibilidade** (perspectiva da equipe de desenvolvimento / arquitetos; foco em modularidade, analisabilidade e testabilidade no backend em Python, `src/vicky/` e `tests/`).

Os limiares e regras de julgamento seguem [Níveis de pontuação e critérios de julgamento](../fase-2/niveis-e-julgamento.md), e os objetivos, questões e hipóteses seguem [Objetivos, questões e hipóteses](../fase-2/objetivos-questoes-hipoteses.md).

> **Situação dos insumos na consolidação:**
> - **G1 (Adequação funcional):** dados consolidados presentes (`resultados-g1.md`, coleta concluída em 20/11/2026, 8 de 8 métricas medidas; `M1.5.1` calculada sobre `E1` com `E2` sem lista).
> - **G2 (Capacidade de interação):** dados por inspeção presentes (`resultados-g2-inspecao.md` v0.6, 8 métricas inspecionadas e `Q2.7` atualizada) e com usuários (`resultados-g2-usuarios.md`, PR #40: `M2.5.1` e `M2.7.2` com 3 participantes, resultados indicativos). `M2.6.1` e `M2.6.2` (#28) não foram coletadas até 22/11/2026 e constam como **A definir**.
> - **G3 (Manutenibilidade):** dados consolidados presentes (`resultados-g3.md`, commit `c2ae570`, 6 de 6 métricas medidas, com repetição independente confirmada por A1 e A2).

---

## 2. Julgamento final de cada objetivo (G1, G2 e G3)

Sem colapsar as características em uma nota única global, cada objetivo é avaliado segundo suas respectivas regras da Fase 2 com base nas evidências disponíveis.

### 2.1 Objetivo G1 - Adequação funcional

Avaliado em `resultados-g1.md` (coleta de 17/11/2026 a 20/11/2026; 8 de 8 métricas medidas, com `M1.5.1` calculada sobre `E1` após `E2` não retornar lista em duas execuções no SciELO).

| Questão / Métrica / Critério | Resultado / Valor medido | Nível / Pontuação | Julgamento / Situação | Evidências / Observações |
| :--- | :---: | :---: | :---: | :--- |
| **Q1.1** (`M1.1.1`, `M1.1.2`) | `M1.1.1`: `0,195` (T1 `0,250`; T2 `0,143`; T3 `0,100`; T4 `0,286`); `M1.1.2`: `0,195` | **Insatisfatório** (`0,00`) | Crítica em Insatisfatório (teto Aceitável) | Recupera cerca de um quinto dos estudos da referência; `M1.1.2` igual a `M1.1.1` (todo resultado veio do PubMed) |
| **Q1.2** (`M1.2.1`) | `72,2%` (4 operantes, 5 parciais em F01-F09) | **Aceitável** (`1,00`) | Consolidado | Fluxo principal executável, mas 5 funções ficam parciais; recuperação de senha (F01) depende de e-mail manual |
| **Q1.3** (`M1.3.1`, `M1.3.2`) | `M1.3.1`: `24,7%` (Insatisfatório); `M1.3.2`: `100%` (40/40, Excelente) | **Aceitável** (`1,50`) | Crítica `M1.3.1` em Insatisfatório | Metadados e links íntegros (40/40), mas apenas ~1/4 dos itens do Top responde ao PICO; kappa entre `0,905` e `1,000` |
| **Q1.4** (`M1.4.1`) | Spearman `0,034` (T1 `-0,120`; T2 `0,187`) | **Insatisfatório** (`0,00`) | Consolidado | Ranking pelo Quality Score não acompanha a rubrica metodológica, mesmo com alta concordância entre A1 e A2 |
| **Q1.5** (`M1.5.1`, `M1.5.2`) | `M1.5.1`: `3,3%` (1/30 em `E1`; `E2` sem lista); `M1.5.2`: `0,586` (T1 `0,579`; T3 `0,593`) | **Insatisfatório** (`0,50`) | Consolidado (`E2` sem retorno) | Apenas 1/30 atende ao filtro de tipo de estudo em `E1`; repetição em 48h mantém ~59% de sobreposição (Jaccard `0,586`) |
| **Pontuação global de G1** | `(0,00 + 1,00 + 1,50 + 0,00 + 0,50) / 5 = 0,60` | **Insatisfatório** | Consolidado | Média das 5 questões na faixa Insatisfatório (`0,60`) |
| **Julgamento do produto (G1)** | 8 de 8 métricas medidas (`M1.5.1` na base `E1`) | - | **Não atende** | Pontuação global `0,60` (Insatisfatório), com falhas críticas em `M1.1.1` e `M1.3.1` e problemas em fontes, ranking e filtros |

### 2.2 Objetivo G2 - Capacidade de interação

A consolidação contempla as 8 métricas obtidas por inspeção (`resultados-g2-inspecao.md` v0.6) e as duas medidas com estudantes (`M2.5.1` e `M2.7.2`, em `resultados-g2-usuarios.md`, PR #40), calculadas com 3 participantes (`P01-P03` / `R01-R03`) e por isso indicativas. `M2.6.1` e `M2.6.2` permanecem **A definir** até a coleta (#28).

| Questão / Métrica | Valor / Resultado observado | Nível / Situação | Evidências e regras aplicadas |
| :--- | :---: | :---: | :--- |
| **Q2.1** - Reconhecimento da adequação (`M2.1.1`) | `M2.1.1`: `9/10` (`90,0%`) | **Bom** | Descreve 9 de 10 cenários (incluindo o limite do produto); Favoritos (`F07`) não aparece nas páginas públicas |
| **Q2.2** - Facilidade de aprendizado (`M2.2.1`, `M2.2.2`) | `M2.2.1`: `8/9` (`88,9%`, Bom); `M2.2.2`: `10/34` (`29,4%`, Insatisfatório) | **Aceitável** | Orientação cobre 8/9 funções (`F08` sem orientação de uso/paginação); `M2.2.2` em Insatisfatório rebaixa `Q2.2` de Bom para Aceitável |
| **Q2.3** - Operabilidade (`M2.3.1`, `M2.3.2`) | `M2.3.1`: `0,25` (`6/8`, Insatisfatório); `M2.3.2`: `77/117` (`65,8%`, Insatisfatório) | **Insatisfatório** | Menor nível entre `M2.3.1` e `M2.3.2`; 6/8 padrões comparáveis variam entre telas e 40/117 mensagens não são claras |
| **Q2.4** - Proteção contra erro (`M2.4.1`, `M2.4.2`) | `M2.4.1`: `4/6` (`66,7%`, Insatisfatório); `M2.4.2`: `2/6` (`33,3%`, Insatisfatório) | **Insatisfatório** | Ação paga (`A01`) traz aviso explícito ("CONSOME 1 CRÉDITO"), sem ação paga desprotegida; falhas em ações/entradas deixam `Q2.4` em Insatisfatório |
| **Q2.5** - Engajamento do usuário (`M2.5.1`) | `M2.5.1`: `2/5` (`40,0%`, Aceitável, indicativo) | **Aceitável** | Três respostas, com maioria de 2 de 3 pela `D14`; apenas painel inicial e Novo projeto foram agradáveis para a maioria. Prioridade secundária: não entra na contagem das 6 questões principais |
| **Q2.6** - Assistência ao usuário (`M2.6.1`, `M2.6.2`) | A definir (não coletadas até 22/11/2026) | **A definir** | Métricas executadas pelos avaliadores (`M2.6.1` e `M2.6.2`); regra exige atenção especial a `M2.6.1` (`F01`) e `M2.6.2` (contraste) |
| **Q2.7** - Autodescritividade (`M2.7.1`, `M2.7.2`) | `M2.7.1`: `3 de 4` (Bom); `M2.7.2`: `11/12` (`91,7%`, Excelente, indicativo) | **Excelente** | `M2.7.2` é a medida de referência, e `M2.7.1` em Bom não rebaixa `Q2.7`. Quality Score entendido pelos 3 participantes; o log auditável (`E11`) só por 1 de 3 |
| **Julgamento do objetivo G2** | 5 de 6 questões principais com nível (`Q2.6` pendente) | **Não atende** | `Q2.3` e `Q2.4` em Insatisfatório. Pela regra da Fase 2, duas ou mais questões principais em Insatisfatório levam a "Não atende", qualquer que venha a ser o nível de `Q2.6` |

### 2.3 Objetivo G3 - Manutenibilidade

Avaliado no commit `c2ae570` (`resultados-g3.md`, `src/vicky/` com 38 arquivos `.py` e `tests/` com 1.034 testes), com repetição independente confirmada por A1 e A2 em todas as 6 métricas.

| Questão / Métrica | Valor / Resultado medido | Nível / Pontos | Evidências e regras aplicadas |
| :--- | :---: | :---: | :--- |
| **Q3.1** - Modularidade (`M3.1.1`, `M3.1.2`) | `M3.1.1`: `2,05` (`78/38`, Excelente, 3 pts); `M3.1.2`: `76,6%` (`11/47` > CC 10, Aceitável, 1 pt) | **Bom** (`2,00`) | Média `(3 + 1) / 2 = 2,00`; bloqueio de `M3.1.2` não acionado, mas `run_full_pipeline` atinge CC = 84 |
| **Q3.2** - Analisabilidade (`M3.2.1`, `M3.2.2`, `M3.2.3`) | `M3.2.1`: `5,3%` (`2/38`, Insatisfatório, 0 pts); `M3.2.2`: `0,15%` (`28/18.927` LOC, Excelente, 3 pts); `M3.2.3`: `0,0%` (`0/33`, Insatisfatório, 0 pts) | **Aceitável** (`1,00`) | Média `(0 + 3 + 0) / 3 = 1,00`; 0/33 funções críticas usam `logging` e 92,7% das violações PEP 8 são `E501` (> 79 chars) |
| **Q3.3** - Testabilidade (`M3.3.1`) | `M3.3.1`: `63,17%` (`4.750/7.519` linhas executáveis, Aceitável, 1 pt) | **Aceitável** (`1,00`) | 1.002 aprovados offline; `web/` tem `87,8%` vs. `41,7%` no núcleo e `24%` em `pipeline.py` (`905/2.769` linhas não cobertas) |
| **Pontuação global de G3** | `(2,00 + 1,00 + 1,00) / 3 = 1,33` | **Aceitável** | Limitação de `Q3.3` não acionada; perfil: `Q3.1` Bom, `Q3.2` Aceitável, `Q3.3` Aceitável |
| **Julgamento do produto (G3)** | 6 de 6 métricas medidas | **Atende parcialmente** | Pontuação global `1,33` na faixa Aceitável |

---

## 3. Relação entre as três características, evidências e limitações (Premissa 1)

### 3.1 Convergências e relações apoiadas por evidências

- **Convergência de risco técnico e funcional em `src/vicky/pipeline.py` e nas fontes de busca (G1, G2 e G3):** os achados de G3 mostram que a dívida técnica do backend se concentra fortemente no orquestrador `pipeline.py`, que acumula pico de complexidade ciclomática (`run_full_pipeline` com CC = 84 em `M3.1.2`), ausência total de `logging` estruturado (`0/33` funções críticas em `M3.2.3`, apoiando-se em `print` e `traceback.print_exc()`, conforme os registros de coleta em `dados/avaliacao/G3/` que mapeiam as 17 funções com `try/except`) e baixa cobertura de testes (`24%` em `M3.3.1`, contra `87,8%` na camada `web/`). Em G1 (`resultados-g1.md` e arquivos de coleta em `dados/avaliacao/G1/`), o comportamento de execução e busca reflete fragilidades operacionais semelhantes: SciELO retornou 0 artigos em todas as execuções (deixando `E2` sem retorno após longas rotações de termos sem encerrar ou devolver lista), Google Acadêmico retornou 0 com erros nas strings (registrados nos dados de coleta em `dados/avaliacao/G1/`), todo resultado veio do PubMed (`M1.1.2` igual a `M1.1.1`), o recall (`0,195`) e a precisão (`24,7%`) ficaram baixos, e o ranking (`M1.4.1`, Spearman `0,034`) não acompanhou a rubrica metodológica. Na inspeção de G2 (`resultados-g2-inspecao.md`), as falhas da triagem em `M2.2.2` e `M2.3.2` expõem mensagens técnicas cruas ou termos de implementação (`ERR22-ERR30`, `MSG35-MSG68`).
- **Convergência entre inspeção e testes com usuários no registro da busca (`E11` / `F08`) e nas telas de resultado:** nos testes com usuários (`resultados-g2-usuarios.md`), o registro da busca (`E11`) foi o elemento menos entendido (apenas 1 de 3 participantes encontrou e explicou), em linha com a inspeção de G2 (`M2.2.1` sem orientação de uso para `F08` e `M2.3.2` com 28 linhas do painel Pipeline usando termos técnicos). Da mesma forma, as telas de resultado (detalhe do projeto, lista de artigos e ficha do artigo) tiveram baixa agradabilidade na estética (1 de 3 respondentes) e forte percepção de excesso de informação (`Q04` com 0 de 3 concordando), convergindo com a variação de padrões visuais em `M2.3.1` (6/8 padrões divergindo entre telas).
- **Baixo acoplamento estrutural vs. concentração de complexidade na orquestração (G3 - Q3.1):** `M3.1.1` indica baixo acoplamento entre os 38 arquivos do pacote (média de `2,05` dependências internas por módulo), mas o baixo acoplamento entre arquivos não impede alta complexidade algorítmica/condicional concentrada dentro de funções específicas do orquestrador (`11` de `47` funções em `pipeline.py` com CC > 10, chegando a `84`).
- **Baixa duplicação de código vs. baixa conformidade ao PEP 8 padrão e ausência de `logging` (G3 - Q3.2):** o pacote apresenta duplicação residual (`0,15%` em `M3.2.2`, apenas `28` de `18.927` linhas), porém falhas relevantes em `M3.2.1` (`5,3%` de arquivos conformes ao PEP 8 padrão, com `1.777` de `1.916` violações sendo `E501` por tamanho de linha) e `M3.2.3` (`0,0%` com `logging`), mostrando que o baixo nível de duplicação não garante observabilidade nem aderência ao estilo padrão sem automação/padronização.

### 3.2 Limitações e cautelas interpretativas (Premissa 1)

| Dimensão / Fonte | Limitação identificada | Efeito na análise das relações |
| :--- | :--- | :--- |
| **Cobertura de dados da Fase 4** | No **G2 com usuários**, `M2.6.1` e `M2.6.2` não foram coletadas até 22/11/2026, e `M2.5.1` e `M2.7.2` foram calculadas com 3 participantes (resultados indicativos); em **G1**, `M1.5.1` foi calculada sobre uma execução (`E1`) por `E2` não ter retornado lista | Exige cautela na generalização dos achados com usuários (`n = 3`) e no fechamento integral da assistência ao usuário (`Q2.6`) e da conformidade a filtros sem retorno (`E2`) |
| **Fotografia estática e recorte de código** | Medições de G3 e inspeção de G2 referem-se ao estado observado no período/commit de referência (`c2ae570`, 29/09/2026, e coletas de 14-20/11/2026) | Mudanças posteriores em produção ou no código alteram os valores observados |
| **Coleta e consolidação em G2 (inspeção e usuários)** | Observação indireta/não ao vivo de parte da triagem por A1 e A2, mensagens não provocadas classificadas pelo inventário, consolidação por A1 com ratificação de A2; no G2 com usuários, `D14` (3 respostas no lugar de 5), ausência de piloto e conta com créditos na parte A | Exige cautela ao extrapolar estados não exercitados diretamente e ao interpretar médias/percentuais em amostras pequenas |
| **Cobertura e métricas em G1 e G3** | Em G1, `E2` não gerou lista no SciELO, recuperação de senha (`F01`) dependeu de e-mail manual e `M1.3.2` conferiu por código/HTTP sem abrir a página do DOI; em G3, `M3.3.1` mede cobertura de linhas (não de ramos/decisões) com 27 testes pulados por dependências externas e `M3.2.1` avalia por arquivo | Limita o alcance de subpassos específicos e exige ler cobertura de linhas e métricas por arquivo junto ao contexto detalhado de cada métrica |

---

## 4. Ligação dos resultados com o propósito da Fase 1

Conforme `docs/fase-1/proposito.md`, a avaliação busca verificar em que medida o **VICKY** atende às necessidades dos estudantes de medicina na busca, triagem e consulta de artigos científicos, fornecendo evidências para priorizar melhorias no produto sob perspectiva dupla (externa via navegador e interna no código-fonte do backend).

| Decisão / Uso pretendido (Fase 1) | Parte interessada / Responsável | O que os resultados atuais sustentam | Lacunas / Pendências para fechamento |
| :--- | :--- | :--- | :--- |
| **Priorizar correções e otimizações no pipeline de LLM, buscas e integrações (PubMed/SciELO/Scholar)** | Synaptha e equipe de desenvolvimento do VICKY | G1 mostra `Não atende` (`0,60` em Insatisfatório): recall (`0,195`) e precisão (`24,7%`) baixos, ranking (`0,034`) desalinhado da rubrica, SciELO retornando 0 com `E2` sem encerrar/gerar lista e Google Acadêmico com 0/erros de string; G3 aponta gargalos em `pipeline.py` (CC até 84, `0/33` `logging`, `24%` de cobertura) | Acompanhar efeitos das correções de busca, filtros, ranking e orquestração em novas execuções |
| **Garantir evolução e facilidade de manutenção do código-fonte** | Equipe de desenvolvimento do VICKY | Diagnóstico objetivo de G3 (`1,33`, Aceitável - *Atende parcialmente*): baixo acoplamento (`2,05`) e baixa duplicação (`0,15%`), mas alta concentração de complexidade, ausência de `logging` e cobertura desigual entre `web/` (`87,8%`) e núcleo (`41,7%`) | Acompanhar evolução pós-refatoração nas métricas G3 |
| **Aprimorar experiência de uso, clareza e proteção contra erros na interface** | Equipe de desenvolvimento do VICKY (interface) | G2 em `Não atende` (`Q2.3` e `Q2.4` em Insatisfatório; `Q2.1` Bom `90,0%`; `Q2.2` Aceitável `29,4%` em `M2.2.2`). Com estudantes, `M2.7.2` em Excelente (`91,7%`, indicativo) e `M2.5.1` em Aceitável (`40,0%`, indicativo, `D14`); registro da busca (`E11`) entendido por apenas 1 de 3 e telas de resultado com baixa agradabilidade/excesso de informação | Coletar `M2.6.1` e `M2.6.2` (`Q2.6`, #28) e reavaliar após ajustes na interface |
| **Validar nível de qualidade frente ao GQM e à ISO/IEC 25040:2024** | Equipe Frances Allen | Rastreabilidade estabelecida para G1 (`Não atende`), G2 (`Não atende` pelas questões principais com dados disponíveis) e G3 (`Atende parcialmente`) frente às regras da Fase 2 | Registrar `M2.6.1` e `M2.6.2` (`Q2.6`) quando concluídos e fechar o alinhamento das sugestões com a equipe |

---

## 5. Sugestões de melhoria para o requisitante

### 5.1 Critério de priorização

Com base nos resultados da Fase 4, a equipe sugere como prioridade inicial para o requisitante a frente de **G1 (Adequação funcional)**, por concentrar o pior desempenho global (`0,60` - *Insatisfatório*, julgamento **Não atende**), com falhas críticas em `M1.1.1` e `M1.3.1` que comprometem diretamente o propósito central do VICKY para o estudante de medicina (recuperação dos estudos relevantes, funcionamento das fontes de busca, conformidade aos filtros e alinhamento do ranking à qualidade metodológica). As sugestões e encaminhamentos desta seção ainda dependem de **alinhamento com a equipe** e com o requisitante para definição do escopo definitivo e da ordem final de execução.

Para organizar as recomendações na tabela a seguir, adota-se o seguinte critério de classificação:

- **Priorizada:** frente que ataca diretamente as falhas críticas identificadas em **G1** (`M1.1.1` e `M1.3.1`, além de busca/fontes, filtros e ranking) e os desdobramentos mais próximos da execução da triagem que dependem ou impactam esse núcleo.
- **Secundária:** melhorias relevantes de manutenção interna do código (`G3`) ou de refinamento de interface/experiência (`G2`) que não resolvem por si sós as falhas de adequação funcional do G1, devendo ser tratadas em paralelo planejado ou em ciclos posteriores.

### 5.2 Candidatas e encaminhamentos identificados nos resultados de G1, G2 e G3

| Frente / Origem | Sugestão / Oportunidade | Justificativa baseada nos resultados da Fase 4 | Status |
| :--- | :--- | :--- | :--- |
| **Busca, fontes, filtros e ranking (G1 - M1.1.1-M1.5.2)** | Investigar e corrigir o retorno zero e a ausência de lista/não encerramento no SciELO (`E2`), revisar geração de strings e erros no Google Acadêmico (conforme `dados/avaliacao/G1/`) e na orquestração de buscas, recalibrar o Quality Score em relação à rubrica metodológica (`M1.4.1`) e adicionar campo explícito de tipo de estudo no formulário (`M1.5.1`) | **G1** teve julgamento **Não atende** (`0,60` - *Insatisfatório*), com falhas críticas em `M1.1.1` (`0,195`) e `M1.3.1` (`24,7%`), além de correlação do ranking (`0,034`), conformidade de filtros (`3,3%` em `E1`) e SciELO sem retorno nas execuções | **Priorizada** |
| **Backend / Orquestração (G3 - M3.1.2, M3.2.3, M3.3.1)** | Decompor `run_full_pipeline` (`CC = 84`), adicionar `logging` estruturado nas funções críticas (`0/33`, priorizando as 17 com `try/except` mapeadas em `dados/avaliacao/G3/`) e ampliar testes unitários em `pipeline.py` (`24%` de cobertura) | Concentra complexidade extrema, ausência de logs estruturados e maior déficit de cobertura (`905` de `2.769` linhas não cobertas) no orquestrador, mas atua como melhoria estrutural de manutenibilidade após/junto ao diagnóstico funcional de G1 | **Secundária** |
| **Registro da busca, exportação e telas de resultado (G2 - inspeção e usuários)** | Renomear e explicar claramente o registro da busca/log (`E11` / `F08`), traduzir termos técnicos do painel Pipeline (`M2.3.2`), verificar abertura de XLSX no macOS e disponibilizar exportação também na lista de artigos (`E12` / `F09`), e reduzir densidade/excesso de informação nas telas de resultado (`M2.5.1`, `Q04`) | Melhora leitura, rastreabilidade visual e experiência no pós-busca (`E11` entendido por 1/3; `Q04` com `0/3`), sem resolver as falhas críticas de G1 nem os problemas de recuperação, filtros e ranking | **Secundária** |
| **Mensagens, consistência visual e proteção de ações (G2 - inspeção)** | Tornar mensagens de erro e status claras e acionáveis (`M2.2.2`, `M2.3.2`), padronizar componentes/mensagens entre telas (`M2.3.1`), exibir limites/cotas e aviso de fixação de parâmetros (`M2.4.1`) e melhorar clareza de validação/orientação (`M2.4.2`, `M2.2.1`, `M2.7.1`) | `Q2.3` e `Q2.4` ficaram em *Insatisfatório* e `Q2.2` foi rebaixada para *Aceitável* (`M2.2.2` em `29,4%`), mas o impacto central para o propósito de busca/triagem continua subordinado aos problemas de G1 | **Secundária** |
| **Estilo e higiene de código (G3 - M3.2.1, M3.2.2)** | Corrigir os 22 alertas do `pyflakes` e adotar verificação/formatação automatizada na esteira (avaliando o custo de refatorar 1.777 ocorrências de `E501`) | Melhora higiene e padronização de código sem alterar a adequação funcional ou o comportamento de busca/triagem do G1 | **Secundária** |

---

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 21/11/2026 | Estrutura da página de julgamento e conclusões da Fase 4 | Guilherme Maciel | - |
| 0.2 | 22/11/2026 | Q2.5 e Q2.7 com os resultados do G2 com usuários (M2.5.1 e M2.7.2) e julgamento do G2 pela regra das questões em Insatisfatório | Gabriel Fae | - |
| 0.3 | 22/11/2026 | Consolidação dos resultados do G1, G2 e G3, relações, limitações, ligação com a Fase 1 e candidatas de melhoria | Guilherme Maciel | - |
