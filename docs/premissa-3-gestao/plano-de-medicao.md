# Plano de medição da gestão

**Ciclo de medição:** _semanal (sugestão: toda segunda-feira)_ · **Responsável:** _gerente do projeto_

## 1. Calendário e Progresso

| ID | Indicador | Fórmula | Fonte | Limite de alerta |
|----|-----------|---------|-------|------------------|
| CP1 | Progresso da milestone | issues fechadas / issues totais da milestone x 100 | GitHub Milestones | abaixo do previsto pelo burnup em mais de 15 p.p. |
| CP2 | Desvio de prazo | data real - data planejada (dias) | Milestones / cronograma | maior que 0 em marco de entrega |
| CP3 | Burnup de issues | issues concluídas acumuladas x tempo | GitHub Projects (Insights) | curva real abaixo da planejada |

## 2. Recursos e Custos

| ID | Indicador | Fórmula | Fonte | Limite de alerta |
|----|-----------|---------|-------|------------------|
| RC1 | Esforço realizado x planejado | horas reais / horas planejadas | Campo "Horas" no Project ou planilha `dados/gestao/esforco.csv` | fora de 0,8 a 1,2 |
| RC2 | Distribuição de esforço | horas do membro / horas totais x 100 | idem | membro com menos de _10%_ ou mais de _30%_ |
| RC3 | Presença em reuniões | reuniões com presença / reuniões realizadas | [Atas](../atas/index.md) | abaixo de 75% |

## 3. Desempenho dos Processos

| ID | Indicador | Fórmula | Fonte | Limite de alerta |
|----|-----------|---------|-------|------------------|
| DP1 | Lead time de issue | média(data de fechamento - data de abertura) | GitHub Issues | maior que _5 dias_ |
| DP2 | Tempo de revisão de PR | média(data do merge - data de abertura do PR) | GitHub Pull Requests | maior que _2 dias_ |
| DP3 | Taxa de retrabalho | PRs com pedido de alteração / PRs totais | GitHub Pull Requests | acima de _40%_ |
| DP4 | Issues sem responsável | issues abertas sem assignee | GitHub Issues | maior que 0 no início do ciclo |

_Os limites são valores iniciais e podem ser recalibrados; toda recalibração deve ser registrada em [Decisões de gestão](decisoes.md)._

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 05/10/2026 | Criação da estrutura do documento | Gabriel Fae | - |
