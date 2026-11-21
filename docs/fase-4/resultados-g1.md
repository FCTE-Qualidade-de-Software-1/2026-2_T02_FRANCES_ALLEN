# Resultados do G1 (adequação funcional)

A coleta do G1 terminou em 20/11/2026. Os valores desta página saem do `calcular_g1.py`, rodado sobre os dados da coleta, e nenhum deles é estimado.

Esta página reúne o resultado das oito métricas do G1, conforme o [Método do G1](../fase-3/metodo-g1.md). Os níveis seguem a tabela de [níveis de pontuação](../fase-2/niveis-e-julgamento.md), fixada antes da coleta.

## Como ler esta página

As siglas desta página são as do [Método do G1](../fase-3/metodo-g1.md) e das [hipóteses da Fase 2](../fase-2/objetivos-questoes-hipoteses.md). As tabelas abaixo trazem o que cada uma quer dizer, e o resto da página usa só o código.

**Métricas**

| Sigla | O que mede |
|-------|------------|
| M1.1.1 | Recall do Top 30 contra a revisão de referência |
| M1.1.2 | Recall descontadas as fontes que não indexam o estudo |
| M1.2.1 | Funções do fluxo que operam |
| M1.3.1 | Precisão: itens do Top 30 relevantes para o PICO |
| M1.3.2 | Metadados e links corretos |
| M1.4.1 | Correlação entre Quality Score e rubrica metodológica |
| M1.5.1 | Conformidade com os filtros |
| M1.5.2 | Estabilidade entre duas execuções, por Jaccard |

**Hipóteses (formuladas antes da coleta)**

| Sigla | O que a equipe esperava |
|-------|-------------------------|
| H1.1 | Recall do Top 30 de 40% a 60%, com ganho de 10 pontos ou mais descontadas as fontes |
| H1.2 | No máximo 1 das 9 funções parcial ou ausente |
| H1.3 | 70% a 85% dos itens relevantes e 90% ou mais com metadados e link corretos |
| H1.4 | Correlação de 0,50 ou mais entre Quality Score e rubrica |
| H1.5 | Filtros cumpridos em 93% ou mais e Jaccard de 0,70 ou mais entre duas execuções |

**Questões**

| Sigla | Pergunta |
|-------|----------|
| Q1.1 | A lista contém os estudos que uma revisão de referência incluiria |
| Q1.2 | Que partes do fluxo o estudante consegue executar |
| Q1.3 | Os artigos respondem ao PICO e vêm bem descritos |
| Q1.4 | A ordem do ranking acompanha um critério de qualidade metodológica |
| Q1.5 | O resultado obedece à configuração e se mantém ao repetir |

**Temas e execuções**

| Sigla | O que é |
|-------|---------|
| T1 | Colchicina na prevenção secundária de eventos cardiovasculares |
| T2 | Ioga para fadiga em pessoas com câncer |
| T3 | Prevalência de diabetes mellitus gestacional no Brasil |
| T4 | Tratamento farmacológico da ataxia de Friedreich |
| T1-B e T3-B | Repetição de T1 e de T3, com a mesma entrada, para medir a estabilidade |
| E1 | Teste de filtros sobre o tema da colchicina: só PubMed, 5 anos, ensaios randomizados |
| E2 | Teste de filtros sobre o tema do diabetes gestacional: só SciELO, 5 anos, estudos observacionais |

**Funções do VICKY avaliadas na M1.2.1**

| Sigla | Função |
|-------|--------|
| F01 | Cadastro e login |
| F02 | Criação de projeto |
| F03 | Geração do PICO |
| F04 | Seleção de bases e quantidade |
| F05 | Triagem completa |
| F06 | Lista por Quality Score |
| F07 | Favoritos |
| F08 | Log auditável |
| F09 | Exportação |

## 1. Execução da coleta

| Campo | Valor |
|-------|-------|
| Período | 17/11/2026 a 20/11/2026 |
| Produto | VICKY em produção, <https://vicky.synaptha.com/> |
| Versão de referência | Termos de Uso de 29/09/2026, acessados em 17/11/2026 |
| Navegador | Google Chrome 157.0.8103.79; área visível e zoom não registrados |
| Condutor (C) | Larissa Gomes Silva |
| Avaliadores | A1 Gabriel Fae, A2 Lucas Avelar; A3 João Felipe Oliveira só nos desempates |
| Triagens feitas | T1 e T2 (17/11); T3 e E1 (18/11); T4 e T1-B (19/11); T3-B (20/11); E2 (segunda tentativa em 20/11, sem lista; ver seção 3) |
| Créditos | 10 antes de T1; 5 depois de T4; 4 depois de T1-B; 3 depois de T3-B; 2 depois da primeira tentativa de E2; 1 depois da segunda tentativa |
| Itens não coletados | F01 passo de recuperação de senha, que depende de e-mail do atendimento (limitação); E2 (SciELO sem retorno, tratada como achado, não como falha de execução) |
| Desvios do método | E2 sem filtro de tipo de estudo no formulário (a restrição foi para o objetivo); amostra de M1.3.2 conferida por código contra o registro oficial do PubMed, sem abrir a página do DOI |

As telas dos subpassos da M1.2.1 estão em `dados/avaliacao/G1/M1.2.1/evidencias/` como capturas PNG (Chrome 1366x768, zoom 100%), nomeadas `AAAAMMDD_Fnn_<subpasso>.png`. Os textos das telas do dia 1 também ficam nessa pasta.

## 2. Valores medidos

| Métrica | Medida | Valor | Nível | Dados brutos |
|---------|--------|:-----:|:-----:|--------------|
| M1.1.1 | Recall@30 normalizado (T1 a T4) | 0,195 (T1 0,250; T2 0,143; T3 0,100; T4 0,286) | Insatisfatório | [M1.1.1/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G1/M1.1.1) |
| M1.1.2 | Recall restrito às fontes (T1 a T4) | 0,195 (igual ao de M1.1.1: todo estudo de referência achado já estava no PubMed) | Insatisfatório | [M1.1.2/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G1/M1.1.2) |
| M1.2.1 | Funções declaradas operantes (F01 a F09) | 72,2% (4 operantes, 5 parciais) | Aceitável | [M1.2.1/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G1/M1.2.1) |
| M1.3.1 | Precisão@30 (T1 a T4) | 24,7% | Insatisfatório | [M1.3.1/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G1/M1.3.1) |
| M1.3.2 | Metadados e links corretos | 100% (40 de 40) | Excelente | [M1.3.2/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G1/M1.3.2) |
| M1.4.1 | Spearman entre Quality Score e rubrica (T1 e T2) | 0,034 (T1 -0,120; T2 0,187) | Insatisfatório | [M1.4.1/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G1/M1.4.1) |
| M1.5.1 | Conformidade com filtros (E1 e E2) | 3,3% (1 de 30 itens; base: uma execução, E1; E2 sem lista, ver seção 3) | Insatisfatório | [M1.5.1/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G1/M1.5.1) |
| M1.5.2 | Estabilidade entre execuções (T1 e T3) | 0,586 (T1 0,579; T3 0,593) | Aceitável | [M1.5.2/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G1/M1.5.2) |

### Concordância entre os avaliadores (M1.3.1)

O kappa de Cohen mínimo é 0,61. Abaixo disso, o tema passa por um rejulgamento independente e, persistindo, sai da média.


| Tema | Itens avaliados | Itens iguais | Kappa | Decididos por A3 |
|------|:---------------:|:------------:|:-----:|:----------------:|
| T1 | 30 | 30 | 1,000 | 0 |
| T2 | 30 | 29 | 0,918 | 0 (T2-30 decidido em consenso entre A1 e A2) |
| T3 | 25 | 24 | 0,905 | 0 (T3-23 decidido em consenso entre A1 e A2) |
| T4 | 30 | 30 | 1,000 | 0 |

Os quatro temas passam do mínimo de 0,61, então nenhum precisa de segunda rodada de julgamento. Só dois itens divergiram (T2-30 e T3-23), e os dois foram decididos em consenso entre A1 e A2, que releram título e resumo e aplicaram a tabela de critérios da seção 4.4. Não foi necessário um terceiro avaliador (A3): pelo método, ele só decide o item quando A1 e A2 não chegam a acordo, e os dois itens fecharam por consenso. O kappa é calculado sobre os julgamentos independentes, antes do consenso, e por isso não muda.

## 3. Principais achados

### Dia 1 (T1 e T2)

Em T1 foram 528 artigos, todos do PubMed, com 144 incluídos. SciELO e Google Acadêmico retornaram 0, e as strings tiveram 24 erros de Google Acadêmico. O Top 30 inclui a própria revisão Cochrane de referência, na posição 14, e é majoritariamente meta-análise. Só 3 dos 12 estudos da referência aparecem no Top.

Em T2 foram 517 artigos analisados, todos do PubMed, com 96 incluídos. As strings PubMed do endpoint vieram fragmentadas: as posições 0 a 2 estavam quebradas e as demais terminavam em `AND (` sem o intervalo de datas. SciELO e Google Acadêmico, de novo, retornaram 0.

A lista `decision=include` difere da ordem do Top nos empates, e o Top real é `include_top`.

### Dia 2 (T3 e E1)

#### T3

Em T3 (prevalência de diabetes gestacional no Brasil, com SciELO e Google Acadêmico marcados) só o PubMed retornou resultado. SciELO e Google Acadêmico retornaram 0, e as strings iniciais tiveram 12 erros de Google Acadêmico. Foram 1500 artigos analisados (422 não analisados) e 25 incluídos, então o Top veio com 25 itens, menos de 30. Houve 5 rotações de termos. A janela foi de 20 anos, e o relato mais antigo da referência é de 2010. A lista de referência tem 32 estudos (Tabela 1 de Mocellin). Pelo método, uma lista com menos de 30 itens vale como está, e as métricas usam os n itens.

#### E1

Em E1 (só PubMed, 5 anos, ensaios randomizados escritos no objetivo) foram 550 artigos analisados, todos do PubMed, e 102 incluídos. O Top 30 ficou com 72 incluídos abaixo do corte. Pelo Publication Type do PubMed, só 1 dos 30 é ensaio randomizado, e os outros 29 são meta-análises ou revisões. Ano e fonte estão conformes nos 30, então a conformidade desta execução é 1 de 30. As strings geradas trazem blocos de Google Acadêmico e SciELO mesmo com só o PubMed marcado, mas a lista só mostra PubMed. O formulário não tem campo de tipo de estudo, então a restrição ficou no objetivo.

#### Google Acadêmico na consulta às fontes (M1.1.2)

Essa conferência é feita à parte da busca do VICKY: buscamos o título de cada relato direto nas fontes. Na consulta de T3, conferimos os 32 relatos da referência também no Google Acadêmico, e todos apareceram. No SciELO, a busca por Nehab 2019 devolveu outro artigo, então contou como não encontrado. Quatro relatos (Santos 2012, Ayach 2010, Oliveira 2015 e Alves 2014) contaram como encontrados no SciELO, pelo mesmo artigo com título em português.

#### Execução e créditos do dia 2

Em 18/11 (dia 2) executamos T3 e E1. Tínhamos 8 créditos antes de T3 e sobraram 6 depois de E1.

### Dia 3 (T4)

Em 19/11 (dia 3) executamos T4 (tratamento farmacológico da ataxia de Friedreich, com PubMed, SciELO e Google Acadêmico marcados e janela de 20 anos, porque o relato mais antigo da referência é de 2003 e nenhuma janela menor o cobre). Foram 557 artigos analisados e 106 incluídos, e o Top 30 veio todo do PubMed, com 76 incluídos abaixo do corte. SciELO e Google Acadêmico retornaram 0, e as strings tiveram 53 erros de Google Acadêmico. A lista de referência tem 8 estudos e 23 relatos, dos quais 14 relatos (7 estudos) estavam publicados até a coleta. Dois estudos da referência aparecem no Top 30 (Lynch 2021 e Pandolfo 2022), o que dá R = 0,286. Tínhamos 6 créditos antes de T4 e sobraram 5. T1-B estava prevista para 19/11 e T3-B e E2 para 20/11.

#### Consulta às fontes de T4 (M1.1.2)

Buscamos o título de cada um dos 14 relatos publicados no PubMed, no SciELO e no Google Acadêmico. O Google Acadêmico trouxe os 14, e o SciELO nenhum. Dois relatos são resumos em anais sem PMID (Lynch 2021, relatos 6 e 7), e a busca por título no PubMed não os achou. Casamos o título por similaridade de 0,85 ou mais e guardamos o valor em cada linha; o método não fixava esse limiar, então tratamos como um refinamento de M1.1.2.

#### T1-B (repetição de T1, dia 3)

Em 19/11 (dia 3) executamos T1-B, a repetição de T1: a mesma entrada (projeto #81), feita 48 h depois do fim de T1 e com a mesma configuração (revisão sistemática, janela de 20 anos, PubMed, SciELO e Google Acadêmico marcados, Top 30). O PubMed recuperou 584 artigos, contra 636 em T1. SciELO e Google Acadêmico retornaram 0 nas duas, e as strings de Google Acadêmico tiveram 12 erros, contra 24 em T1. Foram 500 artigos analisados (528 em T1) e 144 incluídos, o mesmo número das duas execuções. O Top 30 veio completo nas duas, e a maturidade ficou moderada nas duas. O texto do PICO e o das strings mudaram de uma execução para a outra, mas a estrutura é a mesma. Pelo PMID, 22 dos 30 estudos do Top aparecem em T1 e em T1-B (73%), e a união dos dois Tops tem 38 estudos. Tínhamos 5 créditos antes de T1-B e sobraram 4. Ainda não há julgamento de relevância dos itens, então esta página só registra a sobreposição e não a interpreta. T3-B e E2 estão previstas para 20/11.

### Formulário, exportação e cadastro

| Ponto | O que observamos |
|-------|------------------|
| Tipo de estudo | O formulário não tem esse campo; a restrição vai dentro do objetivo |
| Janela de busca | Só aceita 3, 5, 7, 10 ou 20 anos; usamos 20 anos em T1 e T2, e em T1 o relato mais antigo é de 1992 |
| Projeto reaberto | O objetivo e as bases não aparecem, os critérios não podem ser editados e o PICO não vem com P, I, C e O rotulados |
| Google Acadêmico | A fonte é gerada nas strings mesmo desmarcada |
| Créditos | A prévia é gratuita; cada triagem consome 1 crédito (10 para 9 em T1; 9 para 8 em T2) |
| Exportação | PDF resumo, PDF completo e XLSX; sem CSV nem JSON; o download pela interface não concluiu no Chrome do Mac |
| Tempo na tela | A estimativa é inconsistente, e a própria tela pede para não fechar a aba |
| Cadastro | Cria a conta e entra direto, sem verificação de e-mail e com 0 créditos |
| Recuperação de senha | Depende de um e-mail manual do atendimento, porque o envio automático está indisponível |


### Dia 4 (T3-B e E2)

**T3-B (repetição de T3).** Em 20/11 executamos T3-B, com a mesma entrada de T3 (projeto #86), 48 h depois dela e com a mesma configuração: revisão sistemática, janela de 20 anos, PubMed, SciELO e Google Acadêmico marcados, Top 30. Todos os artigos analisados vieram do PubMed; SciELO retornou 0 e o Google Acadêmico também, com 12 erros de strings nas buscas iniciais. Foram 1500 artigos analisados nas duas execuções, 25 incluídos em T3 e 18 em T3-B, e nenhuma das duas chegou a 30 itens no Top (25 e 18). Pelo PMID, 16 estudos aparecem nos dois Tops (64% do Top de T3 e 89% do Top de T3-B), a união tem 27 estudos e o índice de Jaccard é 0,593. O PICO e as strings foram redigidos de novo, com a mesma estrutura. O topo do Quality Score foi 88 em T3 e 85 em T3-B. Tínhamos 4 créditos antes de T3-B e sobraram 3.

**M1.5.2 (estabilidade).** Os dois temas repetidos ficaram abaixo do 0,70 que a hipótese H1.5 previa: T1 com 0,579 (22 dos 30 estudos em comum) e T3 com 0,593. A média é 0,586, nível Aceitável.

**E2 e M1.5.1.** A E2 testaria o cumprimento de filtros em busca só no SciELO: janela de 5 anos, revisão sistemática, Top 30, com a restrição a estudos observacionais primários escrita no objetivo, porque o formulário não tem campo de tipo de estudo. Executamos duas vezes (projetos #87 e #88, 20/11) com a mesma configuração, e nenhuma gerou lista: a #87 passou de 2 horas sem terminar e a #88, repetição da mesma configuração, foi interrompida por decisão da avaliadora após mais de 1 hora sem lista, sem esperar as 2 horas. A E2 é a segunda execução sem retorno e fica sem lista. Por isso a M1.5.1 é calculada só sobre a E1, como o método prevê quando falta uma das execuções ("calculada sobre o que existe e a base é declarada"): 1 item conforme em 30, ou 3,3%, com a base declarada de uma execução e 30 itens. Dos 30 itens da E1, 29 não são ensaios randomizados (a maioria é meta-análise ou revisão), embora todos tenham ano e fonte corretos.

**Achado de adequação funcional: SciELO sem retorno.** O SciELO retornou 0 artigos em todas as execuções que o marcavam: T1, T1-B, T2, T3, T3-B, T4 e as duas da E2 (#88 interrompida por decisão da avaliadora). Nas três primeiras rodadas de busca da E2, cada etapa terminou com sucesso e com 0 resultado em todas as strings (o VICKY lista cada string com +0). Depois, o VICKY refez a busca com termos novos (rotação de termos), primeiro 6 strings, depois outras 6 e depois 19, sempre com 0, e entrou em uma rotação maior, com 65 strings em 3 estratégias, que não terminou até a interrupção. Não vimos limite de tentativas: com uma só fonte e 0 resultado, o processo segue buscando e não fecha a triagem nem devolve lista. A busca direta no site do SciELO encontra artigos sobre diabetes gestacional no Brasil; o zero, portanto, vem da busca dentro do VICKY, e não da falta de literatura. O Google Acadêmico também retornou 0, com erros nas strings. Todo resultado do VICKY neste estudo veio do PubMed, o que explica por que M1.1.2 coincide com M1.1.1. Para o estudante, a consequência é que escolher o SciELO como fonte, sozinha ou com outras, não traz nenhum artigo dela e, no caso de fonte única, a triagem não termina. Tratamos isso como achado da completude e da correção funcional do VICKY, e não como falha de execução da coleta; o método não foi alterado.

**M1.1 e M1.3.1.** O VICKY trouxe 3 dos 12 estudos de referência em T1, 3 dos 21 em T2, 3 dos 32 em T3 (denominador 30) e 2 dos 7 em T4. Dos itens que entraram nos Tops, só 17% a 32% foram julgados relevantes por A1 e A2, porque o Top é dominado por revisões e meta-análises quando o objetivo pedia ensaios ou estudos primários. Os metadados dos itens conferidos estão todos corretos (40 de 40).

**M1.4.1.** O Quality Score quase não acompanha a rubrica: ρ de -0,120 em T1 e 0,187 em T2. As notas da rubrica de A1 e A2 concordam entre si (ρ de 1,000 em T1 e 0,914 em T2), então a falta de correlação não vem de divergência entre avaliadores.

## 4. Hipóteses

Uma hipótese é confirmada quando o valor medido cai na faixa que ela previu. Isso não muda o julgamento: mostra se a leitura preliminar da equipe estava certa. As previsões de H1.1 a H1.5 estão em [níveis e julgamento](../fase-2/niveis-e-julgamento.md).


| Hipótese | Medido | Resultado |
|----------|--------|-----------|
| H1.1 (recall de 40% a 60%; sobe 10 pontos descontando as fontes) | M1.1.1 0,195; M1.1.2 0,195, sem ganho | Refutada |
| H1.2 (no máximo 1 função parcial ou ausente) | 5 parciais | Refutada |
| H1.3 (70% a 85% relevantes; 90% de metadados corretos) | M1.3.1 24,7%; M1.3.2 100% | Refutada na precisão, confirmada nos metadados |
| H1.4 (correlação de 0,50 ou mais) | M1.4.1 0,034 | Refutada |
| H1.5 (filtros em 93% ou mais; Jaccard de 0,70 ou mais) | M1.5.1 3,3% (base: E1); M1.5.2 0,586 | Refutada |

## 5. Respostas às questões

A pontuação de cada questão é a média dos pontos (0 a 3) das suas métricas. M1.1.1 e M1.3.1 são críticas: em Insatisfatório, a questão correspondente não passa de Aceitável. Regras completas em [níveis e julgamento](../fase-2/niveis-e-julgamento.md#2-regras-do-g1-adequacao-funcional).


| Questão | Métricas | Nível | Resposta |
|---------|----------|:-----:|----------|
| Q1.1 | M1.1.1 e M1.1.2 | Insatisfatório (0,00) | A lista recupera cerca de um quinto dos estudos que uma revisão de referência incluiria |
| Q1.2 | M1.2.1 | Aceitável (1,00) | O estudante executa a maior parte do fluxo, mas cinco funções ficam parciais |
| Q1.3 | M1.3.1 e M1.3.2 | Aceitável (1,50) | Os metadados são confiáveis, mas só cerca de um quarto dos itens responde ao PICO |
| Q1.4 | M1.4.1 | Insatisfatório (0,00) | O ranking não acompanha a rubrica metodológica |
| Q1.5 | M1.5.1 e M1.5.2 | Insatisfatório (0,50) | Na E1 só 1 de 30 itens atende ao filtro de tipo de estudo (E2 sem lista porque o SciELO não devolveu resultado), e duas execuções do mesmo tema repetem cerca de 59% do Top |

Objetivo G1: 0,60 ponto, Insatisfatório, julgamento "Não atende". Métricas medidas: 8 de 8 (M1.5.1 com base de uma execução).

## 6. Limitações

- F01: a recuperação de senha depende de e-mail enviado pelo atendimento, então esse subpasso não pôde ser executado de ponta a ponta.
- O SciELO retornou 0 artigos em todas as execuções; o Google Acadêmico retornou 0 com erros de strings. Por isso M1.1.2 coincide com M1.1.1 e a E2 (só SciELO) não gerou lista; M1.5.1 foi calculada só sobre a E1 (seção 3).
- O formulário não tem campo de tipo de estudo; nos testes de filtro a restrição foi escrita no objetivo.
- M1.3.2: conferência feita por código contra o registro oficial do PubMed (título, autores, ano, periódico) e por requisição HTTP ao link, sem abrir a página do DOI; os itens com PMID correspondem a artigos indexados no PubMed.
- T3 e T3-B ficaram com Top menor que 30 (25 e 18 itens).

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 17/11/2026 | Estrutura da página de resultados do G1 e relato do dia 1 da coleta | Larissa Gomes Silva | - |
| 0.2 | 18/11/2026 | Relato do dia 2 (T3 e E1) | Larissa Gomes Silva | - |
| 0.3 | 19/11/2026 | Relato do dia 3 (T4), campos de execução e incluídos de T1 | Larissa Gomes Silva | - |
| 0.4 | 19/11/2026 | Relato de T1-B (dia 3) e comparação com T1 | Larissa Gomes Silva | - |
| 0.5 | 20/11/2026 | Resultados finais do G1 (oito métricas, hipóteses e respostas às questões) e capturas de tela dos subpassos da M1.2.1 | Larissa Gomes Silva | - |
