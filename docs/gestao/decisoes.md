# Decisões de gestão

Cada decisão cita a medição que a motivou, o que fecha o ciclo exigido pela Premissa 3: **medição → interpretação → decisão**. O efeito de cada decisão é verificado na coleta do ciclo seguinte, na coluna "Resultado".

A verificação de D01 a D07 e as decisões D08 a D10 foram feitas na [coleta parcial de 28/10](registro-de-medicoes.md#4-ciclo-2-parcial-2610-a-2810).

## 1. Resumo

| ID | Data | Medição que motivou | Decisão | Status |
|----|------|---------------------|---------|--------|
| D01 | 19/10/2026 | DP3 = 82,6% · CP1 sem backlog (ciclo 0) | Estruturar o backlog da E1 em issues com responsável e milestone | Executada |
| D02 | 18/10/2026 | DP4 = 42,1% em 18/10 (ciclo 0) | Revisão estrutural do material das Fases 1 e 2 | Executada |
| D03 | 25/10/2026 | CP1 = 11,1% · CP2 SPI = 0,05 · artigo com 0 de 9 issues (ciclo 1) | Recalcular o prazo de entrega do artigo e priorizar o caminho crítico | **Executada com atraso** (verificada em 28/10) |
| D04 | 25/10/2026 | DP3 = 82,6% (ciclo 0) · DP2 = 0,11 (ciclo 1) | Readaptar o processo de desenvolvimento e pesquisa: ciclos semanais com ponto de controle e limite de WIP | **Parcialmente executada** (verificada em 28/10) |
| D05 | 25/10/2026 | RC1 e RC2 não mensuráveis nos ciclos 0 e 1 | Tornar obrigatório o registro de horas e validar a linha de base de 42 h | **Não executada**: 0 de 6 integrantes no prazo de 28/10 |
| D06 | 25/10/2026 | 0 de 23 commits ligados a issue · 1 PR sem revisão · autor `user` | Adotar o fluxo branch → PR → revisão por par com `Closes #N` e corrigir a identidade do git | **Não executada**: nenhum PR entre 26 e 28/10 |
| D07 | 25/10/2026 | RC3 da carga planejada de 7,1% a 28,6% (ciclo 1) | Rebalancear a distribuição das issues da E2 | Absorvida pela D08 |
| D08 | 28/10/2026 | CP1 = 100% só após o vencimento · RC3 da carga planejada de 7,1% a 28,6% · remanejamento das divisões no ponto de controle | Registrar o remanejamento das divisões de trabalho e refazer a linha de base da E2 sobre a nova divisão | Em execução |
| D09 | 28/10/2026 | D05 com 0 de 6 integrantes · ponto de controle realizado fora de sala, com resposta parcial | Mover a decisão do ciclo para um canal assíncrono com prazo de resposta e quórum registrado | Em execução |
| D10 | 28/10/2026 | DP2 com 0 chegadas e WIP = 0 · nenhuma issue aberta depois de 19/10 · milestone E2 inexistente em 04/11 | Planejar o ciclo no GitHub antes de ele começar: milestone com data, issues estimadas e marco do ciclo | Proposta |

## 2. Detalhamento

### D01 - Estruturar o backlog da E1

| Item | Registro |
|------|----------|
| Medição | Ciclo 0: 82,6% dos commits em um único dia (DP3) e nenhuma issue ou milestone, o que tornava CP1 e CP2 não mensuráveis |
| Interpretação | Sem trabalho comprometido e rastreável, a equipe não tinha como saber o que faltava para a E1 nem distribuir a carga antes do prazo |
| Decisão | Criar a milestone E1 (vencimento em 26/10) e 18 issues, cada uma com responsável e rótulo de categoria (artigo, fase-1, fase-2, gitpage, gestão, entrega) |
| Responsável | @LucasAvelar2711 (criação da milestone e das issues em 19/10) |
| Resultado no ciclo seguinte | **Parcial no ciclo 1.** O backlog passou a existir e permitiu medir CP1, CP2, DP1 e DP2. Mas a vazão foi de 0,11 (2 de 18 issues fechadas): o backlog foi criado, mas não andou. Isso motivou a D04 |
| Verificação em 28/10 | **Executada, com efeito tardio.** As 18 issues foram declaradas concluídas no ponto de controle (CP1 = 100%), três dias após o vencimento. Duas limitações apareceram: o fechamento não foi registrado no GitHub (ver D06) e, esvaziado o backlog da E1, nenhum trabalho novo foi comprometido, o que levou à D10 |

### D02 - Revisão estrutural do material

| Item | Registro |
|------|----------|
| Medição | 8 dos 19 commits de 18/10 foram retrabalho (DP4 = 42,1%) |
| Interpretação | A produção acelerada gerou inconsistências entre páginas: faixas de pontuação com buracos, G2 desalinhado das sete subcaracterísticas de C2 e a troca de modificabilidade por testabilidade em C3 sem propagação para o modelo de qualidade |
| Decisão | Revisar a estrutura de todo o material das Fases 1 e 2 antes da entrega, com o seguinte checklist: histórico de versão atualizado, legenda e fonte em figuras e tabelas, links internos válidos, termos iguais entre páginas (ISO/IEC 25010:2023) e decisões refletidas em todas as páginas afetadas |
| Evidência | Commits `ef7af41` (faixas de nível sem buracos), `8c048e1` (G2 realinhado), `9558d49` (C3), `4f3d9f3` e `99f5e70` (redação) |
| Responsável | Autores de cada página, com revisão cruzada |
| Resultado no ciclo seguinte | **Em verificação.** O DP4 por PR continua sem base de cálculo, porque não houve PR (ver D06). Pelo commit, o retrabalho subiu em vez de cair: 66,7% no ciclo 1 (medido retroativamente) e 66,7% no parcial do ciclo 2. Os commits [`31cff66`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/commit/31cff66), [`3304199`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/commit/3304199), [`030f62d`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/commit/030f62d) e [`f25cb3d`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/commit/f25cb3d) são todos de correção ou substituição de conteúdo já publicado. Ainda há inconsistência entre testabilidade e modificabilidade em C3 nas Fases 1 e 2 |

### D03 - Recalcular esforço pro artigo

| Item | Registro |
|------|----------|
| Medição | Ciclo 1: CP1 = 11,1% com desvio de 88,9 p.p., SPI = 0,05 e nenhuma das 9 issues do artigo fechada (24 h das 42 h planejadas) |
| Interpretação | Mantido o ritmo do ciclo 1, o artigo não fica pronto no prazo da E1. |
| Decisão | Recalcular o cronograma do artigo a partir das horas restantes: 24 h de valor planejado ainda não entregue no artigo. Ordem de prioridade: template (#2) → seções de conteúdo (#3 a #7) → referencial e metodologia (#8) → referências (#19) → tabela de contribuição (#10). |
| Responsável | Grupo como um todo. |
| Resultado no ciclo seguinte | **Executada com atraso.** As 24 h do artigo foram concluídas entre 26 e 28/10 e o SPI da E1 fechou em 1,00, contra 0,05 no vencimento. A entrega saiu na *release* [`v0.1`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/releases/tag/v0.1) em 26/10 às 20h25, cerca de um dia após o vencimento da milestone, e o fechamento formal das issues levou três dias. Leitura: a decisão recuperou o **escopo**, não o **prazo**. A meta de SPI ≥ 0,90 contra o novo cronograma não é verificável, porque a nova data interna do artigo não chegou a ser registrada |

### D04 - Readaptar o processo de desenvolvimento e pesquisa

| Item | Registro |
|------|----------|
| Medição | Ciclo 0: 82,6% do trabalho em um dia (DP3), com 4 dias ativos em 14. Ciclo 1: razão saída/chegada de 0,11 (DP2) e WIP de 2,7 issues por integrante |
| Interpretação | O processo funcionou em "rajada": nada é feito por vários dias e tudo é feito na véspera. Isso causou o retrabalho do ciclo 0 e o atraso do ciclo 1. É o padrão que o CID chama de fluxo imprevisível (ICM, linha 30) |
| Decisão | Adotar o método descrito na [Seção 3 da página de gestão](index.md#3-como-a-equipe-e-gerida): ciclos semanais de domingo a domingo, ponto de controle na quarta-feira com entrega parcial obrigatória (pelo menos um PR por integrante), limite de 2 issues em andamento por pessoa e issues divididas em partes de até 1 dia de trabalho |
| Responsável | Toda a equipe. A coleta fica com o gerente (Gabriel Fae) de medição do ciclo |
| Resultado no ciclo seguinte | **Parcialmente executada.** O ponto de controle de quarta aconteceu e gerou esta coleta, mas correu fora de sala e **sem a entrega parcial por PR** que a decisão exigia (nenhum PR no período). As duas metas não foram atingidas: o DP3 parcial ficou em 66,7% e a razão saída/chegada não é calculável (0 chegadas). O limite de WIP passou a ser respeitado (0 por integrante, contra 2,7 em 25/10), mas por esvaziamento do backlog, não por controle de fluxo |

### D05 - Registro obrigatório de horas

| Item | Registro |
|------|----------|
| Medição | RC1 e RC2 não mensuráveis nos dois ciclos: só um integrante declarou horas (5 h, sem data por atividade) |
| Interpretação | Sem horas reais não há custo (AC), CPI nem tabela de contribuição confiável. O *proxy* de commits penaliza quem trabalha no Overleaf |
| Decisão | (1) Cada integrante registra em `esforco.csv` as horas retroativas dos ciclos 0 e 1 até o ponto de controle de 28/10. (2) A partir do ciclo 2, o registro é feito ao fechar cada issue. (3) A linha de base de 42 h é revisada e aprovada no planejamento do ciclo 2 |
| Responsável | Cada integrante. A consolidação fica com o gerente de medição |
| Resultado no ciclo seguinte | **Não executada.** Em 28/10, o [`esforco.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/blob/main/dados/gestao/esforco.csv) continha apenas o cabeçalho: **0 de 6** integrantes registraram as horas retroativas dos ciclos 0 e 1, e a situação seguia igual em 04/11. Consequência: RC1, RC2 e o RC3 por horas reais estão não mensuráveis pelo terceiro ciclo seguido e a linha de base de 42 h não pôde ser revista contra dado real. A causa registrada é de comunicação, não de esforço, e virou a D09 |

### D06 - Rastreabilidade do trabalho no repositório

| Item | Registro |
|------|----------|
| Medição | 0 de 23 commits citam uma issue. Houve 1 PR, aprovado em 1h05 sem revisão registrada. 4 commits têm o autor genérico `user` |
| Interpretação | O trabalho existe, mas não é atribuível nem verificável. Isso derruba a qualidade dos dados de todas as métricas e explica parte da distância entre o conteúdo produzido e o SPI |
| Decisão | Toda mudança passa a seguir o fluxo branch → PR com `Closes #N` → revisão por outro integrante → merge. A `main` fica protegida. Cada integrante configura `git config user.name` e `user.email` com a conta do GitHub |
| Responsável | Toda a equipe. A proteção da `main` fica com quem administra o repositório |
| Resultado no ciclo seguinte | **Não executada.** Entre 26 e 28/10 houve 3 commits, **nenhum PR** e **nenhum commit com `Closes #N`**; o único PR do repositório segue sendo o #1, de 18/10, sem revisão. O commit [`030f62d`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/commit/030f62d) ainda saiu com o autor genérico `user`. Mais grave: o fechamento das 18 issues da E1 foi declarado no ponto de controle e **não registrado no GitHub** (em 04/11 a milestone E1 constava aberta, com 16 issues em `OPEN`). Isso rebaixa CP1 e CP2 do ciclo 2 de medidos para declarados e mantém o DP4 por PR sem base de cálculo |

### D07 - Rebalancear a distribuição das issues

| Item | Registro |
|------|----------|
| Medição | Carga planejada da E1 por integrante entre 7,1% (3 h) e 28,6% (12 h) (RC3) |
| Interpretação | A distribuição planejada já nasce fora da faixa de 13% a 20%. Sem correção, a tabela de contribuição final tende a ficar desequilibrada |
| Decisão | No planejamento da E2, distribuir as issues para que cada integrante fique entre 13% e 20% das horas estimadas, usando o RC3 do ciclo 2 (horas reais) como ajuste |
| Responsável | Lucas Avelar |
| Resultado no ciclo seguinte | **Absorvida pela D08.** O remanejamento das divisões de trabalho em 28/10 mudou a base do problema: não se trata mais de redistribuir as issues da E1, mas de montar a linha de base da E2 sobre a nova divisão |

### D08 - Remanejar as divisões de trabalho da equipe

| Item | Registro |
|------|----------|
| Medição | Ciclo 2 parcial: CP1 chegou a 100%, mas só depois do vencimento, com as 9 issues do artigo (24 h das 42 h) concluídas em três dias. Carga planejada da E1 entre 7,1% e 28,6% por integrante (RC3) e 0 de 6 integrantes com horas registradas (D05) |
| Interpretação | A divisão da E1 não correspondeu ao trabalho real: parte das frentes ficou concentrada em poucos integrantes e a recuperação do artigo foi feita em bloco, fora da atribuição original. Manter a atribuição de 19/10 como base de medição produziria um RC3 falso |
| Decisão | (1) Registrar o **remanejamento das divisões de trabalho** feito no ponto de controle de 28/10. (2) A coluna `responsavel` da `linha-de-base-e1.csv` passa a valer apenas como registro histórico do planejamento da E1 e **não é usada para julgar contribuição individual**. (3) A linha de base da E2 é montada sobre a nova divisão, com as horas estimadas distribuídas entre 13% e 20% por integrante. (4) Enquanto não houver horas reais, o RC3 é reportado por *proxy*, com a ressalva explícita de que o trabalho em Overleaf não aparece no repositório |
| Responsável | Equipe no planejamento do ciclo, com a nova divisão registrada em ata. A consolidação fica com o gerente de medição |
| Resultado no ciclo seguinte | _A verificar: nova divisão registrada em ata e linha de base da E2 com RC3 planejado entre 13% e 20% por integrante_ |

### D09 - Canal assíncrono com prazo de resposta

| Item | Registro |
|------|----------|
| Medição | O ponto de controle de 28/10 **não ocorreu em sala**, por falta de tempo de aula, e correu fora de sala de forma assíncrona, com manifestação de parte da equipe. No mesmo prazo, a D05 fechou em 0 de 6 integrantes e a D06 em 0 PRs |
| Interpretação | As duas decisões que não saíram do papel são justamente as que dependem de **cada integrante agir individualmente** (lançar horas, abrir PR). As que dependiam de uma ação concentrada (fechar o escopo do artigo, publicar a *release*) saíram. O gargalo é de combinação e resposta, não de esforço: sem um canal com prazo, a decisão tomada fora de sala não alcança quem não respondeu |
| Decisão | (1) As decisões do ciclo passam a ser registradas em canal assíncrono, com **prazo de resposta de 24 h** e quórum anotado na ata. (2) Quem não se manifestar no prazo fica registrado como "sem manifestação", e a decisão segue valendo. (3) O ponto de controle de quarta tem pauta publicada antes e é registrado em ata mesmo quando ocorre fora de sala. (4) As pendências individuais (horas e PR) são cobradas por item, com responsável e prazo nomeados |
| Responsável | Gerente de medição para a pauta e a ata. Cada integrante pela própria resposta no prazo |
| Resultado no ciclo seguinte | _A verificar: ata do ponto de controle com quórum registrado e as pendências da D05 e da D06 nomeadas por responsável_ |

### D10 - Planejar o ciclo no GitHub antes de ele começar

| Item | Registro |
|------|----------|
| Medição | Ciclo 2 parcial: **0 chegadas** e 16 saídas (razão saída/chegada indefinida), WIP de **0** na data de corte. Nenhuma issue foi aberta depois de 19/10 e, em consulta ao GitHub em 04/11, a milestone E2 não existia e a E1 continuava no estado aberto: o ciclo iniciado em 01/11 **não foi coletado nem planejado no repositório** |
| Interpretação | O projeto repetiu, em espelho, o problema do ciclo 1. Lá, todo o trabalho entrou de uma vez e não saiu; aqui, tudo saiu de uma vez e nada entrou. Em qualquer dos dois casos o fluxo é imprevisível (CID, ICM linha 30). E o efeito sobre a medição é pior: sem backlog, CP1, CP2, DP1 e DP2 voltam a ser não mensuráveis, como no ciclo 0, e a gestão perde justamente os indicadores que a D01 recuperou |
| Decisão | (1) Antes do início de cada ciclo, criar no GitHub a **milestone da entrega com data** e abrir as issues do ciclo com responsável, rótulo de categoria e estimativa em horas, respeitando o limite de 2 por integrante. (2) Fechar a milestone E1 e registrar o fechamento das issues já concluídas, para que a coleta volte a sair da API e não de declaração. (3) Nenhum ciclo começa sem linha de base de horas publicada em `dados/gestao/` |
| Responsável | Quem administra o repositório, no planejamento de domingo. A conferência fica com o gerente de medição no ponto de controle |
| Resultado no ciclo seguinte | _A verificar: milestone E2 criada com data, backlog do ciclo aberto antes do primeiro dia e milestone E1 fechada no GitHub_ |

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 05/10/2026 | Criação da estrutura do documento | Gabriel Fae | - |
| 0.2 | 16/10/2026 | Reorganização da documentação por fases do processo de avaliação | Gabriel Fae | - |
| 0.3 | 25/10/2026 | Registro das decisões D01 a D07 a partir das medições dos ciclos 0 e 1 | Gabriel Fae | - |
| 0.4 | 28/10/2026 | Verificação de D01 a D07 pela coleta parcial do ciclo 2 e registro das decisões D08 (remanejamento das divisões), D09 (canal assíncrono) e D10 (planejamento do ciclo no GitHub) | Gabriel Fae | - |
