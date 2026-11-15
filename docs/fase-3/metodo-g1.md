# Método de coleta do G1 (adequação funcional)

Este método cobre as oito métricas do objetivo G1, de M1.1.1 a M1.5.2. Definição, fórmula e níveis de cada métrica são os da [Fase 2](../fase-2/especificacao-das-metricas.md); esta página fixa o que a Fase 2 deixou para a Fase 3 e diz, passo a passo, como coletar, registrar e calcular. Quem seguir a página na ordem, com as mesmas planilhas, chega ao mesmo valor.

Os dados brutos ficam em [`dados/avaliacao/G1/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G1), e o cálculo é feito pelo script [`calcular_g1.py`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/blob/main/dados/avaliacao/G1/calcular_g1.py), versionado na mesma pasta.

## 1. Métricas cobertas

| Métrica | Questão | Insumo | Execuções do VICKY usadas | Pasta em `dados/avaliacao/G1/` |
|---------|:-------:|--------|---------------------------|--------------------------------|
| [M1.1.1](../fase-2/especificacao-das-metricas.md#m111) Recall@30 normalizado | Q1.1 | Top 30 de T1 a T4 e lista de incluídos de cada revisão de referência | T1, T2, T3, T4 | `M1.1.1/` |
| [M1.1.2](../fase-2/especificacao-das-metricas.md#m112) Recall restrito às fontes | Q1.1 | Consulta manual de cada estudo incluído no PubMed, SciELO e Google Acadêmico | T1, T2, T3, T4 (sem triagem nova) | `M1.1.2/` |
| [M1.2.1](../fase-2/especificacao-das-metricas.md#m121) Funções declaradas operantes | Q1.2 | Um caso de teste por função, F01 a F09 | Projeto rascunho P0, T1 e E1 (sem triagem nova) | `M1.2.1/` |
| [M1.3.1](../fase-2/especificacao-das-metricas.md#m131) Precisão@30 | Q1.3 | Top 30 de cada tema e fichas de A1 e A2 | T1, T2, T3, T4 (sem triagem nova) | `M1.3.1/` |
| [M1.3.2](../fase-2/especificacao-das-metricas.md#m132) Metadados e links corretos | Q1.3 | Amostra sistemática de 10 itens por tema e página oficial de cada artigo | T1, T2, T3, T4 (sem triagem nova) | `M1.3.2/` |
| [M1.4.1](../fase-2/especificacao-das-metricas.md#m141) Spearman entre Quality Score e rubrica | Q1.4 | Quality Score de T1 e T2 e rubrica de A1 e A2 | T1, T2 (sem triagem nova) | `M1.4.1/` |
| [M1.5.1](../fase-2/especificacao-das-metricas.md#m151) Conformidade com filtros | Q1.5 | Duas execuções com filtros restritivos | E1, E2 | `M1.5.1/` |
| [M1.5.2](../fase-2/especificacao-das-metricas.md#m152) Estabilidade entre execuções | Q1.5 | Segunda execução de T1 e de T3, 24 horas ou mais depois da primeira | T1-B, T3-B (e as primeiras de T1 e T3) | `M1.5.2/` |

São oito triagens completas: T1, T2, T3, T4, E1, E2, T1-B e T3-B. Todas as outras métricas reaproveitam essas listas, o que mantém a coleta dentro da estimativa de cerca de oito triagens da Fase 2.

## 2. Por que este método

### 2.1 Lugar no processo de avaliação

Na ISO/IEC 25040:2024, a terceira atividade do processo de avaliação de produto é projetar a avaliação: escolher como cada medida será aplicada, com que dados, por quem e em que ordem, antes de qualquer medição. Esta página é esse projeto para o G1. Ela não muda fórmulas, níveis nem regras de agregação da [Fase 2](../fase-2/index.md); fecha as decisões que a Fase 2 deixou explicitamente para cá, escolhe a massa de dados e declara, na seção 2.6, os três ajustes de procedimento que a coleta exige.

### 2.2 Revisão sistemática como padrão de referência

Para medir completude (Q1.1) é preciso saber quais estudos a lista deveria conter. Montar esse gabarito do zero exigiria a equipe fazer uma revisão sistemática por tema, o que está fora do alcance e introduziria o julgamento da própria equipe no padrão. Por isso cada tema usa uma revisão sistemática publicada e recente (de 2024 a 2026), cuja lista de estudos incluídos foi definida por especialistas com protocolo e busca documentados. Esse é o desenho usual para avaliar ferramentas de apoio à identificação de estudos: comparar o que a ferramenta recupera com os estudos incluídos de revisões já publicadas (O'MARA-EVES et al., 2015). A [ficha de M1.1.1](../fase-2/especificacao-das-metricas.md#m111) já prevê esse padrão; o método escolhe as revisões e diz como tratar o que o VICKY não tem como alcançar (seção 3.3). Nem todas são de acesso aberto: a cópia de T4 no PMC só é liberada em 12/05/2027, e as listas nominais de T1, T2 e T4 ainda precisam ser baixadas da Cochrane Library na etapa 1. Se a lista de um tema não puder ser obtida, entra o tema reserva (seção 3.2).

Três das quatro revisões são da Cochrane, que publica a lista de estudos incluídos em seção própria e segue o mesmo manual de métodos. A quarta, de saúde pública brasileira, foi publicada em periódico nacional indexado no SciELO, porque a Fase 2 pede um tema em que o SciELO pese.

### 2.3 Julgamento por dois avaliadores, às cegas

Relevância (M1.3.1) e qualidade metodológica (M1.4.1) dependem de julgamento humano. A Fase 2 exige dois avaliadores, e M1.3.1 só vale com kappa de Cohen de 0,61 ou mais (COHEN, 1960; LANDIS; KOCH, 1977). O método acrescenta três controles para que o julgamento não seja influenciado pelo próprio VICKY:

1. **Avaliador não conduz a triagem.** Quem executa a triagem vê a posição e o Quality Score de cada artigo; por isso não julga.
2. **Ficha cega.** A1 e A2 recebem título, resumo, ano, periódico e DOI em ordem aleatória, sem posição nem Quality Score. A ficha de M1.3.1 pede título e resumo sem posição nem Quality Score; ano, periódico e DOI entram para ajudar a identificar o artigo e não revelam o ranking. A ordem sai de uma semente fixa, então qualquer pessoa gera a mesma ficha.
3. **Julgamento independente registrado antes da conversa.** Cada ficha sobe ao repositório antes da comparação, e o histórico de commits prova a independência.
4. **Avaliador sem contato com o gabarito.** Quem escolheu as revisões de referência ou leu a lista de estudos incluídos de algum tema já sabe quais artigos a revisão aceitou; por isso não é A1 nem A2.

### 2.4 Decisões que a Fase 2 deixou para esta fase

| Decisão | Onde a Fase 2 deixou em aberto | Decisão desta fase | Seção |
|---------|--------------------------------|--------------------|:-----:|
| Regra de discordância em M1.3.1 | Ficha de M1.3.1, passo 4 | Concordância mantém; consenso entre A1 e A2; sem consenso, A3 decide | 7.1 |
| Kappa abaixo de 0,61 | Ficha e níveis de M1.3.1 | Um rejulgamento independente; persistindo, o tema sai da média | 7.2 |
| Escolha dos 10 itens de M1.3.2 | Ficha de M1.3.2, passo 1 | Amostra sistemática, posições 3, 6, 9, ..., 30 | 4.5 |
| Pesos da rubrica de M1.4.1 | Ficha de M1.4.1 (componentes sem pesos) | Desenho 4, amostra 3, comparador 2, revisão por pares 1 | 4.6 |
| Configuração dos filtros de M1.5.1 | Ficha de M1.5.1 | E1 só PubMed, 5 anos, ensaios randomizados; E2 só SciELO, 5 anos, observacionais primários | 4.7 |
| Temas repetidos em M1.5.2 | Ficha de M1.5.2 ("temas repetidos") | T1 e T3 | 3.5 |
| Janela de busca até a data de corte da revisão | Ficha de M1.1.1, passo 2 | O VICKY só oferece janela relativa ao ano atual; regra na seção 3.3 | 3.3 |
| Definição de função operante, parcial e ausente | Ficha de M1.2.1 (definição sem caso de teste por função) | Subpassos fixos por função; regra mecânica | 4.3 |

### 2.5 Coerência com métricas, níveis e julgamento da Fase 2

Nenhuma fórmula, limiar ou regra de agregação muda nesta fase. A tabela mostra, para cada métrica, o que vem da Fase 2 e o que o método acrescenta para que o valor seja obtido do mesmo jeito por qualquer pessoa.

| Métrica | Fórmula (Fase 2) | Piso de Bom | Papel na agregação (Fase 2) | O que o método fixa |
|---------|------------------|:-----------:|-----------------------------|---------------------|
| M1.1.1 | R = N(Top 30 ∩ Ref) / min(N(Ref), 30), média de T1 a T4 | 0,60 | Crítica em Q1.1 | Revisões, regra do gabarito na data da coleta, unidade estudo, casamento por DOI, PMID e título |
| M1.1.2 | Rr = N(Top 30 ∩ Ref indexada) / min(N(Ref indexada), 30) | 0,70 | Média em Q1.1 | Como consultar cada fonte e o que conta como "encontrado" |
| M1.2.1 | C = (operantes + 0,5 x parciais) / 9 | 85% | Única em Q1.2 | Caso de teste e subpassos de cada função |
| M1.3.1 | P = relevantes / avaliados, média de T1 a T4; kappa por tema | 70% | Crítica em Q1.3; vale com kappa de 0,61 ou mais | Critério de relevância por tema, ficha cega, discordância, kappa baixo |
| M1.3.2 | K = corretos / verificados, 10 itens por tema | 90% | Média em Q1.3 | Amostra sistemática e regra de igualdade de cada campo |
| M1.4.1 | ρ de Spearman entre Quality Score e média da rubrica, média de T1 e T2 | 0,50 | Única em Q1.4 | Pesos e escala de cada componente da rubrica |
| M1.5.1 | F = conformes / avaliados nas duas execuções | 93% | Média em Q1.5 | Configuração de E1 e E2 e a evidência de cada conferência |
| M1.5.2 | J = N(A ∩ B) / N(A ∪ B), média dos temas repetidos | 0,70 | Média em Q1.5 | Temas repetidos, intervalo de 24 a 72 horas, mesma entrada |

O script de cálculo aplica os níveis da [tabela de níveis](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica) e as [regras do G1](../fase-2/niveis-e-julgamento.md#2-regras-do-g1-adequacao-funcional) (média por questão, métricas críticas, teto do objetivo e julgamento) exatamente como estão escritas, para que a Fase 4 não precise refazer a agregação à mão.

### 2.6 Ajustes de procedimento em relação às fichas da Fase 2

Três passos de coleta das fichas da Fase 2 foram ajustados para que a medição possa ser repetida. Nenhum muda fórmula, limiar ou regra de agregação, e os três são declarados na Fase 4.

| Ficha | O que a Fase 2 diz | O que este método faz | Por que | Seção |
|-------|--------------------|-----------------------|---------|:-----:|
| M1.1.1 | Ref é a lista de estudos incluídos da revisão | Sai de Ref o estudo cuja única fonte é registro de ensaio, dado não publicado ou comunicação pessoal | O VICKY busca artigos indexados; um estudo sem relato publicado não pode aparecer em nenhuma lista | 3.3 |
| M1.2.1 | Listar as funções anunciadas na página pública | Usa a lista F01 a F09 do objeto de avaliação da Fase 1 | A própria ficha fixa o denominador em 9 por essa lista | 4.3 |
| M1.1.1 e M1.5.2 | Mesmo artigo é mesmo DOI; em M1.1.1, na falta de DOI, título e ano | DOI; sem DOI, PMID; sem os dois, título normalizado e ano, nas duas métricas | O PMID identifica o mesmo registro sem depender da grafia do título, e M1.5.2 passa a usar a mesma regra de M1.1.1 | 4.9 e 6 |

## 3. Preparação

### 3.1 Papéis

| Papel | Quem pode ser | Faz | Não pode |
|-------|---------------|-----|----------|
| C (condutor) | Responsável pela coleta do G1 (#26) | Prepara o gabarito, executa as oito triagens e os casos de teste de M1.2.1, registra as listas, faz a conferência de M1.3.2 e de M1.5.1, gera as fichas cegas, roda o script | Julgar relevância ou rubrica |
| A1 | Integrante da equipe que não conduziu nenhuma triagem do G1, não escolheu as revisões de referência e não leu a lista de incluídos de nenhum tema | Julga relevância (M1.3.1) e rubrica (M1.4.1); depois de enviar todas as próprias fichas, confere M1.2.1 e revê os itens incorretos de M1.3.2 e os não conformes de M1.5.1 | Abrir o VICKY, as capturas, a lista ranqueada ou `chave_Tn.csv` antes de enviar todas as próprias fichas (T1 a T4 e rubrica) |
| A2 | Outro integrante nas mesmas condições de A1 | Julga relevância e rubrica | O mesmo que A1 |
| A3 | Integrante que não é C, A1 nem A2 | Decide só as discordâncias de M1.3.1 sem consenso | Ver posição ou Quality Score do item |

Os papéis são ocupados por integrantes da equipe, e a relação entre papel e integrante (C, A1, A2 e A3) é registrada com o nome em `M1.3.1/coleta.md`. Integrantes podem ser nomeados, porque o histórico do git já identifica quem enviou cada arquivo; só participantes externos são anonimizados, e o G1 não tem participantes ([README da pasta de dados](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/blob/main/dados/README.md)). Nas planilhas, cada um aparece pelo papel.

**Conhecimento exigido.** A equipe é de engenharia de software, não de medicina, e o método não pede formação clínica: o julgamento é feito contra um PICO escrito e critérios operacionais (seções 4.4 e 4.6). Pede-se de A1 e A2:

- leitura de resumo científico em inglês e português;
- saber o que são população, intervenção, comparador e desfecho (PICO);
- distinguir os desenhos de estudo usados nos critérios: revisão sistemática, ensaio clínico randomizado, coorte, caso-controle, transversal, série ou relato de caso, revisão narrativa e editorial;
- localizar o tamanho da amostra e o grupo de comparação num resumo.

Antes do julgamento, A1 e A2 leem as seções 4.4 e 4.6 (cerca de 20 minutos) e fazem o piloto de calibração da etapa 9 da seção 4. De C se pede familiaridade com a interface do VICKY, consulta ao PubMed, ao SciELO e ao Google Acadêmico e execução de um script Python pelo terminal. A falta de formação clínica dos avaliadores é declarada como limitação na Fase 4; o kappa mede se, apesar dela, o critério foi aplicado de forma consistente.

### 3.2 Temas de teste e PICO

A Fase 2 definiu quatro perfis de tema. Cada perfil existe para expor um fator de variação do [abstraction sheet do G1](../fase-2/objetivos-questoes-hipoteses.md#abstraction-sheet-do-g1).

| Tema | Perfil exigido pela Fase 2 | Tema escolhido | Por que este tema |
|------|----------------------------|----------------|-------------------|
| T1 | Fármaco com desfecho clínico bem estudado | Colchicina na prevenção secundária de eventos cardiovasculares | Fármaco único, desfecho duro e padronizado, ensaios grandes e bem indexados no PubMed: é o caso favorável, em que a base ideal está entre as fontes do VICKY |
| T2 | Intervenção não farmacológica | Ioga para fadiga em pessoas com câncer | A literatura usa termos variados (*yoga*, *Hatha*, *mind-body*), o que testa se a busca derivada do PICO cobre sinônimos |
| T3 | Saúde pública brasileira com literatura no SciELO | Prevalência de diabetes mellitus gestacional no Brasil | Revisão publicada em periódico brasileiro do SciELO, com estudos regionais; o PICO é de prevalência (sem intervenção), o que também testa a geração do PICO |
| T4 | Tema estreito, com poucos estudos | Tratamento farmacológico da ataxia de Friedreich | Doença rara, oito ensaios: mede se o VICKY acha o pouco que existe e quanto ruído completa a lista |

O PICO abaixo é o da revisão de referência e é o critério de relevância de M1.3.1. Ele não é digitado no VICKY: C digita apenas o texto do tema e do objetivo (seção 3.4), e o PICO que o VICKY gerar é registrado como gerado.

| Tema | P (população) | I (intervenção ou exposição) | C (comparador) | O (desfecho) | Desenho pedido |
|------|---------------|------------------------------|----------------|--------------|----------------|
| T1 | Adultos com doença cardiovascular aterosclerótica estabelecida | Colchicina | Placebo ou cuidado usual | Eventos cardiovasculares maiores: infarto, AVC, morte cardiovascular | Ensaio clínico randomizado |
| T2 | Adultos com câncer, durante ou após o tratamento | Ioga | Nenhuma intervenção, lista de espera, cuidado usual ou outro exercício | Fadiga relacionada ao câncer | Ensaio clínico randomizado |
| T3 | Gestantes no Brasil | Condição: diabetes mellitus gestacional | Não se aplica | Prevalência de diabetes mellitus gestacional | Estudo observacional (transversal ou coorte) com estimativa de prevalência |
| T4 | Pessoas com ataxia de Friedreich | Tratamento farmacológico (ex.: omaveloxolona, idebenona) | Placebo | Progressão neurológica ou funcional (ex.: escalas de ataxia) | Ensaio clínico randomizado |

**Reservas.** Se a lista de incluídos de um tema não puder ser obtida até a véspera da primeira triagem (etapa 1 da seção 4), o tema é trocado pela reserva do mesmo perfil, com a mesma regra:

| Tema | Reserva | Revisão de referência | Incluídos (resumo) |
|------|---------|-----------------------|:------------------:|
| T1 | Suplementação de cálcio na gestação para prevenir pré-eclâmpsia | Cluver; Rohwer; Rohwer, Cochrane 2025, DOI [10.1002/14651858.CD001059.pub6](https://doi.org/10.1002/14651858.CD001059.pub6) | 10 ECR |
| T2 | Telerreabilitação para dor cervical | Fandim et al., Cochrane 2025, DOI [10.1002/14651858.CD014428.pub2](https://doi.org/10.1002/14651858.CD014428.pub2) | 13 ECR |
| T3 | Insegurança alimentar e doenças crônicas não transmissíveis no Brasil | Laurentino et al., Rev. Bras. Epidemiol. 2024, DOI [10.1590/1980-549720240041](https://doi.org/10.1590/1980-549720240041) | 27 estudos |
| T4 | Intervenções para ceratopatia neurotrófica | Kruoch et al., Cochrane 2025, DOI [10.1002/14651858.CD015723.pub2](https://doi.org/10.1002/14651858.CD015723.pub2) | 7 ECR |

A troca é registrada em `execucoes.csv` (coluna `observacao`) e declarada na Fase 4.

### 3.3 Revisões de referência e regra do gabarito

| Tema | Revisão de referência | Incluídos | Data da busca da revisão | O que foi conferido e onde (14/11/2026) |
|------|-----------------------|:---------:|--------------------------|----------------------------------|
| T1 | EBRAHIMI, F. et al. *Colchicine for the secondary prevention of cardiovascular events*. Cochrane Database of Systematic Reviews, 2025. DOI [10.1002/14651858.CD014808.pub2](https://doi.org/10.1002/14651858.CD014808.pub2). PMID 41224205, PMC12611456 | 12 estudos (22.983 participantes) | Até fevereiro de 2025 | Número de incluídos e data da busca conferidos no resumo do PubMed (PMID 41224205); DOI e PMCID conferidos no conversor de identificadores do PMC. A lista nominal está na seção de estudos incluídos da revisão completa na Cochrane Library e ainda não foi baixada |
| T2 | MESSER, S. et al. *Yoga for fatigue in people with cancer*. Cochrane Database of Systematic Reviews, 2025. DOI [10.1002/14651858.CD015520](https://doi.org/10.1002/14651858.CD015520). PMID 40421669, PMC12107688 | 21 ECR (2.041 pessoas) | Outubro de 2023 | Número de incluídos e data da busca conferidos no resumo do PubMed (PMID 40421669); DOI e PMCID no conversor do PMC. Lista nominal a baixar da Cochrane Library |
| T3 | MOCELLIN, L. P. et al. *Gestational diabetes mellitus prevalence in Brazil: a systematic review and meta-analysis*. Cadernos de Saúde Pública, 2024. DOI 10.1590/0102-311XEN064919, acesso pelo [PMC11386532](https://pmc.ncbi.nlm.nih.gov/articles/PMC11386532/). PMID 39258680 | 32 estudos (21.942 mulheres) | Não informada no resumo, que delimita os estudos publicados de 2010 a 2021; a data da busca é tirada da seção de métodos do texto completo na etapa 1 | Número de incluídos conferido no resumo do PubMed (PMID 39258680) e lista nominal na Tabela 1 do texto completo no PMC, com os 32 estudos. O DOI é o declarado pela revista no SciELO, no PubMed e no PMC, mas não resolvia em doi.org nem tinha registro no Crossref; por isso o link é o do PMC |
| T4 | LYONS, S. et al. *Pharmacological treatments for Friedreich ataxia*. Cochrane Database of Systematic Reviews, 2026. DOI [10.1002/14651858.CD007791.pub5](https://doi.org/10.1002/14651858.CD007791.pub5). PMID 42117563, PMC13162314 | 8 ECR | 4 de fevereiro de 2025 | Número de incluídos e data da busca conferidos no resumo do PubMed (PMID 42117563). O registro PMC13162314 ainda não está aberto (liberação informada para 12/05/2027). Lista nominal a baixar da Cochrane Library |

Os identificadores e o número de incluídos de cada revisão, inclusive das reservas, estão em [`dados/avaliacao/G1/referencias/referencias.md`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/blob/main/dados/avaliacao/G1/referencias/referencias.md), com a fonte de cada conferência.

Nas revisões Cochrane, a lista que vale é a seção *Characteristics of included studies* e as referências em *References to studies included in this review*. Cada estudo pode ter vários relatos (artigo principal, análises secundárias, resumo de congresso); a planilha guarda todos, agrupados pelo estudo. Em T3 a lista é a Tabela 1, com a referência completa de cada estudo na lista de referências do artigo.

**Regra do gabarito (Ref).** As revisões são de 2024 a 2026, e o VICKY consulta as bases no dia da triagem. Para que Ref seja a mesma para qualquer pessoa que repita a coleta:

1. **Unidade é o estudo.** Ref é o conjunto de estudos incluídos na revisão. Um estudo conta como recuperado quando qualquer um dos seus relatos listados pela revisão aparece no Top 30. O denominador conta estudos, não relatos.
2. **Só entra o que estava publicado e indexado até a data da coleta.** Fica em Ref o estudo que tem ao menos um relato publicado (artigo, resumo em anais ou tese com referência bibliográfica) e indexado em alguma base bibliográfica até a data da triagem do tema. Sai de Ref, com o motivo anotado, o estudo cuja única fonte é registro de ensaio (ClinicalTrials.gov, ICTRP), dado não publicado ou comunicação pessoal com os autores. A coluna `publicado_ate_coleta` registra essa decisão.
3. **Estudo fora das três fontes fica em M1.1.1 e sai de M1.1.2.** É a regra da Fase 2: em M1.1.1 o estudo que o VICKY não tem como alcançar (não indexado no PubMed, no SciELO nem no Google Acadêmico) continua no denominador, porque o estudante perde aquela evidência de fato; em M1.1.2 ele sai, porque o objetivo é separar falha de triagem de limite das bases.
4. **Estudo publicado antes do início da janela do VICKY fica nas duas métricas.** A janela é limite da configuração oferecida pelo próprio VICKY, não das bases; por isso não é descontada. A coluna `antes_da_janela` permite relatar esses casos à parte na Fase 4.
5. **Artigo do Top 30 posterior à data de corte da revisão** não conta como acerto nem altera o denominador. A ficha de M1.1.1 pede janela "até a data de corte da revisão", mas o VICKY só oferece janelas relativas ao ano atual (seção 3.4); por isso a lista pode trazer estudos que a revisão não tinha como incluir. Eles continuam na lista para M1.3.1, M1.3.2 e M1.4.1.

### 3.4 Configuração das triagens

Na versão do código consultada para preparar este método, o formulário de novo projeto tem: tipo de revisão (sistemática ou narrativa), tema, objetivo, janela temporal (últimos 3, 5, 7, 10 ou 20 anos, contados a partir do ano corrente, inclusive), meta de artigos no Top (campo numérico de 1 a 30, com padrão 20, em `templates/projects/new.html` no commit `c2ae570`; conferir em produção), bases (PubMed, SciELO, Google Acadêmico) e o filtro "só artigos com texto completo gratuito". Na etapa 2 da seção 4, C confere o formulário em produção; se houver diferença, vale o que está em produção e a diferença vai para `execucoes.csv`.

Configuração comum às execuções T1 a T4, T1-B e T3-B:

| Campo | Valor |
|-------|-------|
| Tipo de revisão | Revisão sistemática |
| Meta de artigos no Top | 30 |
| Bases | PubMed, SciELO e Google Acadêmico (as três) |
| Só texto completo gratuito | Desmarcado |
| PICO e critérios gerados | Aceitos como gerados, sem edição. O texto gerado é copiado para `M1.1.1/pico_Tn.md` |
| Janela temporal | A menor opção cujo ano inicial cobre o relato mais antigo de Ref; se nenhuma cobrir, 20 anos. Definida na etapa 1, antes da triagem |

Texto digitado, literalmente, em cada tema:

| Tema | Campo "Tema da pesquisa" | Campo "Objetivo" |
|------|--------------------------|------------------|
| T1 | Colchicina na prevenção secundária de eventos cardiovasculares em adultos com doença aterosclerótica | Avaliar o efeito da colchicina, comparada a placebo ou cuidado usual, sobre eventos cardiovasculares maiores (infarto, AVC e morte cardiovascular) em ensaios clínicos randomizados |
| T2 | Ioga para fadiga em pessoas com câncer | Avaliar o efeito da ioga, comparada a nenhuma intervenção, lista de espera, cuidado usual ou outro exercício, sobre a fadiga relacionada ao câncer em adultos durante ou após o tratamento, em ensaios clínicos randomizados |
| T3 | Prevalência de diabetes mellitus gestacional no Brasil | Estimar a prevalência de diabetes mellitus gestacional em gestantes brasileiras a partir de estudos observacionais |
| T4 | Tratamento farmacológico da ataxia de Friedreich | Avaliar o efeito de fármacos, como omaveloxolona e idebenona, comparados a placebo, sobre a progressão neurológica medida por escalas de ataxia, em ensaios clínicos randomizados |

O texto é digitado em português porque é assim que o público do VICKY o usa; a busca nas bases é responsabilidade da ferramenta.

### 3.5 Contas, créditos e divisão das triagens

| Recurso | Uso no G1 | Situação |
|---------|-----------|----------|
| Conta de cortesia (a mesma do G2) | As oito triagens e o projeto rascunho P0 | A conta recebeu 10 créditos de cortesia da equipe do VICKY em 17/10/2026, e o saldo era de 10 em 14/11/2026. São necessários 8; sobram 2 para repetir triagem que falhe. O saldo é conferido de novo na etapa 2 |
| E-mail de teste do G1 | Cadastro e recuperação de senha em M1.2.1 (F01) | Criado só para a coleta; senha fora do repositório |
| Projeto rascunho P0 | F02, F03 e F04 em M1.2.1 | Nunca recebe triagem completa, para que editar o PICO não altere as listas medidas |

Divisão das oito triagens:

| Execução | Tema | Para que serve | Por que assim |
|----------|:----:|----------------|---------------|
| T1, T2, T3, T4 | T1 a T4 | M1.1.1, M1.1.2, M1.3.1, M1.3.2; T1 e T2 também em M1.4.1; T1 também em F05 a F09 de M1.2.1 | Uma lista por tema alimenta cinco métricas; a ficha de M1.4.1 pede T1 e T2 |
| E1, E2 | T1 e T3 com filtros restritivos | M1.5.1; E1 também no subpasso de fonte de F04 | A ficha pede duas execuções; reaproveitar os textos de T1 e T3 evita desenhar temas novos |
| T1-B, T3-B | T1 e T3 repetidos | M1.5.2 (A é a lista de T1 e de T3 já registrada) | T1 tem literatura grande no PubMed, com muitos candidatos disputando 30 posições: é onde a instabilidade do ranking mais aparece. T3 depende do SciELO e do Google Acadêmico, cuja busca não tem a mesma estabilidade documentada do PubMed. A estimativa de cerca de oito triagens da Fase 2 comporta dois temas repetidos, e T1 e T3 cobrem as duas situações de fonte; por isso T2 e T4 não são repetidos |

**Se houver menos de oito créditos**, a ordem de prioridade é: T1, T2, T3, T4 (alimentam as duas métricas críticas), T1-B, E1, T3-B, E2. Execução não feita torna a métrica correspondente "não coletada" no tema, como manda a regra do G1 (sem estimativa). Com uma só execução em M1.5.1 ou um só tema em M1.5.2, a métrica é calculada sobre o que existe e a base é declarada. Uma das triagens de T1 a T4 é observada pelo G2 (ação "iniciar triagem" de M2.4.1); C combina o horário com quem executa o G2, sem crédito extra.

## 4. Passo a passo

### 4.1 Ordem das etapas

| Etapa | Quando | Quem | Atividade | Métricas |
|:-----:|--------|:----:|-----------|----------|
| 1 | Antes do dia 1 | C | Obter a lista de incluídos de T1 a T4, preencher `referencia_Tn.csv`, decidir `publicado_ate_coleta` e a janela de cada tema | M1.1.1, M1.1.2 |
| 2 | Dia 1 | C | Conferir o formulário em produção, anotar créditos, versão dos Termos e do Chrome em `execucoes.csv` | Todas |
| 3 | Dia 1 | C | Casos de teste F01 a F04 no projeto rascunho P0 | M1.2.1 |
| 4 | Dias 1 a 3 | C | Triagens T1 e T2 no dia 1, T3 no dia 2 e T4 no dia 3; registro de cada lista | M1.1.1, M1.3.1, M1.3.2, M1.4.1 |
| 5 | Dia 1 | C | Casos de teste F05 a F09 com o projeto T1 | M1.2.1 |
| 6 | Dias 3 e 4 | C | Triagens T1-B (dia 3) e T3-B (dia 4), 48 horas depois de T1 e de T3, com a mesma entrada | M1.5.2 |
| 7 | Dias 2 e 4 | C | Triagens E1 (dia 2) e E2 (dia 4) | M1.5.1, M1.2.1 (F04) |
| 8 | Dias 1 a 4 | C | Consulta de cada estudo de Ref às três fontes | M1.1.2 |
| 9 | Dia 2 | C, A1, A2 | Gerar as fichas cegas de T1 e T2; piloto de calibração de A1 e A2 (usa a lista de E1) | M1.3.1, M1.4.1 |
| 10 | Dias 2 a 5 | A1, A2 separados | Julgamento de relevância (T1 a T4, cada tema depois da sua ficha cega) e rubrica (T1 e T2); envio das fichas | M1.3.1, M1.4.1 |
| 11 | Dias 3 a 5 | C | Conferência de metadados e links; conferência dos filtros | M1.3.2, M1.5.1 |
| 11a | Dia 5, depois de A1 enviar todas as fichas | A1 | Conferência de M1.2.1 pelas capturas; revisão dos itens incorretos de M1.3.2 e dos não conformes de M1.5.1 | M1.2.1, M1.3.2, M1.5.1 |
| 12 | Dia 5 | A1, A2, A3 | Kappa, discordâncias e consolidado | M1.3.1 |
| 13 | Dia 5 | C | Cálculo com o script e conferência | Todas |

São no máximo duas triagens por dia, para não concentrar a coleta num dia só e para ficar dentro do limite diário de prévias da conta. Os dias seguem o [cronograma](cronograma.md): dia 1 é 16/11/2026 e dia 5 é 20/11/2026.

A prévia do PICO tem limite diário por conta. Se o limite for atingido num dia, as triagens restantes passam para o dia seguinte; o intervalo de M1.5.2 conta a partir do fim da execução A de cada tema.

### 4.2 Etapa comum: executar uma triagem e registrar a lista

Vale para T1 a T4, T1-B, T3-B, E1 e E2.

1. Abrir <https://vicky.synaptha.com/> no Google Chrome de computador, logado na conta de cortesia. Anotar o saldo de créditos em `creditos_antes`.
2. Criar um projeto novo e preencher os campos com os valores das seções 3.4 (T e T-B) ou 4.7 (E1 e E2). Copiar o texto do tema e do objetivo desta página; não redigitar.
3. Gerar os critérios. Copiar o PICO e os critérios gerados, sem editar, para `M1.1.1/pico_Tn.md` (`M1.5.1/pico_En.md` em E1 e E2, `M1.5.2/pico_Tn-B.md` em T1-B e T3-B). Capturar a tela.
4. Iniciar a triagem completa. Anotar data e hora de início. Não usar o botão de parar.
5. Ao terminar, anotar data e hora de fim, status e `creditos_depois`. Capturar a tela da lista.
6. Exportar a lista em XLSX pelo menu "Exportar" do detalhe do projeto (F09). No commit `c2ae570` o menu oferece PDF resumo, PDF completo e XLSX; CSV e JSON, citados na Fase 1, só são baixados se a interface em produção oferecer a opção (a conferir na etapa 2). Guardar os arquivos sem nenhuma edição em `exportacao/` da pasta da métrica, com o nome `Tn_AAAAMMDD.xlsx` (e `.csv` ou `.json`, se existirem).
7. Preencher a planilha da lista (`top30_Tn.csv`) a partir da exportação XLSX, uma linha por artigo, na ordem exibida. A coluna `fonte_exibida` é a base que o VICKY mostra no item. A coluna `resumo` é copiada da exportação; se a exportação não trouxer o resumo, C o copia do PubMed ou da página oficial do artigo. Se a exportação falhar, a planilha é preenchida pela tela, com captura de cada página da lista.
8. Se a lista tiver menos de 30 itens, registrar todos e anotar o número em `observacao`. A lista vale como está.

### 4.3 M1.2.1: funções declaradas operantes

Cada função tem subpassos fixos, tirados da descrição declarada em [objeto de avaliação](../fase-1/objeto-de-avaliacao.md#3-principais-funcionalidades).

**Por que a lista da Fase 1, e não a página pública.** O procedimento da ficha de M1.2.1 começa por listar as funções anunciadas na página pública. O método usa a lista F01 a F09 do objeto de avaliação da Fase 1 porque a própria ficha fixa o denominador em 9 e define as funções por essa lista (campo "Definição"), e porque a lista da Fase 1 já reúne o que o VICKY anuncia no site, nos Termos de Uso e no código. Listar de novo na página pública poderia mudar o denominador entre a Fase 2 e a coleta. Na etapa 2, C confere em produção se cada função continua anunciada e anota a diferença em `execucoes.csv`, sem mudar o denominador. A classificação é mecânica: **operante** quando todos os subpassos executam até o fim; **parcial** quando ao menos um executa e outro não; **ausente** quando nenhum executa ou a função não é encontrada. Cada subpasso exige captura de tela.

| Função | Onde | Subpassos (cada um é sim ou não) |
|--------|------|----------------------------------|
| F01 Cadastro e login | Janela anônima, e-mail de teste do G1 | (a) criar conta com nome, e-mail, senha e aceite dos Termos; (b) entrar com a conta criada; (c) pedir recuperação de senha, receber o e-mail e definir senha nova que permite entrar |
| F02 Criação de projeto | Projeto P0, com o texto de T1 | (a) criar projeto com tema e objetivo; (b) ajustar população, período, tipo de estudo e objetivo, como a descrição promete; (c) escolher o modo de revisão; (d) reabrir o projeto e ver os valores salvos |
| F03 Protocolo PICO | Projeto P0 | (a) gerar PICO com os quatro componentes; (b) gerar critérios de inclusão e de exclusão; (c) alterar um critério e ver a alteração salva |
| F04 Bases e quantidade | Projeto P0 e execução E1 | (a) escolher bases e ver a escolha salva em P0; (b) escolher a quantidade do Top (campo numérico de 1 a 30, padrão 20 no commit `c2ae570`; conferir em produção) e ver salva; (c) em E1, configurada só com PubMed, a lista exibe apenas itens com fonte PubMed |
| F05 Triagem completa | Execução T1 | (a) iniciar a triagem e o saldo cair 1 crédito; (b) acompanhar o andamento na tela; (c) a triagem terminar com lista; (d) o resultado mostrar os artigos excluídos com o motivo, que é a evidência visível da dupla checagem prometida |
| F06 Lista ranqueada | Lista de T1 | (a) itens em ordem decrescente de Quality Score; (b) cada item com Quality Score de 0 a 100; (c) os links dos itens nas posições 1 a 5 abrem a fonte do artigo |
| F07 Favoritos | Lista de T1 | (a) marcar um artigo; (b) desmarcar; (c) a marcação persistir depois de recarregar a página |
| F08 Log auditável | Projeto T1 | (a) o log é acessível pela interface; (b) traz os termos de busca usados; (c) traz os critérios de inclusão e exclusão aplicados |
| F09 Exportação | Projeto T1 | (a) PDF, (b) XLSX, (c) CSV e (d) JSON baixam pela interface, abrem e trazem os mesmos artigos da tela |

Em F09, cada formato é baixado pela opção da interface. No commit `c2ae570`, o menu "Exportar" (`templates/projects/detail.html`) oferece PDF resumo, PDF completo e XLSX; a rota `/projetos/{id}/export` (`web/app.py`) também aceita CSV e JSON, mas sem opção na tela. Como no G2 por inspeção, só vale o que o estudante consegue fazer pela interface normal: formato sem opção na tela em produção conta como subpasso não executado, e a forma de acesso observada é anotada.

Em F02 o subpasso (b) é verificado como prometido, sem supor onde o campo está: se a população ou o tipo de estudo só puderem ser ajustados pelo texto do objetivo ou pela edição dos critérios, o subpasso conta como executado e a forma é anotada; se não houver forma nenhuma, conta como não executado.

**Registro:** uma linha por função em `M1.2.1/casos_funcoes.csv`. C preenche `classificacao_executor`; A1, depois de enviar todas as próprias fichas (etapa 11a), olhando só as capturas e esta tabela, preenche `classificacao_conferente`. A espera existe porque as capturas de F05 e F06 mostram a lista de T1 com posição e Quality Score. Se as duas coincidirem, `classificacao_final` repete o valor. Se divergirem, C e A1 reabrem a captura e aplicam a regra; a decisão e o motivo vão em `observacao`.

### 4.4 M1.3.1: precisão@30

1. **Ficha cega (C).** Para cada tema, depois de preencher `top30_Tn.csv`, rodar:

    ```bash
    python3 dados/avaliacao/G1/calcular_g1.py ficha-cega --tema T1
    ```

    O comando cria `M1.3.1/ficha_cega_T1.csv` (item, título, resumo, ano, periódico, DOI, em ordem aleatória) e `M1.3.1/chave_T1.csv` (item e posição). A ordem vem da semente 20261114 mais o número do tema, então o mesmo Top 30 gera sempre a mesma ficha. A1 e A2 recebem só a ficha cega.

2. **Piloto de calibração (A1 e A2, juntos).** C separa os 10 primeiros itens da lista de E1 que não estão no Top 30 de T1 (comparação por DOI) e entrega título e resumo. A1 e A2 julgam cada um sozinho contra o PICO de T1, comparam e discutem as divergências. O piloto serve para alinhar a leitura do critério; não entra em nenhuma métrica e é registrado em `M1.3.1/piloto.md`.

3. **Julgamento (A1 e A2, separados).** Para cada item, contra o PICO do tema (seção 3.2), cada avaliador marca `relevante` como sim ou não:

    | Componente | Atendido quando | Não atendido quando |
    |------------|-----------------|---------------------|
    | População | O estudo é feito na população do tema ou num subgrupo dela | A população é outra (ex.: em T1, pacientes sem doença aterosclerótica; em T3, gestantes de outro país) |
    | Intervenção ou exposição | O estudo avalia a intervenção do tema (em T3, a ocorrência de diabetes gestacional) | A intervenção é outra ou aparece só como cointervenção |
    | Desfecho | O estudo mede o desfecho do tema | O desfecho medido é outro |
    | Desenho | O desenho é o pedido na seção 3.2 | É outro desenho, inclusive revisão sistemática, revisão narrativa, protocolo, editorial ou carta |

    O artigo é relevante só quando os quatro componentes são atendidos. O comparador não é exigido, porque a definição da Fase 2 cita população, intervenção, desfecho e tipo de estudo. O julgamento usa título e resumo. Componente que o resumo não menciona não reprova o artigo; componente que o resumo contradiz reprova. Se o desenho não puder ser identificado pelo resumo, o avaliador consulta o *Publication Type* do registro no PubMed; sem essa informação, o desenho conta como não atendido. Item sem resumo é julgado pelo título e pelo *Publication Type*, com `sem_resumo` na justificativa.

4. **Envio.** Cada avaliador salva `M1.3.1/julgamento_A1_Tn.csv` (ou `A2`) e envia ao repositório antes de ver a ficha do outro. Na coluna `componente_que_falhou`, o avaliador indica o primeiro componente não atendido (populacao, intervencao, desfecho, desenho) ou deixa vazio quando o item é relevante.

5. **Kappa e consolidação.** Seção 7.1 e 7.2.

### 4.5 M1.3.2: metadados e links corretos

1. **Amostra.** Os 10 itens são os das posições 3, 6, 9, 12, 15, 18, 21, 24, 27 e 30 do Top 30 de cada tema. Com lista de n itens, as posições são round(i x n / 10), para i de 1 a 10; com 10 itens ou menos, entram todos. O comando abaixo mostra as posições:

    ```bash
    python3 dados/avaliacao/G1/calcular_g1.py amostra --tema T1
    ```

    A amostra sistemática cobre o topo, o meio e o fim da lista em partes iguais e não depende de escolha de ninguém. A posição 1 fica de fora por construção, o que é aceitável porque nada indica que os metadados variem com a posição.

2. **Conferência (C).** Para cada item, abrir o link exibido pelo VICKY e a página oficial do artigo: a página do DOI (`https://doi.org/<DOI>`); sem DOI, o registro no PubMed; sem os dois, o registro no SciELO. Comparar os cinco campos:

    | Campo | Correto quando | Incorreto quando |
    |-------|----------------|------------------|
    | Título | Igual ao oficial, ignorando maiúsculas, acentos, pontuação final e tradução oficial registrada na página | Palavra trocada, faltando ou título de outro artigo |
    | Autores | Os nomes exibidos aparecem na mesma ordem na página oficial; lista truncada com "et al." é aceita | Autor trocado, faltando entre os exibidos ou com nome errado |
    | Ano | Igual ao ano que a página oficial usa na citação sugerida do artigo. Quando a publicação on-line antecipada e o fascículo têm anos diferentes, vale o da citação sugerida | Outro ano |
    | Periódico | Mesmo periódico, por extenso ou pela abreviatura oficial | Outro periódico ou ausente |
    | Link | Abre uma página do mesmo artigo (editora, DOI, PubMed, SciELO ou PDF) | Link quebrado, página de busca genérica ou outro artigo |

3. O item é correto só se os cinco campos estiverem corretos. Capturar a tela de cada item incorreto.
4. **Revisão (A1).** Depois de enviar todas as próprias fichas (etapa 11a), A1 revê, pelas capturas, todos os itens marcados como incorretos. Divergência é reaberta pelos dois, e a decisão vai em `observacao`.

### 4.6 M1.4.1: Quality Score e rubrica

1. A1 e A2 usam a mesma ficha cega de T1 e T2 da seção 4.4, sem posição nem Quality Score, e dão a cada um dos 30 artigos a nota da rubrica, independentemente da relevância. A ficha da Fase 2 define os componentes; os pesos são os desta tabela:

    | Componente | Pontos | Escala |
    |------------|:------:|--------|
    | Nível de evidência do desenho | 0 a 4 | 4: revisão sistemática de ensaios randomizados; 3: ensaio clínico randomizado; 2: coorte, caso-controle ou ensaio não randomizado; 1: transversal, série ou relato de caso, qualitativo, piloto sem grupo controle; 0: revisão narrativa, editorial, opinião, estudo pré-clínico |
    | Tamanho da amostra | 0 a 3 | 3: 1.000 participantes ou mais; 2: de 100 a 999; 1: de 30 a 99; 0: menos de 30 ou não informado. Em revisão sistemática, soma dos participantes dos estudos incluídos |
    | Presença de comparador | 0 a 2 | 2: grupo controle concorrente (placebo, cuidado usual ou outra intervenção); 1: comparador não concorrente (histórico, antes e depois); 0: sem comparador |
    | Revisão por pares | 0 a 1 | 1: publicado em periódico científico com revisão por pares; 0: *preprint*, resumo de congresso, tese ou relatório |

2. **Por que esses pesos.** A ordem dos desenhos segue a tabela de níveis de evidência do Oxford Centre for Evidence-Based Medicine para benefício de tratamento (OCEBM, 2011): revisão sistemática de ensaios randomizados no nível 1, ensaio randomizado no nível 2, coorte controlada não randomizada no nível 3 e série de casos, caso-controle ou controle histórico no nível 4. A rubrica agrupa os níveis 3 e 4 de forma própria (caso-controle com coorte, em 2 pontos) e dá 0 ao que a tabela não classifica como estudo clínico; esse agrupamento e o peso de 40% para o desenho são convenção da equipe. Amostra e comparador medem precisão e controle de viés dentro do desenho (30% e 20%). A revisão por pares separa o publicado do não revisado, mas quase todos os itens de uma busca no PubMed e no SciELO a têm, por isso pesa 10%. Os pesos são convenção da equipe, registrados antes da coleta, como os demais limiares da Fase 2.
3. Na falta de informação no resumo, o avaliador pode abrir o texto completo para achar o desenho e o tamanho da amostra. Não pode abrir o VICKY.
4. Cada avaliador salva `M1.4.1/rubrica_A1_Tn.csv` (ou `A2`), uma linha por item, com os quatro componentes. A nota é a soma, recalculada pelo script.
5. Não há consenso: como define a Fase 2, a nota do artigo é a média das notas de A1 e A2. O script informa, sem efeito na métrica, a correlação entre as notas dos dois avaliadores.

### 4.7 M1.5.1: conformidade com filtros

| Execução | Tema e objetivo | Bases | Janela | Tipo de estudo | Demais campos |
|----------|-----------------|-------|--------|----------------|---------------|
| E1 | Texto de T1; objetivo de T1 com o acréscimo "Incluir somente ensaios clínicos randomizados." | Só PubMed | Últimos 5 anos | Ensaio clínico randomizado | Revisão sistemática, Top 30, sem filtro de texto gratuito |
| E2 | Texto de T3; objetivo de T3 com o acréscimo "Incluir somente estudos observacionais primários, transversais ou de coorte; excluir revisões." | Só SciELO | Últimos 5 anos | Observacional primário | Revisão sistemática, Top 30, sem filtro de texto gratuito |

Cada execução restringe as três dimensões da ficha (janela, tipo de estudo e fonte), e as duas usam fontes diferentes. Na versão do código consultada não há campo próprio de tipo de estudo; por isso a restrição vai no objetivo, que alimenta os critérios gerados. Se em produção existir campo de tipo de estudo, C usa o campo, mantém o objetivo e anota em `execucoes.csv`.

Para cada item das duas listas, C confere e registra em `M1.5.1/conferencia_En.csv`:

| Coluna | Conforme quando | Evidência |
|--------|-----------------|-----------|
| `ano_ok` | O ano da citação sugerida na página oficial (a mesma regra de M1.3.2) está entre o ano inicial da janela e o ano da coleta | `ano_oficial` |
| `tipo_ok` | E1: relato de ensaio randomizado, inclusive análise secundária de ensaio, pelo *Publication Type* do PubMed ou pelo método descrito no resumo. E2: estudo observacional primário (transversal, coorte ou caso-controle). Revisão, protocolo, editorial e relato de caso não são conformes em nenhuma das duas | `tipo_observado` |
| `fonte_ok` | A fonte exibida pelo VICKY no item (`fonte_exibida`) é a configurada: PubMed em E1, SciELO em E2, como no subpasso (c) de F04. Se a lista não mostrar a fonte do item, vale o registro na base configurada (PMID no PubMed em E1; busca por DOI ou título em <https://search.scielo.org/> em E2); sem registro, o item não é conforme | `fonte_verificada` |

O item é conforme só quando as três colunas são sim. Item fora de qualquer filtro é defeito, como diz a ficha. A1 revê os itens não conformes pelas evidências, como em M1.3.2, depois de enviar todas as próprias fichas (etapa 11a).

### 4.8 M1.5.2: estabilidade entre execuções

1. A execução A é a triagem de T1 (e de T3) da etapa 4, já registrada em `M1.1.1/top30_T1.csv`.
2. A execução B começa entre 24 e 72 horas depois do fim de A. O mínimo é o da Fase 2; o máximo reduz a chance de a versão em produção mudar entre as duas.
3. B usa um projeto novo com a mesma entrada de A: mesmo tipo de revisão, texto do tema e do objetivo copiados desta página, mesma janela, mesmas bases, Top 30. O PICO gerado de novo não é editado, mesmo que difira do de A; a diferença é anotada, porque faz parte do que um estudante que repete a busca encontraria.
4. Registrar B em `M1.5.2/top30_T1-B.csv` pela etapa comum da seção 4.2.
5. Se, entre A e B, o VICKY mostrar mudança visível (versão dos Termos, nova opção no formulário), anotar em `execucoes.csv`; a comparação continua válida, e a mudança é declarada na Fase 4.

### 4.9 M1.1.1 e M1.1.2: cruzamento e consulta às fontes

1. **Gabarito (etapa 1, C).** Preencher `M1.1.1/referencia_Tn.csv` com uma linha por relato de cada estudo incluído: `estudo_id` (o identificador do estudo na revisão, ex.: `Tardif 2019`), `relato_id` (sequencial), `relato_principal`, autores, título, ano, periódico, DOI e PMID. Conferir que o número de estudos distintos bate com o número de incluídos da seção 3.3; se não bater, parar e anotar o motivo antes de seguir.
2. **Cruzamento (script).** Um relato de Ref e um item do Top 30 são o mesmo artigo quando têm o mesmo DOI. Se um dos lados não tiver DOI, vale o mesmo PMID; sem os dois, o mesmo título normalizado (sem acento, pontuação e caixa) e o mesmo ano. O script aplica essa regra.
3. **Correspondência manual.** Se C identificar o mesmo artigo com título diferente (tradução, título abreviado), registra o par em `M1.1.1/correspondencia_manual_Tn.csv` com a justificativa; o script soma esses pares. Nenhum par entra sem justificativa escrita.
4. **Consulta às fontes (etapa 8, C).** Para cada relato de Ref, procurar nas três fontes e anotar sim ou não em `M1.1.2/consulta_fontes_Tn.csv`:

    | Fonte | Como procurar | Encontrado quando |
    |-------|---------------|-------------------|
    | PubMed | DOI no campo de busca; sem resultado, o título entre aspas | O registro do mesmo relato aparece |
    | SciELO | Título entre aspas em <https://search.scielo.org/> | O registro do mesmo relato aparece |
    | Google Acadêmico | Título entre aspas em <https://scholar.google.com/> | O relato aparece na primeira página de resultados |

    Um estudo é "indexado" quando ao menos um de seus relatos é encontrado em ao menos uma fonte. Anotar a data da consulta.

## 5. Registro

Estrutura de `dados/avaliacao/G1/`. Os modelos de cada planilha, só com o cabeçalho, estão em [`modelos/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G1/modelos); para usar, copiar o modelo para a pasta da métrica com o nome da tabela abaixo.

```text
dados/avaliacao/G1/
├── calcular_g1.py                  # cálculo (seção 6)
├── execucoes.csv                   # uma linha por triagem, inclusive as que falharam
├── modelos/                        # cabeçalhos das planilhas, sem dado
├── M1.1.1/
│   ├── referencia_Tn.csv           # gabarito de cada tema
│   ├── top30_Tn.csv                # lista das execuções T1 a T4
│   ├── correspondencia_manual_Tn.csv   # só se houver par manual
│   ├── pico_Tn.md                  # PICO e critérios gerados, sem edição
│   └── exportacao/Tn_AAAAMMDD.xlsx # exportação original do VICKY (e .csv ou .json, se a produção oferecer)
├── M1.1.2/consulta_fontes_Tn.csv
├── M1.2.1/
│   ├── casos_funcoes.csv
│   └── evidencias/AAAAMMDD_Fnn_<subpasso>.png
├── M1.3.1/
│   ├── ficha_cega_Tn.csv e chave_Tn.csv     # gerados pelo script
│   ├── piloto.md
│   ├── julgamento_A1_Tn.csv e julgamento_A2_Tn.csv
│   ├── julgamento_A1_Tn_rodada2.csv e julgamento_A2_Tn_rodada2.csv   # só se houver rejulgamento
│   ├── consolidado_Tn.csv
│   └── coleta.md                   # kappa por tema, critério esclarecido, datas
├── M1.3.2/conferencia_Tn.csv e evidencias/
├── M1.4.1/rubrica_A1_Tn.csv e rubrica_A2_Tn.csv (T1 e T2)
├── M1.5.1/top_En.csv, pico_En.md, conferencia_En.csv e exportacao/
└── M1.5.2/top30_Tn-B.csv, pico_Tn-B.md e exportacao/
```

| Planilha | Modelo | Colunas |
|----------|--------|---------|
| `execucoes.csv` | `execucoes.csv` | `id_execucao` (T1, T1-B, E1...), `tema`, `finalidade`, `data_hora_inicio`, `data_hora_fim`, `condutor` (papel), `conta`, `texto_tema`, `texto_objetivo`, `tipo_revisao`, `janela_anos`, `ano_inicio`, `ano_fim`, `fontes`, `top`, `so_acesso_aberto`, `status`, `creditos_antes`, `creditos_depois`, `versao_termos`, `versao_chrome`, `observacao` |
| `top30_Tn.csv`, `top_En.csv`, `top30_Tn-B.csv` | `top30_TEMA.csv` | `posicao`, `quality_score`, `titulo`, `autores`, `ano`, `periodico`, `doi`, `pmid`, `link`, `fonte_exibida`, `resumo` |
| `referencia_Tn.csv` | `referencia_TEMA.csv` | `estudo_id`, `relato_id`, `relato_principal`, `autores`, `titulo`, `ano`, `periodico`, `doi`, `pmid`, `publicado_ate_coleta` (sim/nao), `antes_da_janela` (sim/nao), `observacao` |
| `correspondencia_manual_Tn.csv` | `correspondencia_manual_TEMA.csv` | `posicao`, `relato_id`, `justificativa` |
| `consulta_fontes_Tn.csv` | `consulta_fontes_TEMA.csv` | `estudo_id`, `relato_id`, `titulo`, `doi`, `pubmed`, `scielo`, `scholar` (sim/nao), `data_consulta`, `observacao` |
| `casos_funcoes.csv` | `casos_funcoes.csv` | `funcao`, `caso`, `data_hora`, `resultado_observado`, `classificacao_executor`, `classificacao_conferente`, `classificacao_final` (operante/parcial/ausente), `captura`, `observacao` |
| `julgamento_Ax_Tn.csv` | `julgamento_AVALIADOR_TEMA.csv` | `item`, `relevante` (sim/nao), `componente_que_falhou`, `justificativa` |
| `consolidado_Tn.csv` | `consolidado_TEMA.csv` | `item`, `a1`, `a2`, `final` (sim/nao), `decidido_por` (concordancia/consenso/A3), `justificativa` |
| `conferencia_Tn.csv` (M1.3.2) | `conferencia_m132_TEMA.csv` | `posicao`, `doi`, `pagina_oficial`, `titulo_ok`, `autores_ok`, `ano_ok`, `periodico_ok`, `link_ok` (sim/nao), `observacao` |
| `rubrica_Ax_Tn.csv` | `rubrica_AVALIADOR_TEMA.csv` | `item`, `desenho` (0-4), `amostra` (0-3), `comparador` (0-2), `revisao_pares` (0-1), `nota`, `justificativa` |
| `conferencia_En.csv` (M1.5.1) | `conferencia_m151_EXECUCAO.csv` | `posicao`, `doi`, `ano_oficial`, `ano_ok`, `tipo_observado`, `tipo_ok`, `fonte_verificada`, `fonte_ok` (sim/nao), `evidencia` |

Regras de registro:

- Data e hora em horário de Brasília, no formato `AAAA-MM-DD HH:MM`.
- A versão do VICKY é identificada pela data e hora de acesso e pela versão dos Termos de Uso exibida no site, como no G2, porque a tela não mostra número de versão.
- A exportação original do VICKY nunca é editada. Correção de transcrição é feita na planilha, com commit que diga o que mudou.
- Só entra dado real de coleta. Antes de enviar uma captura, conferir que ela não mostra nome ou e-mail de pessoa real, senha ou saldo de outra conta.
- As planilhas aceitam vírgula ou ponto e vírgula como separador e devem ser salvas em UTF-8.

## 6. Cálculo

Com as planilhas preenchidas, a partir da raiz do repositório:

```bash
python3 dados/avaliacao/G1/calcular_g1.py calcular --saida dados/avaliacao/G1/resultados.csv
```

O script usa só a biblioteca padrão do Python (3.9 ou superior). Ele imprime o detalhe por tema, o valor e o nível de cada métrica e a agregação por questão e do objetivo, e grava o resumo em `resultados.csv`. Arquivo ausente deixa a métrica ou o tema como "não coletado"; nada é estimado.

| Métrica | O script calcula | Arquivos lidos |
|---------|------------------|----------------|
| M1.1.1 | Por tema, R = estudos de Ref recuperados / min(estudos de Ref, 30), só com `publicado_ate_coleta = sim`; média dos temas | `referencia_Tn`, `top30_Tn`, `correspondencia_manual_Tn` |
| M1.1.2 | Rr com Ref indexada (estudos com algum relato encontrado em alguma fonte); média dos temas | os de M1.1.1 e `consulta_fontes_Tn` |
| M1.2.1 | C = (operantes + 0,5 x parciais) / 9, sobre `classificacao_final` | `casos_funcoes` |
| M1.3.1 | Kappa de Cohen por tema sobre `relevante` de A1 e A2 (da rodada 2, quando existir); P = `final = sim` / itens do consolidado; média dos temas válidos | `julgamento_*`, `consolidado_Tn` |
| M1.3.2 | K = itens com os cinco campos corretos / itens verificados, somando os quatro temas | `conferencia_Tn` |
| M1.4.1 | ρ de Spearman (postos médios nos empates) entre `quality_score` e a média das notas de A1 e A2, ligados pela chave da ficha cega; média de T1 e T2 | `top30_Tn`, `chave_Tn`, `rubrica_*` |
| M1.5.1 | F = itens com as três conformidades / itens conferidos, somando E1 e E2 | `conferencia_En` |
| M1.5.2 | J = interseção / união entre A e B, com a mesma regra de identidade de M1.1.1; média dos temas repetidos | `top30_Tn`, `top30_Tn-B` |

Duas observações sobre as fórmulas:

- Em M1.3.2 o valor é calculado sobre os 40 itens juntos, porque a ficha da Fase 2 define K sobre "verificados", sem média por tema. Nas demais métricas por tema, a Fase 2 pede a média dos temas, e o script segue isso.
- Na agregação, o teto das métricas críticas (Q1.1 e Q1.3 não passam de Aceitável se M1.1.1 ou M1.3.1 for Insatisfatório) é aplicado ao nível da questão. Com duas métricas por questão, a média já fica abaixo de 1,75 nesse caso; a regra está no script para o caso de a outra métrica não ser coletada.

**Conferência do cálculo.** Antes de publicar na Fase 4, uma segunda pessoa roda o mesmo comando sobre o mesmo commit e compara a saída. Qualquer diferença indica arquivo não enviado ou editado depois do cálculo. Os valores, o nível e a resposta a cada questão são publicados na Fase 4 (#26), comparando cada hipótese de H1.1 a H1.5 com o valor observado, sem mudar os limiares.

## 7. Discordância e repetição

### 7.1 Discordância em M1.3.1

1. Com as duas fichas no repositório, C calcula o kappa do tema (o script mostra o valor e a concordância bruta no detalhe) e registra em `M1.3.1/coleta.md` o kappa, a concordância bruta e a proporção de itens que cada avaliador marcou como relevantes.
2. Item em que A1 e A2 concordam fica com o julgamento comum (`decidido_por = concordancia`).
3. Item em que discordam é reaberto pelos dois, que releem título e resumo e aplicam a tabela da seção 4.4. Chegando a acordo, registram `decidido_por = consenso` e o motivo.
4. Sem acordo, A3 recebe só a linha da ficha cega e o PICO do tema, decide sozinho e a linha recebe `decidido_por = A3`.
5. P é calculado sobre `consolidado_Tn.csv`. O kappa é sempre o das fichas independentes, nunca o do consolidado.

### 7.2 Kappa abaixo de 0,61

A Fase 2 diz que M1.3.1 só vale com kappa de 0,61 ou mais. Quando um tema fica abaixo:

1. C lê a coluna `componente_que_falhou` das duas fichas e identifica o componente que concentra as divergências, sem mostrar aos avaliadores as respostas um do outro item a item.
2. A1 e A2, com C, reescrevem em `M1.3.1/coleta.md` a regra do componente problemático (por exemplo, se análise secundária de ensaio conta como ensaio randomizado). A regra nova vale para os temas seguintes e é reaplicada aos temas já julgados: se ela mudar o julgamento de algum item já consolidado, o item é reaberto pela seção 7.1 e a mudança é registrada.
3. A1 e A2 rejulgam o tema inteiro, cada um sozinho, pelo menos 24 horas depois da primeira rodada, com os mesmos itens em nova ordem: C roda `calcular_g1.py ficha-cega --tema Tn --rodada 2`, que gera `ficha_cega_Tn_rodada2.csv` com a semente do tema mais 100 e mantém os códigos dos itens. As fichas vão para `julgamento_A1_Tn_rodada2.csv` e `julgamento_A2_Tn_rodada2.csv`.
4. Os dois kappas são relatados. Vale o da rodada 2, e o consolidado é refeito sobre ela.
5. Se a rodada 2 também ficar abaixo de 0,61, o tema é declarado inválido para M1.3.1: sai da média e o motivo é relatado. Não há terceira rodada, para não forçar concordância.
6. M1.3.1 precisa de pelo menos três dos quatro temas válidos, para que a média não dependa de metade dos perfis da Fase 2. Com menos que isso, a métrica é declarada não aplicável, como prevê a regra do G1 para métrica que não pode ser coletada, e a Fase 4 relata que Q1.3 foi respondida só com M1.3.2.

Caso particular: se A1 e A2 marcarem todos os itens do tema com a mesma resposta, o kappa é indefinido (concordância esperada igual a 1). Com concordância total, o tema é considerado válido e o relatório registra "kappa indefinido, concordância total".

Quando quase todos os itens de um tema caem numa só classe (quase todos relevantes ou quase todos irrelevantes), o kappa cai mesmo com concordância bruta alta, porque a concordância esperada por acaso fica perto de 1. Por isso a concordância bruta e a proporção de relevantes ficam ao lado do kappa em `coleta.md`, e a Fase 4 explica o caso se ele acontecer. A regra de validade continua a do kappa.

**Risco de prazo.** O rejulgamento exige 24 horas, e o julgamento vai até o dia 5 (20/11). Um tema julgado no dia 5 só seria rejulgado em 21/11, fora da coleta, no dia do artigo v2 pelo [cronograma](cronograma.md). Se a rodada 2 não couber até o fim da coleta, ela é a primeira atividade cortada: o tema fica com o kappa da primeira rodada e, abaixo de 0,61, sai da média pelo passo 5, com o motivo declarado.

### 7.3 Repetição e falhas

| Situação | O que fazer |
|----------|-------------|
| Triagem termina com erro ou não termina em 2 horas | Registrar a linha em `execucoes.csv` com `status = falhou`, conferir se o crédito voltou (os Termos preveem devolução por falha) e repetir com a mesma configuração. Depois de três falhas no mesmo tema, a métrica fica "não coletada" naquele tema |
| Lista com menos de 30 itens | Vale como está; M1.3.1 e M1.4.1 usam os n itens, e a amostra de M1.3.2 segue a fórmula da seção 4.5 |
| B começou com menos de 24 horas ou mais de 72 horas depois do fim de A | B é descartada e repetida dentro da faixa, se houver crédito; sem crédito, o tema sai de M1.5.2 |
| Lista de incluídos inacessível antes do dia 1 | Trocar pelo tema reserva do mesmo perfil (seção 3.2) |
| Número de estudos do gabarito diferente do informado pela revisão | Parar, reler a seção de estudos incluídos e anotar a causa (ex.: estudo com dois braços contado como dois) antes de qualquer cálculo |
| Exportação falha | Transcrever a lista da tela, com captura de cada página |
| Avaliador vê a lista, a posição ou o Quality Score antes de enviar a ficha | O avaliador é trocado no tema afetado e a troca é registrada |
| Erro de transcrição descoberto depois | Corrigir a planilha com commit que explique a correção; nunca editar a exportação original |
| Mudança visível em produção durante a coleta | Anotar a data em `execucoes.csv`; refazer só o que depende da tela alterada, se houver crédito |

## Referências desta página

- COHEN, J. A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, v. 20, n. 1, p. 37-46, 1960.
- EBRAHIMI, F. et al. Colchicine for the secondary prevention of cardiovascular events. *Cochrane Database of Systematic Reviews*, 2025. DOI: 10.1002/14651858.CD014808.pub2.
- LANDIS, J. R.; KOCH, G. G. The measurement of observer agreement for categorical data. *Biometrics*, v. 33, n. 1, p. 159-174, 1977.
- LYONS, S. et al. Pharmacological treatments for Friedreich ataxia. *Cochrane Database of Systematic Reviews*, 2026. DOI: 10.1002/14651858.CD007791.pub5.
- MESSER, S. et al. Yoga for fatigue in people with cancer. *Cochrane Database of Systematic Reviews*, 2025. DOI: 10.1002/14651858.CD015520.
- MOCELLIN, L. P. et al. Gestational diabetes mellitus prevalence in Brazil: a systematic review and meta-analysis. *Cadernos de Saúde Pública*, v. 40, n. 8, e00064919, 2024. DOI: 10.1590/0102-311XEN064919 (não resolvia em doi.org em 14/11/2026). Disponível em: <https://pmc.ncbi.nlm.nih.gov/articles/PMC11386532/>.
- OCEBM LEVELS OF EVIDENCE WORKING GROUP. *The Oxford 2011 Levels of Evidence*. Oxford Centre for Evidence-Based Medicine, 2011. Disponível em: <https://www.cebm.ox.ac.uk/resources/levels-of-evidence/ocebm-levels-of-evidence>.
- O'MARA-EVES, A. et al. Using text mining for study identification in systematic reviews: a systematic review of current approaches. *Systematic Reviews*, v. 4, n. 5, 2015. DOI: 10.1186/2046-4053-4-5.

As demais referências (ISO/IEC 25040:2024, ISO/IEC 25023:2016, Basili; Caldiera; Rombach, 1994) estão em [Referências](../sobre/referencias.md).

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 04/11/2026 | Criação da página | Lucas Avelar | - |
| 0.2 | 09/11/2026 | Esqueleto com o que a Fase 2 define e os pontos em aberto para a responsável | Gabriel Fae | - |
| 0.3 | 14/11/2026 | Método completo: justificativa, temas e revisões de referência, regra do gabarito, papéis e conhecimento exigido, divisão das oito triagens, casos de teste de M1.2.1, critérios de relevância e rubrica, amostra de M1.3.2, filtros de M1.5.1, registro, script de cálculo e regras de discordância e repetição | Lucas Avelar | - |
| 0.4 | 14/11/2026 | Revisões de referência com PMID e local da conferência (DOI de T3 sem registro em doi.org), exportação a partir do XLSX, quantidade do Top de 1 a 30, justificativa da lista de funções de M1.2.1, fonte da hierarquia de evidências, coluna `versao_chrome`, papéis nomeados e "o VICKY" | Lucas Avelar | - |
| 0.5 | 14/11/2026 | Revisão: créditos confirmados, conferências fora do período de julgamento, avaliadores sem contato com as revisões, ajustes de procedimento declarados (2.6), ano pela citação sugerida, fonte exibida em M1.5.1, intervalo de M1.5.2 contado do fim de A, regra nova reaplicada aos temas já julgados, três de quatro temas válidos, concordância bruta ao lado do kappa e risco da rodada 2 | Larissa Gomes | - |
