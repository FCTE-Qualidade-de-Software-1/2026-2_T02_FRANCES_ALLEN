# Decisões de gestão

Cada decisão cita a medição que a motivou, o que fecha o ciclo exigido pela Premissa 3: **medição → interpretação → decisão**. O efeito de cada decisão é verificado na coleta do ciclo seguinte, na coluna "Resultado".

## 1. Resumo

| ID | Data | Medição que motivou | Decisão | Status |
|----|------|---------------------|---------|--------|
| D01 | 19/10/2026 | DP3 = 82,6% · CP1 sem backlog (ciclo 0) | Estruturar o backlog da E1 em issues com responsável e milestone | Executada |
| D02 | 18/10/2026 | DP4 = 42,1% em 18/10 (ciclo 0) | Revisão estrutural do material das Fases 1 e 2 | Executada |
| D03 | 25/10/2026 | CP1 = 11,1% · CP2 SPI = 0,05 · artigo com 0 de 9 issues (ciclo 1) | Recalcular o prazo de entrega do artigo e priorizar o caminho crítico | Em execução |
| D04 | 25/10/2026 | DP3 = 82,6% (ciclo 0) · DP2 = 0,11 (ciclo 1) | Readaptar o processo de desenvolvimento e pesquisa: ciclos semanais com ponto de controle e limite de WIP | Em execução |
| D05 | 25/10/2026 | RC1 e RC2 não mensuráveis nos ciclos 0 e 1 | Tornar obrigatório o registro de horas e validar a linha de base de 42 h | Em execução |
| D06 | 25/10/2026 | 0 de 23 commits ligados a issue · 1 PR sem revisão · autor `user` | Adotar o fluxo branch → PR → revisão por par com `Closes #N` e corrigir a identidade do git | Em execução |
| D07 | 25/10/2026 | RC3 da carga planejada de 7,1% a 28,6% (ciclo 1) | Rebalancear a distribuição das issues da E2 | Proposta |

## 2. Detalhamento

### D01 - Estruturar o backlog da E1

| Item | Registro |
|------|----------|
| Medição | Ciclo 0: 82,6% dos commits em um único dia (DP3) e nenhuma issue ou milestone, o que tornava CP1 e CP2 não mensuráveis |
| Interpretação | Sem trabalho comprometido e rastreável, a equipe não tinha como saber o que faltava para a E1 nem distribuir a carga antes do prazo |
| Decisão | Criar a milestone E1 (vencimento em 26/10) e 18 issues, cada uma com responsável e rótulo de categoria (artigo, fase-1, fase-2, gitpage, gestão, entrega) |
| Responsável | @LucasAvelar2711 (criação da milestone e das issues em 19/10) |
| Resultado no ciclo seguinte | **Parcial.** O backlog passou a existir e permitiu medir CP1, CP2, DP1 e DP2 no ciclo 1. Mas a vazão foi de 0,11 (2 de 18 issues fechadas): o backlog foi criado, mas não andou. Isso motivou a D04 |

### D02 - Revisão estrutural do material

| Item | Registro |
|------|----------|
| Medição | 8 dos 19 commits de 18/10 foram retrabalho (DP4 = 42,1%) |
| Interpretação | A produção acelerada gerou inconsistências entre páginas: faixas de pontuação com buracos, G2 desalinhado das sete subcaracterísticas de C2 e a troca de modificabilidade por testabilidade em C3 sem propagação para o modelo de qualidade |
| Decisão | Revisar a estrutura de todo o material das Fases 1 e 2 antes da entrega, com o seguinte checklist: histórico de versão atualizado, legenda e fonte em figuras e tabelas, links internos válidos, termos iguais entre páginas (ISO/IEC 25010:2023) e decisões refletidas em todas as páginas afetadas |
| Evidência | Commits `ef7af41` (faixas de nível sem buracos), `8c048e1` (G2 realinhado), `9558d49` (C3), `4f3d9f3` e `99f5e70` (redação) |
| Responsável | Autores de cada página, com revisão cruzada |
| Resultado no ciclo seguinte | _A verificar no ciclo 2 pelo DP4 medido em PRs. Ainda há inconsistência entre testabilidade e modificabilidade em C3 nas Fases 1 e 2_ |

### D03 - Recalcular esforço pro artigo

| Item | Registro |
|------|----------|
| Medição | Ciclo 1: CP1 = 11,1% com desvio de 88,9 p.p., SPI = 0,05 e nenhuma das 9 issues do artigo fechada (24 h das 42 h planejadas) |
| Interpretação | Mantido o ritmo do ciclo 1, o artigo não fica pronto no prazo da E1. |
| Decisão | Recalcular o cronograma do artigo a partir das horas restantes: 24 h de valor planejado ainda não entregue no artigo. Ordem de prioridade: template (#2) → seções de conteúdo (#3 a #7) → referencial e metodologia (#8) → referências (#19) → tabela de contribuição (#10). |
| Responsável | Grupo como um todo. |
| Resultado no ciclo seguinte | _A verificar no ciclo 2: SPI das issues do artigo ≥ 0,90 em relação ao novo cronograma_ |

### D04 - Readaptar o processo de desenvolvimento e pesquisa

| Item | Registro |
|------|----------|
| Medição | Ciclo 0: 82,6% do trabalho em um dia (DP3), com 4 dias ativos em 14. Ciclo 1: razão saída/chegada de 0,11 (DP2) e WIP de 2,7 issues por integrante |
| Interpretação | O processo funcionou em "rajada": nada é feito por vários dias e tudo é feito na véspera. Isso causou o retrabalho do ciclo 0 e o atraso do ciclo 1. É o padrão que o CID chama de fluxo imprevisível (ICM, linha 30) |
| Decisão | Adotar o método descrito na [Seção 3 da página de gestão](index.md#3-como-a-equipe-e-gerida): ciclos semanais de domingo a domingo, ponto de controle na quarta-feira com entrega parcial obrigatória (pelo menos um PR por integrante), limite de 2 issues em andamento por pessoa e issues divididas em partes de até 1 dia de trabalho |
| Responsável | Toda a equipe. A coleta fica com o gerente (Gabriel Fae) de medição do ciclo |
| Resultado no ciclo seguinte | _A verificar no ciclo 2: DP3 ≤ 40% e razão saída/chegada ≥ 0,90_ |

### D05 - Registro obrigatório de horas

| Item | Registro |
|------|----------|
| Medição | RC1 e RC2 não mensuráveis nos dois ciclos: só um integrante declarou horas (5 h, sem data por atividade) |
| Interpretação | Sem horas reais não há custo (AC), CPI nem tabela de contribuição confiável. O *proxy* de commits penaliza quem trabalha no Overleaf |
| Decisão | (1) Cada integrante registra em `esforco.csv` as horas retroativas dos ciclos 0 e 1 até o ponto de controle de 28/10. (2) A partir do ciclo 2, o registro é feito ao fechar cada issue. (3) A linha de base de 42 h é revisada e aprovada no planejamento do ciclo 2 |
| Responsável | Cada integrante. A consolidação fica com o gerente de medição |
| Resultado no ciclo seguinte | _A verificar em 28/10: 6 de 6 integrantes com horas registradas_ |

### D06 - Rastreabilidade do trabalho no repositório

| Item | Registro |
|------|----------|
| Medição | 0 de 23 commits citam uma issue. Houve 1 PR, aprovado em 1h05 sem revisão registrada. 4 commits têm o autor genérico `user` |
| Interpretação | O trabalho existe, mas não é atribuível nem verificável. Isso derruba a qualidade dos dados de todas as métricas e explica parte da distância entre o conteúdo produzido e o SPI |
| Decisão | Toda mudança passa a seguir o fluxo branch → PR com `Closes #N` → revisão por outro integrante → merge. A `main` fica protegida. Cada integrante configura `git config user.name` e `user.email` com a conta do GitHub |
| Responsável | Toda a equipe. A proteção da `main` fica com quem administra o repositório |
| Resultado no ciclo seguinte | _A verificar no ciclo 2: 100% dos PRs ligados a issue e com revisão registrada_ |

### D07 - Rebalancear a distribuição das issues

| Item | Registro |
|------|----------|
| Medição | Carga planejada da E1 por integrante entre 7,1% (3 h) e 28,6% (12 h) (RC3) |
| Interpretação | A distribuição planejada já nasce fora da faixa de 13% a 20%. Sem correção, a tabela de contribuição final tende a ficar desequilibrada |
| Decisão | No planejamento da E2, distribuir as issues para que cada integrante fique entre 13% e 20% das horas estimadas, usando o RC3 do ciclo 2 (horas reais) como ajuste |
| Responsável | Lucas Avelar |
| Resultado no ciclo seguinte | _A verificar no planejamento da E2_ |

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 05/10/2026 | Criação da estrutura do documento | Gabriel Fae | - |
| 0.2 | 16/10/2026 | Reorganização da documentação por fases do processo de avaliação | Gabriel Fae | - |
| 0.3 | 25/10/2026 | Registro das decisões D01 a D07 a partir das medições dos ciclos 0 e 1 | Gabriel Fae | - |
