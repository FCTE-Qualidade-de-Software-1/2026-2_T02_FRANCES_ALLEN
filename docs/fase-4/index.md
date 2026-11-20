# Fase 4 - Executar e concluir a avaliação

Quarta e última fase do processo de avaliação de produto da família **SQuaRE** (ISO/IEC 25040:2024). Os métodos da [Fase 3](../fase-3/index.md) são executados, as medidas são obtidas, as questões do GQM da [Fase 2](../fase-2/index.md) são respondidas e a qualidade do VICKY é julgada contra os níveis e critérios definidos antes da coleta. A fase fecha com as conclusões e com uma ação de melhoria medida antes e depois.

!!! warning "Fase em execução"
    Coleta de 14 a 20/11/2026 e entrega final em 22/11/2026, conforme o [cronograma](../fase-3/cronograma.md). Cada página abaixo indica o estado da sua coleta. Esta página só mostra valor que já está em arquivo do repositório; o que ainda não foi calculado aparece como **[PENDENTE]**.

## Conteúdo desta fase

| Página | Conteúdo | Responsável | Issue | Estado em 20/11/2026 |
|--------|----------|-------------|:-----:|----------------------|
| [Resultados do G1](resultados-g1.md) (adequação funcional) | Triagens T1 a T4, julgamento de A1 e A2, kappa, M1.1.1 a M1.5.2 e respostas de Q1.1 a Q1.5 | Larissa Gomes | #26 | Triagens e fichas de A1 e A2 no repositório; kappa e cálculo em andamento |
| [Resultados do G2 por inspeção](resultados-g2-inspecao.md) | M2.1.1 a M2.4.2 e M2.7.1, concordância entre avaliadores e respostas das questões | Gabriel Fae | #27 | Fichas de A2 no repositório (PR #34); fichas de A1 e consolidação (etapa 7) pendentes |
| Resultados do G2 com usuários | Formulário de estética, sessões remotas, teste com teclado e axe DevTools: M2.5.1, M2.6.1, M2.6.2 e M2.7.2 | João Felipe Oliveira | #28 | Coleta replanejada pela [D13](../gestao/decisoes.md#d13-adaptar-a-coleta-com-usuarios-ao-prazo-da-entrega-2), sessões de 19 a 21/11 |
| [Resultados do G3](resultados-g3.md) (manutenibilidade) e ação de melhoria | M3.1.1 a M3.3.1 na linha de base de 14/11, repetição por A2, julgamento do G3 e candidata de melhoria | Guilherme Moura | #29 | Linha de base, repetição e julgamento concluídos (PR #35); ação de melhoria e medida depois pendentes |
| Julgamento e conclusões | Julgamento por característica, relação entre as características, ligação com o propósito da Fase 1 e sugestões ao requisitante | Guilherme Maciel | #30 | A iniciar; depende do G1 e do G2 |

## Como os resultados viram julgamento

O caminho de cada número até a conclusão segue as regras da Fase 2, sem mudança de fórmula, limiar ou agregação ([níveis e julgamento](../fase-2/niveis-e-julgamento.md)):

1. **Medida.** Cada métrica é coletada pelo seu método, e o dado bruto fica em `dados/avaliacao/` com a data da coleta e a versão do VICKY.
2. **Nível.** O valor medido é comparado com os níveis da métrica e recebe de 0 a 3 pontos.
3. **Questão.** A pontuação de uma questão é a média dos pontos das suas métricas, classificada em Insatisfatório, Aceitável, Bom ou Excelente. Métrica crítica no nível Insatisfatório limita a questão, como M1.1.1 e M1.3.1 no G1.
4. **Hipótese.** Cada questão confronta o valor obtido com a hipótese escrita antes da coleta, que é confirmada ou refutada.
5. **Objetivo e produto.** As questões de cada objetivo compõem a nota do objetivo, que vira o julgamento do VICKY em cada característica (atende, atende parcialmente ou não atende): adequação funcional (G1), capacidade de interação (G2) e manutenibilidade (G3). As regras de cada objetivo estão nas seções 2 a 4 de [níveis e julgamento](../fase-2/niveis-e-julgamento.md).

## Síntese dos resultados

| Objetivo | Métricas medidas | Perfil das questões | Pontuação do objetivo | Nível | Julgamento do VICKY | Fonte |
|----------|:----------------:|---------------------|:---------------------:|:-----:|---------------------|-------|
| G1 - Adequação funcional | [PENDENTE: kappa e cálculo do G1] | [PENDENTE: kappa e cálculo do G1] | [PENDENTE: kappa e cálculo do G1] | [PENDENTE] | [PENDENTE] | [Resultados do G1](resultados-g1.md) |
| G2 - Capacidade de interação | [PENDENTE: consolidação da inspeção e coleta com usuários] | [PENDENTE] | [PENDENTE] | [PENDENTE] | [PENDENTE] | [Resultados do G2 por inspeção](resultados-g2-inspecao.md) |
| G3 - Manutenibilidade | 6 de 6 | Q3.1 Bom (2,00) · Q3.2 Aceitável (1,00) · Q3.3 Aceitável (1,00) | 1,33 | Aceitável | **Atende parcialmente** | [Resultados do G3](resultados-g3.md) |

_Tabela 1 - Síntese do julgamento por objetivo. Fonte: elaborada pela equipe a partir das páginas de resultados de cada objetivo._

### G1 - Adequação funcional

!!! warning "[PENDENTE: kappa e cálculo do G1]"
    A coleta do G1 (#26) fecha em 20/11/2026 com as conferências, o kappa de Cohen de cada tema e o cálculo por `dados/avaliacao/G1/calcular_g1.py`. Nenhum valor desta seção é estimado.

| Métrica | Medida | Valor | Nível | Pontos |
|---------|--------|:-----:|:-----:|:------:|
| M1.1.1 (crítica) | Recall@30 normalizado (T1 a T4) | [PENDENTE] | [PENDENTE] | [PENDENTE] |
| M1.1.2 | Recall restrito às fontes (T1 a T4) | [PENDENTE] | [PENDENTE] | [PENDENTE] |
| M1.2.1 | Funções declaradas operantes (F01 a F09) | [PENDENTE] | [PENDENTE] | [PENDENTE] |
| M1.3.1 (crítica) | Precisão@30 (T1 a T4) | [PENDENTE] | [PENDENTE] | [PENDENTE] |
| M1.3.2 | Metadados e links corretos | [PENDENTE] | [PENDENTE] | [PENDENTE] |
| M1.4.1 | Spearman entre Quality Score e rubrica (T1 e T2) | [PENDENTE] | [PENDENTE] | [PENDENTE] |
| M1.5.1 | Conformidade com filtros (E1 e E2) | [PENDENTE] | [PENDENTE] | [PENDENTE] |
| M1.5.2 | Estabilidade entre execuções (T1 e T3) | [PENDENTE] | [PENDENTE] | [PENDENTE] |

| Tema | Kappa de Cohen (mínimo 0,61) |
|------|:----------------------------:|
| T1 a T4 | [PENDENTE: kappa e cálculo do G1] |

| Questão | Métricas | Pontuação | Nível |
|---------|----------|:---------:|:-----:|
| Q1.1 | M1.1.1 e M1.1.2 | [PENDENTE] | [PENDENTE] |
| Q1.2 | M1.2.1 | [PENDENTE] | [PENDENTE] |
| Q1.3 | M1.3.1 e M1.3.2 | [PENDENTE] | [PENDENTE] |
| Q1.4 | M1.4.1 | [PENDENTE] | [PENDENTE] |
| Q1.5 | M1.5.1 e M1.5.2 | [PENDENTE] | [PENDENTE] |

**Julgamento do G1:** [PENDENTE: kappa e cálculo do G1]. O objetivo é a média das cinco questões e não passa de Bom se alguma ficar em Insatisfatório ([níveis e julgamento, seção 2](../fase-2/niveis-e-julgamento.md#2-regras-do-g1-adequacao-funcional)).

### G2 - Capacidade de interação

!!! warning "[PENDENTE: fichas de A1 e consolidação da inspeção; coleta com usuários]"
    Em 20/11/2026, as fichas de A2 das oito métricas da inspeção estão no repositório, com capturas de 19/11 (PR #34, `dados/avaliacao/G2/M2.*/A2.md`). As fichas de A1 ainda não foram publicadas, e o `consolidado.md` de cada métrica está em branco. Pelo método, o valor de cada métrica sai só do consolidado (etapa 7, `dados/avaliacao/G2/calcular_g2_inspecao.py`), por isso nenhum valor do G2 aparece aqui. As métricas com usuários (M2.5.1, M2.6.1, M2.6.2 e M2.7.2) seguem a D13.

| Questão | Como o nível é obtido | Nível |
|---------|-----------------------|:-----:|
| Q2.1 | Nível de M2.1.1 | [PENDENTE] |
| Q2.2 | Nível de M2.2.1, um nível abaixo se M2.2.2 for Insatisfatório | [PENDENTE] |
| Q2.3 | Menor nível entre M2.3.1 e M2.3.2 | [PENDENTE] |
| Q2.4 | Nível de M2.4.1, um nível abaixo se M2.4.2 for Insatisfatório; Insatisfatório se ação paga estiver desprotegida | [PENDENTE] |
| Q2.5 | Nível de M2.5.1 (formulário de estética, D13); relatada, fora da contagem do julgamento | [PENDENTE] |
| Q2.6 | Nível de M2.6.1, com M2.6.2 (contraste) como complementar | [PENDENTE] |
| Q2.7 | Nível de M2.7.2, um nível abaixo se M2.7.1 for Insatisfatório | [PENDENTE] |

**Julgamento do G2:** [PENDENTE], pelas regras da [seção 3 de níveis e julgamento](../fase-2/niveis-e-julgamento.md#3-regras-do-g2-capacidade-de-interacao).

### G3 - Manutenibilidade

Coleta de A1 em 14/11/2026 e repetição independente de A2 em 18/11/2026 no commit `c2ae570` do VICKY, com os mesmos valores de A, B e nível nas seis métricas. Valores de `dados/avaliacao/G3/resultados.csv`; pontos, questões e julgamento da [página de resultados do G3](resultados-g3.md).

| Métrica | A | B | Valor | Nível | Pontos |
|---------|:-:|:-:|:-----:|:-----:|:------:|
| M3.1.1 Acoplamento de componentes | 78 | 38 | 2,05 | Excelente | 3 |
| M3.1.2 Adequação da complexidade ciclomática | 11 | 47 | 76,6% | Aceitável | 1 |
| M3.2.1 Conformidade de estilo PEP 8 | 2 | 38 | 5,3% | Insatisfatório | 0 |
| M3.2.2 Densidade de código duplicado | 28 | 18.927 | 0,15% | Excelente | 3 |
| M3.2.3 Completude de logs do sistema | 0 | 33 | 0,0% | Insatisfatório | 0 |
| M3.3.1 Completude de testes automatizados | 4.750 | 7.519 | 63,17% | Aceitável | 1 |

_Tabela 2 - Medidas do G3 na linha de base (commit `c2ae570`). Fonte: `dados/avaliacao/G3/resultados.csv`._

| Questão | Cálculo | Pontuação | Nível |
|---------|---------|:---------:|:-----:|
| Q3.1 Modularidade | (3 + 1) / 2 | 2,00 | Bom |
| Q3.2 Analisabilidade | (0 + 3 + 0) / 3 | 1,00 | Aceitável |
| Q3.3 Testabilidade | 1 / 1 | 1,00 | Aceitável |
| **G3** | (2,00 + 1,00 + 1,00) / 3 | **1,33** | **Aceitável** |

_Tabela 3 - Da métrica ao objetivo no G3. Fonte: [resultados do G3](resultados-g3.md), seção 5._

**Julgamento do G3:** a manutenibilidade do VICKY **atende parcialmente**. As regras bloqueadoras não foram acionadas: M3.1.2 ficou em Aceitável e Q3.3 em Aceitável. Das hipóteses, H3.1 e H3.2 foram parcialmente confirmadas e H3.3 foi refutada (cobertura de 63,17%, abaixo dos 70% previstos).

O principal achado é a concentração da dívida técnica em `src/vicky/pipeline.py`: `run_full_pipeline` com complexidade ciclomática 84, nenhuma das 33 funções críticas com `logging` e 24% de cobertura no arquivo, que responde por 905 das 2.769 linhas não cobertas (`dados/avaliacao/G3/M3.1.2/radon-cc.txt`, `M3.2.3/funcoes.csv` e `M3.3.1/pytest-cov.txt`). É o alvo da ação de melhoria.

## Ação de melhoria

| Campo | Situação em 20/11/2026 |
|-------|------------------------|
| Alvo | `run_full_pipeline` em `src/vicky/pipeline.py`, com `logging` no lugar de `print` ([candidata do G3](resultados-g3.md#7-sugestao-de-acao-de-melhoria-candidata-do-g3)) |
| Métricas de verificação | M3.1.2, M3.2.3 e M3.3.1, pelo mesmo método do G3 com outro commit (`COMMIT=<hash> coletar.sh`) |
| Antes | M3.1.2 = 76,6%; M3.2.3 = 0,0%; M3.3.1 = 63,17% (`dados/avaliacao/G3/resultados.csv`) |
| Depois | [PENDENTE: commit da melhoria e coleta depois (#29)] |

## Questões a responder

| Objetivo | Questões | Onde a resposta fica |
|----------|----------|----------------------|
| G1 - Adequação funcional | Q1.1 a Q1.5 | [Resultados do G1](resultados-g1.md) |
| G2 - Capacidade de interação | Q2.1 a Q2.7 | [Resultados do G2 por inspeção](resultados-g2-inspecao.md) e com usuários |
| G3 - Manutenibilidade | Q3.1 a Q3.3 | [Resultados do G3](resultados-g3.md) |

## Desvios do método

Toda diferença entre o que a Fase 3 previu e o que foi executado é registrada aqui, com o motivo e o efeito na medida.

| Data | Método | Desvio | Motivo | Efeito na medida |
|------|--------|--------|--------|------------------|
| 19/11/2026 | G2 com usuários | M2.5.1 passa a formulário online assíncrono com cinco respondentes; M2.7.2 passa a sessões remotas com três participantes válidos e regra da maioria ([D13](../gestao/decisoes.md#d13-adaptar-a-coleta-com-usuarios-ao-prazo-da-entrega-2)) | 0 de 5 sessões presenciais realizadas até 18/11, por indisponibilidade dos estudantes recrutados | M2.7.2 apresentada como indicativa (n = 3); ameaças à validade declaradas nos resultados |
| 17/11/2026 | G1 | Evidências da coleta guardadas como texto do DOM, sem captura de imagem | `screencapture` indisponível por SSH | [PENDENTE: confirmação da condutora do G1 e efeito na conferência de M1.2.1] |
| 19/11/2026 | G1 | Casamento de título na consulta às fontes de M1.1.2 por similaridade de 0,85 ou mais, limiar que o método não fixava | Relatos sem PMID e títulos em português | [PENDENTE: confirmação da condutora do G1] |
| 14 e 18/11/2026 | G3 | Nenhum | - | - |

_Os dois desvios do G1 vêm da página de resultados do G1 em construção (branch `larissa/g1-dia1`) e ficam a confirmar até o fechamento da #26._

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 16/10/2026 | Criação da página | Gabriel Fae | - |
| 0.2 | 18/11/2026 | Estrutura da Fase 4: páginas de resultados por objetivo, caminho da medida ao julgamento, questões a responder e registro de desvios | Lucas Avelar | - |
| 0.3 | 20/11/2026 | Síntese dos resultados: G3 completo, G1 e G2 com marcadores de pendência, ação de melhoria e desvios registrados até 20/11 | Lucas Avelar | - |
