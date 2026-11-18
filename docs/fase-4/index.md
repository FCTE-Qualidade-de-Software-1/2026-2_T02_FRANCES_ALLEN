# Fase 4 - Executar e concluir a avaliação

Quarta e última fase do processo de avaliação de produto da família **SQuaRE** (ISO/IEC 25040:2024). Os métodos da [Fase 3](../fase-3/index.md) são executados, as medidas são obtidas, as questões do GQM da [Fase 2](../fase-2/index.md) são respondidas e a qualidade do VICKY é julgada contra os níveis e critérios definidos antes da coleta. A fase fecha com as conclusões e com uma ação de melhoria medida antes e depois.

!!! warning "Fase em execução"
    Coleta de 14 a 20/11/2026 e entrega final em 22/11/2026, conforme o [cronograma](../fase-3/cronograma.md). Cada página abaixo indica o estado da sua coleta.

## Conteúdo desta fase

| Página | Conteúdo | Responsável | Issue | Estado |
|--------|----------|-------------|:-----:|--------|
| Resultados do G1 (adequação funcional) | Triagens T1 a T4, julgamento de A1 e A2, kappa, M1.1.1 a M1.5.2 e respostas de Q1.1 a Q1.5 | Larissa Gomes | #26 | Coleta em andamento |
| [Resultados do G2 por inspeção](resultados-g2-inspecao.md) | M2.1.1 a M2.4.2 e M2.7.1, concordância entre avaliadores e respostas das questões | Gabriel Fae | #27 | Coleta em andamento |
| Resultados do G2 com usuários | Sessões com estudantes, teste com teclado e axe DevTools: M2.5.1, M2.6.1, M2.6.2 e M2.7.2 | João Felipe Oliveira | #28 | Coleta em andamento |
| Resultados do G3 e ação de melhoria | M3.1.1 a M3.3.1 na linha de base de 14/11, refatoração de `run_full_pipeline` e medida depois da melhoria | Guilherme Moura | #29 | Linha de base coletada |
| Julgamento e conclusões | Pontuação de cada questão, julgamento por característica, conclusão sobre o VICKY e limitações | Guilherme Maciel | #30 | A iniciar |

## Como os resultados viram julgamento

O caminho de cada número até a conclusão segue as regras da Fase 2, sem mudança de fórmula, limiar ou agregação ([níveis e julgamento](../fase-2/niveis-e-julgamento.md)):

1. **Medida.** Cada métrica é coletada pelo seu método, e o dado bruto fica em `dados/avaliacao/` com a data da coleta e a versão do VICKY.
2. **Nível.** O valor medido é comparado com os níveis da métrica e recebe de 0 a 3 pontos.
3. **Questão.** A pontuação de uma questão é a média dos pontos das suas métricas, classificada em Insatisfatório, Aceitável, Bom ou Excelente. Métrica crítica no nível Insatisfatório limita a questão, como M1.1.1 e M1.3.1 no G1.
4. **Hipótese.** Cada questão confronta o valor obtido com a hipótese escrita antes da coleta, que é confirmada ou refutada.
5. **Objetivo e produto.** As questões de cada objetivo compõem a nota do objetivo, que vira o julgamento do VICKY em cada característica (atende, atende parcialmente ou não atende): adequação funcional (G1), capacidade de interação (G2) e manutenibilidade (G3). As regras de cada objetivo estão nas seções 2 a 4 de [níveis e julgamento](../fase-2/niveis-e-julgamento.md).

## Questões a responder

| Objetivo | Questões | Onde a resposta fica |
|----------|----------|----------------------|
| G1 - Adequação funcional | Q1.1 a Q1.5 | Resultados do G1 |
| G2 - Capacidade de interação | Q2.1 a Q2.7 | Resultados do G2 por inspeção e com usuários |
| G3 - Manutenibilidade | Q3.1 a Q3.3 | Resultados do G3 |

## Desvios do método

Toda diferença entre o que a Fase 3 previu e o que foi executado é registrada aqui, com o motivo e o efeito na medida.

| Data | Método | Desvio | Motivo | Efeito na medida |
|------|--------|--------|--------|------------------|
| - | - | Nenhum registrado até 18/11/2026 | - | - |

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 16/10/2026 | Criação da página | Gabriel Fae | - |
| 0.2 | 18/11/2026 | Estrutura da Fase 4: páginas de resultados por objetivo, caminho da medida ao julgamento, questões a responder e registro de desvios | Lucas Avelar | - |
