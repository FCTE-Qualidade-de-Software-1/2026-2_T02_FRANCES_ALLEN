# Fase 4 - Executar e concluir a avaliação

Quarta e última fase do processo de avaliação de produto da família **SQuaRE** (ISO/IEC 25040:2024). Os métodos da [Fase 3](../fase-3/index.md) são executados, as medidas são obtidas, as questões do GQM da [Fase 2](../fase-2/index.md) são respondidas e a qualidade do VICKY é julgada contra os níveis e critérios definidos antes da coleta. A fase fecha com as conclusões e com uma ação de melhoria proposta e sua medida de verificação; executada e medida antes e depois. 

!!! note "Fase concluída na Entrega 2"
    Coleta de 14 a 20/11/2026 e entrega final em 22/11/2026, conforme o [cronograma](../fase-3/cronograma.md). Esta página só mostra valor que está em arquivo do repositório. O que não foi medido até a entrega está declarado como desvio: M2.6.1 e M2.6.2 (Q2.6 sem nível).

## Conteúdo desta fase

| Página | Conteúdo | Responsável | Issue | Estado em 22/11/2026 |
|--------|----------|-------------|:-----:|----------------------|
| [Resultados do G1](resultados-g1.md) (adequação funcional) | Triagens T1 a T4, julgamento de A1 e A2, kappa, M1.1.1 a M1.5.2 e respostas de Q1.1 a Q1.5 | Larissa Gomes | #26 | Concluído (PR #36): oito métricas, kappa de T1 a T4 e respostas de Q1.1 a Q1.5 |
| [Resultados do G2 por inspeção](resultados-g2-inspecao.md) | M2.1.1 a M2.4.2 e M2.7.1, concordância entre avaliadores e respostas das questões | Gabriel Fae | #27 | Concluído (PRs #34 e #37): consolidação de A1 e A2, oito métricas e respostas de Q2.1 a Q2.4 e parte da Q2.7 |
| [Resultados do G2 com usuários](resultados-g2-usuarios.md) | Formulário de estética, sessões remotas, teste com teclado e axe DevTools: M2.5.1, M2.6.1, M2.6.2 e M2.7.2 | João Felipe Oliveira e Gabriel Fae | #28 | Sessões em 19 e 20/11/2026 (P01 a P03) e formulário com três respostas (D14); M2.7.2 e M2.5.1 calculadas; M2.6.1 e M2.6.2 não coletadas |
| [Resultados do G3](resultados-g3.md) (manutenibilidade) e ação de melhoria | M3.1.1 a M3.3.1 na linha de base de 14/11, repetição por A2, julgamento do G3 e candidata de melhoria | Guilherme Moura | #29 | Linha de base, repetição e julgamento concluídos (PR #35); ação de melhoria e medida depois pendentes |
| [Julgamento e conclusões](julgamento-e-conclusoes.md) | Julgamento por característica, relação entre as características, ligação com o propósito da Fase 1 e sugestões ao requisitante | Guilherme Maciel | #30 | Consolidado com G1, G2 e G3 (PRs #38, #40 e #41) |

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
| G1 - Adequação funcional | 8 de 8 | Q1.1 Insatisfatório (0,00) · Q1.2 Aceitável (1,00) · Q1.3 Aceitável (1,50) · Q1.4 Insatisfatório (0,00) · Q1.5 Insatisfatório (0,50) | 0,60 | Insatisfatório | **Não atende** | [Resultados do G1](resultados-g1.md) |
| G2 - Capacidade de interação | 8 de 8 por inspeção; 2 de 4 com usuários (M2.6.1 e M2.6.2 não coletadas) | Q2.1 Bom · Q2.2 Aceitável · Q2.3 Insatisfatório · Q2.4 Insatisfatório · Q2.5 Aceitável (indicativo) · Q2.6 sem nível · Q2.7 Bom (indicativo) | - | - | **Não atende** | [Resultados do G2 por inspeção](resultados-g2-inspecao.md) e [com usuários](resultados-g2-usuarios.md) |
| G3 - Manutenibilidade | 6 de 6 | Q3.1 Bom (2,00) · Q3.2 Aceitável (1,00) · Q3.3 Aceitável (1,00) | 1,33 | Aceitável | **Atende parcialmente** | [Resultados do G3](resultados-g3.md) |

_Tabela 1 - Síntese do julgamento por objetivo. Fonte: elaborada pela equipe a partir das páginas de resultados de cada objetivo._

### G1 - Adequação funcional

Coleta de 17 a 20/11/2026 nos temas T1 a T4, com repetição de T1 e T3 e as execuções de filtro E1 e E2. Valores, kappa e respostas da [página de resultados do G1](resultados-g1.md), seções 2 a 5.

| Métrica | Medida | Valor | Nível | Pontos |
|---------|--------|:-----:|:-----:|:------:|
| M1.1.1 (crítica) | Recall@30 normalizado (T1 a T4) | 0,195 | Insatisfatório | 0 |
| M1.1.2 | Recall restrito às fontes (T1 a T4) | 0,195 | Insatisfatório | 0 |
| M1.2.1 | Funções declaradas operantes (F01 a F09) | 72,2% | Aceitável | 1 |
| M1.3.1 (crítica) | Precisão@30 (T1 a T4) | 24,7% | Insatisfatório | 0 |
| M1.3.2 | Metadados e links corretos | 100% (40 de 40) | Excelente | 3 |
| M1.4.1 | Spearman entre Quality Score e rubrica (T1 e T2) | 0,034 | Insatisfatório | 0 |
| M1.5.1 | Conformidade com filtros (E1 e E2) | 3,3% (base: E1) | Insatisfatório | 0 |
| M1.5.2 | Estabilidade entre execuções (T1 e T3) | 0,586 | Aceitável | 1 |

| Tema | Kappa de Cohen (mínimo 0,61) |
|------|:----------------------------:|
| T1 a T4 | 1,000; 0,918; 0,905; 1,000 (todos acima do mínimo, nenhum item decidido por A3) |

| Questão | Métricas | Pontuação | Nível |
|---------|----------|:---------:|:-----:|
| Q1.1 | M1.1.1 e M1.1.2 | 0,00 | Insatisfatório |
| Q1.2 | M1.2.1 | 1,00 | Aceitável |
| Q1.3 | M1.3.1 e M1.3.2 | 1,50 | Aceitável |
| Q1.4 | M1.4.1 | 0,00 | Insatisfatório |
| Q1.5 | M1.5.1 e M1.5.2 | 0,50 | Insatisfatório |

**Julgamento do G1:** a adequação funcional do VICKY **não atende** (0,60, Insatisfatório). Os pontos fortes são os metadados (M1.3.2, 100%) e a operação da maior parte do fluxo (M1.2.1); recall, precisão, correlação do ranking com a rubrica e conformidade com filtros ficaram em Insatisfatório. O objetivo é a média das cinco questões e não passa de Bom se alguma ficar em Insatisfatório ([níveis e julgamento, seção 2](../fase-2/niveis-e-julgamento.md#2-regras-do-g1-adequacao-funcional)).

### G2 - Capacidade de interação

!!! note "Inspeção e coleta com usuários"
    A inspeção foi consolidada em 20/11/2026 por A1 e ratificada por A2 (concordância de 42,9% a 100% por métrica, nenhum item decidido por A3); os níveis de Q2.1 a Q2.4 vêm da [página do G2 por inspeção](resultados-g2-inspecao.md), seção 5. As sessões com usuários foram feitas em 19 e 20/11/2026 (P01 a P03), e o formulário de estética teve três respostas, calculadas pela D14 com maioria de 2 de 3; os níveis de Q2.5 e Q2.7 vêm da [página do G2 com usuários](resultados-g2-usuarios.md) e são indicativos (n = 3). M2.6.1 e M2.6.2 não foram coletadas até a entrega, e a Q2.6 fica sem nível.

| Questão | Como o nível é obtido | Nível |
|---------|-----------------------|:-----:|
| Q2.1 | Nível de M2.1.1 | Bom |
| Q2.2 | Nível de M2.2.1, um nível abaixo se M2.2.2 for Insatisfatório | Aceitável |
| Q2.3 | Menor nível entre M2.3.1 e M2.3.2 | Insatisfatório |
| Q2.4 | Nível de M2.4.1, um nível abaixo se M2.4.2 for Insatisfatório; Insatisfatório se ação paga estiver desprotegida | Insatisfatório |
| Q2.5 | Nível de M2.5.1 (formulário de estética, D13); relatada, fora da contagem do julgamento | Aceitável (40,0%, indicativo) |
| Q2.6 | Nível de M2.6.1, com M2.6.2 (contraste) como complementar | Sem nível (M2.6.1 e M2.6.2 não coletadas) |
| Q2.7 | Nível de M2.7.2, um nível abaixo se M2.7.1 for Insatisfatório | Bom (M2.7.2 = 10/12, 83,3%, indicativo); M2.7.1 = Bom (3 de 4), não rebaixa |

**Julgamento do G2:** a capacidade de interação do VICKY **não atende**. Q2.3 e Q2.4 ficaram em Insatisfatório, e duas ou mais questões principais em Insatisfatório levam a "Não atende" qualquer que fosse o nível da Q2.6; detalhe em [julgamento e conclusões](julgamento-e-conclusoes.md). Regras pelas regras da [seção 3 de níveis e julgamento](../fase-2/niveis-e-julgamento.md#3-regras-do-g2-capacidade-de-interacao).

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

| Campo | Situação em 22/11/2026 |
|-------|------------------------|
| Alvo | `run_full_pipeline` em `src/vicky/pipeline.py`, com `logging` no lugar de `print` ([candidata do G3](resultados-g3.md#7-sugestao-de-acao-de-melhoria-candidata-do-g3)) |
| Métricas de verificação | M3.1.2, M3.2.3 e M3.3.1, pelo mesmo método do G3 com outro commit (`COMMIT=<hash> coletar.sh`) |
| Antes | M3.1.2 = 76,6%; M3.2.3 = 0,0%; M3.3.1 = 63,17% (`dados/avaliacao/G3/resultados.csv`) |
| Depois | Executada no PR #1 do fork da Vicky (commit `7e9ccd8`, suíte offline com 1.067 testes aprovados): M3.1.2 = 85,5% (Bom); M3.2.3 = 100,0% (Excelente); M3.3.1 = 65,22% (Aceitável). Dados em [`dados/avaliacao/G3-depois/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G3-depois) |

## Questões a responder

| Objetivo | Questões | Onde a resposta fica |
|----------|----------|----------------------|
| G1 - Adequação funcional | Q1.1 a Q1.5 | [Resultados do G1](resultados-g1.md) |
| G2 - Capacidade de interação | Q2.1 a Q2.7 | [Resultados do G2 por inspeção](resultados-g2-inspecao.md) e [com usuários](resultados-g2-usuarios.md) |
| Julgamento final | G1, G2 e G3 | [Julgamento e conclusões](julgamento-e-conclusoes.md) |
| G3 - Manutenibilidade | Q3.1 a Q3.3 | [Resultados do G3](resultados-g3.md) |

## Desvios do método

Toda diferença entre o que a Fase 3 previu e o que foi executado é registrada aqui, com o motivo e o efeito na medida.

| Data | Método | Desvio | Motivo | Efeito na medida |
|------|--------|--------|--------|------------------|
| 19/11/2026 | G2 com usuários | M2.5.1 passa a formulário online assíncrono, planejado com cinco respondentes; M2.7.2 passa a sessões remotas com três participantes válidos e regra da maioria ([D13](../gestao/decisoes.md#d13-adaptar-a-coleta-com-usuarios-ao-prazo-da-entrega-2)) | 0 de 5 sessões presenciais realizadas até 18/11, por indisponibilidade dos estudantes recrutados | M2.7.2 apresentada como indicativa (n = 3); ameaças à validade declaradas nos resultados |
| 19/11/2026 | G2 com usuários | Ajustes antes da P01: tema do cartão A trocado para "O uso de células-tronco para restauração de tecido", conta da equipe com créditos no lugar de conta nova e nenhuma sessão piloto ([método, seção 2.9](../fase-3/metodo-g2-usuarios.md#29-ajustes-feitos-antes-da-primeira-sessao)) | Preparo das sessões remotas no prazo | Nenhum nos 12 elementos de M2.7.2; a criação de conta (F01) saiu da sessão |
| 22/11/2026 | G2 com usuários | M2.5.1 calculada com três respostas, e não cinco, com maioria de 2 de 3 ([D14](../gestao/decisoes.md#d14-calcular-m251-com-as-tres-respostas-obtidas)) | Só três respostas ao formulário até a entrega | Resultado indicativo; respondentes já tinham usado o produto na sessão |
| 22/11/2026 | G2 com usuários | M2.6.1 e M2.6.2 não coletadas | Coleta não concluída até a entrega | Q2.6 sem nível; o julgamento do G2 não muda (Q2.3 e Q2.4 em Insatisfatório) |
| 23/11/2026 | Ação de melhoria | Medida depois feita em 23/11, um dia depois do prazo original, com o prazo prorrogado pela professora | Prazo da Entrega 2 | Nenhum: mesmo método e mesmos scripts do G3, em pasta separada da linha de base |
| 18 e 20/11/2026 | G1 | E1 e E2 sem filtro de tipo de estudo no formulário; a restrição foi escrita no objetivo | O formulário não tem campo de tipo de estudo | M1.5.1 mede o cumprimento da restrição pelo objetivo; com a E2 sem lista, a base é só a E1 (30 itens) |
| 20/11/2026 | G1 | Amostra de M1.3.2 conferida por código contra o registro oficial do PubMed, sem abrir a página do DOI | Conferência reprodutível dos 40 itens | Metadados e links conferidos por título, autores, ano, periódico e requisição HTTP ao link |
| 19/11/2026 | G1 | Casamento de título na consulta às fontes de M1.1.2 por similaridade de 0,85 ou mais, limiar que o método não fixava | Relatos sem PMID e títulos em português | Tratado como refinamento de M1.1.2; o valor de similaridade fica em cada linha |
| 14 e 18/11/2026 | G3 | Nenhum | - | - |

_Os desvios do G1 vêm da página de resultados do G1; o registro completo está nas seções 1 e 3 dela._

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 16/10/2026 | Criação da página | Gabriel Fae | - |
| 0.2 | 18/11/2026 | Estrutura da Fase 4: páginas de resultados por objetivo, caminho da medida ao julgamento, questões a responder e registro de desvios | Lucas Avelar | - |
| 0.3 | 20/11/2026 | Síntese dos resultados: G3 completo, G1 e G2 com marcadores de pendência, ação de melhoria e desvios registrados até 20/11 | Lucas Avelar | - |
| 0.4 | 22/11/2026 | G1 completo e G2 por inspeção (Q2.1 a Q2.4) na síntese; estado das páginas atualizado | Lucas Avelar | - |
| 0.5 | 22/11/2026 | G2 com usuários (Q2.5 e Q2.7 indicativos, Q2.6 sem nível) e julgamento do G2 na síntese; links para resultados com usuários e julgamento; desvios do G2 com usuários e da ação de melhoria; revisão da Larissa | Lucas Avelar | Larissa Gomes |
