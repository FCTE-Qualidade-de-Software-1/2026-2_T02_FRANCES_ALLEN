# Julgamento e conclusões

## 1. Introdução e escopo da consolidação

Esta página reúne o julgamento consolidado da qualidade do **VICKY** (<https://vicky.synaptha.com/>) na **Fase 4** a partir das três características adaptadas da **ISO/IEC 25010:2023** e do método **GQM**:

- **G1 — Adequação funcional** (perspectiva dos estudantes de medicina; foco em completude, correção e pertinência funcional).
- **G2 — Capacidade de interação** (perspectiva dos estudantes de medicina; foco em reconhecimento da adequação, facilidade de aprendizado, operabilidade, proteção contra erro do usuário, engajamento do usuário, assistência ao usuário e autodescritividade).
- **G3 — Manutenibilidade** (perspectiva da equipe de desenvolvimento / arquitetos; foco em modularidade, analisabilidade e testabilidade no backend em Python, `src/vicky/` e `tests/`).

Os limiares e regras de julgamento seguem [Níveis de pontuação e critérios de julgamento](../fase-2/niveis-e-julgamento.md), e os objetivos, questões e hipóteses seguem [Objetivos, questões e hipóteses](../fase-2/objetivos-questoes-hipoteses.md).

> **Situação dos insumos na consolidação:**
> - **G3 (Manutenibilidade):** dados consolidados presentes (`resultados-g3.md`, commit `c2ae570`, 6 de 6 métricas medidas).
> - **G2 (Capacidade de interação):** dados por inspeção presentes (`resultados-g2-inspecao.md`, 8 métricas inspecionadas) e com usuários (`resultados-g2-usuarios.md`: `M2.5.1` e `M2.7.2`, com três participantes, resultados indicativos). `M2.6.1` e `M2.6.2` (#28) não foram coletadas até 22/11/2026 e constam como **A definir**.
> - **G1 (Adequação funcional):** resultados da Fase 4 ainda não incorporados nesta versão (`M1.1.1` a `M1.5.2`, `Q1.1` a `Q1.5` e julgamento global marcados como **A definir**).

---

## 2. Julgamento final de cada objetivo (G1, G2 e G3)

Sem colapsar as características em uma nota única global, cada objetivo é avaliado segundo suas respectivas regras da Fase 2 com base nas evidências disponíveis.

### 2.1 Objetivo G1 — Adequação funcional

| Questão / Métrica / Critério | Resultado / Valor medido | Nível / Pontuação | Julgamento / Situação | Evidências / Observações |
| :--- | :---: | :---: | :---: | :--- |
| **Q1.1** (M1.1.1, M1.1.2) | A definir | A definir | A definir | Aguardando resultados da Fase 4 do G1 |
| **Q1.2** (M1.2.1) | A definir | A definir | A definir | Aguardando resultados da Fase 4 do G1 |
| **Q1.3** (M1.3.1, M1.3.2) | A definir | A definir | A definir | Aguardando resultados da Fase 4 do G1 |
| **Q1.4** (M1.4.1) | A definir | A definir | A definir | Aguardando resultados da Fase 4 do G1 |
| **Q1.5** (M1.5.1, M1.5.2) | A definir | A definir | A definir | Aguardando resultados da Fase 4 do G1 |
| **Pontuação global de G1** | A definir | A definir | A definir | Média simples das 5 questões; sujeita aos tetos de M1.1.1/M1.3.1 e ao limite de **Bom** se alguma questão ficar em Insatisfatório |
| **Julgamento do produto (G1)** | — | — | **A definir** | Preencher após incorporação dos dados do G1 na Fase 4 |

### 2.2 Objetivo G2 — Capacidade de interação

A consolidação atual contempla as 8 métricas obtidas por inspeção (`resultados-g2-inspecao.md`) e as duas medidas com estudantes (`M2.5.1` e `M2.7.2`, em `resultados-g2-usuarios.md`), calculadas com três participantes e por isso indicativas. `M2.6.1` e `M2.6.2` permanecem **A definir** até a coleta (#28).

| Questão / Métrica | Valor / Resultado observado | Nível / Situação | Evidências e regras aplicadas |
| :--- | :---: | :---: | :--- |
| **Q2.1** — Reconhecimento da adequação (`M2.1.1`) | `M2.1.1`: 9/10 (90,0%) | **Bom** | Descreve 9 de 10 cenários (incluindo o limite do produto); Favoritos (F07) não aparece nas páginas públicas |
| **Q2.2** — Facilidade de aprendizado (`M2.2.1`, `M2.2.2`) | `M2.2.1`: 8/9 (88,9%, Bom); `M2.2.2`: 10/34 (29,4%, Insatisfatório) | **Aceitável** | Orientação cobre 8/9 funções (F08 sem orientação de uso/paginação); `M2.2.2` em Insatisfatório rebaixa Q2.2 de Bom para Aceitável |
| **Q2.3** — Operabilidade (`M2.3.1`, `M2.3.2`) | `M2.3.1`: 0,25 (6/8, Insatisfatório); `M2.3.2`: 77/117 (65,8%, Insatisfatório) | **Insatisfatório** | Menor nível entre M2.3.1 e M2.3.2; 6/8 padrões comparáveis variam entre telas e 40/117 mensagens não são claras |
| **Q2.4** — Proteção contra erro (`M2.4.1`, `M2.4.2`) | `M2.4.1`: 4/6 (66,7%, Insatisfatório); `M2.4.2`: 2/6 (33,3%, Insatisfatório) | **Insatisfatório** | Ação paga (`A01`) traz aviso explícito ("CONSOME 1 CRÉDITO"), sem ação paga desprotegida; falhas em ações/entradas deixam Q2.4 em Insatisfatório |
| **Q2.5**: Engajamento do usuário (`M2.5.1`) | `M2.5.1`: 2/5 (40,0%, Aceitável, indicativo) | **Aceitável** (indicativo) | Três respostas, com maioria de 2 de 3 pela D14; só a página inicial e o Novo projeto foram agradáveis para a maioria. Prioridade secundária: não entra na contagem das 6 questões principais |
| **Q2.6**: Assistência ao usuário (`M2.6.1`, `M2.6.2`) | A definir (não coletadas até 22/11/2026) | **A definir** | Métricas executadas pelos avaliadores (`M2.6.1` e `M2.6.2`); regra exige atenção especial a `M2.6.1` (F01) e `M2.6.2` (contraste) |
| **Q2.7**: Autodescritividade (`M2.7.1`, `M2.7.2`) | `M2.7.1`: 3 de 4 (Bom); `M2.7.2`: 10/12 (83,3%, Bom, indicativo) | **Bom** (indicativo) | `M2.7.2` é a medida de referência, e `M2.7.1` em Bom não rebaixa Q2.7. Quality Score entendido pelos 3 participantes; o log auditável (E11) e o campo de objetivo (E02) só por 1 de 3 cada |
| **Julgamento do objetivo G2** | 5 de 6 questões principais com nível (`Q2.6` pendente) | **Não atende** | `Q2.3` e `Q2.4` em Insatisfatório. Pela regra da Fase 2, duas ou mais questões principais em Insatisfatório levam a "Não atende", qualquer que venha a ser o nível de `Q2.6` |

### 2.3 Objetivo G3 — Manutenibilidade

Avaliado no commit `c2ae570` (`resultados-g3.md`, `src/vicky/` com 38 arquivos `.py` e `tests/` com 1.034 testes), com repetição independente confirmada por A1 e A2 em todas as 6 métricas.

| Questão / Métrica | Valor / Resultado medido | Nível / Pontos | Evidências e regras aplicadas |
| :--- | :---: | :---: | :--- |
| **Q3.1** — Modularidade (`M3.1.1`, `M3.1.2`) | `M3.1.1`: 2,05 (78/38, Excelente, 3 pts); `M3.1.2`: 76,6% (11/47 > CC 10, Aceitável, 1 pt) | **Bom** (`2,00`) | Média `(3 + 1) / 2 = 2,00`; bloqueio de `M3.1.2` não acionado, mas `run_full_pipeline` atinge CC = 84 |
| **Q3.2** — Analisabilidade (`M3.2.1`, `M3.2.2`, `M3.2.3`) | `M3.2.1`: 5,3% (2/38, Insatisfatório, 0 pts); `M3.2.2`: 0,15% (28/18.927 LOC, Excelente, 3 pts); `M3.2.3`: 0,0% (0/33, Insatisfatório, 0 pts) | **Aceitável** (`1,00`) | Média `(0 + 3 + 0) / 3 = 1,00`; 0/33 funções críticas usam `logging` e 92,7% das violações PEP 8 são `E501` (> 79 chars) |
| **Q3.3** — Testabilidade (`M3.3.1`) | `M3.3.1`: 63,17% (4.750/7.519 linhas executáveis, Aceitável, 1 pt) | **Aceitável** (`1,00`) | 1.002 aprovados offline; `web/` tem 87,8% vs. 41,7% no núcleo e 24% em `pipeline.py` (905/2.769 linhas não cobertas) |
| **Pontuação global de G3** | `(2,00 + 1,00 + 1,00) / 3 = 1,33` | **Aceitável** | Limitação de `Q3.3` não acionada; perfil: Q3.1 Bom, Q3.2 Aceitável, Q3.3 Aceitável |
| **Julgamento do produto (G3)** | 6 de 6 métricas medidas | **Atende parcialmente** | Pontuação global `1,33` na faixa Aceitável |

---

## 3. Relação entre as três características, evidências e limitações (Premissa 1)

### 3.1 Convergências e relações apoiadas por evidências

- **Convergência de risco técnico em `src/vicky/pipeline.py` (G3 e observação de pipeline em G2):** os achados de G3 mostram que a dívida técnica do backend não se distribui de modo uniforme, mas se concentra no orquestrador `pipeline.py`, que acumula pico de complexidade ciclomática (`run_full_pipeline` com CC = 84 em `M3.1.2`), ausência total de `logging` estruturado (`0/33` funções críticas em `M3.2.3`, apoiando-se em `print` e `traceback.print_exc()`) e baixa cobertura de testes (`24%` em `M3.3.1`, contra `87,8%` na camada `web/`). Na inspeção de G2 (`resultados-g2-inspecao.md`), as falhas da triagem em `M2.2.2` e `M2.3.2` refletem essa fragilidade operacional ao expor texto técnico cru ou termos internos de execução (`ERR22`–`ERR30`, `MSG35`–`MSG68`).
- **Baixo acoplamento estrutural vs. concentração de complexidade na orquestração (G3 — Q3.1):** `M3.1.1` indica baixo acoplamento entre os 38 arquivos do pacote (média de `2,05` dependências internas por módulo), mas o baixo acoplamento entre arquivos não impede alta complexidade algorítmica/condicional concentrada dentro de funções específicas do orquestrador (`11` de `47` funções em `pipeline.py` com CC > 10, chegando a `84`).
- **Baixa duplicação de código vs. baixa conformidade ao PEP 8 padrão e ausência de `logging` (G3 — Q3.2):** o pacote apresenta duplicação residual (`0,15%` em `M3.2.2`, apenas `28` de `18.927` linhas), porém falhas relevantes em `M3.2.1` (`5,3%` de arquivos conformes ao PEP 8 padrão, com `1.777` de `1.916` violações sendo `E501` por tamanho de linha) e `M3.2.3` (`0,0%` com `logging`), mostrando que o baixo nível de duplicação não garante observabilidade nem aderência ao estilo padrão sem automação/padronização.
- **Relação entre G1, G2 e G3 (fluxo de triagem e experiência do usuário):** A definir / complementar com os resultados do G1 e das métricas de G2 com usuários.

### 3.2 Limitações e cautelas interpretativas (Premissa 1)

| Dimensão / Fonte | Limitação identificada | Efeito na análise das relações |
| :--- | :--- | :--- |
| **Cobertura de dados da Fase 4** | Resultados de **G1** ainda não incorporados; no **G2 com usuários**, `M2.6.1` e `M2.6.2` não coletadas, e `M2.5.1` e `M2.7.2` calculadas com três participantes (indicativas) | Impede concluir relações cruzadas completas entre adequação funcional (G1), experiência/acessibilidade com usuários (G2) e manutenibilidade (G3) |
| **Fotografia estática e recorte de código** | Medições de G3 e inspeção de G2 referem-se ao estado observado no período/commit de referência (`c2ae570`, 29/09/2026, e coletas de 14–20/11/2026) | Mudanças posteriores em produção ou no código alteram os valores observados |
| **Coleta e consolidação em G2 (inspeção)** | Observação indireta/não ao vivo de parte da triagem por A1 e A2, ausência de provocação de algumas mensagens no ambiente (classificadas pelo inventário) e consolidação por A1 com ratificação posterior de A2 | Exige cautela ao extrapolar estados não exercitados diretamente na interface |
| **Cobertura e métricas em G3** | `M3.3.1` mede cobertura de linhas (não de ramos/decisões) e registra 27 testes pulados por dependências externas; `M3.2.1` avalia conformidade por arquivo | A cobertura de linhas não garante ausência de falhas em ramificações não testadas, e a métrica por arquivo em `M3.2.1` penaliza igualmente violações isoladas e múltiplas |

---

## 4. Ligação dos resultados com o propósito da Fase 1

Conforme `docs/fase-1/proposito.md`, a avaliação busca verificar em que medida o **VICKY** atende às necessidades dos estudantes de medicina na busca, triagem e consulta de artigos científicos, fornecendo evidências para priorizar melhorias no produto sob perspectiva dupla (externa via navegador e interna no código-fonte do backend).

| Decisão / Uso pretendido (Fase 1) | Parte interessada / Responsável | O que os resultados atuais sustentam | Lacunas / Pendências para fechamento |
| :--- | :--- | :--- | :--- |
| **Priorizar correções e otimizações no pipeline de LLM e integrações (PubMed/Scholar)** | Synaptha e equipe de desenvolvimento do VICKY | Evidências de gargalos no orquestrador `pipeline.py` (CC até 84, 0% de `logging` nas 33 funções críticas e 24% de cobertura de testes) e exposição de mensagens técnicas/imprecisas no fluxo de triagem em G2 | Falta integrar os resultados de **G1** (completude, precisão, metadados, ranking e filtros/repetibilidade) para avaliar diretamente a qualidade da triagem entregue |
| **Garantir evolução e facilidade de manutenção do código-fonte** | Equipe de desenvolvimento do VICKY | Diagnóstico objetivo de G3 (`1,33`, Aceitável — *Atende parcialmente*): baixo acoplamento (`2,05`) e baixa duplicação (`0,15%`), mas alta concentração de complexidade, ausência de `logging` e cobertura desigual entre `web/` (`87,8%`) e núcleo (`41,7%`) | Acompanhar evolução pós-refatoração nas métricas G3 |
| **Aprimorar experiência de uso e proteção contra erros na interface** | Equipe de desenvolvimento do VICKY (interface) | Inspeção de G2 aponta `Q2.1` em Bom (`90,0%`), `Q2.2` em Aceitável (rebaixada por `M2.2.2` em `29,4%`), e `Q2.3` e `Q2.4` em Insatisfatório, com confirmação de que a ação paga (`A01`) exibe aviso de consumo de crédito | Com estudantes, `M2.7.2` em Bom (83,3%) e `M2.5.1` em Aceitável (40,0%), ambas indicativas; o registro da busca (E11) foi o elemento menos entendido. Faltam `M2.6.1` e `M2.6.2` |
| **Validar nível de qualidade frente ao GQM e à ISO/IEC 25040:2024** | Equipe Frances Allen | Rastreabilidade estabelecida para G2 (inspeção) e G3 frente às regras da Fase 2 | A definir o fechamento completo de G1 e das métricas de usuários de G2 |

---

## 5. Sugestões de melhoria para o requisitante

### 5.1 Alinhamento com a equipe

> **Pendência de definição com a equipe:** ainda falta uma definição conjunta com a equipe sobre a priorização final e o fechamento das sugestões de melhoria a serem encaminhadas ao requisitante (considerando os resultados pendentes de G1 e G2 com usuários, o escopo de ação e o alinhamento entre os membros).

### 5.2 Candidatas e encaminhamentos preliminares identificados nos dados atuais

| Frente / Origem | Sugestão / Oportunidade | Justificativa baseada nos dados atuais | Status |
| :--- | :--- | :--- | :--- |
| **Backend / Orquestração (G3 — `M3.1.2`, `M3.2.3`, `M3.3.1`)** | Decompor `run_full_pipeline` (CC = 84), adicionar `logging` estruturado nas funções críticas (`0/33`) e ampliar testes unitários em `pipeline.py` (`24%` de cobertura) | Concentração de complexidade, falta de logs estruturados e maior déficit de cobertura de testes no mesmo módulo central | Pendente de alinhamento com a equipe |
| **Estilo e higiene de código (G3 — `M3.2.1`, `M3.2.2`)** | Tratar os 22 alertas do `pyflakes` e padronizar formatação/linting na esteira (com atenção ao custo de refatorar 1.777 ocorrências de `E501`) | Reduzir alertas lógicos e melhorar consistência sem perder o foco no gargalo principal de `pipeline.py` | Pendente de alinhamento com a equipe |
| **Interface e mensagens ao usuário (G2 — inspeção)** | Tornar mensagens de erro e status mais claras e acionáveis (`M2.2.2`, `M2.3.2`), padronizar componentes/mensagens entre telas (`M2.3.1`), informar limites/cotas (`M2.4.1`) e orientar o uso de F08 (`M2.2.1`) e F07/login (`M2.1.1`, `M2.7.1`) | Evitar exposição de erro técnico cru ao usuário e reduzir ambiguidades durante configuração e acompanhamento da triagem | Pendente de alinhamento com a equipe |
| **Adequação funcional (G1)** | A definir | A definir após incorporação dos resultados do G1 na Fase 4 | A definir |

---

## 6. Encerramento e rastreabilidade

- **Critério de pronto da issue:** o julgamento de cada objetivo deve citar explicitamente os dados que o sustentam; os blocos de G1 e das métricas com usuários de G2 devem ser preenchidos assim que esses dados forem consolidados na Fase 4.


## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 21/11/2026 | Estrutura da página de julgamento e conclusões da Fase 4 | Guilherme Maciel | - |
| 0.2 | 22/11/2026 | Q2.5 e Q2.7 com os resultados do G2 com usuários (M2.5.1 e M2.7.2) e julgamento do G2 pela regra das questões em Insatisfatório | Gabriel Fae | - |
| 0.3 | 22/11/2026 | Q2.5 e Q2.7 marcadas como indicativas; Q2.7 em Bom, com o uso de E02 corrigido pela gravação na M2.7.2 | Gabriel Fae | - |