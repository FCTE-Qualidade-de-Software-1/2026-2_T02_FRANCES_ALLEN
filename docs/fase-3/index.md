# Fase 3 - Projetar a avaliação

Terceira fase do processo de avaliação de produto da família **SQuaRE** (ISO/IEC 25040:2024). Os objetivos, as métricas e os critérios de julgamento definidos na [Fase 2](../fase-2/index.md) recebem aqui o **plano de execução**: o método de coleta de cada métrica, as instruções para o avaliador, os recursos e o ambiente necessários e o cronograma da avaliação.

## Conteúdo desta fase

| Página | Conteúdo | Responsável | Issue |
|--------|----------|-------------|:-----:|
| [Método do G1](metodo-g1.md) | Justificativa, temas de teste e revisões de referência, passo a passo de coleta de M1.1.1 a M1.5.2, fichas dos avaliadores, script de cálculo e regra de discordância | Lucas Avelar, pela D12 (revisão: Larissa Gomes) | #20 |
| [Método do G2 por inspeção](metodo-g2-inspecao.md) | Roteiro de inspeção das telas e do código para M2.1.1 a M2.4.2 e M2.7.1 | Gabriel Fae | #21 |
| [Método do G2 com usuários](metodo-g2-usuarios.md) | Sessões com estudantes, teste com teclado, axe DevTools, recrutamento, gravação e anonimização para M2.5.1, M2.6.1, M2.6.2 e M2.7.2 | Lucas Avelar, pela D12, com João Felipe Oliveira (revisão: João Felipe Oliveira) | #22 |
| [Instrumentos do G2 com usuários](instrumentos-g2-usuarios.md) | Cartões de tarefa, ficha de uso, questionário de compreensão com gabarito, questionário de estética e bloco qualitativo | Lucas Avelar, pela D12, com João Felipe Oliveira (revisão: João Felipe Oliveira) | #22 |
| [Termo de consentimento](termo-de-consentimento.md) | Termo lido e assinado antes de cada sessão com participante | Lucas Avelar, pela D12 (revisão: João Felipe Oliveira) | #22 |
| [Método do G3](metodo-g3.md) | Ferramentas, versões, comando e regra de contagem de M3.1.1 a M3.3.1, cálculo por script e coleta de 14/11/2026 | Lucas Avelar, pela D12 (revisão: Guilherme Moura) | #23 |
| [Recursos, ambiente e consistência](recursos-e-ambiente.md) | Hardware, software, contas, créditos, massa de dados, conhecimento exigido, tabela de consistência entre a Fase 2 e a Fase 3 e decisões pendentes | Lucas Avelar, pela D12 (revisão: Guilherme Maciel) | #24 |
| [Cronograma da avaliação](cronograma.md) | Atividades da Fase 3 e da Fase 4, responsáveis, datas, dependências e riscos | Lucas Avelar | #25 |

Pela [D12](../gestao/decisoes.md), trabalho não entregue no prazo passa a outro integrante, e a professora é comunicada de cada redistribuição. As páginas assumidas dessa forma são revisadas pelo dono original antes do ponto de controle de 16/11.

## O que cada método precisa trazer

Para que outra pessoa da equipe consiga repetir a coleta sem ajuda, cada página de método segue a mesma estrutura:

1. **Métricas cobertas**, com o código da Fase 2.
2. **Por que este método**: a justificativa da forma de coleta escolhida e a coerência com as métricas, os níveis e o julgamento da Fase 2.
3. **Preparação**: o que precisa existir antes da coleta (conta, créditos, tema, versão do código, ferramenta instalada).
4. **Passo a passo** da coleta, na ordem em que o avaliador executa.
5. **Registro**: o que o avaliador anota em cada passo e em qual pasta de `dados/avaliacao/` o dado bruto fica.
6. **Cálculo**: como o dado bruto vira o valor da métrica, apontando para a ficha da [especificação das métricas](../fase-2/especificacao-das-metricas.md).
7. **Discordância e repetição**: o que fazer quando dois avaliadores discordam ou quando uma coleta precisa ser refeita.

## Cobertura das métricas

As 26 métricas da Fase 2 estão distribuídas nos quatro métodos. A ligação de cada uma com recurso, ambiente, níveis e julgamento está na [tabela de consistência](recursos-e-ambiente.md#5-tabela-de-consistencia-entre-a-fase-2-e-a-fase-3).

| Método | Métricas | Forma de coleta | Depende de |
|--------|:--------:|-----------------|------------|
| [G1](metodo-g1.md) | 8 | Triagens em quatro temas e julgamento de dois avaliadores | Créditos e revisões de referência |
| [G2 por inspeção](metodo-g2-inspecao.md) | 8 | Inspeção de telas e código por dois avaliadores | Conta de cortesia e triagem do G1 |
| [G2 com usuários](metodo-g2-usuarios.md) | 4 | Sessões com cinco estudantes, teste com teclado e axe DevTools | Recrutamento, termo e projeto triado |
| [G3](metodo-g3.md) | 6 | Análise estática e cobertura de testes | Acesso ao fork e commit definido |

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 16/10/2026 | Criação da página | Gabriel Fae | - |
| 0.2 | 04/11/2026 | Estrutura da Fase 3: páginas por método, responsáveis e estrutura comum dos métodos | Lucas Avelar | - |
| 0.3 | 09/11/2026 | Cobertura das 26 métricas nos quatro métodos | Gabriel Fae | - |
| 0.4 | 14/11/2026 | Páginas de instrumentos e termo de consentimento no conteúdo, "Por que este método" na estrutura comum e responsáveis atualizados pela D12 | Lucas Avelar | - |
