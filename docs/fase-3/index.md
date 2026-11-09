# Fase 3 - Projetar a avaliação

Terceira fase do processo de avaliação de produto da família **SQuaRE** (ISO/IEC 25040:2024). Os objetivos, as métricas e os critérios de julgamento definidos na [Fase 2](../fase-2/index.md) recebem aqui o **plano de execução**: o método de coleta de cada métrica, as instruções para o avaliador, os recursos e o ambiente necessários e o cronograma da avaliação.

## Conteúdo desta fase

| Página | Conteúdo | Responsável | Issue |
|--------|----------|-------------|:-----:|
| [Método do G1](metodo-g1.md) | Passo a passo de coleta de M1.1.1 a M1.5.2, temas de teste, fichas dos avaliadores e regra de discordância | Larissa Gomes | #20 |
| [Método do G2 por inspeção](metodo-g2-inspecao.md) | Roteiro de inspeção das telas e do código para M2.1.1 a M2.4.2 e M2.7.1 | Gabriel Fae | #21 |
| [Método do G2 com usuários](metodo-g2-usuarios.md) | Testes de cenário, questionário de estética, teste com teclado, axe DevTools, consentimento e anonimização | João Felipe Oliveira | #22 |
| [Método do G3](metodo-g3.md) | Ferramentas, versões e comando de cada métrica de M3.1.1 a M3.3.1 | Guilherme Moura | #23 |
| [Recursos, ambiente e consistência](recursos-e-ambiente.md) | Hardware, software, contas, créditos, massa de dados e tabela de consistência entre a Fase 2 e a Fase 3 | Guilherme Maciel | #24 |
| [Cronograma da avaliação](cronograma.md) | Atividades da Fase 3 e da Fase 4, responsáveis, datas e dependências | Lucas Avelar | #25 |

## O que cada método precisa trazer

Para que outra pessoa da equipe consiga repetir a coleta sem ajuda, cada página de método segue a mesma estrutura:

1. **Métricas cobertas**, com o código da Fase 2.
2. **Preparação**: o que precisa existir antes da coleta (conta, créditos, tema, versão do código, ferramenta instalada).
3. **Passo a passo** da coleta, na ordem em que o avaliador executa.
4. **Registro**: o que o avaliador anota em cada passo e em qual pasta de `dados/avaliacao/` o dado bruto fica.
5. **Cálculo**: como o dado bruto vira o valor da métrica, apontando para a ficha da [especificação das métricas](../fase-2/especificacao-das-metricas.md).
6. **Discordância e repetição**: o que fazer quando dois avaliadores discordam ou quando uma coleta precisa ser refeita.

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
