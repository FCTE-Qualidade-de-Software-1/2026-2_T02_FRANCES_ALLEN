# Registro de medições

Valores medidos a cada ciclo, com interpretação. As fórmulas e faixas de decisão estão no [plano de medição](plano-de-medicao.md), e os dados brutos ficam em [`dados/gestao/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/gestao). Situação: (OK) dentro da faixa · (A) alerta · (AN) ação necessária · (--) não mensurável no ciclo.

| Ciclo | Período | Marco | Coleta |
|-------|---------|-------|--------|
| 0 (retroativo) | 05/10 a 18/10/2026 | Estruturação e produção das Fases 1 e 2 | 25/10/2026, a partir do `git log` |
| 1 | 19/10 a 25/10/2026 | Milestone E1 (vence em 25/10, 21h) | 25/10/2026, às 20h30. Três commits do ciclo entraram depois dessa hora e foram incorporados retroativamente na coleta de 28/10 |
| 2 | 26/10 a 01/11/2026 | Fechamento da E1 (*release* `v0.1`) | Parcial em 28/10/2026. A coleta de 01/11 não foi feita no dia e foi **fechada retroativamente em 13/11**, a partir do `git log` e da API do GitHub |
| 3 (retroativo) | 02/11 a 08/11/2026 | Abertura da E2: milestones e issues da Fase 3 e da Fase 4 (04/11) | Coletas de 04/11 e 08/11 não feitas no dia. **Medido retroativamente em 13/11**, a partir do `git log` e da API do GitHub |
| 4 (em curso) | 09/11 a 15/11/2026 | Ponto de controle interno de 11/11 e prazo interno da Fase 3 (14/11) | **Parcial em 13/11/2026, às 21h46** (data de corte), a partir do `git log` e da API do GitHub. A coleta completa é em 15/11 |

## 1. Painel dos ciclos

| Métrica | Ciclo 0 | Ciclo 1 | Ciclo 2 | Ciclo 3 | Ciclo 4 (parcial, até 13/11) |
|---------|---------|---------|---------|---------|------------------------------|
| CP1 Comprometido x concluído | (--) sem backlog formal | (--) 11,1% concluído (issues criadas com base no artigo.) | (OK) 100% (18 de 18), desvio de 0 p.p., mas concluído **depois** do vencimento | (AN) E2 Fase 3: 1 de 7 (14,3%) com 39,0% do período, desvio de 24,7 p.p. | (AN) E2 Fase 3: 2 de 7 (28,6%) com 82,5% do período, desvio de 54,0 p.p. |
| CP2 SPI (hora/valor) | (--) sem linha de base | (AN) 0,05 | (OK) 1,00 na data de corte · 0,05 no vencimento · atraso de 1 a 3 dias | (AN) 0,37 (PV 5,5 h · EV 2 h) | (AN) 0,35 (PV 11,6 h · EV 4 h); 0,20 por contagem de issues |
| RC1 Variação de esforço | (--) horas não registradas | (--) horas não registradas | (AN) 0 de 6 integrantes registraram horas até o prazo da D05 | (--) nenhuma issue fechada com horas registradas | (AN) +50% na #21 (3 h reais / 2 h estimadas); equipe não mensurável |
| RC2 CPI (hora/valor) | (--) horas não registradas | (--) horas não registradas | (--) sem `AC`, por falta das horas reais. Custo planejado da E1: **R$2.100** (42 h × R$50) | (--) `AC` de 2 h (R$100) sem relação com a issue fechada | (AN) 0,67 nas entregas do ciclo (EV 2 h / AC 3 h = R$150), só de 1 integrante |
| RC3 Contribuição individual | (AN) 0% a 34,8% (*proxy*: commits) | (A) 7,1% a 28,6% (carga planejada) | (AN) larigs 66,7% · Guilherme-Moura 33,3% · demais 0% (*proxy*: commits) | (AN) Faehzin 50% · LucasAvelar2711 50% · demais 0% (*proxy*: commits) | (AN) Faehzin 100% (*proxy*: commits) |
| DP1 *Lead time* | (--) sem issues | (AN) média de 3,1 dias nas fechadas; abertas com 6,2 dias | (AN) 9,3 dias nas 16 declaradas em 28/10; nenhuma fechada no GitHub no ciclo | (AN) 16,0 dias no GitHub (9,3 declarados) nas 16 fechadas; abertas com 4,4 dias | (AN) #21 com cerca de 6 dias; abertas com 9,3 dias |
| DP2 Razão saída/chegada | (--) sem issues | (AN) 0,11 (2 saídas para 18 chegadas) | (A) 16 saídas e 0 chegadas: razão indefinida. WIP de 0 na data de corte | (OK) 1,33 (16 saídas, 12 chegadas), mas as saídas só regularizam o ciclo 2. WIP de 12 (2,0 por integrante) | (A) 1 saída e 0 chegadas: razão indefinida. WIP de 11 (1,8 por integrante) |
| DP3 Índice de pico | (AN) 82,6% em 18/10 | (AN) 100% em 25/10 (3 commits, medido retroativamente) | (AN) 66,7% em 28/10, 2 dias ativos em 7 | (AN) 100% em 04/11, 1 dia ativo em 7 | (A) 50%, 2 dias ativos em 5 |
| DP4 Retrabalho | (AN) 39,1% | (AN) 66,7% (2 de 3 commits, medido retroativamente) | (AN) 66,7% (2 de 3 commits) · nenhum PR no período | (AN) 50% (2 de 4 commits) | (OK) 0% por commit (0 de 2) · PR #32 integrado sem revisão |

## 2. Ciclo 0 (retroativo): 05/10 a 18/10

### 2.1 Medições

| Métrica | Valor | Limite | Situação | Interpretação |
|---------|-------|--------|:--------:|---------------|
| CP1 / CP2 | Não aplicável | - | (--) | Não existiam milestone nem issues. O trabalho não tinha compromisso registrado, e a ausência dessa informação já é um achado (*lack of information*, PSM cap. 2) |
| RC1 / RC2 | Não aplicável | - | (--) | Só um membro declarou horas. Revisão necessária. |
| RC3 (*proxy*: commits) | Faehzin 34,8% · LucasAvelar2711 26,1% · Guilherme-Moura 17,4% · larigs 13,0% · GuilhermeMM3 8,7% · MrBolt2005 0% | 13% a 20% | (AN) | Distribuição desigual. A estruturação inicial do repositório concentrou commits e trabalho, considerando que João Felipe trabalhou no overleaf |
| RC3 (*proxy*: linhas, sem os commits de estruturação) | LucasAvelar2711 44,4% · Faehzin 20,9% · larigs 16,5% · Guilherme-Moura 16,1% · GuilhermeMM3 2,2% · MrBolt2005 0% | 13% a 20% | (AN) | Em volume de conteúdo, os objetivos GQM (G2 e diagrama) concentraram a produção |
| DP3 Índice de pico | 19 de 23 commits em 18/10 = **82,6%**. 4 dias ativos em 14 | ≤ 40% | (AN) | O trabalho se acumulou em um único dia, às vésperas da criação das issues da E1 |
| DP4 Retrabalho | 9 de 23 commits = **39,1%** (em 18/10: 8 de 19 = 42,1%) | ≤ 20% | (AN) | O pico gerou revisão de estrutura em sequência: faixas de nível com buracos, G2 realinhado às sete subcaracterísticas, troca de modificabilidade por testabilidade em C3, correções de redação |
| Revisão de PR | -- | - | (--) | Não houve revisão formal. |

### 2.2 Gráficos

```mermaid
---
config:
  themeVariables:
    xyChart:
      plotColorPalette: "#B4531A"
      titleColor: "#7D8E95"
      xAxisLabelColor: "#7D8E95"
      xAxisTitleColor: "#7D8E95"
      xAxisLineColor: "#7D8E95"
      xAxisTickColor: "#7D8E95"
      yAxisLabelColor: "#7D8E95"
      yAxisTitleColor: "#7D8E95"
      yAxisLineColor: "#7D8E95"
      yAxisTickColor: "#7D8E95"
      backgroundColor: "transparent"
---
xychart-beta
    title "Commits por dia (05/10 a 28/10/2026)"
    x-axis "Dia de outubro" [05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    y-axis "Commits" 0 --> 20
    bar [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 19, 0, 0, 0, 0, 0, 0, 3, 1, 0, 2]
```

_Figura 1 - Commits por dia no repositório, sem os commits de merge, de 05/10 a 28/10 (29 commits). Os 23 commits até 18/10 são o ciclo 0, os 3 de 25/10 são o ciclo 1 e os 3 de 26 a 28/10 são o parcial do ciclo 2. A barra de 25/10 foi acrescentada na coleta de 28/10: na coleta do próprio ciclo 1 ela aparecia como zero, porque os commits entraram depois do horário da coleta. Indicador DP3. Fonte: [`commits.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/blob/main/dados/gestao/commits.csv)._

```mermaid
---
config:
  themeVariables:
    xyChart:
      plotColorPalette: "#0B5563"
      titleColor: "#7D8E95"
      xAxisLabelColor: "#7D8E95"
      xAxisTitleColor: "#7D8E95"
      xAxisLineColor: "#7D8E95"
      xAxisTickColor: "#7D8E95"
      yAxisLabelColor: "#7D8E95"
      yAxisTitleColor: "#7D8E95"
      yAxisLineColor: "#7D8E95"
      yAxisTickColor: "#7D8E95"
      backgroundColor: "transparent"
---
xychart-beta horizontal
    title "Commits por integrante - ciclo 0"
    x-axis ["Faehzin", "LucasAvelar2711", "Guilherme-Moura", "larigs", "GuilhermeMM3", "MrBolt2005"]
    y-axis "Commits" 0 --> 10
    bar [8, 6, 4, 3, 2, 0]
```

_Figura 2 - Commits por integrante no ciclo 0, como proxy do RC3 até o registro de horas. Fonte: `commits.csv`._

```mermaid
---
config:
  themeVariables:
    xyChart:
      plotColorPalette: "#0B5563"
      titleColor: "#7D8E95"
      xAxisLabelColor: "#7D8E95"
      xAxisTitleColor: "#7D8E95"
      xAxisLineColor: "#7D8E95"
      xAxisTickColor: "#7D8E95"
      yAxisLabelColor: "#7D8E95"
      yAxisTitleColor: "#7D8E95"
      yAxisLineColor: "#7D8E95"
      yAxisTickColor: "#7D8E95"
      backgroundColor: "transparent"
---
xychart-beta horizontal
    title "Linhas alteradas por integrante - ciclo 0 (sem os commits de estruturacao)"
    x-axis ["LucasAvelar2711", "Faehzin", "larigs", "Guilherme-Moura", "GuilhermeMM3", "MrBolt2005"]
    y-axis "Linhas adicionadas + removidas" 0 --> 750
    bar [719, 338, 267, 261, 36, 0]
```

_Figura 3 - Volume de conteúdo por integrante no ciclo 0, em linhas adicionadas mais removidas, excluídos os três commits de estruturação do repositório (1.658 linhas das 3.279 do ciclo). É o segundo *proxy* do RC3 e corresponde aos percentuais da tabela 2.1: LucasAvelar2711 44,4%, Faehzin 20,9%, larigs 16,5%, Guilherme-Moura 16,1% e GuilhermeMM3 2,2%, de um total de 1.621 linhas. **Não há gráfico de horas nem de custo neste ciclo:** não existia linha de base de horas e nenhum integrante registrou esforço, então RC1 e RC2 não são calculáveis para o período. Fonte: [`commits.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/blob/main/dados/gestao/commits.csv) (colunas `linhas_adicionadas` e `linhas_removidas`)._
```mermaid
---
config:
  themeVariables:
    pie1: "#0B5563"
    pie2: "#B4531A"
    pieStrokeColor: "#FFFFFF"
    pieOuterStrokeColor: "#7D8E95"
    pieSectionTextColor: "#FFFFFF"
    pieTitleTextColor: "#7D8E95"
    pieLegendTextColor: "#7D8E95"
---
pie showData title Natureza dos commits - ciclo 0
    "Conteúdo novo" : 14
    "Retrabalho" : 9
```

_Figura 4 - Proporção de commits de retrabalho no ciclo 0. Indicador DP4. Fonte: `commits.csv` (coluna `tipo`)._

## 3. Ciclo 1: 19/10 a 25/10 (milestone E1)

### 3.1 Medições

| Métrica | Valor | Limite | Situação | Interpretação |
|---------|-------|--------|:--------:|---------------|
| CP1 Comprometido x concluído | 2 de 18 issues = **11,1%**, com 100% do período decorrido (desvio de 88,9 p.p.). Issues do artigo: 0 de 9 | desvio ≤ 5 p.p. | (AN) | Backlog aberto pois se relaciona à completude do artigo. |
| CP2 SPI | PV = 42 h · EV = 2 h (#11 e #15) · **SPI = 0,05** | ≥ 0,90 | (AN) | Só 5% do valor planejado foi entregue formalmente. O caminho crítico é o artigo, que concentra 24 h das 42 h |
| RC1 / RC2 | Não mensurável | - | (--) | -- |
| RC3 (carga planejada) | MrBolt2005 28,6% (12 h) · Guilherme-Moura 21,4% (9 h) · GuilhermeMM3 16,7% (7 h) · Faehzin 14,3% (6 h) · larigs 11,9% (5 h) · LucasAvelar2711 7,1% (3 h) | 13% a 20% | (A) | --|
| DP1 *Lead time* | Fechadas: média de **3,1 dias** (#15 com 0,01 dia e #11 com 6,2 dias) · abertas: idade média de **6,2 dias** | ≤ 3 dias | (AN) | As duas issues fechadas são as de menor esforço (1 h cada). A idade das 16 abertas já estava acima do limite na data de corte |
| DP2 Razão saída/chegada | 2 saídas para 18 chegadas = **0,11** · WIP de 16 issues (**2,7** por integrante) | ≥ 0,90 · WIP ≤ 2 | (AN) | Todo o backlog da E1 entrou de uma vez em 19/10 e quase nada saiu. O WIP nasceu acima do limite depois fixado na D04 |
| DP3 Índice de pico (retroativo) | 3 de 3 commits em 25/10 = **100%**. 1 dia ativo em 7 | ≤ 40% | (AN) | **Correção retroativa.** Na coleta de 25/10, às 20h30, o ciclo não tinha commits no repositório. Os três commits do ciclo saíram todos em 25/10, dois deles depois da coleta: [`3ce20cc`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/commit/3ce20cc) às 20h36, [`31cff66`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/commit/31cff66) às 21h55 e [`3304199`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/commit/3304199) às 22h26. O padrão de rajada do ciclo 0 se repetiu, agora na véspera da entrega |
| DP4 Retrabalho (retroativo) | 2 de 3 commits = **66,7%** | ≤ 20% | (AN) | `31cff66` reescreve a H1.5 em Jaccard 0,70 para coincidir com o nível Bom de M1.5.2 e `3304199` enxuga o texto da Fase 2 e realinha F05: as duas correções vêm da revisão estrutural da D02 |
| Rastreabilidade | 0 de 3 commits com `Closes #N` · nenhum PR no ciclo | 100% | (AN) | O trabalho do artigo ocorreu fora do repositório (Overleaf) e as correções da Fase 2 entraram direto no `main` |

### 3.2 Gráficos

```mermaid
---
config:
  themeVariables:
    xyChart:
      plotColorPalette: "#8C9BA1, #B4531A"
      titleColor: "#7D8E95"
      xAxisLabelColor: "#7D8E95"
      xAxisTitleColor: "#7D8E95"
      xAxisLineColor: "#7D8E95"
      xAxisTickColor: "#7D8E95"
      yAxisLabelColor: "#7D8E95"
      yAxisTitleColor: "#7D8E95"
      yAxisLineColor: "#7D8E95"
      yAxisTickColor: "#7D8E95"
      backgroundColor: "transparent"
---
xychart-beta
    title "Burnup da milestone E1 (issues)"
    x-axis "Dia de outubro" [19, 20, 21, 22, 23, 24, 25]
    y-axis "Issues concluídas (acumulado)" 0 --> 18
    line [2.6, 5.1, 7.7, 10.3, 12.9, 15.4, 18]
    line [1, 1, 1, 1, 1, 1, 2]
```

_Figura 5 - Burnup da E1: linha cinza = planejado (18 issues distribuídas de forma linear até 25/10), linha terracota = concluído. Indicador CP1. Fonte: [`linha-de-base-e1.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/blob/main/dados/gestao/linha-de-base-e1.csv)._

```mermaid
---
config:
  themeVariables:
    xyChart:
      plotColorPalette: "#0B5563, #B4531A"
      titleColor: "#7D8E95"
      xAxisLabelColor: "#7D8E95"
      xAxisTitleColor: "#7D8E95"
      xAxisLineColor: "#7D8E95"
      xAxisTickColor: "#7D8E95"
      yAxisLabelColor: "#7D8E95"
      yAxisTitleColor: "#7D8E95"
      yAxisLineColor: "#7D8E95"
      yAxisTickColor: "#7D8E95"
      backgroundColor: "transparent"
---
xychart-beta
    title "Valor planejado (PV) x valor agregado (EV) em horas - E1"
    x-axis "Dia de outubro" [19, 20, 21, 22, 23, 24, 25]
    y-axis "Horas (acumulado)" 0 --> 45
    bar [6, 12, 18, 24, 30, 36, 42]
    line [1, 1, 1, 1, 1, 1, 2]
```

_Figura 6 - Análise de valor agregado da E1: barras = PV, linha = EV. SPI = EV / PV. Indicador CP2. Fonte: `linha-de-base-e1.csv`._

```mermaid
---
config:
  themeVariables:
    xyChart:
      plotColorPalette: "#0B5563, #B4531A, #8C9BA1"
      titleColor: "#7D8E95"
      xAxisLabelColor: "#7D8E95"
      xAxisTitleColor: "#7D8E95"
      xAxisLineColor: "#7D8E95"
      xAxisTickColor: "#7D8E95"
      yAxisLabelColor: "#7D8E95"
      yAxisTitleColor: "#7D8E95"
      yAxisLineColor: "#7D8E95"
      yAxisTickColor: "#7D8E95"
      backgroundColor: "transparent"
---
xychart-beta
    title "Horas da E1 por integrante - planejado x entregue no ciclo 1"
    x-axis ["MrBolt2005", "Guilherme-Moura", "GuilhermeMM3", "Faehzin", "larigs", "LucasAvelar2711"]
    y-axis "Horas estimadas" 0 --> 13
    bar [12, 9, 7, 6, 5, 3]
    line [0, 0, 1, 1, 0, 0]
    line [7, 7, 7, 7, 7, 7]
```

_Figura 7 - Carga da E1 por integrante: barras = horas planejadas (42 h no total), linha terracota = horas entregues até 25/10 (2 h, das issues #11 e #15) e linha cinza = distribuição ideal de 7 h por pessoa, ou 16,7%. É o RC3 pela carga planejada somado ao EV do CP2 por integrante. Duas ressalvas: as horas são **estimadas**, porque nenhuma hora real foi registrada, e a atribuição é a de 19/10, anterior ao remanejamento de 28/10 ([D08](decisoes.md#d08-remanejar-as-divisoes-de-trabalho-da-equipe)). Fonte: `linha-de-base-e1.csv`._

```mermaid
---
config:
  themeVariables:
    xyChart:
      plotColorPalette: "#B4531A"
      titleColor: "#7D8E95"
      xAxisLabelColor: "#7D8E95"
      xAxisTitleColor: "#7D8E95"
      xAxisLineColor: "#7D8E95"
      xAxisTickColor: "#7D8E95"
      yAxisLabelColor: "#7D8E95"
      yAxisTitleColor: "#7D8E95"
      yAxisLineColor: "#7D8E95"
      yAxisTickColor: "#7D8E95"
      backgroundColor: "transparent"
---
xychart-beta
    title "Horas estimadas da E1 por categoria de trabalho"
    x-axis ["artigo", "fase-1", "fase-2", "gestao", "entrega", "gitpage"]
    y-axis "Horas estimadas" 0 --> 25
    bar [24, 6, 5, 4, 2, 1]
```

_Figura 8 - Distribuição das 42 h da E1 por categoria. O artigo concentra 24 h, 57% do valor planejado da entrega, e é o caminho crítico citado na [D03](decisoes.md#d03-recalcular-esforco-pro-artigo): no fim do ciclo 1 nenhuma das suas 9 issues estava fechada, o que por si só explica o SPI de 0,05. Fonte: `linha-de-base-e1.csv` (coluna `categoria`)._


## 4. Ciclo 2 (parcial): 26/10 a 28/10

Coleta do **ponto de controle de quarta-feira** definido na [D04](decisoes.md#d04-readaptar-o-processo-de-desenvolvimento-e-pesquisa). Escopo previsto para esta coleta: **CP1, CP2, DP2 e as horas retroativas dos ciclos 0 e 1**. As demais métricas ficam para a coleta completa de domingo. Data de corte: **28/10/2026, 21h**.

### 4.1 Contexto da coleta

| Item | Registro |
|------|----------|
| Fechamento da E1 | As **18 issues da milestone E1 foram declaradas concluídas** no ponto de controle. A entrega saiu na *release* [`v0.1`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/releases/tag/v0.1) ("Release E1 - Ponto de Controle 1"), publicada em **26/10 às 20h25**, sobre o commit [`030f62d`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/commit/030f62d). A retrospectiva da E1 entrou no repositório em 28/10 ([`5741d9c`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/commit/5741d9c) e [`f25cb3d`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/commit/f25cb3d)) |
| Remanejamento das divisões | A equipe **remanejou as divisões de trabalho** no ponto de controle. A coluna `responsavel` da [`linha-de-base-e1.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/blob/main/dados/gestao/linha-de-base-e1.csv) passa a valer apenas como registro histórico do planejamento da E1: ela não descreve quem executou o trabalho no fechamento e não vale para a E2 (ver [D08](decisoes.md#d08-remanejar-as-divisoes-de-trabalho-da-equipe)) |
| Onde a decisão foi tomada | O ponto de controle **não ocorreu em sala**, por falta de tempo de aula, e correu **fora de sala, de forma assíncrona**, com manifestação de parte da equipe. É o mesmo fator que explica o resultado das horas retroativas abaixo (ver [D09](decisoes.md#d09-canal-assincrono-com-prazo-de-resposta)) |
| Qualidade do dado (importante) | O fechamento das issues foi **declarado em lote** no ponto de controle e **não foi registrado no GitHub**: em consulta à API em 04/11, a milestone E1 ainda constava `open`, com 16 das 18 issues no estado `OPEN` e sem `closedAt`. CP1 e CP2 desta coleta vêm da **declaração do ponto de controle e da *release* `v0.1`**, não do estado das issues na API. É exatamente a falha de rastreabilidade que a [D06](decisoes.md#d06-rastreabilidade-do-trabalho-no-repositorio) deveria ter corrigido, e ela rebaixa a confiança de CP1, CP2, DP1 e DP2 de "medido" para "declarado" |

**Dados brutos desta coleta.** A [`linha-de-base-e1.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/blob/main/dados/gestao/linha-de-base-e1.csv) ganhou duas colunas, que separam o que foi medido do que foi declarado: `fechada_em` continua sendo a data de fechamento **registrada no GitHub** (preenchida só para as issues #11 e #15) e `concluida_em_declarado` traz a data de conclusão **declarada no ponto de controle** (28/10 para as 16 restantes), com `status_28_10` indicando qual das duas vale para cada issue. A [`commits.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/blob/main/dados/gestao/commits.csv) recebeu as 6 linhas dos ciclos 1 e 2 que faltavam, com a mesma classificação manual de `tipo` descrita no plano de medição. Como `concluida_em_declarado` é a data do ponto de controle e não a da conclusão real de cada item, o *lead time* (DP1) calculado sobre ela é um **limite superior**.

### 4.2 Medições

| Métrica | Valor | Limite | Situação | Interpretação |
|---------|-------|--------|:--------:|---------------|
| CP1 Comprometido x concluído | `I_conc` = 18 de `I_comp` = 18 = **100% concluído**, com 100% do período decorrido: **desvio de 0 p.p.** (era 88,9 p.p. em 25/10) | desvio ≤ 5 p.p. | (OK) | O escopo da E1 foi entregue **integralmente, mas fora do prazo**. As 9 issues do artigo, que no ciclo 1 estavam todas abertas, foram concluídas em três dias. O indicador entra na faixa OK porque, passado o fim da milestone, `%Planejado` satura em 100% e o desvio se anula: o atraso não aparece mais no CP1 e tem de ser lido no CP2 |
| CP2 SPI na data de corte | `PV` = 42 h (saturado no total da E1) · `EV` = 42 h · **SPI = 1,00** | ≥ 0,90 | (OK) | Todo o valor planejado da E1 virou entrega |
| CP2 SPI no vencimento | No vencimento da milestone (25/10, 21h): `PV` = 42 h · `EV` = 2 h · **SPI = 0,05** | ≥ 0,90 | (AN) | É este o número que descreve o prazo da E1. O SPI converge para 1,00 em qualquer projeto que termine, por mais atrasado que esteja, então o atraso tem de ser registrado em dias, na linha abaixo |
| CP2 Variação de prazo (em dias) | *Release* `v0.1` em 26/10, 20h25 = **~1 dia** após o vencimento · fechamento formal das issues até 28/10 = **3 dias** após o vencimento. Em um ciclo de 7 dias, 14% a 43% de atraso | - | (A) | Efeito direto da [D03](decisoes.md#d03-recalcular-esforco-pro-artigo): com o cronograma do artigo recalculado, as 24 h do caminho crítico saíram, mas estouraram o prazo da E1 |
| DP2 Vazão | **16 saídas** em 3 dias (as outras 2 das 18 já haviam saído no ciclo 1). Extrapolado, 37 issues/semana | - | (A) | Não é vazão sustentável: é a drenagem, de uma só vez, do backlog acumulado de 18 issues. Serve como teto, não como capacidade da equipe |
| DP2 Razão saída/chegada | **0 chegadas** e 16 saídas: razão **indefinida** (divisão por zero) | ≥ 0,90 | (A) | A razão não é calculável porque nenhuma issue nova foi aberta no ciclo. Olhando só o fluxo de saída, o indicador inverteu em relação ao ciclo 1 (0,11): o problema deixou de ser trabalho que não sai e passou a ser trabalho novo que não entra |
| DP2 Trabalho em andamento (WIP) | **0 issues abertas** na data de corte, contra 16 em 25/10. 0 por integrante | ≤ 2 por integrante | (A) | O limite da D04 passou a ser respeitado, mas pelo motivo errado: o WIP é zero porque o backlog da E1 esvaziou e **o da E2 não existe**. Com WIP zero e nenhuma chegada, o ciclo seguinte começa sem trabalho comprometido e CP1, CP2, DP1 e DP2 voltam a ser não mensuráveis (ver [D10](decisoes.md#d10-planejar-o-ciclo-no-github-antes-de-ele-comecar)) |
| Horas retroativas dos ciclos 0 e 1 | [`esforco.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/blob/main/dados/gestao/esforco.csv) continua **só com o cabeçalho**: **0 de 6 integrantes** registraram horas até o prazo de 28/10 | 6 de 6 | (AN) | A [D05](decisoes.md#d05-registro-obrigatorio-de-horas) **não foi executada**. Sem `H_real` não há `AC`, logo RC1, RC2 e o RC3 por horas reais seguem não mensuráveis pelo terceiro ciclo seguido, e a base hora/valor do plano continua sustentada só por estimativa. A causa registrada é a mesma do contexto: a cobrança correu fora de sala e parte da equipe não respondeu |
| Rastreabilidade (verificação da D06) | 3 commits no período, **0 com `Closes #N`** · **0 PRs** abertos ou revisados (o único PR do repositório é o #1, de 18/10, sem revisão) · `030f62d` ainda com o autor genérico `user` | 100% dos PRs ligados a issue e revisados | (AN) | A **D06 não foi executada**: o fluxo branch → PR → revisão não entrou em uso, os commits foram direto no `main` e a identidade do git não foi corrigida. Por isso o DP4 por PR, previsto para a coleta de domingo, continua sem base de cálculo |
| DP3 / DP4 (parcial, informativo) | 3 commits em 26 a 28/10: [`030f62d`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/commit/030f62d) (26/10, Guilherme-Moura, retrabalho: README reescrito, 21 linhas por 20), `5741d9c` (28/10, larigs, novo: retrospectiva) e `f25cb3d` (28/10, larigs, retrabalho: troca do arquivo errado). Pico de **66,7%** em 28/10, 2 dias ativos em 3, retrabalho de **66,7%** | pico ≤ 40% · retrabalho ≤ 20% | (--) | Fecha na coleta de domingo. Os dois indicadores já apontam fora da faixa, e os três commits do período são de documentação e correção: o conteúdo do artigo continua fora do repositório |

### 4.3 Gráficos

```mermaid
---
config:
  themeVariables:
    xyChart:
      plotColorPalette: "#8C9BA1, #B4531A"
      titleColor: "#7D8E95"
      xAxisLabelColor: "#7D8E95"
      xAxisTitleColor: "#7D8E95"
      xAxisLineColor: "#7D8E95"
      xAxisTickColor: "#7D8E95"
      yAxisLabelColor: "#7D8E95"
      yAxisTitleColor: "#7D8E95"
      yAxisLineColor: "#7D8E95"
      yAxisTickColor: "#7D8E95"
      backgroundColor: "transparent"
---
xychart-beta
    title "Burnup da E1 estendido ate o ponto de controle (issues)"
    x-axis "Dia de outubro" [19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    y-axis "Issues concluidas (acumulado)" 0 --> 18
    line [2.6, 5.1, 7.7, 10.3, 12.9, 15.4, 18, 18, 18, 18]
    line [1, 1, 1, 1, 1, 1, 2, 2, 2, 18]
```

_Figura 9 - Burnup da E1 estendido até 28/10: linha cinza = planejado, linha terracota = concluído. As 16 issues restantes foram declaradas concluídas em bloco no ponto de controle, três dias após o vencimento da milestone. Indicador CP1. Fonte: [`linha-de-base-e1.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/blob/main/dados/gestao/linha-de-base-e1.csv) e declaração do ponto de controle de 28/10._

```mermaid
---
config:
  themeVariables:
    xyChart:
      plotColorPalette: "#0B5563, #B4531A"
      titleColor: "#7D8E95"
      xAxisLabelColor: "#7D8E95"
      xAxisTitleColor: "#7D8E95"
      xAxisLineColor: "#7D8E95"
      xAxisTickColor: "#7D8E95"
      yAxisLabelColor: "#7D8E95"
      yAxisTitleColor: "#7D8E95"
      yAxisLineColor: "#7D8E95"
      yAxisTickColor: "#7D8E95"
      backgroundColor: "transparent"
---
xychart-beta
    title "PV x EV em horas - E1 ate o ponto de controle"
    x-axis "Dia de outubro" [19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    y-axis "Horas (acumulado)" 0 --> 45
    bar [6, 12, 18, 24, 30, 36, 42, 42, 42, 42]
    line [1, 1, 1, 1, 1, 1, 2, 2, 2, 42]
```

_Figura 10 - Valor planejado (barras) e valor agregado (linha) da E1 até 28/10. O encontro das duas curvas no fim do período é o que faz o SPI ir de 0,05 a 1,00 sem que o atraso desapareça: ele passa a ser lido na variação de prazo em dias. Indicador CP2. Fonte: `linha-de-base-e1.csv`._

```mermaid
---
config:
  themeVariables:
    xyChart:
      plotColorPalette: "#0B5563, #B4531A"
      titleColor: "#7D8E95"
      xAxisLabelColor: "#7D8E95"
      xAxisTitleColor: "#7D8E95"
      xAxisLineColor: "#7D8E95"
      xAxisTickColor: "#7D8E95"
      yAxisLabelColor: "#7D8E95"
      yAxisTitleColor: "#7D8E95"
      yAxisLineColor: "#7D8E95"
      yAxisTickColor: "#7D8E95"
      backgroundColor: "transparent"
---
xychart-beta
    title "Trabalho em andamento (WIP) por dia e limite da equipe"
    x-axis "Dia de outubro" [19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    y-axis "Issues abertas" 0 --> 18
    line [17, 17, 17, 17, 17, 17, 16, 16, 16, 0]
    line [12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
```

_Figura 11 - WIP diário (linha azul) contra o limite da equipe de 12 issues, ou 2 por integrante (linha terracota). O WIP ficou acima do limite por nove dias e caiu a zero de uma vez no ponto de controle. Indicador DP2. Fonte: issues da milestone E1 e declaração do ponto de controle._

```mermaid
---
config:
  themeVariables:
    xyChart:
      plotColorPalette: "#0B5563, #B4531A"
      titleColor: "#7D8E95"
      xAxisLabelColor: "#7D8E95"
      xAxisTitleColor: "#7D8E95"
      xAxisLineColor: "#7D8E95"
      xAxisTickColor: "#7D8E95"
      yAxisLabelColor: "#7D8E95"
      yAxisTitleColor: "#7D8E95"
      yAxisLineColor: "#7D8E95"
      yAxisTickColor: "#7D8E95"
      backgroundColor: "transparent"
---
xychart-beta
    title "Custo da E1 em reais - planejado (PV x VH) x agregado (EV x VH)"
    x-axis "Dia de outubro" [19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    y-axis "Reais (acumulado)" 0 --> 2200
    bar [300, 600, 900, 1200, 1500, 1800, 2100, 2100, 2100, 2100]
    line [50, 50, 50, 50, 50, 50, 100, 100, 100, 2100]
```

_Figura 12 - A curva do CP2 convertida em reais pelo valor-hora de referência de R$50: barras = custo planejado (PV × VH) e linha = valor entregue (EV × VH). A E1 vale **R$2.100** de esforço planejado; no vencimento havia R$100 entregues e, no ponto de controle, os R$2.100 completos. **Isto não é o CPI:** o CPI exige o custo real (`AC` = horas reais × VH) e, com o `esforco.csv` vazio, não há `AC`, então o RC2 segue não mensurável. Fonte: `linha-de-base-e1.csv` e o VH de R$50 do [plano de medição](plano-de-medicao.md)._

```mermaid
---
config:
  themeVariables:
    xyChart:
      plotColorPalette: "#0B5563, #8C9BA1"
      titleColor: "#7D8E95"
      xAxisLabelColor: "#7D8E95"
      xAxisTitleColor: "#7D8E95"
      xAxisLineColor: "#7D8E95"
      xAxisTickColor: "#7D8E95"
      yAxisLabelColor: "#7D8E95"
      yAxisTitleColor: "#7D8E95"
      yAxisLineColor: "#7D8E95"
      yAxisTickColor: "#7D8E95"
      backgroundColor: "transparent"
---
xychart-beta
    title "Simulacao: quanto a E1 pagaria a cada integrante pelas horas planejadas"
    x-axis ["MrBolt2005", "Guilherme-Moura", "GuilhermeMM3", "Faehzin", "larigs", "LucasAvelar2711"]
    y-axis "Reais" 0 --> 650
    bar [600, 450, 350, 300, 250, 150]
    line [350, 350, 350, 350, 350, 350]
```

_Figura 13 - Simulação de remuneração da E1 a R$50 por hora: MrBolt2005 R$600 (12 h), Guilherme-Moura R$450 (9 h), GuilhermeMM3 R$350 (7 h), Faehzin R$300 (6 h), larigs R$250 (5 h) e LucasAvelar2711 R$150 (3 h), de um total de R$2.100._

### 4.4 Leitura do ciclo e decisões disparadas

1. **O escopo foi salvo, o prazo não.** CP1 fechou em 100% e o SPI em 1,00, mas ambos só na data de corte: no vencimento o SPI era 0,05 e a entrega saiu com 1 a 3 dias de atraso. A D03 funcionou como ação de recuperação, não como ação de prazo.
2. **O risco mudou de lado.** No ciclo 1 o problema era trabalho que entrava e não saía (razão de 0,11, WIP de 2,7 por pessoa). Agora é o contrário: nenhuma chegada, WIP zero e nenhum backlog para o ciclo seguinte. Dispara a **D10**.
3. **As duas decisões de infraestrutura de medição não saíram do papel.** D05 (horas) com 0 de 6 e D06 (PR e rastreabilidade) com 0 PRs e 0 `Closes #N`. Enquanto isso, três das dez métricas do plano (RC1, RC2 e o RC3 por horas reais) seguem não mensuráveis e os números de CP1 e CP2 dependem de declaração, não de registro. É o achado mais grave desta coleta.
4. **A causa comum é de comunicação, não de esforço.** O ponto de controle correu fora de sala, por falta de tempo em aula, e com resposta parcial da equipe. Dispara a **D09**.
5. **O remanejamento das divisões invalida a base de atribuição da E1.** A carga planejada por integrante (de 7,1% a 28,6%) não serve mais para julgar contribuição individual. Dispara a **D08**, que absorve a D07.

## 5. Ciclo 2 (fechamento retroativo): 26/10 a 01/11

A coleta completa de 01/11 não foi feita no dia. Ela foi fechada em 13/11 com os mesmos dados que ela teria: o `git log` e a API do GitHub, que guardam data e hora de cada evento. Nada mudou no repositório entre 29/10 e 01/11, então os valores da coleta parcial de 28/10 viram os valores finais do ciclo, e esta seção registra só o que ficou para domingo.

| Métrica | Valor | Limite | Situação | Interpretação |
|---------|-------|--------|:--------:|---------------|
| DP1 *Lead time* | 16 issues declaradas concluídas em 28/10: **9,3 dias** da abertura (19/10, 14h35) à declaração. No GitHub, nenhuma issue foi fechada no ciclo | ≤ 3 dias | (AN) | Como a data é a do ponto de controle, e não a da conclusão real, 9,3 dias é um limite superior. Mesmo assim fica três vezes acima da faixa |
| DP3 Índice de pico | 2 de 3 commits em 28/10 = **66,7%**. 2 dias ativos em 7 (26 e 28/10). Nenhum commit de 29/10 a 01/11 | ≤ 40% | (AN) | O ciclo terminou com quatro dias sem atividade no repositório, o que antecipa o ciclo 3 sem backlog (D10) |
| DP4 Retrabalho | 2 de 3 commits = **66,7%**. Nenhum PR | ≤ 20% | (AN) | Os três commits do ciclo são de documentação e correção. Sem PR, o DP4 por PR segue sem base de cálculo |
| RC3 Contribuição individual (*proxy*: commits) | larigs 2 (**66,7%**) · Guilherme-Moura 1 (**33,3%**) · demais 0 | 13% a 20% | (AN) | Com três commits, o *proxy* não diz nada sobre a equipe. O trabalho do ciclo foi o artigo, que está no Overleaf e não aparece no repositório |
| RC1 / RC2 | Nenhuma hora registrada com data no ciclo | - | (--) | O `esforco.csv` continuava vazio em 01/11 |

## 6. Ciclo 3 (retroativo): 02/11 a 08/11

### 6.1 Contexto

| Item | Registro |
|------|----------|
| Abertura da E2 | Em **04/11 (quarta-feira), às 14h26**, foram criadas as milestones "E2 - Ponto de controle (Fase 3)", com vencimento em 15/11 às 21h, e "E2 - Entrega final (Fase 4 e artigo v2)", com vencimento em 21/11 às 21h. No mesmo minuto foram abertas as 12 issues #20 a #31, cada uma com responsável e rótulo, duas por integrante. A #14, pendente da E1, foi movida para a milestone da Fase 3 e fechada |
| Regularização da E1 | Também em 04/11, entre 14h19 e 14h26, as 15 issues da E1 que estavam abertas foram fechadas no GitHub. A milestone **E1 continua aberta**, com 0 issues abertas e 17 fechadas |
| Linha de base da E2 | As issues foram abertas **sem horas estimadas**, e as datas de fim planejadas estão só no [cronograma da avaliação](../fase-3/cronograma.md). A estimativa foi feita pelo gerente de medição **em 13/11, depois do início da E2**: 2 h para cada issue da Fase 3 (#14 e #20 a #25, 14 h) e de 3 h a 5 h para as da Fase 4, conforme o trabalho de preparar o formulário, as questões e a medição (#26, #27 e #28 com 5 h; #29 e #31 com 4 h; #30 com 3 h; 26 h). Total da E2: **40 h**, ou **R$2.000**. Está em [`linha-de-base-e2.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/blob/main/dados/gestao/linha-de-base-e2.csv). Por ser posterior, a estimativa vale para calcular CP2, RC1 e RC2, mas não serviu para planejar os ciclos 3 e 4 |
| PR | O PR [#32](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/pull/32) (Fase 3 e correções da E1) foi aberto em 04/11 com `Refs #25` e pedido de revisão por dono de página. É o primeiro PR desde o #1 |

### 6.2 Medições

| Métrica | Valor | Limite | Situação | Interpretação |
|---------|-------|--------|:--------:|---------------|
| CP1 Comprometido x concluído | Milestone "E2 - Ponto de controle": `I_comp` = 7 (#14 e #20 a #25), `I_conc` = 1 (#14) = **14,3%**. Em 08/11, 23h59, tinham passado **39,0%** do período da milestone (de 04/11, 14h26, a 15/11, 21h): **desvio de 24,7 p.p.** | ≤ 5 p.p. | (AN) | A única issue fechada é uma sobra da E1. Nenhum dos seis métodos da Fase 3 foi entregue no ciclo |
| CP2 SPI | Milestone "E2 - Ponto de controle": 14 h estimadas. Em 08/11, 23h59, `PV` = 39,0% × 14 h = **5,5 h** · `EV` = 2 h (#14) · **SPI = 0,37** | ≥ 0,90 | (AN) | Pela estimativa retroativa, o ciclo entregou pouco mais de um terço do valor planejado. A única issue fechada é uma sobra da E1 |
| RC1 / RC2 | 2 h registradas com data no ciclo (Faehzin, PSM). `AC` = 2 h = **R$100**. A issue fechada (#14) não tem horas registradas | - | (--) | O trabalho com horas registradas (PSM) não tem issue, e a issue fechada não tem horas, então não há par estimado x real nem CPI com significado |
| RC3 (*proxy*: commits) | Faehzin 2 (**50%**) · LucasAvelar2711 2 (**50%**) · demais 0 | 13% a 20% | (AN) | Dois integrantes concentraram todo o trabalho no repositório |
| RC3 (*proxy*: linhas) | Faehzin 431 (**59,6%**) · LucasAvelar2711 292 (**40,4%**) · demais 0 | 13% a 20% | (AN) | Mesma leitura do *proxy* de commits |
| RC3 (carga planejada da E2) | 38 h estimadas nas issues #20 a #31: Faehzin, larigs e MrBolt2005 com 7 h (**18,4%** cada) · Guilherme-Moura e LucasAvelar2711 com 6 h (**15,8%**) · GuilhermeMM3 com 5 h (**13,2%**) | 13% a 20% | (OK) | Primeira distribuição planejada dentro da faixa para os seis integrantes. A #14, sobra da E1 com 2 h, fica de fora |
| DP1 *Lead time* | 16 issues fechadas no GitHub em 04/11 (15 da E1 e a #14): **16,0 dias** de média. Pela data declarada (28/10), 9,3 dias. Abertas em 08/11: 12, com idade média de **4,4 dias** | ≤ 3 dias | (AN) | Os 16,0 dias medem a demora para registrar o fechamento, não para fazer o trabalho. A diferença de 6,7 dias entre o declarado e o registrado é o custo da falha de rastreabilidade da D06 |
| DP2 Razão saída/chegada | **12 chegadas** (#20 a #31) e **16 saídas**: razão **1,33** | ≥ 0,90 | (OK) | Pela regra, OK. Na prática, as 16 saídas são o registro de trabalho declarado no ciclo 2: nenhuma entrega nova do ciclo 3 virou issue fechada. Sem as regularizações, a razão seria 0 de 12 |
| DP2 WIP | **12 issues abertas** em 08/11, **2,0 por integrante** | ≤ 2 por integrante | (OK) | No limite da D04. Metade do WIP são issues da Fase 4, que só começam em 13/11 |
| DP3 Índice de pico | 4 de 4 commits em 04/11 = **100%**. **1 dia ativo em 7** | ≤ 40% | (AN) | Repete o padrão dos ciclos 0 e 1: todo o trabalho do ciclo entrou em uma tarde, no mesmo intervalo de 6 minutos (14h33 a 14h39) |
| DP4 Retrabalho | 2 de 4 commits = **50%**: [`bacaa08`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/commit/bacaa08) (correções da E1) e [`3dd61ca`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/commit/3dd61ca) (gráficos do PSM corrigidos) | ≤ 20% | (AN) | Um dos retrabalhos é esperado (as correções pedidas na avaliação da E1). O outro corrige um commit de 6 minutos antes |
| Rastreabilidade | 0 de 4 commits com `Closes #N`. 1 PR aberto (#32), ligado à #25 por `Refs` | 100% dos PRs ligados a issue e revisados | (A) | Primeiro uso do fluxo de PR da D06 |

### 6.3 Gráficos

```mermaid
---
config:
  themeVariables:
    xyChart:
      plotColorPalette: "#B4531A"
      titleColor: "#7D8E95"
      xAxisLabelColor: "#7D8E95"
      xAxisTitleColor: "#7D8E95"
      xAxisLineColor: "#7D8E95"
      xAxisTickColor: "#7D8E95"
      yAxisLabelColor: "#7D8E95"
      yAxisTitleColor: "#7D8E95"
      yAxisLineColor: "#7D8E95"
      yAxisTickColor: "#7D8E95"
      backgroundColor: "transparent"
---
xychart-beta
    title "Commits por dia (26/10 a 13/11/2026)"
    x-axis "Dia" ["26/10", "27", "28", "29", "30", "31", "01/11", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13"]
    y-axis "Commits" 0 --> 5
    bar [1, 0, 2, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 1, 0, 0, 0, 1]
```

_Figura 14 - Commits por dia nos ciclos 2, 3 e 4, sem os commits de merge (9 commits). Em 19 dias, só 5 tiveram commit, e 04/11 sozinho concentra 4. O merge do PR #32, em 11/11, não aparece porque não traz conteúdo novo. Indicador DP3. Fonte: [`commits.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/blob/main/dados/gestao/commits.csv)._

## 7. Ciclo 4 (parcial): 09/11 a 13/11

### 7.1 Contexto

| Item | Registro |
|------|----------|
| Data de corte | 13/11/2026, 21h46, quando a #21 foi fechada no GitHub |
| #21 (método do G2 por inspeção) | Fechada no GitHub em 13/11, às 21h46. A conclusão foi **declarada pelo responsável como 10/11** (terça-feira); só faltava o registro de horas. A coleta usa 10/11 para CP1, CP2 e DP1, e o fechamento no GitHub aparece como data registrada |
| PR #32 | Integrado em 11/11, às 12h32, **sem nenhuma revisão registrada**, depois de 6,9 dias aberto. A descrição pedia revisão de três donos de página e o OK do Guilherme Moura para uma mudança de decisão da Fase 1 |
| Commits fora de PR | [`e642ffb`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/commit/e642ffb) (13/11) entrou direto no `main`, sem PR e sem `Closes #21` |
| Horas | Primeiro registro no `esforco.csv`, em 13/11: 4 linhas e 11 h, todas de Faehzin, sendo 3 h da #21 neste ciclo |

### 7.2 Medições

| Métrica | Valor | Limite | Situação | Interpretação |
|---------|-------|--------|:--------:|---------------|
| CP1 Comprometido x concluído | Milestone "E2 - Ponto de controle": `I_conc` = 2 (#14 e #21) de 7 = **28,6%**. Na data de corte já tinham passado **82,5%** do período: **desvio de 54,0 p.p.** Na quarta-feira, 11/11, às 21h, o desvio era de 35,9 p.p. (28,6% contra 64,5%) | ≤ 5 p.p. | (AN) | O desvio cresceu de 24,7 para 54,0 p.p. em cinco dias. Faltando 2 dias para o vencimento, 5 das 7 issues estão abertas. Sem contar a #14, que é da E1, a Fase 3 tem 1 de 6 issues fechadas (16,7%) |
| CP2 SPI (hora/valor) | Milestone "E2 - Ponto de controle": `PV` = 82,5% × 14 h = **11,6 h** · `EV` = 4 h (#14 e #21) · **SPI = 0,35**. Em 11/11, às 21h, era 0,44 (`PV` = 9,0 h) | ≥ 0,90 | (AN) | Um terço do valor planejado foi entregue com 82,5% do prazo. Como toda issue da Fase 3 vale 2 h, o SPI em horas acompanha o CP1 |
| CP2 SPI por contagem (*proxy*) | Pelo [cronograma](../fase-3/cronograma.md), 5 issues deviam estar prontas até 13/11 (#20 a #23 em 12/11 e #24 em 13/11). Fechada: 1 (#21). **SPI = 1 / 5 = 0,20** | ≥ 0,90 | (AN) | Usa as datas de fim do cronograma em vez da distribuição linear da milestone. Os métodos #20, #22 e #23 têm rascunho no `main` desde 09/11, o que indica trabalho feito e não fechado |
| CP2 Variação de prazo | #20, #22 e #23: **1 dia** após o fim planejado (12/11). #24 no dia do fim planejado | - | (A) | O prazo interno da Fase 3 (14/11) ainda não venceu. O ponto de controle da disciplina é em 16/11 |
| RC1 Variação de esforço | #21 (Faehzin): `H_real` = 3 h, `H_est` = 2 h, **TVE = +50%** | -20% a +20% | (AN) | O método levou 1 h a mais que o estimado, mas a estimativa de 2 h foi feita depois da entrega. Para a equipe, o RC1 continua não mensurável: o gerente de medição não tem como obter as horas dos outros cinco integrantes (ver D12) |
| RC2 CPI | Entregas do ciclo: `EV` = 2 h (#21) · `AC` = 3 h = **R$150** · **CPI = 0,67** | ≥ 0,90 | (AN) | Cada hora gasta entregou 40 min de valor planejado. O CPI vale só para a #21: as horas de quem trabalhou sem fechar issue não estão no `AC`. Total registrado até a data de corte: **11 h = R$550**, todo de um integrante |
| RC3 (*proxy*: commits) | Faehzin 2 de 2 = **100%** | 13% a 20% | (AN) | O `e642ffb` soma 1.419 linhas, a maioria de modelos de fichas gerados com apoio de IA (declarado em [Uso de IA](../sobre/uso-de-ia.md)), o que distorce ainda mais o *proxy* de linhas. Por isso esta coleta não usa linhas no ciclo 4 |
| DP1 *Lead time* | #21: cerca de **6 dias** (de 04/11, 14h26, a 10/11, data declarada). No GitHub, 9,3 dias. Abertas: 11, com idade média de **9,3 dias** | ≤ 3 dias | (AN) | A #21 cobre um método inteiro; pela D04 ela deveria estar dividida em partes de até 1 dia. As abertas incluem as 6 issues da Fase 4, abertas com antecedência de propósito (D10), que pesam na idade sem estarem atrasadas |
| DP2 Razão saída/chegada | **0 chegadas** e **1 saída** (#21): razão indefinida | ≥ 0,90 | (A) | O backlog já estava aberto desde 04/11, então zero chegadas é esperado. O problema é a saída: 1 issue em 5 dias |
| DP2 WIP | **11 abertas**, **1,8 por integrante** (Faehzin 1; os outros cinco com 2) | ≤ 2 por integrante | (OK) | Dentro do limite |
| DP3 Índice de pico | 1 de 2 commits no dia de maior atividade = **50%**. 2 dias ativos em 5 (09 e 13/11) | ≤ 40% | (A) | Melhor que os ciclos anteriores, mas com só dois commits o índice tem pouca informação |
| DP4 Retrabalho | Por commit: 0 de 2 = **0%**. O `e642ffb` mistura correções do método (50 linhas incluídas e 38 removidas) e conteúdo novo (fichas e página da Fase 4) e foi classificado como novo pelo que predomina. Por PR: 1 PR integrado (#32), 0 pedidos de ajuste, **0 revisões** | ≤ 20% | (OK) | O DP4 por PR dá 0%, mas só porque ninguém revisou. Um PR sem revisão não tem como receber pedido de ajuste, então esse 0% não indica qualidade |
| Rastreabilidade | 0 de 2 commits com `Closes #N`. 1 PR integrado sem revisão. A #21 foi fechada à mão, 3 dias depois da conclusão declarada | 100% | (AN) | O fluxo de PR da D06 foi usado uma vez, mas sem a etapa que dá sentido a ele: a revisão |

### 7.3 Gráficos

```mermaid
---
config:
  themeVariables:
    xyChart:
      plotColorPalette: "#8C9BA1, #B4531A"
      titleColor: "#7D8E95"
      xAxisLabelColor: "#7D8E95"
      xAxisTitleColor: "#7D8E95"
      xAxisLineColor: "#7D8E95"
      xAxisTickColor: "#7D8E95"
      yAxisLabelColor: "#7D8E95"
      yAxisTitleColor: "#7D8E95"
      yAxisLineColor: "#7D8E95"
      yAxisTickColor: "#7D8E95"
      backgroundColor: "transparent"
---
xychart-beta
    title "Burnup da milestone E2 - Ponto de controle (issues)"
    x-axis "Dia de novembro" [04, 05, 06, 07, 08, 09, 10, 11, 12, 13]
    y-axis "Issues concluídas (acumulado)" 0 --> 7
    line [0, 0.6, 1.3, 1.9, 2.5, 3.2, 3.8, 4.5, 5.1, 5.7]
    line [1, 1, 1, 1, 1, 1, 2, 2, 2, 2]
```

_Figura 15 - Burnup da milestone "E2 - Ponto de controle (Fase 3)" até a data de corte: linha cinza = planejado (7 issues distribuídas de forma linear até o vencimento, em 15/11) e linha terracota = concluído (#14 em 04/11 e #21 em 10/11, data declarada). Indicador CP1. Fonte: API de issues do GitHub e [`linha-de-base-e2.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/blob/main/dados/gestao/linha-de-base-e2.csv)._

```mermaid
---
config:
  themeVariables:
    xyChart:
      plotColorPalette: "#0B5563, #B4531A"
      titleColor: "#7D8E95"
      xAxisLabelColor: "#7D8E95"
      xAxisTitleColor: "#7D8E95"
      xAxisLineColor: "#7D8E95"
      xAxisTickColor: "#7D8E95"
      yAxisLabelColor: "#7D8E95"
      yAxisTitleColor: "#7D8E95"
      yAxisLineColor: "#7D8E95"
      yAxisTickColor: "#7D8E95"
      backgroundColor: "transparent"
---
xychart-beta
    title "Fase 3: issues previstas x fechadas, pelo cronograma"
    x-axis "Dia de novembro" [09, 10, 11, 12, 13, 14]
    y-axis "Issues (acumulado)" 0 --> 6
    bar [0, 0, 0, 4, 5, 6]
    line [0, 1, 1, 1, 1, 1]
```

_Figura 16 - SPI por contagem das issues da Fase 3 (#20 a #25): barras = issues com fim planejado até o dia, pelo cronograma; linha = issues fechadas. Em 13/11, 5 previstas e 1 fechada (SPI = 0,20). A barra de 14/11 é o prazo interno da Fase 3. Indicador CP2 (*proxy*). Fonte: [cronograma da avaliação](../fase-3/cronograma.md) e API de issues do GitHub._

```mermaid
---
config:
  themeVariables:
    xyChart:
      plotColorPalette: "#0B5563"
      titleColor: "#7D8E95"
      xAxisLabelColor: "#7D8E95"
      xAxisTitleColor: "#7D8E95"
      xAxisLineColor: "#7D8E95"
      xAxisTickColor: "#7D8E95"
      yAxisLabelColor: "#7D8E95"
      yAxisTitleColor: "#7D8E95"
      yAxisLineColor: "#7D8E95"
      yAxisTickColor: "#7D8E95"
      backgroundColor: "transparent"
---
xychart-beta horizontal
    title "Commits por integrante - ciclos 2 a 4 (26/10 a 13/11)"
    x-axis ["Faehzin", "LucasAvelar2711", "larigs", "Guilherme-Moura", "GuilhermeMM3", "MrBolt2005"]
    y-axis "Commits" 0 --> 5
    bar [4, 2, 2, 1, 0, 0]
```

_Figura 17 - Commits por integrante desde o fim da E1, sem os de merge (9 commits): Faehzin 44,4%, LucasAvelar2711 22,2%, larigs 22,2%, Guilherme-Moura 11,1%, GuilhermeMM3 e MrBolt2005 0%. É o *proxy* do RC3 enquanto só 1 de 6 integrantes registra horas, com a mesma ressalva dos ciclos anteriores: o trabalho fora do repositório (Overleaf e rascunhos locais) não aparece. Fonte: [`commits.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/blob/main/dados/gestao/commits.csv)._

### 7.4 Leitura dos ciclos 2 a 4 e decisões disparadas

1. **O backlog voltou, a entrega não.** A D10 trouxe a E2 para o GitHub em 04/11, com milestones e duas issues por integrante, e CP1, DP1 e DP2 voltaram a ser mensuráveis. Mas, das 6 issues de método da Fase 3, só 1 fechou até 13/11. O desvio do CP1 foi a 54,0 p.p., e o SPI por contagem ficou em 0,20 a dois dias do vencimento. O SPI em horas é 0,35. Dispara a **D11**.
2. **A rajada continua.** O ciclo 3 teve 100% dos commits em uma tarde, e nos três ciclos houve 5 dias ativos em 19. O ciclo 4 parcial é o primeiro abaixo de 60% de pico, mas com só 2 commits.
3. **As horas começaram a entrar, por uma pessoa só.** O `esforco.csv` saiu do zero em 13/11 com 11 h, todas de um integrante, e a E2 ganhou estimativa (40 h) em 13/11. Com isso, RC1 e RC2 foram calculados pela primeira vez (TVE de +50% e CPI de 0,67), mas só para a #21. As horas dos outros cinco integrantes não podem ser obtidas pelo gerente de medição, então RC1 e RC2 da equipe ficam fora do alcance desta medição. Dispara a **D12**.
4. **O PR foi usado, a revisão não.** O #32 é o primeiro PR desde o #1 e foi integrado sem nenhuma revisão, apesar do pedido na descrição. O DP4 por PR dá 0%, mas esse número só mostra que não houve revisão.
5. **O fechamento continua sendo declarado.** A E1 foi registrada no GitHub 6,7 dias depois da conclusão declarada, e a #21, 3 dias depois. Enquanto o fechamento não sair do PR (`Closes #N`), CP1 e DP1 dependem de declaração.

## 8. Próxima coleta

| Ciclo | Data | O que coletar | Situação |
|-------|------|---------------|----------|
| 2 (completo) | Domingo, 01/11/2026 | Todas as métricas | **Realizada retroativamente em 13/11.** Registrada na seção 5 |
| 3 | 04/11 e 08/11/2026 | Todas as métricas, mais a verificação da D08, D09 e D10 | **Realizada retroativamente em 13/11.** Registrada na seção 6 |
| 4 (parcial) | 11/11/2026 | CP1, CP2 e DP2 | **Realizada em 13/11**, com o valor de 11/11 recalculado. Registrada na seção 7 |
| 4 (completo) | Domingo, 15/11/2026 | Todas as métricas, o fechamento da milestone "E2 - Ponto de controle" e a verificação da D11 | Pendente |
| 5 (parcial) | Quarta-feira, 18/11/2026 | CP1 e DP2 da milestone "E2 - Entrega final" e horas das issues fechadas | Pendente |

## 9. Evolução entre os ciclos

Comparação dos ciclos 0 a 4 em cada indicador, para mostrar o que melhorou, o que piorou e o que ficou igual. O ciclo 4 é parcial (até 13/11), e a comparação será refeita na coleta completa de 15/11. Os valores são os das seções 2 a 7; quando um ciclo tem dois valores (declarado e registrado, por exemplo), vale o que está no painel da seção 1.

### 9.1 Tendência por indicador

| Indicador | C0 | C1 | C2 | C3 | C4 (parcial) | Limite | Tendência |
|-----------|:--:|:--:|:--:|:--:|:------------:|:------:|-----------|
| Métricas mensuráveis (de 9) | 3 | 6 | 8 | 7 | **9** | 9 | **Melhora.** Pela primeira vez as nove métricas têm valor, graças às milestones da E2, à estimativa de horas e ao primeiro registro de horas |
| Métricas em ação necessária (AN) | 3 | 5 | 5 | 6 | 6 | 0 | **Piora e depois estabiliza.** Medir mais revelou mais problemas; de C3 para C4 o número parou de subir |
| Métricas em OK | 0 | 0 | 2 | 1 | 1 | 9 | **Constante em nível baixo** |
| CP1 desvio (p.p.) | - | 88,9 | 0,0 | 24,7 | 54,0 | ≤ 5 | **Piora dentro da E2.** O 0,0 de C2 é a saturação depois do vencimento da E1, não recuperação |
| CP2 SPI | - | 0,05 | 1,00 | 0,37 | 0,35 | ≥ 0,90 | **Constante em nível ruim.** O 1,00 de C2 é a convergência da E1 já vencida |
| RC1 TVE | - | - | - | - | +50% | ±20% | **Primeira medição**, só da #21 |
| RC2 CPI | - | - | - | - | 0,67 | ≥ 0,90 | **Primeira medição**, só da #21 |
| RC3 maior participação (*proxy*: commits) | 34,8% | 66,7% | 66,7% | 50,0% | 100% | 13% a 20% | **Piora.** O trabalho no repositório se concentra cada vez mais |
| RC3 integrantes com commit no ciclo | 5 de 6 | 2 de 6 | 2 de 6 | 2 de 6 | 1 de 6 | 6 de 6 | **Piora** |
| RC3 carga planejada dentro de 13% a 20% | - | 2 de 6 | - | 6 de 6 | 6 de 6 | 6 de 6 | **Melhora.** A E2 foi distribuída por igual |
| DP1 *lead time* das fechadas (dias) | - | 3,1 | 9,3 | 16,0 | 6,0 | ≤ 3 | **Melhora em C4**, ainda o dobro do limite |
| DP2 WIP por integrante | - | 2,7 | 0,0 | 2,0 | 1,8 | ≤ 2 | **Melhora.** Dentro do limite desde C3 |
| DP3 índice de pico | 82,6% | 100% | 66,7% | 100% | 50,0% | ≤ 40% | **Oscila.** C4 é o melhor valor, mas com só 2 commits |
| DP3 dias ativos | 4 de 14 (29%) | 1 de 7 (14%) | 2 de 7 (29%) | 1 de 7 (14%) | 2 de 5 (40%) | - | **Leve melhora em C4** |
| DP4 retrabalho (por commit) | 39,1% | 66,7% | 66,7% | 50,0% | 0,0% | ≤ 20% | **Melhora**, sobre uma base pequena de commits |
| Commits no ciclo | 23 | 3 | 3 | 4 | 2 | - | **Queda de volume** depois do ciclo 0 |
| Horas registradas com data no ciclo | 6 | 0 | 0 | 2 | 3 | - | **Começou a entrar**, de um só integrante |
| PRs integrados / revisados | 1 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | 1 / 0 | todos revisados | **Constante.** Nenhuma revisão registrada em nenhum ciclo |

### 9.2 Gráficos

```mermaid
---
config:
  themeVariables:
    xyChart:
      plotColorPalette: "#0B5563, #B4531A, #8C9BA1"
      titleColor: "#7D8E95"
      xAxisLabelColor: "#7D8E95"
      xAxisTitleColor: "#7D8E95"
      xAxisLineColor: "#7D8E95"
      xAxisTickColor: "#7D8E95"
      yAxisLabelColor: "#7D8E95"
      yAxisTitleColor: "#7D8E95"
      yAxisLineColor: "#7D8E95"
      yAxisTickColor: "#7D8E95"
      backgroundColor: "transparent"
---
xychart-beta
    title "Situação das métricas em cada ciclo"
    x-axis "Ciclo" ["C0", "C1", "C2", "C3", "C4 (parcial)"]
    y-axis "Métricas (de 9)" 0 --> 9
    line [3, 6, 8, 7, 9]
    line [3, 5, 5, 6, 6]
    line [0, 0, 2, 1, 1]
```

_Figura 18 - Linha azul = métricas mensuráveis, linha terracota = métricas em ação necessária (AN), linha cinza = métricas em OK. A distância entre a azul e a terracota é o que está medido e sob controle: ela cresceu de 0 para 3 métricas, enquanto o número de AN se estabilizou em 6. Fonte: painel da seção 1._

```mermaid
---
config:
  themeVariables:
    xyChart:
      plotColorPalette: "#B4531A, #0B5563"
      titleColor: "#7D8E95"
      xAxisLabelColor: "#7D8E95"
      xAxisTitleColor: "#7D8E95"
      xAxisLineColor: "#7D8E95"
      xAxisTickColor: "#7D8E95"
      yAxisLabelColor: "#7D8E95"
      yAxisTitleColor: "#7D8E95"
      yAxisLineColor: "#7D8E95"
      yAxisTickColor: "#7D8E95"
      backgroundColor: "transparent"
---
xychart-beta
    title "CP1 - desvio entre planejado e concluído (p.p.)"
    x-axis "Ciclo" ["C1", "C2", "C3", "C4 (parcial)"]
    y-axis "Desvio (p.p.)" 0 --> 100
    bar [88.9, 0, 24.7, 54.0]
    line [5, 5, 5, 5]
```

_Figura 19 - Barras = desvio do CP1 em pontos percentuais, linha = limite de 5 p.p. C1 e C2 se referem à milestone E1; C3 e C4, à milestone "E2 - Ponto de controle". O zero de C2 é a saturação da E1 depois do vencimento. Indicador CP1._

```mermaid
---
config:
  themeVariables:
    xyChart:
      plotColorPalette: "#0B5563, #8C9BA1"
      titleColor: "#7D8E95"
      xAxisLabelColor: "#7D8E95"
      xAxisTitleColor: "#7D8E95"
      xAxisLineColor: "#7D8E95"
      xAxisTickColor: "#7D8E95"
      yAxisLabelColor: "#7D8E95"
      yAxisTitleColor: "#7D8E95"
      yAxisLineColor: "#7D8E95"
      yAxisTickColor: "#7D8E95"
      backgroundColor: "transparent"
---
xychart-beta
    title "CP2 - SPI por ciclo"
    x-axis "Ciclo" ["C1", "C2", "C3", "C4 (parcial)"]
    y-axis "SPI" 0 --> 1.1
    bar [0.05, 1.00, 0.37, 0.35]
    line [0.9, 0.9, 0.9, 0.9]
```

_Figura 20 - Barras = SPI em horas, linha = limite de 0,90. C1 e C2 são da E1 (42 h), e C3 e C4 da "E2 - Ponto de controle" (14 h, estimadas em 13/11). Fora o 1,00 de C2, que é convergência depois do vencimento, nenhum ciclo passou de 0,40. Indicador CP2._

```mermaid
---
config:
  themeVariables:
    xyChart:
      plotColorPalette: "#B4531A, #0B5563, #8C9BA1"
      titleColor: "#7D8E95"
      xAxisLabelColor: "#7D8E95"
      xAxisTitleColor: "#7D8E95"
      xAxisLineColor: "#7D8E95"
      xAxisTickColor: "#7D8E95"
      yAxisLabelColor: "#7D8E95"
      yAxisTitleColor: "#7D8E95"
      yAxisLineColor: "#7D8E95"
      yAxisTickColor: "#7D8E95"
      backgroundColor: "transparent"
---
xychart-beta
    title "RC3 - concentração do trabalho no repositório"
    x-axis "Ciclo" ["C0", "C1", "C2", "C3", "C4 (parcial)"]
    y-axis "Participação (%)" 0 --> 100
    bar [34.8, 66.7, 66.7, 50.0, 100]
    line [20, 20, 20, 20, 20]
    line [16.7, 16.7, 16.7, 16.7, 16.7]
```

_Figura 21 - Barras = maior participação de um integrante nos commits do ciclo, linha azul = limite superior da faixa OK (20%), linha cinza = participação ideal (16,7%). A barra subiu de 34,8% para 100%, enquanto a carga planejada da E2 está entre 13,2% e 18,4% para todos: o plano está equilibrado, a execução registrada não. Indicador RC3 (*proxy*: commits)._

```mermaid
---
config:
  themeVariables:
    xyChart:
      plotColorPalette: "#0B5563, #B4531A"
      titleColor: "#7D8E95"
      xAxisLabelColor: "#7D8E95"
      xAxisTitleColor: "#7D8E95"
      xAxisLineColor: "#7D8E95"
      xAxisTickColor: "#7D8E95"
      yAxisLabelColor: "#7D8E95"
      yAxisTitleColor: "#7D8E95"
      yAxisLineColor: "#7D8E95"
      yAxisTickColor: "#7D8E95"
      backgroundColor: "transparent"
---
xychart-beta
    title "Commits e dias ativos por ciclo"
    x-axis "Ciclo" ["C0", "C1", "C2", "C3", "C4 (parcial)"]
    y-axis "Quantidade" 0 --> 25
    bar [23, 3, 3, 4, 2]
    line [4, 1, 2, 1, 2]
```

_Figura 22 - Barras = commits do ciclo (sem merge), linha = dias com pelo menos um commit. Depois do ciclo 0, o repositório recebeu de 2 a 4 commits por ciclo, em 1 ou 2 dias. O ciclo 0 tem 14 dias, os demais 7, e o ciclo 4 parcial tem 5. Indicador DP3._

```mermaid
---
config:
  themeVariables:
    xyChart:
      plotColorPalette: "#B4531A, #0B5563, #8C9BA1, #C9D3D6"
      titleColor: "#7D8E95"
      xAxisLabelColor: "#7D8E95"
      xAxisTitleColor: "#7D8E95"
      xAxisLineColor: "#7D8E95"
      xAxisTickColor: "#7D8E95"
      yAxisLabelColor: "#7D8E95"
      yAxisTitleColor: "#7D8E95"
      yAxisLineColor: "#7D8E95"
      yAxisTickColor: "#7D8E95"
      backgroundColor: "transparent"
---
xychart-beta
    title "DP3 e DP4 - pico de atividade e retrabalho (%)"
    x-axis "Ciclo" ["C0", "C1", "C2", "C3", "C4 (parcial)"]
    y-axis "Percentual" 0 --> 100
    line [82.6, 100, 66.7, 100, 50.0]
    line [39.1, 66.7, 66.7, 50.0, 0]
    line [40, 40, 40, 40, 40]
    line [20, 20, 20, 20, 20]
```

_Figura 23 - Linha terracota = índice de pico (DP3), linha azul = retrabalho por commit (DP4), linha cinza = limite do pico (40%), linha cinza-clara = limite do retrabalho (20%). As duas curvas caem em C4, mas com 2 commits no ciclo cada commit vale 50 pontos, então a queda ainda não é tendência. Indicadores DP3 e DP4._

```mermaid
---
config:
  themeVariables:
    xyChart:
      plotColorPalette: "#B4531A, #8C9BA1"
      titleColor: "#7D8E95"
      xAxisLabelColor: "#7D8E95"
      xAxisTitleColor: "#7D8E95"
      xAxisLineColor: "#7D8E95"
      xAxisTickColor: "#7D8E95"
      yAxisLabelColor: "#7D8E95"
      yAxisTitleColor: "#7D8E95"
      yAxisLineColor: "#7D8E95"
      yAxisTickColor: "#7D8E95"
      backgroundColor: "transparent"
---
xychart-beta
    title "DP1 - lead time médio das issues fechadas (dias)"
    x-axis "Ciclo" ["C1", "C2", "C3", "C4 (parcial)"]
    y-axis "Dias" 0 --> 18
    bar [3.1, 9.3, 16.0, 6.0]
    line [3, 3, 3, 3]
```

_Figura 24 - Barras = *lead time* médio das issues fechadas no ciclo, linha = limite de 3 dias. O pico de C3 (16,0 dias) é o fechamento no GitHub, em 04/11, das issues da E1 declaradas prontas em 28/10. C4 é só a #21, pela data declarada. Indicador DP1._

```mermaid
---
config:
  themeVariables:
    xyChart:
      plotColorPalette: "#0B5563, #8C9BA1"
      titleColor: "#7D8E95"
      xAxisLabelColor: "#7D8E95"
      xAxisTitleColor: "#7D8E95"
      xAxisLineColor: "#7D8E95"
      xAxisTickColor: "#7D8E95"
      yAxisLabelColor: "#7D8E95"
      yAxisTitleColor: "#7D8E95"
      yAxisLineColor: "#7D8E95"
      yAxisTickColor: "#7D8E95"
      backgroundColor: "transparent"
---
xychart-beta
    title "DP2 - trabalho em andamento por integrante"
    x-axis "Ciclo" ["C1", "C2", "C3", "C4 (parcial)"]
    y-axis "Issues abertas por integrante" 0 --> 3
    bar [2.7, 0, 2.0, 1.8]
    line [2, 2, 2, 2]
```

_Figura 25 - Barras = issues abertas por integrante na data de corte, linha = limite de 2 da D04. C2 é zero porque o backlog da E1 esvaziou e o da E2 ainda não existia; a partir de C3 o WIP fica no limite ou abaixo dele. Indicador DP2._

### 9.3 Síntese

- **Melhorou:** a capacidade de medir (9 de 9 métricas com valor em C4, contra 3 em C0), o WIP (dentro do limite desde C3), a distribuição planejada (6 de 6 integrantes na faixa) e, com a ressalva de poucos commits, o pico e o retrabalho em C4.
- **Piorou:** o cumprimento de prazo dentro da E2 (desvio do CP1 de 24,7 para 54,0 p.p.) e a concentração do trabalho registrado (de 5 para 1 integrante com commit no ciclo).
- **Ficou igual:** o SPI abaixo de 0,40 em todo ciclo que não está saturado, nenhuma revisão de PR em nenhum ciclo e as horas vindas de um único integrante.

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 05/10/2026 | Criação da estrutura do documento | Gabriel Fae | - |
| 0.2 | 16/10/2026 | Reorganização da documentação por fases do processo de avaliação | Gabriel Fae | - |
| 0.3 | 25/10/2026 | Registro dos ciclos 0 (retroativo) e 1, painel de indicadores, gráficos e síntese | Gabriel Fae | - |
| 0.4 | 28/10/2026 | Coleta parcial do ciclo 2 (CP1, CP2, DP2 e horas retroativas), correção retroativa de DP3 e DP4 do ciclo 1, preenchimento de DP1 e DP2 do ciclo 1 e situação da coleta completa de 01/11 | Gabriel Fae | - |
| 0.5 | 28/10/2026 | Cinco gráficos de esforço, entrega e custo: volume por integrante no ciclo 0, horas planejadas x entregues e horas por categoria no ciclo 1, custo da E1 em reais e simulação de pagamento por integrante no ciclo 2 | Gabriel Fae | - |
| 0.6 | 13/11/2026 | Fechamento retroativo do ciclo 2, ciclo 3 medido retroativamente e coleta parcial do ciclo 4 a partir do `git log` e da API do GitHub, com painel estendido e três gráficos novos | Gabriel Fae | - |
| 0.7 | 13/11/2026 | Linha de base de horas da E2 (40 h) aplicada a CP2, RC1 e RC2 dos ciclos 3 e 4, e seção 9 com a evolução entre os ciclos: tabela de tendências e oito gráficos | Gabriel Fae | - |
