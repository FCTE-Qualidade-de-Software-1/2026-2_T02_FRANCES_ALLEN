# Método do G2 com usuários (capacidade de interação)

Este método cobre as quatro métricas do G2 que não saem só da inspeção: duas medidas com estudantes de Medicina (M2.5.1 e M2.7.2) e duas de acessibilidade, executadas pelos avaliadores (M2.6.1 e M2.6.2). Definição, fórmula e níveis são os da [Fase 2](../fase-2/especificacao-das-metricas.md); esta página diz como executar a coleta. As oito métricas de inspeção estão no [Método do G2 por inspeção](metodo-g2-inspecao.md), e esta página reaproveita dele o ambiente (seção 2.2), a organização das pastas e a regra de discordância, sem repeti-los.

Os instrumentos aplicados aos participantes (cartões de tarefa, ficha de observação, questionário de compreensão com gabarito e questionário de estética) estão em [Instrumentos do G2 com usuários](instrumentos-g2-usuarios.md). O termo assinado antes de cada sessão está em [Termo de consentimento](termo-de-consentimento.md).

## 1. Métricas cobertas

| Métrica | Medida | Quem fornece o dado | Instrumento | Denominador (B) | Pasta em `dados/avaliacao/G2/` |
|---------|--------|---------------------|-------------|-----------------|--------------------------------|
| [M2.5.1](../fase-2/especificacao-das-metricas.md#m251) | UIn-1-S | Participantes P01 a P05 | Questionário de estética das 5 telas | 5 telas | `M2.5.1/` |
| [M2.6.1](../fase-2/especificacao-das-metricas.md#m261) | UAc-1-G | Avaliadores T1 e T2 | Teste só com teclado, por função | 9 funções (F01 a F09) | `M2.6.1/` |
| [M2.6.2](../fase-2/especificacao-das-metricas.md#m262) | Medida adicional | Avaliadores A1 e A2 | axe DevTools e conferência manual | Pares de texto e fundo avaliados nas 8 telas | `M2.6.2/` |
| [M2.7.2](../fase-2/especificacao-das-metricas.md#m272) | ULe-4-S | Participantes P01 a P05 | Teste de cenário com pensamento em voz alta e questionário de compreensão | 12 elementos e passos | `M2.7.2/` |

M2.5.1 e M2.7.2 saem da mesma sessão com o participante. M2.6.1 e M2.6.2 não usam participantes e podem correr em paralelo às sessões.

## 2. Por que este método

### 2.1 Participantes reais para M2.5.1 e M2.7.2

As duas medidas perguntam o que o **estudante** percebe, e não o que a equipe percebe. A nota 3 da UIn-1-S, na ISO/IEC 25023:2016, recomenda que a estética seja medida com representantes do público-alvo; a Fase 2 adotou essa nota na ficha de M2.5.1. A ULe-4-S mede o que o usuário entende "sem estudo prévio, treinamento ou ajuda" ([ficha de M2.7.2](../fase-2/especificacao-das-metricas.md#m272)). A equipe não serve como fonte desse dado: todos já leram as telas, e parte leu o código, o que a própria [abstraction sheet do G2](../fase-2/objetivos-questoes-hipoteses.md) aponta como fator que faz a interface parecer mais clara do que é. Por isso os participantes são estudantes de Medicina, o público declarado do VICKY na [Fase 1](../fase-1/objeto-de-avaliacao.md#1-identificacao), que nunca usaram o produto.

### 2.2 Uso observado e explicação, os dois juntos

A Fase 2 exige, para M2.7.2, que o elemento tenha sido **usado** sem ajuda **e explicado** corretamente. Cada metade cobre uma falha da outra: o participante pode acertar o uso por tentativa e erro sem entender o elemento, ou explicar bem um rótulo que não soube usar. Por isso a sessão tem duas partes. Na primeira, o participante executa tarefas dadas em linguagem de estudante, sem o nome dos controles, e pensa em voz alta enquanto o observador registra o uso de cada elemento. Na segunda, responde ao questionário de compreensão, e a resposta é comparada a um gabarito escrito antes da primeira sessão. Pensar em voz alta expõe o raciocínio no momento do uso, que a gravação preserva para a conferência posterior.

### 2.3 Estética logo depois do uso real

M2.5.1 é aplicada no fim da mesma sessão, como pede a ficha. O participante julga cada tela depois de tê-la usado numa tarefa com propósito, e não só olhando uma imagem. A nota é pedida tela por tela, sobre a captura fixa da tela, para que os cinco participantes julguem exatamente o mesmo objeto.

### 2.4 Uma sessão por participante, sem repetição

Um participante só é "de primeira vez" uma vez. Se a sessão falhar depois que ele viu o VICKY, ele não pode repetir, e o método prevê reservas em vez de nova sessão (seção 7). Pela mesma razão, a sessão piloto não usa estudante elegível.

### 2.5 Acessibilidade pelos avaliadores, com regra objetiva

M2.6.1 simula o perfil motor, como declara a Fase 2: não há participante com deficiência motora. Para que dois avaliadores cheguem ao mesmo resultado, o sucesso de uma função foi decomposto em três condições verificáveis (WCAG 2.2, critérios 2.1.1, 2.4.7 e 2.5.8). M2.6.2 usa o axe DevTools, ferramenta definida na Fase 2, para os pares que a ferramenta decide sozinha, e conferência manual para os que ela marca como incertos (texto sobre imagem ou degradê), seguindo o critério 1.4.3 da WCAG 2.2.

### 2.6 Ligação com a ISO/IEC 25040

Na ISO/IEC 25040:2024, projetar a avaliação inclui definir os métodos de medição, os recursos e as condições em que cada medida é obtida, antes da execução. Esta página fixa essas condições para as quatro métricas: quem participa, com qual conta, em qual ordem, com qual instrumento e com qual regra de cálculo, de modo que outra pessoa da equipe consiga repetir a coleta e chegar ao mesmo dado.

### 2.7 Coerência com a Fase 2

| Métrica | O que a Fase 2 fixa | Como este método cumpre |
|---------|---------------------|-------------------------|
| M2.5.1 | A = telas agradáveis para pelo menos 3 de 5; notas 4 e 5 contam; B = 5 telas; piso de Bom 60%; fora da contagem do G2 | Questionário com as mesmas 5 telas e a mesma escala; regra de 3 de 5 aplicada sem ajuste (seção 6) |
| M2.6.1 | A = funções concluídas só com teclado, foco visível e alvos de 24 por 24 pixels; B = F01 a F09; piso de Bom 88%; F01 não concluída leva a Insatisfatório | Três condições por função, verificadas em cada passo do caminho da função; F05 observada numa triagem do G1 |
| M2.6.2 | A = pares com 4,5:1 (ou 3:1 para texto grande); B = pares avaliados; 8 telas; dois avaliadores; piso de Bom 95% | axe com versão registrada, as 8 telas da ficha, conferência manual dos incertos, dois avaliadores independentes |
| M2.7.2 | A = elementos entendidos por pelo menos 3 de 5; entendido = usado sem ajuda **e** explicado corretamente; B = 12 elementos; piso de Bom 75%; Quality Score não entendido leva a Insatisfatório | Cartões de tarefa que fazem o participante passar pelos 12 elementos; ficha de uso e questionário com gabarito; regra do Quality Score verificada à parte |

## 3. Preparação

### 3.1 Recrutamento e critérios de inclusão

| Item | Definição |
|------|-----------|
| Quantos | 5 participantes válidos (P01 a P05), mais 2 reservas convidados desde o início |
| Onde | Estudantes de Medicina da UnB (Faculdade de Medicina, campus Darcy Ribeiro), por contatos pessoais da equipe, ligas acadêmicas e centro acadêmico. Estudantes de Medicina de outras instituições do DF também são elegíveis |
| Convite | Mensagem curta com o objetivo, a duração (cerca de 1 hora e 15 minutos), a gravação de tela e voz sem rosto e a ausência de remuneração. O termo completo é lido na sessão |
| Inclusão | 18 anos ou mais (os Termos do VICKY restringem o uso a maiores de 18); matrícula ativa em Medicina; nunca ter usado o VICKY; aceitar o termo, inclusive a gravação |
| Exclusão | Já ter acessado o VICKY, inclusive a página pública; ter vínculo com a Synaptha ou com a equipe de desenvolvimento do VICKY; ter visto as telas por colega da equipe; ser integrante desta equipe |
| Pergunta de triagem | "Você já entrou no site do VICKY ou viu alguém usando?" Resposta sim exclui. Feita no convite e repetida no início da sessão |
| Perfil registrado | Faixa do curso (1º ao 4º semestre, 5º ao 8º, internato), se já fez revisão sistemática ou de literatura e se já usou ferramenta de triagem. Esses dados não entram no cálculo; servem para interpretar o resultado na Fase 4, como prevê a abstraction sheet |

Não se exige conhecimento de metodologia científica: a promessa do VICKY, registrada na Fase 1, é que o estudante não precisa saber montar um PICO.

### 3.2 Papéis

| Papel | Quem | Responsabilidade | Não pode |
|-------|------|------------------|----------|
| Condutor (C) | João Felipe Oliveira, responsável pela issue #22; na ausência dele, outro integrante que tenha feito o piloto | Lê o termo, entrega os cartões, faz os lembretes neutros, aplica os questionários e decide quando dar ajuda mínima | Explicar a interface, ler rótulos em voz alta, apontar a tela antes do limite de 3 minutos |
| Observador (O) | Um integrante escalado por sessão, registrado em `sessoes.csv` | Preenche a ficha de uso de cada elemento com o momento da gravação, cuida da gravação e anota ocorrências | Falar com o participante durante as tarefas |
| Terceiro (A3) | Integrante que não esteve na sessão | Decide divergências de classificação que C e O não resolverem, olhando só a gravação e o gabarito | Ver a ficha de C ou de O antes de decidir |
| Avaliadores de teclado (T1, T2) | Dois integrantes | Executam M2.6.1 de forma independente | Consultar a ficha do outro antes de enviar a sua |
| Avaliadores de contraste (A1, A2) | Dois integrantes, pelo menos um sem ter lido o código | Executam M2.6.2 de forma independente | Idem |

A relação entre os códigos (C, O, T1, T2, A1, A2, A3) e as pessoas fica em `coleta.md` de cada pasta, sem dado do participante.

**Conhecimento exigido dos condutores e avaliadores.** C e O leem esta página e os instrumentos, fazem a sessão piloto juntos e conhecem o gabarito antes da primeira sessão. T1 e T2 sabem navegar por teclado no Chrome e conhecem os critérios 2.1.1, 2.4.7 e 2.5.8 da WCAG 2.2. A1 e A2 sabem rodar o axe, usar o seletor de cor do DevTools e conhecem o critério 1.4.3 da WCAG 2.2.

### 3.3 Tema dado ao participante

O participante cria o projeto sobre o **tema T1 do G1** (fármaco com desfecho clínico bem estudado, definido no [Método do G1](metodo-g1.md)). Na parte B ele abre o projeto já triado desse mesmo tema. Assim as duas partes contam uma história só (o estudante prepara a busca e depois recebe o resultado), e a parte B não exige nenhuma triagem além das que o G1 já faz.

O tema vai no cartão da parte A escrito em uma frase, em linguagem de estudante, igual para os cinco participantes, e o cartão também traz os requisitos que obrigam o uso dos 12 elementos (janela de anos, quantidade, bases, acesso aberto). O texto final do cartão é fixado em `M2.7.2/coleta.md` antes do piloto e não muda entre participantes. Se o T1 não estiver triado até a véspera da P01, usa-se o projeto triado mais antigo do G1, com o tema dele no cartão, e a troca é registrada em `coleta.md`.

### 3.4 Contas e créditos por parte da sessão

| Parte da sessão | Conta | Créditos | Cuidado |
|-----------------|-------|:--------:|---------|
| Parte A (F01 a F04) | Conta nova, criada pelo próprio participante durante a sessão, com nome "Participante P0x", e-mail de teste da equipe com sufixo do participante (ex.: `caixa+p01@...`) e senha entregue no cartão | 0 | Nenhum dado pessoal do participante entra no VICKY. No código consultado (`c2ae570`), conta nova começa sem crédito, então "Criar e iniciar tudo direto" não gasta dinheiro mesmo se clicado por engano; isso é conferido em produção antes do piloto |
| Parte B (F06 a F09) | Conta de cortesia da equipe, já logada pelo condutor antes de o participante sentar, aberta na lista de projetos | 0 consumidos | O projeto triado do G1 só é usado depois que o Top 30 e o log desse projeto foram exportados e guardados em `dados/avaliacao/G1/`. O condutor impede a exclusão do projeto se o participante tentar (registrado como ocorrência). Ao fim de cada sessão, o condutor desmarca os favoritos feitos pelo participante, para a próxima sessão começar do mesmo estado |
| M2.6.1 | Conta nova criada pelo próprio T1 (e por T2) no teste de F01, usada para F02 a F04; conta de cortesia para F06 a F09 | 0 | F05 é observada numa triagem já prevista no G1 |
| M2.6.2 | Janela anônima nas telas públicas; conta de cortesia nas internas | 0 | Nenhuma |

As sessões não consomem crédito. A dependência é um projeto triado do G1, como já previsto no [índice da Fase 3](index.md#cobertura-das-metricas).

A caixa de e-mail de teste é criada pela equipe antes do piloto; a senha dela e as senhas das contas ficam fora do repositório. Se a produção exigir confirmação de e-mail para gerar a prévia (o código consultado tem essa opção), o observador confirma o e-mail pela caixa de teste durante a sessão, e o tempo gasto é anotado como ocorrência, sem contar como ajuda.

### 3.5 Limite de prévias por conta e por IP (risco a checar)

No código consultado pela equipe (`c2ae570`), a prévia dos critérios tem limite de 20 por conta e 60 por origem (IP) em 24 horas. A sessão usa de 1 a 3 prévias, e o teste de teclado mais 1 ou 2 por avaliador, o que fica longe do limite por conta. O risco está no limite por IP:

- a etapa E08 da [inspeção](metodo-g2-inspecao.md#m222-e-m232-inventarios-de-mensagens) esgota de propósito a cota de uma conta e, se feita na mesma rede, consome cerca de 20 prévias da origem;
- redes da universidade costumam sair para a internet por poucos IPs compartilhados.

Por isso: (1) antes do piloto, o condutor confere em produção o limite vigente e anota em `M2.7.2/coleta.md`; (2) as sessões usam a rede do celular do condutor (roteamento), e não a rede da universidade; (3) a E08 da inspeção não é feita no mesmo dia nem na mesma rede de uma sessão; (4) no máximo três sessões por dia.

### 3.6 Termo, gravação e anonimização

| Item | Regra |
|------|-------|
| Termo | [Termo de consentimento](termo-de-consentimento.md), impresso em duas vias (`dados/avaliacao/G2/termo-de-consentimento.docx`). Lido com o participante antes de qualquer acesso ao VICKY. Sem assinatura, inclusive da opção de gravação, não há sessão |
| O que se grava | Tela do computador e voz, sem câmera. Gravador: OBS Studio no computador da sessão, com a fonte de vídeo "Captura de tela" e o microfone; nenhuma webcam configurada |
| Teste da gravação | 10 segundos gravados e reproduzidos antes do termo ser assinado, e conferência do arquivo no fim |
| Nome do arquivo | `P0x_AAAAMMDD.mkv` (sem nome de pessoa) |
| Guarda | Logo após a sessão, o observador calcula o hash (`shasum -a 256 P0x_AAAAMMDD.mkv`), envia o arquivo para a pasta restrita no Google Drive da equipe, compartilhada só com os seis integrantes e com a professora, e apaga a cópia local |
| Repositório público | Recebe só o registro: código do participante, data, duração e hash SHA-256 do arquivo (`M2.7.2/sessoes.csv`), mais as respostas e anotações anonimizadas. Nenhum vídeo, áudio ou termo assinado entra no repositório |
| Termos assinados | Digitalizados para uma subpasta separada da pasta das gravações, no mesmo Drive restrito. O papel fica com o aluno responsável. A ligação entre nome e código (P01 a P05) existe só no termo |
| Anonimato na tela | O participante usa o nome "Participante P0x" e o e-mail de teste; o navegador usa um perfil limpo, sem favoritos, contas ou notificações. Voz não é anonimizável na gravação bruta, e por isso a gravação nunca sai da pasta restrita |
| Transcrição | Trechos citados no repositório e no relatório não trazem nome, instituição, semestre exato nem outro dado que identifique o participante |
| Prazo | Gravações e termos digitalizados são excluídos ao fim do semestre 2026/2. A exclusão é registrada em `M2.7.2/coleta.md` |
| Desistência | Se o participante pedir, a gravação e as respostas dele são apagadas, e a linha em `sessoes.csv` fica só com o motivo `retirado` |

### 3.7 Ambiente da sessão

| Item | Valor |
|------|-------|
| Local | Sala reservada e silenciosa no campus Darcy Ribeiro, próxima à Faculdade de Medicina, ou outra sala combinada com o participante. O local de cada sessão vai para `sessoes.csv` |
| Computador | Notebook da equipe, Google Chrome atualizado (versão anotada), perfil limpo, zoom de 100%, janela maximizada; mouse externo à disposição do participante |
| Rede | Roteamento pelo celular do condutor (seção 3.5) |
| Produto | VICKY em produção, <https://vicky.synaptha.com/> |
| Material impresso | Termo em duas vias, cartões de tarefa A e B, folha com a escala de 1 a 5 |
| Na tela, para os questionários | Capturas fixas das 5 telas (`M2.5.1/telas/`) e recortes dos 12 elementos (`M2.7.2/elementos/`), abertos no visualizador de imagens |

Se a sessão for feita fora desse ambiente (por exemplo, em outro computador), a diferença é registrada em `sessoes.csv` na coluna `observacao`.

### 3.8 Antes da primeira sessão

1. Conferir em produção os rótulos dos 12 elementos e as definições do [gabarito](instrumentos-g2-usuarios.md#4-gabarito-dos-12-elementos), em especial os itens marcados "a confirmar na interface" (E02, E05, E11 e E12), e registrar a conferência em `M2.7.2/coleta.md`. Se uma definição mudar, o gabarito é corrigido antes do piloto e não muda mais. Elemento que não existir em produção sai de B, com registro.
2. Fazer as capturas fixas das 5 telas de M2.5.1 e os recortes dos 12 elementos, na conta de cortesia, com a área visível de 1366 por 768 pixels.
3. Conferir que conta nova começa com 0 crédito e se a prévia exige e-mail confirmado.
4. Conferir o limite de prévias vigente (seção 3.5).
5. Fazer uma sessão piloto completa com uma pessoa que não seja elegível (por exemplo, estudante de outro curso da saúde). O piloto calibra o tempo e o texto dos cartões; seus dados não entram em `dados/`. Mudança no cartão depois do piloto é registrada em `coleta.md`, e o texto fica congelado a partir da P01.

## 4. Passo a passo

### 4.1 Sessão com o participante (M2.7.2 e M2.5.1)

Tempo total estimado: 75 minutos, com folga até 90.

| Bloco | Tempo | Quem | O que acontece | Registro |
|:-----:|:-----:|:----:|----------------|----------|
| 0 | 10 min | C | Acolhida, pergunta de triagem, leitura do termo, dúvidas, assinatura das duas vias e escolha da opção de gravação | Termo assinado (fora do repositório) |
| 1 | 5 min | C e O | Teste da gravação; início da gravação; explicação do pensar em voz alta com um exemplo neutro fora do VICKY (por exemplo, contar em voz alta as janelas da própria casa); perguntas do perfil (seção 3.1) | `perfil.csv` |
| 2 | 20 min | Participante | **Parte A**, com o cartão A: abrir <https://vicky.synaptha.com/>, criar a conta com os dados do cartão, criar o projeto do tema dado, ajustar o que o cartão pede, ver os critérios antes de gastar crédito e dizer se mudaria algum | Ficha de uso (`observacao-uso.csv`) |
| 3 | 15 min | Participante | **Parte B**, com o cartão B: abrir o projeto já triado, interpretar a lista, escolher e favoritar 3 artigos, encontrar onde o VICKY registra como a busca foi feita e por que artigos ficaram de fora, salvar o resultado num arquivo que abra em planilha | Ficha de uso |
| 4 | 15 min | C | Questionário de compreensão (M2.7.2): para cada um dos 12 recortes, "Com suas palavras, o que é isto e para que serve?" A resposta é falada e gravada; O anota a resposta literal | `respostas-compreensao.csv` |
| 5 | 7 min | C | Questionário de estética (M2.5.1): as 5 capturas, uma por vez, na ordem do fluxo, com a frase e a escala de 1 a 5. Se houver tempo e o participante aceitar, o bloco qualitativo opcional | `respostas.csv` e `qualitativo.csv` |
| 6 | 3 min | C e O | Fim da gravação, agradecimento, entrega da segunda via do termo; depois que o participante sai, hash, envio ao Drive, limpeza dos favoritos da conta de cortesia e logout | `sessoes.csv` |

**Regras durante as partes A e B.**

1. O condutor entrega o cartão e diz só: "Faça o que o cartão pede, falando o que você pensa. Eu não posso explicar o site, mas posso ler o cartão de novo."
2. Lembretes permitidos, e só eles: "O que você está pensando agora?", "Continue falando o que pensa", "O que você faria se estivesse sozinho?". Lembrete não é ajuda.
3. **Ajuda** é qualquer informação sobre a interface: apontar a tela, dizer um rótulo, confirmar se o caminho está certo. Só é dada se o participante ficar 3 minutos sem avanço no mesmo passo ou pedir para desistir dele. A ajuda é a mínima (apontar a região da tela) e todo elemento envolvido recebe `uso = com_ajuda`.
4. O observador marca, para cada elemento, o código de uso e o momento da gravação (seção 5.2). Se o participante errar e corrigir sozinho, sem ajuda, o uso conta como `sem_ajuda`, com a correção anotada.
5. Tempo-limite: 25 minutos para a parte A e 20 para a parte B. Esgotado o tempo, o condutor passa ao bloco seguinte, e os elementos não alcançados ficam com `uso = nao_usou`.
6. Se o participante clicar em "Criar e iniciar tudo direto" ou equivalente, ninguém interrompe: a conta não tem crédito. O elemento E08 recebe `uso = incorreto`.
7. Se o participante tentar excluir o projeto da conta de cortesia, o condutor interrompe e registra a ocorrência. Isso não conta como ajuda em nenhum dos 12 elementos.

**Regras do questionário de compreensão.** Os recortes mostram só o rótulo e o controle, sem o texto de ajuda que o VICKY exibe ao lado, para que o participante não leia a resposta. A ordem é a do fluxo (E01 a E12). O condutor pode pedir uma única vez "Pode explicar um pouco mais?". Não comenta se a resposta está certa.

**Regras do questionário de estética.** As capturas são da página inteira, mostradas na ordem do fluxo (página inicial, novo projeto, detalhe do projeto, lista de artigos, ficha do artigo), uma de cada vez. A "página inicial" é o painel que o usuário logado vê (`/dashboard`), e não a página pública de apresentação (`/`): a medida avalia o produto em uso, e a página pública é material de divulgação, que o participante não usa durante as tarefas. As capturas são tiradas da versão em produção no dia da primeira sessão, com a data registrada, porque a produção pode diferir do commit `c2ae570`. O participante responde com um número inteiro de 1 a 5. Se der um valor fracionado, o condutor pede que escolha um inteiro.

### 4.2 Teste só com teclado (M2.6.1)

Feito por T1 e T2, cada um sozinho, no ambiente da [seção 2.2 da inspeção](metodo-g2-inspecao.md#22-ambiente) (Chrome em computador, 1366 por 768 pixels, zoom de 100%), com o mouse e o trackpad desconectados ou desativados. Teclas permitidas: Tab, Shift+Tab, Enter, Espaço e setas, como na ficha da Fase 2. Se um passo só puder ser feito com outra tecla (por exemplo, Esc para fechar um menu), isso é anotado e o passo conta como não acionável.

**Critério de sucesso.** Uma função conta em A só quando, em **todos** os passos do caminho abaixo:

1. **Acionável:** cada controle do caminho é alcançado e acionado só com as teclas permitidas (WCAG 2.2, critério 2.1.1);
2. **Foco visível:** depois de cada tecla, o avaliador consegue ver, sem procurar, qual controle tem o foco (critério 2.4.7). Foco que some, vai para um elemento invisível ou fica atrás de outro elemento é falha;
3. **Alvo mínimo:** cada controle clicável do caminho tem pelo menos 24 por 24 pixels, medidos no DevTools (seção 4.2.1), salvo as exceções do critério 2.5.8 (espaçamento suficiente, link dentro de frase, controle equivalente na mesma página, controle nativo do navegador sem estilo próprio, apresentação essencial).

| Função | Caminho testado (do início ao resultado) | Conta e momento |
|--------|------------------------------------------|-----------------|
| F01 | Abrir `/signup`, preencher nome, e-mail, senha e confirmação, marcar o aceite, enviar; sair; entrar por `/login`; abrir a recuperação de senha e enviar o pedido | Conta nova de T1 ou T2 |
| F02 | Abrir "Novo projeto", escolher o tipo de revisão, preencher tema e objetivo, escolher a janela de anos, salvar como rascunho | Conta nova |
| F03 | Gerar a prévia dos critérios, chegar aos critérios gerados e editar um deles | Conta nova; gasta 1 prévia |
| F04 | Em novo projeto, marcar e desmarcar cada base, ligar o filtro de acesso aberto e alterar a quantidade do Top | Conta nova |
| F05 | Iniciar a triagem completa, confirmar se houver confirmação e acompanhar o andamento até a lista | Triagem prevista do G1, feita por T1 com o teclado e T2 observando. Combinado com quem executa o G1 |
| F06 | Abrir a lista de artigos do projeto triado, ler o Quality Score de um artigo, abrir a ficha dele e o link da fonte | Conta de cortesia |
| F07 | Favoritar e desfavoritar um artigo na lista e na ficha | Conta de cortesia |
| F08 | Chegar ao registro da busca e dos critérios aplicados (log) do projeto triado | Conta de cortesia |
| F09 | Abrir o menu de exportação e baixar um arquivo em cada formato oferecido | Conta de cortesia |

F05 é observada uma única vez, porque cada triagem custa um crédito; por isso não há segunda execução independente dessa função, e a evidência é a gravação da tela de T1. As demais funções são executadas por T1 e T2.

#### 4.2.1 Como medir o alvo

Com o controle visível, abrir o DevTools (F12, que é tecla do avaliador e não do teste), escolher o controle com o seletor de elementos e ler largura e altura na aba *Computed*. O avaliador mede todo controle do caminho que pareça menor que um ícone comum (setas, estrelas de favorito, "x", links curtos). Abaixo de 24 por 24 pixels, verificar as exceções do critério 2.5.8 e anotar qual se aplica.

**Registro por função** (`M2.6.1/T1.md` e `T2.md`): `funcao`, `passo`, `acionavel (sim/nao)`, `foco_visivel (sim/nao)`, `alvos_abaixo_de_24px` (controle e tamanho), `excecao_2_5_8`, `concluida (sim/nao)`, `captura`.

### 4.3 axe DevTools (M2.6.2)

Feito por A1 e A2, cada um sozinho, no mesmo ambiente da inspeção.

**Ferramentas e versões.**

| Ferramenta | Uso | Versão registrada em `coleta.md` |
|------------|-----|----------------------------------|
| Extensão axe DevTools (Deque), versão gratuita, na Chrome Web Store | Lista as violações de contraste e os itens que precisam de revisão manual em cada tela | Versão da extensão em `chrome://extensions` |
| axe-core 4.10.2, arquivo `axe.min.js` baixado de <https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.10.2/axe.min.js> | Conta os pares aprovados, que a extensão não exibe, e por isso dá o denominador B | Fixa: 4.10.2 |
| Seletor de cor do DevTools (painel *Styles*) | Mede a razão de contraste dos pares incertos | Versão do Chrome |

A extensão mostra só os problemas; sem os pares aprovados não há como calcular B. Por isso a contagem sai do axe-core, que é o motor da própria extensão, rodado no Console. Se a versão do axe-core usada pela extensão for diferente de 4.10.2, as duas versões são anotadas, e a contagem de violações das duas é comparada (seção 7).

**Telas e estado de cada uma.**

| ID | Tela | Rota | Estado |
|----|------|------|--------|
| S1 | Página inicial | `/` | Janela anônima, topo da página |
| S2 | Cadastro | `/signup` | Janela anônima, formulário vazio |
| S3 | Login | `/login` | Janela anônima, formulário vazio |
| S4 | Lista de projetos | `/projetos` | Conta de cortesia, com o projeto triado na lista |
| S5 | Novo projeto | `/projetos/novo` | Conta de cortesia, valores padrão |
| S6 | Detalhe do projeto | `/projetos/<id>` | Projeto triado do G1, menus fechados |
| S7 | Lista de artigos | `/projetos/<id>/registros` | Mesmo projeto, ordem padrão |
| S8 | Ficha do artigo | `/projetos/<id>/registros/<fonte>/<id>` | Primeiro artigo da lista |

As rotas são as do código no commit `c2ae570`; a rota real de cada tela em produção é anotada em `coleta.md`.

**Passo a passo, por tela.**

1. Abrir a tela no estado da tabela e esperar o carregamento terminar. Fechar menus e avisos que não façam parte do estado.
2. Abrir o DevTools, aba **axe DevTools**, e escolher **Scan all of my page** (varredura da página inteira), com o padrão WCAG 2.2 AA e as boas práticas desligadas nas configurações da extensão.
3. No resultado, filtrar a regra de contraste (*Elements must meet minimum color contrast ratio thresholds*, id `color-contrast`). Anotar o número de problemas e o número de itens em *Needs review*.
4. Exportar o relatório pelo botão **Export** da extensão em JSON, salvo como `M2.6.2/relatorios/AAAAMMDD_A1_S1_extensao.json`. Se a versão gratuita não oferecer exportação, fazer a captura do painel (`AAAAMMDD_A1_S1_extensao.png`) e anotar isso em `coleta.md`.
5. Na aba **Console**, colar o conteúdo de `axe.min.js` (o Chrome pode pedir que se digite `allow pasting` antes) e depois rodar:

    ```js
    axe.run(document, { runOnly: ['color-contrast'] }).then(r => {
      const n = g => r[g].reduce((s, x) => s + x.nodes.length, 0);
      console.log(r.testEngine.version, 'aprovados', n('passes'),
                  'violacoes', n('violations'), 'incertos', n('incomplete'));
      copy(JSON.stringify(r));
    });
    ```

6. Colar o conteúdo copiado num arquivo `M2.6.2/relatorios/AAAAMMDD_A1_S1_axe-core.json` e anotar os três números na ficha.
7. **Conferência manual dos incertos.** Para cada item em `incomplete`, localizar o elemento, abrir o seletor de cor do texto no painel *Styles* e ler a razão de contraste. Se o fundo for imagem ou degradê, usar o conta-gotas no ponto do fundo atrás do texto que dá o **menor** contraste. Classificar como aprovado quando a razão for de pelo menos 4,5:1, ou 3:1 para texto grande (24 pixels, ou 18,66 pixels em negrito). Registrar a razão medida e a captura.

Cada elemento com texto avaliado pelo axe é um par de texto e fundo. Um mesmo elemento que aparece em várias telas (menu lateral, rodapé) conta uma vez por tela, porque o estudante o encontra em cada uma.

O axe é rodado uma vez por tela e por avaliador, com a página aberta à mão. Isso não é automação contra a produção, que os Termos de Uso proíbem.

**Registro por tela** (`M2.6.2/A1.md` e `A2.md`): `tela`, `rota`, `aprovados_axe`, `violacoes_axe`, `incertos`, `incertos_aprovados_manual`, `relatorio_extensao`, `relatorio_axe_core`. Por par incerto: `tela`, `seletor`, `texto`, `razao_medida`, `texto_grande (sim/nao)`, `aprovado (sim/nao)`, `captura`.

## 5. Registro

### 5.1 Arquivos de cada pasta

```text
dados/avaliacao/G2/
├── termo-de-consentimento.docx   # termo em branco para imprimir
├── M2.5.1/
│   ├── respostas.csv             # participante, tela, nota (1 a 5), comentario
│   ├── qualitativo.csv           # bloco opcional, fora do cálculo
│   └── telas/                    # as 5 capturas fixas mostradas aos participantes
├── M2.6.1/
│   ├── coleta.md                 # data, Chrome, área visível, papéis T1 e T2, projeto triado usado
│   ├── T1.md e T2.md             # ficha por função e passo
│   ├── consolidado.md            # resultado único por função e cálculo
│   └── evidencias/               # AAAAMMDD_T1_F0x_<passo>.png
├── M2.6.2/
│   ├── coleta.md                 # versões da extensão, do axe-core e do Chrome; rotas reais
│   ├── A1.md e A2.md             # contagens por tela e pares incertos
│   ├── consolidado.md            # contagem final por tela e cálculo
│   └── relatorios/               # JSON da extensão e do axe-core, capturas dos incertos
└── M2.7.2/
    ├── coleta.md                 # texto congelado dos cartões, limite de prévias, conferências, ocorrências
    ├── sessoes.csv               # registro de cada sessão, com hash da gravação
    ├── perfil.csv                # perfil anonimizado do participante
    ├── observacao-uso.csv        # uso de cada elemento por participante
    ├── respostas-compreensao.csv # resposta literal e classificação de C e O
    ├── consolidado.md            # entendido por participante e elemento, e cálculo
    └── elementos/                # recortes dos 12 elementos mostrados no questionário
```

As fichas `.md` seguem o formato da inspeção: tabela com os itens já listados e as colunas em branco, preenchível pelo GitHub. Os `.csv` trazem só o cabeçalho até a primeira sessão. Nada é preenchido com dado simulado.

### 5.2 Colunas dos arquivos das sessões

| Arquivo | Colunas | Valores |
|---------|---------|---------|
| `sessoes.csv` | `participante`, `data`, `inicio`, `fim`, `duracao_min`, `local`, `condutor`, `observador`, `arquivo_gravacao`, `sha256`, `termo_assinado`, `gravacao_autorizada`, `situacao`, `observacao` | `situacao`: `valida`, `interrompida`, `retirado` ou `piloto_descartado` |
| `perfil.csv` | `participante`, `faixa_curso`, `fez_revisao`, `usou_ferramenta_triagem` | `faixa_curso`: `1-4`, `5-8` ou `internato` |
| `observacao-uso.csv` | `participante`, `elemento`, `uso`, `momento_gravacao`, `observacao` | `uso`: `sem_ajuda`, `com_ajuda`, `incorreto` ou `nao_usou` |
| `respostas-compreensao.csv` | `participante`, `elemento`, `resposta_literal`, `classificacao_c`, `classificacao_o`, `classificacao_final`, `decidido_por` | `classificacao_*`: `correta` ou `incorreta`; `decidido_por`: `consenso` ou `A3` |
| `M2.5.1/respostas.csv` | `participante`, `tela`, `nota`, `comentario` | `tela`: `inicial`, `novo_projeto`, `detalhe_projeto`, `lista_artigos`, `ficha_artigo`; `nota`: 1 a 5 |
| `M2.5.1/qualitativo.csv` | `participante`, `afirmacao`, `nota` | `afirmacao`: Q01 a Q10 |

`classificacao_c` e `classificacao_o` são preenchidas separadamente, depois da sessão, por C e por O, cada um sem ver a do outro (seção 7).

## 6. Cálculo

As fórmulas estão nas [fichas da Fase 2](../fase-2/especificacao-das-metricas.md) e os níveis em [níveis de pontuação](../fase-2/niveis-e-julgamento.md). O cálculo só usa sessões com `situacao = valida`, e só é feito com exatamente cinco.

| Métrica | Regra por item | A | B | Regra especial nos níveis |
|---------|----------------|---|---|---------------------------|
| M2.5.1 | Tela agradável para o participante quando `nota` é 4 ou 5 | Telas agradáveis para pelo menos 3 dos 5 participantes | 5 | - |
| M2.6.1 | Função com `concluida = sim` no `consolidado.md` | Funções concluídas | 9 | F01 não concluída leva a Insatisfatório |
| M2.6.2 | Par aprovado pelo axe ou aprovado na conferência manual | Soma, nas 8 telas, de `aprovados_axe` e `incertos_aprovados_manual` | Soma, nas 8 telas, de aprovados, violações e incertos | - |
| M2.7.2 | Elemento entendido pelo participante quando `uso = sem_ajuda` **e** `classificacao_final = correta` | Elementos entendidos por pelo menos 3 dos 5 participantes | 12, menos elementos que não existam em produção (seção 3.8) | Quality Score (E10) não entendido por pelo menos 3 dos 5 leva a Insatisfatório, qualquer que seja X |

A regra de M2.7.2 incorpora a proposta original do roteiro (respostas acertadas por pelo menos 3 dos 5 compõem A) e acrescenta a condição de uso sem ajuda que a ficha da Fase 2 exige.

Exemplo de leitura: se o Quality Score for entendido por 2 dos 5 participantes e outros 10 elementos por 3 ou mais, X = 10/12 = 83%, que cairia em Bom, mas a regra especial leva M2.7.2 a Insatisfatório.

O valor, o nível e a evidência são publicados na Fase 4. Os limiares não mudam depois da coleta. As hipóteses H2.5, H2.6 e H2.7 são comparadas com os valores medidos, sem efeito no julgamento.

## 7. Discordância e repetição

### 7.1 Classificação das explicações (M2.7.2)

1. Depois da sessão, C e O classificam sozinhos cada resposta como `correta` ou `incorreta`, usando só o gabarito. Correta é a resposta que traz o ponto essencial do elemento e não comete o erro que invalida, conforme o [gabarito](instrumentos-g2-usuarios.md#4-gabarito-dos-12-elementos). Vocabulário diferente do da tela não torna a resposta incorreta.
2. Se concordam, a classificação é final, com `decidido_por = consenso`.
3. Se divergem, os dois ouvem de novo o trecho da gravação e reaplicam o gabarito. Sem acordo, A3 ouve o trecho e decide, com `decidido_por = A3`.
4. Se a divergência vier de gabarito ambíguo, a interpretação adotada é escrita em `M2.7.2/coleta.md` e reaplicada às respostas de todos os participantes para aquele elemento.

O código de uso (`observacao-uso.csv`) é conferido pelo condutor com a gravação no mesmo dia; divergência entre o registro do observador e a gravação se resolve pela gravação.

### 7.2 Notas de estética (M2.5.1)

A nota é do participante e não passa por classificação. Nota em branco conta como "não agradável" para aquela tela, que é a leitura conservadora, e o caso fica registrado.

### 7.3 Teclado e contraste (M2.6.1 e M2.6.2)

Seguem a [regra da inspeção](metodo-g2-inspecao.md#6-discordancia-e-repeticao): fichas enviadas ao repositório antes da comparação, divergência resolvida sobre a evidência, A3 sem consenso, resultado sim ou não por item, sem média.

Em M2.6.2, as contagens do axe-core devem coincidir entre A1 e A2, porque a ferramenta é determinística. Se não coincidirem, a causa é o estado da tela (menu aberto, aviso, conteúdo diferente). Os dois rodam de novo, juntos, no estado da tabela da seção 4.3, e vale essa execução. Nos pares incertos, a divergência se resolve medindo juntos no mesmo ponto do fundo.

Em M2.6.1, uma função em que T1 e T2 divergem é executada de novo pelos dois juntos, com gravação da tela, e vale o que a gravação mostra.

### 7.4 Quando a sessão não termina como previsto

| Situação | O que fazer |
|----------|-------------|
| Participante desiste no meio | A sessão para na hora, sem insistência. Pergunta-se se ele autoriza o uso do que foi gravado só como registro de ocorrência; os dados não entram no cálculo. `situacao = retirado` ou `interrompida`. Convida-se uma reserva |
| VICKY fora do ar ou prévia bloqueada antes do fim da parte A | Sessão interrompida. O participante já viu o produto e não pode repetir. Convida-se uma reserva, e a causa vai para `coleta.md` |
| Falha da gravação percebida no fim | Sessão interrompida, porque sem gravação as explicações não podem ser conferidas. Convida-se uma reserva |
| Tempo-limite de uma parte esgotado | A sessão continua; os elementos não alcançados ficam com `nao_usou` e contam como não entendidos para esse participante |
| Participante revela durante a sessão que já usou o VICKY | Sessão interrompida por critério de exclusão; reserva |
| Mudança visível em produção entre sessões | Registrar a data em `coleta.md`. Se a mudança atingir um dos 12 elementos ou uma das 5 telas, as sessões anteriores e posteriores não são comparáveis naquele item, e o caso é declarado na Fase 4 |
| Menos de cinco sessões válidas até a data da Fase 4 | **Não calcular** M2.5.1 nem M2.7.2. Não se aplica proporção sobre quatro participantes nem se ajusta a regra de "3 de 5". O desvio é registrado em `M2.7.2/coleta.md` e declarado na Fase 4 como métrica não coletada, sem nível por estimativa |
| Falha no teste de teclado por causa externa | Repetir em outro horário. Persistindo, a função fica `nao_coletado`, sai de B e é declarada na Fase 4 |

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 04/11/2026 | Criação da página | Lucas Avelar | - |
| 0.2 | 09/11/2026 | Esqueleto com o que a Fase 2 define e os pontos em aberto para o responsável | Gabriel Fae | - |
| 0.3 | 14/11/2026 | Método completo: justificativa, recrutamento, papéis, contas, limite de prévias, termo e anonimização, roteiro da sessão com tempos, teste com teclado, passo a passo do axe, registro, cálculo e repetição. Incorpora o roteiro de M2.7.2 e o questionário qualitativo escritos por João Felipe Oliveira | Lucas Avelar e João Felipe Oliveira | - |
