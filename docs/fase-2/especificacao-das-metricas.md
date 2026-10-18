# Especificação das métricas

Cada métrica possui uma ficha com os campos exigidos pela Premissa 2: **definição, procedimento de cálculo, fonte dos dados, procedimento de coleta e critérios de interpretação**.

## Resumo

| ID | Métrica | Questão | Característica | Fonte dos dados |
|----|---------|---------|----------------|-----------------|
| M1.1.1 | Recall@30 normalizado (adaptada de FCp-1-G) | Q1.1 | C1 | Lista de incluídos da revisão de referência; Top 30 da VICKY |
| M1.1.2 | Recall restrito às fontes (adaptada de FCp-1-G) | Q1.1 | C1 | Revisão de referência; consulta manual ao PubMed, SciELO e Google Acadêmico; Top 30 |
| M1.2.1 | Funções declaradas operantes (adaptada de FCp-1-G) | Q1.2 | C1 | Página pública da VICKY; um caso de teste por função |
| M1.3.1 | Precisão@30 (adaptada de FCr-1-G) | Q1.3 | C1 | Top 30 de cada tema; ficha de julgamento de dois avaliadores |
| M1.3.2 | Metadados e links corretos (adaptada de FCr-1-G) | Q1.3 | C1 | Amostra de 10 itens por tema; página oficial de cada artigo |
| M1.4.1 | Spearman entre Quality Score e rubrica (adaptada de FAp-1-G) | Q1.4 | C1 | Quality Score exibido; nota da rubrica de dois avaliadores |
| M1.5.1 | Conformidade com filtros (adaptada de FAp-1-G) | Q1.5 | C1 | Duas execuções com filtros restritivos; conferência item a item |
| M1.5.2 | Estabilidade entre execuções (adaptada de FAp-1-G) | Q1.5 | C1 | Dois Top 30 do mesmo tema, com intervalo de 24 horas ou mais |
| M2.1.1 | Consistência operacional (UOp-1-G) | Q2.1 | C2 | Inspeção das telas |
| M2.1.2 | Clareza das mensagens (UOp-2-G) | Q2.1 | C2 | Inspeção das telas e do código |
| M2.2.1 | Prevenção de erro de operação (UEp-1-G) | Q2.2 | C2 | Inspeção das telas e do código |
| M2.2.2 | Correção de erro de entrada (UEp-2-S) | Q2.2 | C2 | Inspeção dos formulários |
| M2.2.3 | Recuperabilidade de erro do usuário (UEp-3-S) | Q2.2 | C2 | Inspeção das telas |
| M2.3.1 | Autodescrição dos pontos de entrada (UAp-3-S) | Q2.3 | C2 | Inspeção das páginas de entrada |
| M2.3.2 | Interface autoexplicativa (ULe-4-S) | Q2.3 | C2 | Testes de cenário com estudantes |
| M3.1.1 | _-_ | Q3.1 | C3 | _-_ |

## Temas de teste de G1

As métricas de G1 usam quatro temas de teste (T1 a T4): um fármaco com desfecho clínico bem estudado, uma intervenção não farmacológica, um tema de saúde pública brasileira com literatura no SciELO e um tema estreito com poucos estudos. Cada tema tem uma revisão sistemática recente como referência, e a lista de estudos incluídos dessa revisão serve de padrão para M1.1.1 e M1.1.2. Os mesmos Top 30 alimentam M1.3.1, M1.3.2, M1.4.1 e M1.5.1. A coleta completa exige cerca de oito triagens na ferramenta (estimativa), cada uma consumindo 1 crédito.

## Fichas

### M1.1.1

| Campo | Definição |
|-------|-----------|
| Nome | Recall@30 normalizado |
| Medida da ISO/IEC 25023:2016 | FCp-1-G, *Functional coverage* (genérica), adaptada: conta estudos da revisão de referência recuperados, em vez de funções implementadas |
| Subcaracterística | Completude funcional |
| Questão / objetivo | Q1.1 / G1 |
| Definição | Proporção dos estudos incluídos na revisão de referência que aparecem no Top 30 da VICKY. O denominador é limitado a 30 para não penalizar a ferramenta quando a revisão de referência é maior que a lista. Métrica crítica de Q1.1. |
| Procedimento de cálculo | R = N(Top 30 ∩ Ref) / min(N(Ref), 30), onde Top 30 é o conjunto de artigos da lista ranqueada e Ref é o conjunto de estudos incluídos na revisão de referência. Mesmo artigo significa mesmo DOI. O valor final é a média de R em T1 a T4. |
| Unidade e escala | Razão adimensional, de 0 a 1 |
| Fonte dos dados | Lista de estudos incluídos de cada revisão de referência; Top 30 gerado pela VICKY para cada tema |
| Procedimento de coleta | (1) Escolher a revisão de referência de cada tema. (2) Executar a triagem completa na VICKY, em navegador de computador, com janela de busca até a data de corte da revisão. (3) Registrar o Top 30 em planilha. (4) Cruzar o Top 30 com a lista de incluídos por DOI e, na falta de DOI, por título e ano. (5) Calcular R por tema e a média. |
| Critério de interpretação | Quanto maior, melhor. Ver [níveis de pontuação](niveis-e-julgamento.md). |
| Local dos dados brutos | `dados/avaliacao/G1/M1.1.1/` |

### M1.1.2

| Campo | Definição |
|-------|-----------|
| Nome | Recall restrito às fontes |
| Medida da ISO/IEC 25023:2016 | FCp-1-G, *Functional coverage* (genérica), adaptada: conta estudos recuperados, restritos aos que as fontes indexam |
| Subcaracterística | Completude funcional |
| Questão / objetivo | Q1.1 / G1 |
| Definição | Mesma proporção de M1.1.1, calculada apenas sobre os estudos da revisão de referência que o PubMed, o SciELO ou o Google Acadêmico indexam. Separa falha de triagem da VICKY de limite das bases. |
| Procedimento de cálculo | Rr = N(Top 30 ∩ Ref indexada) / min(N(Ref indexada), 30), onde Ref indexada é o subconjunto de Ref presente em ao menos uma das três fontes. O valor final é a média de Rr em T1 a T4. |
| Unidade e escala | Razão adimensional, de 0 a 1 |
| Fonte dos dados | Lista de incluídos da revisão de referência; resultado da consulta manual às três fontes; Top 30 de M1.1.1 |
| Procedimento de coleta | (1) Consultar cada estudo da revisão de referência no PubMed, no SciELO e no Google Acadêmico e anotar se foi encontrado. (2) Montar Ref indexada com os estudos encontrados em ao menos uma fonte. (3) Cruzar com o Top 30 já registrado para M1.1.1. (4) Calcular Rr por tema e a média. |
| Critério de interpretação | Quanto maior, melhor. A diferença entre M1.1.2 e M1.1.1 mostra o que as bases não cobrem. Ver [níveis de pontuação](niveis-e-julgamento.md). |
| Local dos dados brutos | `dados/avaliacao/G1/M1.1.2/` |

### M1.2.1

| Campo | Definição |
|-------|-----------|
| Nome | Funções declaradas operantes |
| Medida da ISO/IEC 25023:2016 | FCp-1-G, *Functional coverage* (genérica), adaptada: função parcial conta meia |
| Subcaracterística | Completude funcional |
| Questão / objetivo | Q1.2 / G1 |
| Definição | Proporção das funções anunciadas pela VICKY que existem e executam o que prometem. Detecta promessa não cumprida. São 9 funções, F01 a F09 (ver [objeto de avaliação](../fase-1/objeto-de-avaliacao.md#3-principais-funcionalidades)); a inclusão de F05 é proposta pendente de aprovação do grupo. |
| Procedimento de cálculo | C = (operantes + 0,5 x parciais) / declaradas, com declaradas = 9. Operante é a função que executa o fluxo previsto até o fim; parcial, a que executa só parte dele; ausente, a que não existe ou não executa (definição proposta, a validar pelo grupo). |
| Unidade e escala | Proporção, de 0% a 100% |
| Fonte dos dados | Página pública da VICKY e capturas de tela de um caso de teste por função |
| Procedimento de coleta | (1) Listar as funções anunciadas na página pública. (2) Definir um caso de teste por função. (3) Executar cada caso com uma conta de teste, em navegador de computador, e capturar a tela. (4) Classificar cada função como operante, parcial ou ausente. (5) Calcular C. |
| Critério de interpretação | Quanto maior, melhor. Ver [níveis de pontuação](niveis-e-julgamento.md). |
| Local dos dados brutos | `dados/avaliacao/G1/M1.2.1/` |

### M1.3.1

| Campo | Definição |
|-------|-----------|
| Nome | Precisão@30 |
| Medida da ISO/IEC 25023:2016 | FCr-1-G, *Functional correctness* (genérica), adaptada: julga cada artigo da lista, em vez de cada função |
| Subcaracterística | Correção funcional |
| Questão / objetivo | Q1.3 / G1 |
| Definição | Proporção dos 30 artigos da lista julgados relevantes ao PICO. Um artigo é relevante quando corresponde à população, à intervenção e ao desfecho do PICO e ao tipo de estudo pedido. Métrica crítica de Q1.3. |
| Procedimento de cálculo | P = relevantes / avaliados, sobre os 30 artigos de cada tema. O valor final é a média de P em T1 a T4. O kappa de Cohen entre os dois avaliadores é calculado para cada tema. |
| Unidade e escala | Proporção, de 0% a 100% |
| Fonte dos dados | Top 30 de cada tema; ficha de julgamento preenchida por dois avaliadores |
| Procedimento de coleta | (1) Entregar aos avaliadores título e resumo de cada artigo, sem posição nem Quality Score. (2) Cada avaliador julga a relevância ao PICO do tema e preenche a ficha. (3) Calcular o kappa de Cohen entre os dois. (4) Resolver as discordâncias [PREENCHER FASE 3: regra para discordâncias] e calcular P. |
| Critério de interpretação | Quanto maior, melhor. O resultado só vale com kappa de 0,61 ou mais, faixa de concordância substancial (Landis; Koch, 1977). Ver [níveis de pontuação](niveis-e-julgamento.md). |
| Local dos dados brutos | `dados/avaliacao/G1/M1.3.1/` |

### M1.3.2

| Campo | Definição |
|-------|-----------|
| Nome | Metadados e links corretos |
| Medida da ISO/IEC 25023:2016 | FCr-1-G, *Functional correctness* (genérica), adaptada: confere metadados e link de cada artigo, em vez de cada função |
| Subcaracterística | Correção funcional |
| Questão / objetivo | Q1.3 / G1 |
| Definição | Proporção dos itens verificados cujo título, autores, ano, periódico e link estão corretos. Um campo errado torna o item incorreto, porque quebra a citação. |
| Procedimento de cálculo | K = corretos / verificados, sobre uma amostra de 10 itens do Top 30 por tema (40 itens no total). |
| Unidade e escala | Proporção, de 0% a 100% |
| Fonte dos dados | Itens da amostra no Top 30; página oficial de cada artigo |
| Procedimento de coleta | (1) Selecionar 10 itens por tema [PREENCHER FASE 3: critério de seleção da amostra]. (2) Abrir o link exibido pela VICKY e a página oficial do artigo. (3) Comparar título, autores, ano, periódico e link. (4) Marcar o item como correto só se os cinco campos coincidirem. (5) Calcular K. |
| Critério de interpretação | Quanto maior, melhor. Ver [níveis de pontuação](niveis-e-julgamento.md). |
| Local dos dados brutos | `dados/avaliacao/G1/M1.3.2/` |

### M1.4.1

| Campo | Definição |
|-------|-----------|
| Nome | Spearman entre Quality Score e rubrica |
| Medida da ISO/IEC 25023:2016 | FAp-1-G, *Functional appropriateness of usage objective* (genérica), adaptada: verifica se a ordem do ranking serve ao objetivo do estudante |
| Subcaracterística | Pertinência funcional |
| Questão / objetivo | Q1.4 / G1 |
| Definição | Concordância entre a ordem de 0 a 100 do Quality Score e a ordem de uma rubrica metodológica. Como a documentação pública não descreve o cálculo do Quality Score (a confirmar no código-fonte), a métrica indica concordância com a rubrica adotada, não a validade do escore. |
| Procedimento de cálculo | ρ de Spearman entre o Quality Score e a nota da rubrica nos 30 artigos. A rubrica atribui a cada artigo uma nota de 0 a 10 a partir do nível de evidência do desenho, do tamanho da amostra, da presença de comparador e da revisão por pares; a nota final é a média dos dois avaliadores. O valor final é a média de ρ em T1 e T2. |
| Unidade e escala | Coeficiente adimensional, de -1 a 1 |
| Fonte dos dados | Quality Score exibido na lista; notas da rubrica de dois avaliadores |
| Procedimento de coleta | (1) Registrar o Quality Score de cada artigo do Top 30 de T1 e T2. (2) Dois avaliadores atribuem a nota da rubrica sem ver o escore. (3) Calcular a média das duas notas por artigo. (4) Calcular ρ por tema e a média. |
| Critério de interpretação | Quanto maior, melhor. Com 30 itens, ρ de cerca de 0,36 é o valor crítico para se distinguir de zero a 5% de significância, em teste bilateral (Zar, 1972). Ver [níveis de pontuação](niveis-e-julgamento.md). |
| Local dos dados brutos | `dados/avaliacao/G1/M1.4.1/` |

### M1.5.1

| Campo | Definição |
|-------|-----------|
| Nome | Conformidade com filtros |
| Medida da ISO/IEC 25023:2016 | FAp-1-G, *Functional appropriateness of usage objective* (genérica), adaptada: verifica se o resultado obedece à configuração do estudante |
| Subcaracterística | Pertinência funcional |
| Questão / objetivo | Q1.5 / G1 |
| Definição | Proporção dos itens da lista que obedecem aos filtros configurados pelo estudante: janela de tempo, tipo de estudo e fonte. Item fora do filtro é defeito, pois filtro é regra objetiva. |
| Procedimento de cálculo | F = conformes / avaliados, sobre todos os itens das listas geradas nas duas execuções com filtros restritivos. |
| Unidade e escala | Proporção, de 0% a 100% |
| Fonte dos dados | Listas geradas com filtros restritivos; metadados de cada item |
| Procedimento de coleta | (1) Configurar duas execuções com filtros restritivos de janela de tempo, tipo de estudo e fonte. (2) Registrar a configuração usada. (3) Conferir item a item se ano, tipo de estudo e fonte respeitam a configuração. (4) Calcular F. |
| Critério de interpretação | Quanto maior, melhor. Ver [níveis de pontuação](niveis-e-julgamento.md). |
| Local dos dados brutos | `dados/avaliacao/G1/M1.5.1/` |

### M1.5.2

| Campo | Definição |
|-------|-----------|
| Nome | Estabilidade entre execuções |
| Medida da ISO/IEC 25023:2016 | FAp-1-G, *Functional appropriateness of usage objective* (genérica), adaptada: verifica se o resultado se repete, o que permite registrar e replicar a busca |
| Subcaracterística | Pertinência funcional |
| Questão / objetivo | Q1.5 / G1 |
| Definição | Sobreposição entre os Top 30 de duas execuções idênticas do mesmo tema. Mede se o registro da busca permite replicar a revisão. |
| Procedimento de cálculo | J = N(A ∩ B) / N(A ∪ B) (índice de Jaccard), onde A e B são os Top 30 das duas execuções, comparados por DOI. O valor final é a média de J nos temas repetidos. |
| Unidade e escala | Razão adimensional, de 0 a 1 |
| Fonte dos dados | Dois Top 30 do mesmo tema, com a mesma configuração |
| Procedimento de coleta | (1) Executar a triagem completa de um tema e registrar o Top 30 (A). (2) Esperar ao menos 24 horas. (3) Repetir a execução com a mesma configuração e registrar o Top 30 (B). (4) Cruzar A e B por DOI e calcular J. |
| Critério de interpretação | Quanto maior, melhor. Valor abaixo de 1,00 é esperado, porque a triagem depende de modelo de linguagem e pode variar entre execuções. Ver [níveis de pontuação](niveis-e-julgamento.md). |
| Local dos dados brutos | `dados/avaliacao/G1/M1.5.2/` |

### M2.1.1

| Campo | Definição |
|-------|-----------|
| Nome | Consistência operacional |
| Medida da ISO/IEC 25023:2016 | UOp-1-G, *Operational consistency* (genérica) |
| Subcaracterística | Operabilidade |
| Questão / objetivo | Q2.1 / G2 |
| Definição | Quanto os padrões de interação que se repetem no VICKY são executados da mesma forma em todas as telas do escopo onde aparecem |
| Procedimento de cálculo | X = 1 - A / B, onde A = padrões de interação executados de forma inconsistente e B = padrões de interação que precisam ser consistentes. Lista inicial de B (10): acionar a ação principal, confirmar ação irreversível, exibir erro, exibir sucesso, exibir lista vazia, indicar o campo em foco, navegar pelo menu, acompanhar processo longo, preencher formulário, sair da conta. A equipe expressa a medida como 1 - A / B para que, como nas demais medidas do G2, valor maior signifique melhor; a cláusula 2, alínea d, da norma permite modificar uma medida desde que a mudança seja justificada |
| Unidade e escala | De 0 a 1; 1 significa nenhuma inconsistência |
| Fonte dos dados | Telas do VICKY em produção e templates do código-fonte |
| Procedimento de coleta | Para cada padrão, o avaliador registra como ele aparece em cada tela do escopo (captura de tela). Um padrão é inconsistente quando duas ou mais telas o resolvem de forma visual ou comportamental diferente, como um estado vazio com ícone e cor diferentes ou uma confirmação ora em janela própria, ora na caixa nativa do navegador. Dois avaliadores fazem a contagem de forma independente, pelo menos um deles sem ter lido o código; as divergências são resolvidas em conjunto e registradas |
| Critério de interpretação | Quanto maior, melhor; ver [níveis de pontuação](niveis-e-julgamento.md) |
| Local dos dados brutos | `dados/avaliacao/M2.1.1/` |

### M2.1.2

| Campo | Definição |
|-------|-----------|
| Nome | Clareza das mensagens |
| Medida da ISO/IEC 25023:2016 | UOp-2-G, *Message clarity* (genérica) |
| Subcaracterística | Operabilidade |
| Questão / objetivo | Q2.1 / G2 |
| Definição | Proporção das mensagens do sistema (erro, sucesso, aviso e andamento) que comunicam ao estudante o resultado certo ou a instrução certa |
| Procedimento de cálculo | X = A / B, onde A = mensagens que comunicam o resultado ou a instrução de forma correta e compreensível para o estudante e B = mensagens do fluxo do escopo |
| Unidade e escala | Razão de 0 a 1, apresentada em % |
| Fonte dos dados | Inventário das mensagens no código-fonte (fork do VICKY) e disparo das mensagens em produção |
| Procedimento de coleta | 1) Listar no código todas as mensagens das rotas do escopo. 2) Disparar em produção as que podem ser provocadas sem gastar crédito, com um roteiro fixo de entradas inválidas (campo vazio, e-mail inválido, senha curta, senhas diferentes, e-mail já cadastrado, senha errada, tema vazio, limite de pré-visualizações) e guardar a captura de tela. 3) Classificar cada mensagem: é clara quando diz o que aconteceu em linguagem do estudante. Mensagem com texto técnico cru do servidor, ou que não diz o resultado, conta como não clara. Dois avaliadores fazem a contagem de forma independente, pelo menos um deles sem ter lido o código; as divergências são resolvidas em conjunto e registradas |
| Critério de interpretação | Quanto maior, melhor; ver [níveis de pontuação](niveis-e-julgamento.md) |
| Local dos dados brutos | `dados/avaliacao/M2.1.2/` |

### M2.2.1

| Campo | Definição |
|-------|-----------|
| Nome | Prevenção de erro de operação |
| Medida da ISO/IEC 25023:2016 | UEp-1-G, *Avoidance of user operation error* (genérica) |
| Subcaracterística | Proteção contra erro do usuário |
| Questão / objetivo | Q2.2 / G2 |
| Definição | Proporção das ações e entradas do estudante que poderiam causar perda de crédito, de trabalho ou de configuração e que estão protegidas contra o engano |
| Procedimento de cálculo | X = A / B, onde A = ações e entradas protegidas (confirmação antes de executar, aviso explícito do efeito ou bloqueio de entrada inválida) e B = ações e entradas que poderiam ser protegidas. Lista inicial de B: iniciar a triagem completa (consome 1 crédito), excluir projeto, parar a triagem em andamento, definir a quantidade do Top (não pode ser alterada depois), ativar o filtro de acesso aberto, gerar pré-visualização (consome a cota diária) |
| Unidade e escala | Razão de 0 a 1, apresentada em % |
| Fonte dos dados | Telas do VICKY em produção e código-fonte |
| Procedimento de coleta | O avaliador verifica a proteção de cada item pela tela e confirma no código. Na ação de iniciar a triagem completa, verifica-se só o que acontece antes do clique final, sem consumir crédito. Dois avaliadores fazem a contagem de forma independente, pelo menos um deles sem ter lido o código; as divergências são resolvidas em conjunto e registradas |
| Critério de interpretação | Quanto maior, melhor; ação que consome crédito sem proteção tem regra própria nos níveis; ver [níveis de pontuação](niveis-e-julgamento.md) |
| Local dos dados brutos | `dados/avaliacao/M2.2.1/` |

### M2.2.2

| Campo | Definição |
|-------|-----------|
| Nome | Correção de erro de entrada |
| Medida da ISO/IEC 25023:2016 | UEp-2-S, *User entry error correction* (específica) |
| Subcaracterística | Proteção contra erro do usuário |
| Questão / objetivo | Q2.2 / G2 |
| Definição | Proporção dos erros de entrada detectados pelo VICKY para os quais ele sugere ao estudante o valor correto, em vez de só recusar ou corrigir em silêncio |
| Procedimento de cálculo | X = A / B, onde A = erros de entrada para os quais o sistema sugere o valor correto e B = erros de entrada que o sistema detecta |
| Unidade e escala | Razão de 0 a 1, apresentada em % |
| Fonte dos dados | Formulários de cadastro, login, recuperação de senha e criação de projeto, em produção |
| Procedimento de coleta | O avaliador aplica um roteiro fixo de entradas inválidas nos formulários do escopo (e-mail sem domínio, senha curta, senhas diferentes, tema vazio, quantidade do Top fora de 1 a 30) e registra, para cada uma, se o sistema detectou o erro e se sugeriu o valor correto. Correção silenciosa, em que o sistema troca o valor sem avisar, conta como detectada e não sugerida. Dois avaliadores fazem a contagem de forma independente, pelo menos um deles sem ter lido o código; as divergências são resolvidas em conjunto e registradas |
| Critério de interpretação | Quanto maior, melhor; ver [níveis de pontuação](niveis-e-julgamento.md) |
| Local dos dados brutos | `dados/avaliacao/M2.2.2/` |

### M2.2.3

| Campo | Definição |
|-------|-----------|
| Nome | Recuperabilidade de erro do usuário |
| Medida da ISO/IEC 25023:2016 | UEp-3-S, *User error recoverability* (específica) |
| Subcaracterística | Proteção contra erro do usuário |
| Questão / objetivo | Q2.2 / G2 |
| Definição | Proporção dos erros que o estudante pode cometer no fluxo do escopo e que o VICKY permite desfazer ou corrigir depois, sem recomeçar nem pagar de novo |
| Procedimento de cálculo | X = A / B, onde A = erros do usuário que podem ser desfeitos ou corrigidos depois e B = erros do usuário que podem ocorrer no fluxo. Lista inicial de B: tema digitado errado, quantidade do Top errada, bases escolhidas erradas, filtro de acesso aberto ativado sem querer, projeto excluído por engano, triagem parada por engano, favorito marcado errado, senha esquecida |
| Unidade e escala | Razão de 0 a 1, apresentada em % |
| Fonte dos dados | Telas do VICKY em produção |
| Procedimento de coleta | Para cada erro da lista, o avaliador tenta corrigi-lo pela interface, sem gastar crédito, e registra se conseguiu e como. Dois avaliadores fazem a contagem de forma independente, pelo menos um deles sem ter lido o código; as divergências são resolvidas em conjunto e registradas |
| Critério de interpretação | Quanto maior, melhor; ver [níveis de pontuação](niveis-e-julgamento.md) |
| Local dos dados brutos | `dados/avaliacao/M2.2.3/` |

### M2.3.1

| Campo | Definição |
|-------|-----------|
| Nome | Autodescrição dos pontos de entrada |
| Medida da ISO/IEC 25023:2016 | UAp-3-S, *Entry point self-descriptiveness* (específica) |
| Subcaracterística | Autodescritividade |
| Questão / objetivo | Q2.3 / G2 |
| Definição | Proporção das páginas por onde o estudante entra no VICKY que explicam, na primeira tela visível, para que o produto serve |
| Procedimento de cálculo | X = A / B, onde A = páginas de entrada que explicam o propósito do produto e B = páginas de entrada: página inicial (`/`), cadastro (`/signup`), login (`/login`) e painel após o login (`/dashboard`) |
| Unidade e escala | Razão de 0 a 1, apresentada em % |
| Fonte dos dados | Páginas de entrada do VICKY em produção, em navegador desktop |
| Procedimento de coleta | O avaliador abre cada página e registra, com captura de tela, se a primeira tela visível, sem rolar, diz o que o VICKY faz: buscar e triar artigos científicos sobre um tema. Dois avaliadores fazem a contagem de forma independente, pelo menos um deles sem ter lido o código; as divergências são resolvidas em conjunto e registradas |
| Critério de interpretação | Quanto maior, melhor; ver [níveis de pontuação](niveis-e-julgamento.md) |
| Local dos dados brutos | `dados/avaliacao/M2.3.1/` |

### M2.3.2

| Campo | Definição |
|-------|-----------|
| Nome | Interface autoexplicativa |
| Medida da ISO/IEC 25023:2016 | ULe-4-S, *Self-explanatory user interface* (específica) |
| Subcaracterística | Autodescritividade |
| Questão / objetivo | Q2.3 / G2 |
| Definição | Proporção dos elementos de informação e dos passos do fluxo que um estudante, no primeiro uso, entende e usa corretamente sem estudo prévio, treinamento ou ajuda |
| Procedimento de cálculo | X = A / B, onde A = elementos e passos entendidos sem ajuda pela maioria dos participantes (pelo menos 3 de 5) e B = elementos e passos necessários para um usuário de primeira vez concluir as tarefas comuns. Lista inicial de B (12): campo do tema, campo de objetivo, tipo de revisão (sistemática ou narrativa), janela de anos, quantidade do Top, escolha das bases, filtro de acesso aberto, diferença entre salvar rascunho, gerar prévia e iniciar a triagem, critérios PICO gerados, Quality Score, log auditável e exportação |
| Unidade e escala | Razão de 0 a 1, apresentada em % |
| Fonte dos dados | Testes de cenário com estudantes de medicina e questionário de compreensão, conforme a profundidade definida em [Escopo e profundidade](../fase-1/escopo.md) |
| Procedimento de coleta | Cinco estudantes de medicina que nunca usaram o VICKY executam, em desktop, dois cenários: criar um projeto e gerar o PICO para um tema dado (F01 a F04), e abrir um projeto já triado, interpretar a lista, favoritar artigos, abrir o log e exportar (F06 a F09). O participante pensa em voz alta e a tela é gravada, com termo de consentimento e identificação anonimizada (P01 a P05). Ao fim, um questionário curto pede que ele explique com as próprias palavras cada elemento da lista B; a resposta é comparada com a definição do elemento no VICKY. Um elemento conta como entendido para o participante se ele o usou sem pedir ajuda e o explicou corretamente |
| Critério de interpretação | Quanto maior, melhor; o Quality Score tem regra própria nos níveis; ver [níveis de pontuação](niveis-e-julgamento.md) |
| Local dos dados brutos | `dados/avaliacao/M2.3.2/` |

_Copiar a ficha para cada métrica restante._

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 05/10/2026 | Criação da estrutura do documento | Gabriel Fae | - |
| 0.2 | 16/10/2026 | Reorganização da documentação por fases do processo de avaliação | Gabriel Fae | - |
| 0.3 | 18/10/2026 | Fichas das métricas do G2 (capacidade de interação), pela ISO/IEC 25023 | Lucas Avelar | Gabriel Fae |
| 0.4 | 18/10/2026 | Resumo e fichas das oito métricas do objetivo G1 (M1.1.1 a M1.5.2) | Larissa Gomes Silva | - |
