# Plano de medição da gestão

Este plano instancia o **modelo de informação de medição** do PSM para o projeto da equipe. Cada métrica traz a necessidade de informação que atende, suas medidas base e derivadas, o indicador, o critério de decisão e a ação de gestão disparada. As faixas de decisão partem das especificações do PSM CID (Parte 2, seção 8) e foram adaptadas ao porte do projeto. Toda recalibração é registrada em [Decisões de gestão](decisoes.md).

## 1. Parâmetros gerais

| Parâmetro | Valor |
|-----------|-------|
| Ciclo de medição | Semanal, de domingo a domingo. Coleta parcial na quarta-feira e completa no domingo |
| Entidade medida | Projeto da equipe: issues, commits, pull requests e horas registradas |
| Responsável pela coleta | Gabriel Fae |
| Integrantes | 6 (participação ideal: 1/6 ≈ 16,7% do esforço por integrante) |
| Linha de base de horas da E1 | **42 h** distribuídas nas 18 issues da milestone E1 ([`linha-de-base-e1.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/blob/main/dados/gestao/linha-de-base-e1.csv)). |
| Valor-hora de referência (VH) | R$50, base pesquisada online. Usado só para converter horas em custo (R$) no RC2 |
| Prazo da E1 | Milestone E1 com vencimento em 26/10/2026 00:00 |
| Avaliações/Critério de decisão | OK - continuar, valor dentro do esperado; REV - revisar, valor fora do esperado; REP - replanejar, valor totalmente fora do esperado; | 

## 2. Calendário e Progresso

### CP1 - Comprometido x concluído

| Elemento | Especificação |
|----------|---------------|
| Necessidade de informação | As issues comprometidas no ciclo ou na milestone estão sendo entregues? |
| Referência | CID, ICM linha 1; especificação 8.3 *Committed vs. Completed* |
| Medidas base | `I_comp`: issues comprometidas na milestone · `I_conc`: issues fechadas como prontas até a data de corte |
| Medidas derivadas | `%Concluído = I_conc / I_comp × 100` · `%Planejado(t)`: fração do período da milestone já decorrida |
| Indicador | Desvio = `%Planejado(t) − %Concluído`, em pontos percentuais (p.p.), mais o gráfico de *burnup* |
| Fonte e coleta | Milestone e datas de fechamento das issues no GitHub, coletadas na quarta-feira e no domingo |
| Critério de decisão | (OK) desvio ≤ 5 p.p. · (REV) 5 a 10 p.p. · (REP) > 10 p.p. (faixas do CID 8.3) |
| Ação disparada | (REV): Investigar bloqueios na reunião de quarta. (REP) Replanejar: redistribuir issues, dividir escopo ou renegociar o prazo interno |

### CP2 - Índice de desempenho de prazo (SPI), base hora/valor

| Elemento | Especificação |
|----------|---------------|
| Necessidade de informação | O valor entregue, em horas planejadas, acompanha o cronograma? |
| Referência | CID, ICM linha 8 (*Earned Value*, *Estimate vs. Actual Schedule*) |
| Medidas base | `H_est(i)`: horas estimadas da issue *i* · data de fechamento de cada issue |
| Medidas derivadas | `PV(t)` (valor planejado) = horas estimadas que deveriam estar prontas em *t*, com distribuição linear no período da milestone · `EV(t)` (valor agregado) = soma de `H_est` das issues fechadas até *t* |
| Indicador | `SPI = EV / PV` e a curva PV x EV |
| Fonte e coleta | `linha-de-base-e1.csv` mais as datas de fechamento no GitHub, coletadas na quarta-feira e no domingo |
| Critério de decisão | (OK) SPI ≥ 0,90 · (REV) 0,75 ≤ SPI < 0,90 · (REP) SPI < 0,75 |
| Ação disparada | (REV) Priorizar as issues do caminho crítico (artigo antes da GitPage). (REP) Recalcular a data de entrega e registrar o novo prazo como decisão |

## 3. Recursos e Custos

### RC1 - Variação de esforço (estimado x real)

| Elemento | Especificação |
|----------|---------------|
| Necessidade de informação | As estimativas de horas são realistas? Há sobrecarga? |
| Referência | CID, ICM linhas 8 e 9 (*Estimate vs. Actual Effort*, *Estimation Accuracy*) |
| Medidas base | `H_real`: horas registradas em `esforco.csv` · `H_est`: horas estimadas das mesmas issues |
| Medida derivada | `TVE = (ΣH_real − ΣH_est) / ΣH_est × 100`, calculada por integrante e para a equipe |
| Indicador | TVE por integrante e para a equipe |
| Fonte e coleta | `esforco.csv` e `linha-de-base-e1.csv`, coletados no domingo |
| Critério de decisão | (OK) −20% a +20% · (REP) de +20% a +40% ou de −40% a −20% · (REV) acima de +40% ou abaixo de −40% |
| Ação disparada | (REP) com TVE acima de +40% para um integrante: transferir tarefas secundárias dele. No fim da *release*, aplicar o fator de correção observado nas estimativas da próxima |

### RC2 - Índice de desempenho de custo (CPI), base hora/valor

| Elemento | Especificação |
|----------|---------------|
| Necessidade de informação | Quanto esforço está custando cada hora de valor entregue? |
| Referência | CID, ICM linhas 7 e 8 (*Cost*, *Effort*, *Earned Value*) |
| Medidas base | `AC` (custo real) = horas reais registradas no período · `EV` (vindo do CP2) |
| Medidas derivadas | `CPI = EV / AC` · `Custo (R$) = AC × VH` |
| Indicador | CPI do ciclo e acumulado, mais o custo do ciclo em R$ |
| Fonte e coleta | `esforco.csv` e cálculo do CP2, coletados no domingo |
| Critério de decisão | (OK) CPI ≥ 0,90 · (REV) 0,75 a 0,90 · (REP) < 0,75 (cada hora gasta entrega menos de 45 min de valor planejado) |
| Ação disparada | (REP) Revisar a granularidade das issues (issues grandes escondem retrabalho) e recalibrar a estimativa |

### RC3 - Contribuição individual

| Elemento | Especificação |
|----------|---------------|
| Necessidade de informação | O trabalho está bem distribuído entre os 6 integrantes? |
| Referência | CID, ICM linha 10 (*Personnel Effort*) |
| Medidas base | `H_real(i)` por integrante. Enquanto as horas não forem registradas, usar *proxies*: commits, linhas alteradas e horas estimadas atribuídas |
| Medida derivada | `PCI(i) = H_real(i) / ΣH_real × 100`, com Σ PCI = 100% |
| Indicador | PCI por integrante, comparado com o ideal de 16,7% |
| Fonte e coleta | `esforco.csv` (prioritário), `commits.csv` e `linha-de-base-e1.csv`, coletados no domingo |
| Critério de decisão | (OK) 13% a 20% · (REV) 10% a 13% ou 20% a 25% · (REP) < 10% ou > 25% |
| Ação disparada | (REP) abaixo de 10%: atribuir issues de revisão, referências ou integração. |

## 4. Desempenho dos Processos

### DP1 - *Lead time* de issue

| Elemento | Especificação |
|----------|---------------|
| Necessidade de informação | Quanto tempo uma demanda leva, do registro até a entrega? |
| Referência | CID, ICM linha 32; especificação 8.5 *Cycle Time / Lead Time* |
| Medidas base | Data e hora de abertura e de fechamento de cada issue |
| Medidas derivadas | `Lead time = fechamento − abertura` (dias) · Idade das abertas = data de corte − abertura |
| Indicador | Média do *lead time* das issues fechadas no ciclo e idade média das abertas |
| Fonte e coleta | API de issues do GitHub, coletada no domingo |
| Critério de decisão | (OK) ≤ 3 dias · (REV) 3 a 5 dias · (REP) > 5 dias. Investigar casos que fiquem mais de 10% acima da média (CID 8.5) |
| Ação disparada | (REP) Dividir issues grandes em partes de até 1 dia de trabalho e revisar as que estão paradas no ponto de controle |

### DP2 - Vazão e trabalho em andamento

| Elemento | Especificação |
|----------|---------------|
| Necessidade de informação | O fluxo de trabalho anda? A saída acompanha a entrada? |
| Referência | CID, ICM linhas 30 e 37; especificação 8.4 *Cumulative Flow* |
| Medidas base | Issues abertas no ciclo (chegadas) · issues fechadas no ciclo (saídas) · issues abertas na data de corte (WIP) |
| Medidas derivadas | `Vazão = saídas / semana` · `Razão saída/chegada` |
| Indicador | Razão saída/chegada (sinaleiro do CID) e WIP |
| Fonte e coleta | Issues do GitHub (estados ao longo do tempo), coletadas na quarta-feira e no domingo |
| Critério de decisão | (OK) razão ≥ 0,90 · (REV) 0,75 a 0,90 · (REP) < 0,75 (faixas do CID). WIP acima de 2 por integrante gera alerta |
| Ação disparada | (REP) Parar de abrir trabalho novo e concentrar a equipe em fechar o que está em andamento |

### DP3 - Concentração do trabalho

| Elemento | Especificação |
|----------|---------------|
| Necessidade de informação | O trabalho é distribuído ao longo do ciclo ou acumulado em um único dia? |
| Referência | CID, ICM linha 30 (*Is the flow of work as efficient and predictable as needed?*) |
| Medidas base | Commits por dia no ciclo · número de dias do ciclo |
| Medidas derivadas | `Índice de pico = commits no dia de maior atividade / commits do ciclo × 100` · `Dias ativos` = dias com pelo menos um commit |
| Indicador | Índice de pico e dias ativos por ciclo |
| Fonte e coleta | `commits.csv` (gerado do `git log`), coletado no domingo |
| Critério de decisão | (OK) pico ≤ 40% · (REV) 40% a 60% · (REP) > 60% |
| Ação disparada | (REP) Exigir entregas parciais (PR) até o ponto de controle de quarta |

### DP4 - Taxa de retrabalho

| Elemento | Especificação |
|----------|---------------|
| Necessidade de informação | Quanto do esforço é gasto corrigindo o que já foi entregue? |
| Referência | CID, ICM linha 19 (*Rework Stories*, *Rework Hours*) |
| Medidas base | Commits do ciclo · commits de retrabalho. A partir do ciclo 2, também PRs com pedido de ajuste |
| Medida derivada | `Retrabalho = commits de retrabalho / commits × 100`. Depois que o fluxo de PR estiver adotado: `PRs com ajuste / PRs × 100` |
| Indicador | Taxa de retrabalho do ciclo |
| Fonte e coleta | `commits.csv` (coluna `tipo`) e PRs do GitHub, coletados no domingo |
| Critério de decisão | (OK) ≤ 20% · (REV) 20% a 35% · (REP) > 35% |
| Ação disparada | (REP) Identificar a causa (mudança de decisão, erro de estrutura ou de padronização) e criar um checklist de revisão para essa causa |

**Critério de classificação do retrabalho.** Um commit é "retrabalho" quando corrige, realinha ou substitui conteúdo já publicado: correção ortográfica ou de frase, realinhamento a uma decisão alterada, ajuste de estrutura ou de faixas de pontuação, reorganização de páginas. É "novo" quando acrescenta conteúdo inédito. A classificação do ciclo 0 foi feita manualmente a partir da mensagem e do conteúdo de cada commit e está registrada em `commits.csv`.


## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 05/10/2026 | Criação da estrutura do documento | Gabriel Fae | - |
| 0.2 | 16/10/2026 | Reorganização da documentação por fases do processo de avaliação | Gabriel Fae | - |
| 0.3 | 25/10/2026 | Plano reestruturado pelo modelo de informação do PSM: 10 métricas ligadas ao CID, base hora/valor (SPI e CPI), parâmetros e limitações dos dados | Gabriel Fae | - |
