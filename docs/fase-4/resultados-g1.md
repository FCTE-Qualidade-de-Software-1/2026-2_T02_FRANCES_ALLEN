# Resultados do G1 (adequação funcional)

!!! warning "Coleta em andamento (#26)"
    A coleta do G1 segue por quatro dias. Os campos marcados com _a preencher_ recebem os valores calculados pelo `calcular_g1.py` quando a coleta terminar. Nenhum valor desta página é estimado.

Esta página reúne o resultado das oito métricas do G1, conforme o [Método do G1](../fase-3/metodo-g1.md). Os níveis seguem a tabela de [níveis de pontuação](../fase-2/niveis-e-julgamento.md), fixada antes da coleta.

## 1. Execução da coleta

| Campo | Valor |
|-------|-------|
| Período | início em 17/11/2026; fim previsto em 20/11/2026 (_a preencher_ quando o dia 4 fechar) |
| Produto | VICKY em produção, <https://vicky.synaptha.com/> |
| Versão de referência | Termos de Uso de 29/09/2026, acessados em 17/11/2026 |
| Navegador | Google Chrome 157.0.8103.79; área visível e zoom não registrados |
| Condutor (C) | Larissa Gomes Silva |
| Avaliadores | A1 Gabriel Fae, A2 Lucas Avelar; A3 João Felipe Oliveira só nos desempates |
| Triagens feitas | T1 e T2 (dia 1); T3 e E1 (dia 2); T4 (dia 3); T1-B, T3-B e E2 _a preencher_ |
| Créditos | 10 antes de T1; 5 depois de T4 |
| Itens não coletados | _a preencher_ (ou "nenhum") |
| Desvios do método | _a preencher_ (ou "nenhum") |

Como o `screencapture` não está disponível por SSH, as evidências que guardamos são texto do DOM, não imagem.

## 2. Valores medidos

| Métrica | Medida | Valor | Nível | Dados brutos |
|---------|--------|:-----:|:-----:|--------------|
| M1.1.1 | Recall@30 normalizado (T1 a T4) | _a preencher_ | _a preencher_ | [M1.1.1/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G1/M1.1.1) |
| M1.1.2 | Recall restrito às fontes (T1 a T4) | _a preencher_ | _a preencher_ | [M1.1.2/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G1/M1.1.2) |
| M1.2.1 | Funções declaradas operantes (F01 a F09) | _a preencher_ | _a preencher_ | [M1.2.1/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G1/M1.2.1) |
| M1.3.1 | Precisão@30 (T1 a T4) e kappa | _a preencher_ | _a preencher_ | [M1.3.1/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G1/M1.3.1) |
| M1.3.2 | Metadados e links corretos | _a preencher_ | _a preencher_ | [M1.3.2/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G1/M1.3.2) |
| M1.4.1 | Spearman entre Quality Score e rubrica (T1 e T2) | _a preencher_ | _a preencher_ | [M1.4.1/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G1/M1.4.1) |
| M1.5.1 | Conformidade com filtros (E1 e E2) | _a preencher_ | _a preencher_ | [M1.5.1/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G1/M1.5.1) |
| M1.5.2 | Estabilidade entre execuções (T1 e T3) | _a preencher_ | _a preencher_ | [M1.5.2/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G1/M1.5.2) |

### Concordância entre os avaliadores (M1.3.1)

O kappa de Cohen mínimo é 0,61. Abaixo disso, o tema passa por um rejulgamento independente e, persistindo, sai da média.

| Tema | Itens avaliados | Itens iguais | Kappa | Decididos por A3 |
|------|:---------------:|:------------:|:-----:|:----------------:|
| T1 | _a preencher_ | _a preencher_ | _a preencher_ | _a preencher_ |
| T2 | _a preencher_ | _a preencher_ | _a preencher_ | _a preencher_ |
| T3 | _a preencher_ | _a preencher_ | _a preencher_ | _a preencher_ |
| T4 | _a preencher_ | _a preencher_ | _a preencher_ | _a preencher_ |

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

### Achados dos dias seguintes

| Métrica | Achado | Evidência |
|---------|--------|-----------|
| _a preencher_ | _a preencher_ | _a preencher_ (nome do arquivo em `dados/avaliacao/G1/`) |

## 4. Hipóteses

Uma hipótese é confirmada quando o valor medido cai na faixa que ela previu. Isso não muda o julgamento: mostra se a leitura preliminar da equipe estava certa. As previsões de H1.1 a H1.5 estão em [níveis e julgamento](../fase-2/niveis-e-julgamento.md).

| Hipótese | Medido | Resultado |
|----------|--------|-----------|
| H1.1 | _a preencher_ | _confirmada ou refutada_ |
| H1.2 | _a preencher_ | _confirmada ou refutada_ |
| H1.3 | _a preencher_ | _confirmada ou refutada_ |
| H1.4 | _a preencher_ | _confirmada ou refutada_ |
| H1.5 | _a preencher_ | _confirmada ou refutada_ |

## 5. Respostas às questões

A pontuação de cada questão é a média dos pontos (0 a 3) das suas métricas. M1.1.1 e M1.3.1 são críticas: em Insatisfatório, a questão correspondente não passa de Aceitável. Regras completas em [níveis e julgamento](../fase-2/niveis-e-julgamento.md#2-regras-do-g1-adequacao-funcional).

| Questão | Métricas | Nível | Resposta |
|---------|----------|:-----:|----------|
| Q1.1 | M1.1.1 e M1.1.2 | _a preencher_ | _a preencher_ |
| Q1.2 | M1.2.1 | _a preencher_ | _a preencher_ |
| Q1.3 | M1.3.1 e M1.3.2 | _a preencher_ | _a preencher_ |
| Q1.4 | M1.4.1 | _a preencher_ | _a preencher_ |
| Q1.5 | M1.5.1 e M1.5.2 | _a preencher_ | _a preencher_ |

O objetivo G1 é a média das cinco questões e não passa de Bom se alguma ficar em Insatisfatório. Métricas medidas: _a preencher_ de 8.

## 6. Limitações

- A coleta do dia 1 não tem capturas de imagem, só texto do DOM.
- _a preencher_: itens não coletados, mudanças em produção durante a coleta e diferenças entre as execuções.

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 17/11/2026 | Estrutura da página de resultados do G1 e relato do dia 1 da coleta | Larissa Gomes Silva | - |
| 0.2 | 18/11/2026 | Relato do dia 2 (T3 e E1) | Larissa Gomes Silva | - |
| 0.3 | 19/11/2026 | Relato do dia 3 (T4), campos de execução e incluídos de T1 | Larissa Gomes Silva | - |
