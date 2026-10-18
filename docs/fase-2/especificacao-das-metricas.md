# Especificação das métricas

Cada métrica possui uma ficha com os campos exigidos pela Premissa 2: **definição, procedimento de cálculo, fonte dos dados, procedimento de coleta e critérios de interpretação**.

## Resumo

| ID | Métrica | Questão | Característica | Fonte dos dados |
|----|---------|---------|----------------|-----------------|
| M1.1.1 | _-_ | Q1.1 | C1 | _-_ |
| M1.2.1 | _-_ | Q1.2 | C1 | _-_ |
| M2.1.1 | Consistência operacional (UOp-1-G) | Q2.1 | C2 | Inspeção das telas |
| M2.1.2 | Clareza das mensagens (UOp-2-G) | Q2.1 | C2 | Inspeção das telas e do código |
| M2.2.1 | Prevenção de erro de operação (UEp-1-G) | Q2.2 | C2 | Inspeção das telas e do código |
| M2.2.2 | Correção de erro de entrada (UEp-2-S) | Q2.2 | C2 | Inspeção dos formulários |
| M2.2.3 | Recuperabilidade de erro do usuário (UEp-3-S) | Q2.2 | C2 | Inspeção das telas |
| M2.3.1 | Autodescrição dos pontos de entrada (UAp-3-S) | Q2.3 | C2 | Inspeção das páginas de entrada |
| M2.3.2 | Interface autoexplicativa (ULe-4-S) | Q2.3 | C2 | Testes de cenário com estudantes |
| M3.1.1 | _-_ | Q3.1 | C3 | _-_ |

## Fichas

### M1.1.1

| Campo | Definição |
|-------|-----------|
| Nome | _-_ |
| Questão / objetivo | Q1.1 / G1 |
| Definição | _o que a métrica representa_ |
| Procedimento de cálculo | _fórmula, ex.: X = A / B, onde A = ..., B = ..._ |
| Unidade e escala | _ex.: segundos, razão_ |
| Fonte dos dados | _ex.: sessões de teste com usuários, relatório do Lighthouse, inspeção_ |
| Procedimento de coleta | _passo a passo, ferramenta, ambiente, quem coleta, quando_ |
| Critério de interpretação | _quanto maior/menor, melhor; ver [níveis de pontuação](niveis-e-julgamento.md)_ |
| Local dos dados brutos | _ex.: `dados/avaliacao/M1.1.1/`_ |

### M1.2.1

| Campo | Definição |
|-------|-----------|
| Nome | _-_ |
| Questão / objetivo | Q1.2 / G1 |
| Definição | _-_ |
| Procedimento de cálculo | _-_ |
| Unidade e escala | _-_ |
| Fonte dos dados | _-_ |
| Procedimento de coleta | _-_ |
| Critério de interpretação | _-_ |
| Local dos dados brutos | _-_ |

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
