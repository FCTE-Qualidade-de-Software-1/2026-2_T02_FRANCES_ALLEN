# Método do G2 com usuários (capacidade de interação)

Este método cobre as quatro métricas do G2 que não saem só da inspeção: duas medidas com estudantes de Medicina (M2.5.1 e M2.7.2) e duas de acessibilidade, executadas pelos avaliadores (M2.6.1 e M2.6.2). Definição, fórmula e níveis são os da [Fase 2](../fase-2/especificacao-das-metricas.md); esta página diz como executar a coleta. As oito métricas de inspeção estão no [Método do G2 por inspeção](metodo-g2-inspecao.md), e esta página reaproveita dele o ambiente (seção 2.2), a organização das pastas e a regra de discordância, sem repeti-los.

Os instrumentos aplicados aos participantes (cartões de tarefa, ficha de observação, questionário de compreensão com gabarito e questionário de estética) estão em [Instrumentos do G2 com usuários](instrumentos-g2-usuarios.md). O termo aceito antes de cada sessão e no início do formulário está em [Termo de consentimento](termo-de-consentimento.md).

> **Versão 0.6 ([D13](../gestao/decisoes.md#d13-adaptar-a-coleta-com-usuarios-ao-prazo-da-entrega-2)).** M2.5.1 passou a ser coletada por um formulário online assíncrono, com cinco respondentes, e M2.7.2 por sessões remotas individuais, com três participantes válidos. O condutor deixou de ser uma pessoa fixa e o observador passou a ser opcional. O que mudou, por que e com quais consequências está na [seção 2.8](#28-adaptacao-da-versao-06-d13).

> **Execução (19 a 22/11/2026).** As três sessões válidas foram feitas em 19 e 20/11, e o formulário de estética teve três respostas, todas dos participantes das sessões. A M2.5.1 foi calculada com elas pela [D14](../gestao/decisoes.md#d14-calcular-m251-com-as-tres-respostas-obtidas). Os ajustes e desvios estão nas seções [2.9](#29-ajustes-feitos-antes-da-primeira-sessao) e [2.10](#210-execucao-das-sessoes-e-do-formulario), e os valores, em [Resultados do G2 com usuários](../fase-4/resultados-g2-usuarios.md).

## 1. Métricas cobertas

| Métrica | Medida | Quem fornece o dado | Instrumento | Denominador (B) | Pasta em `dados/avaliacao/G2/` |
|---------|--------|---------------------|-------------|-----------------|--------------------------------|
| [M2.5.1](../fase-2/especificacao-das-metricas.md#m251) | UIn-1-S | 5 respondentes válidos (códigos R01 a R05) | Questionário de estética das 5 telas, em formulário online assíncrono | 5 telas | `M2.5.1/` |
| [M2.6.1](../fase-2/especificacao-das-metricas.md#m261) | UAc-1-G | Avaliadores K1 e K2 | Teste só com teclado, por função | 9 funções (F01 a F09) | `M2.6.1/` |
| [M2.6.2](../fase-2/especificacao-das-metricas.md#m262) | Medida adicional | Avaliadores A1 e A2 | axe DevTools e conferência manual | Pares de texto e fundo avaliados nas 8 telas | `M2.6.2/` |
| [M2.7.2](../fase-2/especificacao-das-metricas.md#m272) | ULe-4-S | 3 participantes válidos (códigos P01 a P05), em sessão remota | Teste de cenário com pensamento em voz alta e questionário de compreensão | 12 elementos e passos | `M2.7.2/` |

M2.7.2 sai da sessão remota com o participante. M2.5.1 sai de um formulário online que o respondente preenche sozinho, quando preferir. M2.6.1 e M2.6.2 não usam participantes e podem correr em paralelo às sessões.

## 2. Por que este método

### 2.1 Participantes reais para M2.5.1 e M2.7.2

As duas medidas perguntam o que o **estudante** percebe, e não o que a equipe percebe. A nota 3 da UIn-1-S, na ISO/IEC 25023:2016, recomenda que a estética seja medida com representantes do público-alvo; a Fase 2 adotou essa nota na ficha de M2.5.1. A ULe-4-S mede o que o usuário entende "sem estudo prévio, treinamento ou ajuda" ([ficha de M2.7.2](../fase-2/especificacao-das-metricas.md#m272)). A equipe não serve como fonte desse dado: todos já leram as telas, e parte leu o código, o que a própria [abstraction sheet do G2](../fase-2/objetivos-questoes-hipoteses.md) aponta como fator que faz a interface parecer mais clara do que é. Por isso os participantes são estudantes de Medicina, o público declarado do VICKY na [Fase 1](../fase-1/objeto-de-avaliacao.md#1-identificacao), que nunca usaram o produto.

### 2.2 Uso observado e explicação, os dois juntos

A Fase 2 exige, para M2.7.2, que o elemento tenha sido **usado** sem ajuda **e explicado** corretamente. Cada metade cobre uma falha da outra: o participante pode acertar o uso por tentativa e erro sem entender o elemento, ou explicar bem um rótulo que não soube usar. Por isso a sessão tem duas partes. Na primeira, o participante executa tarefas dadas em linguagem de estudante, sem o nome dos controles, e pensa em voz alta enquanto o observador registra o uso de cada elemento. Na segunda, responde ao questionário de compreensão, e a resposta é comparada a um gabarito escrito antes da primeira sessão. Pensar em voz alta expõe o raciocínio no momento do uso, que a gravação preserva para a conferência posterior.

### 2.3 Estética em formulário assíncrono

Até a versão 0.5, M2.5.1 era aplicada no fim da sessão, depois do uso real. Desde a versão 0.6 ([D13](../gestao/decisoes.md#d13-adaptar-a-coleta-com-usuarios-ao-prazo-da-entrega-2)), ela é coletada por um formulário online que o estudante preenche sozinho, pelo celular ou pelo computador, porque o público-alvo não tinha horário para sessões no prazo da entrega. O formulário mostra as mesmas 5 capturas fixas, na mesma ordem, com a mesma frase e a mesma escala, de modo que os cinco respondentes continuam julgando exatamente o mesmo objeto. O que se perde é o uso prévio: o respondente julga a tela pela imagem, sem tê-la usado numa tarefa. Essa diferença é uma ameaça à validade, declarada na seção 2.8 e na Fase 4.

### 2.4 Uma sessão por participante, sem repetição

Um participante só é "de primeira vez" uma vez. Se a sessão falhar depois que ele viu o VICKY, ele não pode repetir, e o método prevê reservas em vez de nova sessão (seção 7). Pela mesma razão, a sessão piloto não usa estudante elegível, e quem já respondeu ao formulário de estética não pode mais fazer a sessão, porque já viu as telas. A ordem inversa é permitida: quem fez a sessão recebe o link do formulário no fim dela.

### 2.5 Acessibilidade pelos avaliadores, com regra objetiva

M2.6.1 simula o perfil motor, como declara a Fase 2: não há participante com deficiência motora. Para que dois avaliadores cheguem ao mesmo resultado, o sucesso de uma função foi decomposto em três condições verificáveis (WCAG 2.2, critérios 2.1.1, 2.4.7 e 2.5.8). M2.6.2 usa o axe DevTools, ferramenta definida na Fase 2, para os pares que a ferramenta decide sozinha, e conferência manual para os que ela marca como incertos (texto sobre imagem ou degradê), seguindo o critério 1.4.3 da WCAG 2.2.

### 2.6 Ligação com a ISO/IEC 25040

Na ISO/IEC 25040:2024, projetar a avaliação inclui definir os métodos de medição, os recursos e as condições em que cada medida é obtida, antes da execução. Esta página fixa essas condições para as quatro métricas: quem participa, com qual conta, em qual ordem, com qual instrumento e com qual regra de cálculo, de modo que outra pessoa da equipe consiga repetir a coleta e chegar ao mesmo dado.

### 2.7 Coerência com a Fase 2

| Métrica | O que a Fase 2 fixa | Como este método cumpre |
|---------|---------------------|-------------------------|
| M2.5.1 | A = telas agradáveis para pelo menos 3 de 5; notas 4 e 5 contam; B = 5 telas; piso de Bom 60%; fora da contagem do G2 | Formulário online com as mesmas 5 telas e a mesma escala; regra de 3 de 5 aplicada sem ajuste (seção 6). A fonte dos dados na ficha foi atualizada pela D13 |
| M2.6.1 | A = funções concluídas só com teclado, foco visível e alvos de 24 por 24 pixels; B = F01 a F09; piso de Bom 88%; F01 não concluída leva a Insatisfatório | Três condições por função, verificadas em cada passo do caminho da função; F05 observada numa triagem do G1 |
| M2.6.2 | A = pares com 4,5:1 (ou 3:1 para texto grande); B = pares avaliados; 8 telas; dois avaliadores; piso de Bom 95% | axe com versão registrada, as 8 telas da ficha, conferência manual dos incertos, dois avaliadores independentes |
| M2.7.2 | A = elementos entendidos pela maioria dos participantes (2 de 3, ou 3 de 5), desde a D13; entendido = usado sem ajuda **e** explicado corretamente; B = 12 elementos; piso de Bom 75%; Quality Score não entendido leva a Insatisfatório | Cartões de tarefa que fazem o participante passar pelos 12 elementos; ficha de uso e questionário com gabarito; maioria calculada sobre três participantes válidos (seção 6); regra do Quality Score verificada à parte |

### 2.8 Adaptação da versão 0.6 (D13)

As sessões estavam previstas para 16 a 18/11, e nenhuma aconteceu: os estudantes de Medicina recrutados pela equipe estavam comprometidos com o Intermed no período da coleta, e os integrantes têm aula nos horários em que uma sessão presencial de 75 minutos caberia. Pela regra da versão 0.5, sem cinco sessões válidas até a Fase 4, M2.5.1 e M2.7.2 não seriam calculadas. A equipe decidiu adaptar a coleta antes de qualquer sessão ([D13](../gestao/decisoes.md#d13-adaptar-a-coleta-com-usuarios-ao-prazo-da-entrega-2)), de modo que nenhum dado coletado foi reinterpretado.

| O que mudou | Versão 0.5 | Versão 0.6 | Por quê |
|-------------|------------|------------|---------|
| Coleta de M2.5.1 | Questionário no fim da sessão presencial | Formulário online assíncrono, com 5 respondentes válidos (R01 a R05) e o mesmo limiar de 3 de 5 (seção 4.4) | Leva cerca de 5 minutos e pode ser respondido pelo celular, a qualquer hora, o que mantém n = 5 mesmo com o público indisponível para sessões |
| Formato da sessão de M2.7.2 | Presencial, em sala da UnB, cerca de 75 minutos | Remota, pelo Google Meet, com o participante no próprio computador e cerca de 1 hora (seção 4.1) | Elimina deslocamento e permite horários à noite; o bloco de estética saiu da sessão |
| Participantes de M2.7.2 | 5 válidos e 2 reservas (P01 a P07) | 3 válidos e 2 reservas (P01 a P05) | Quantidade que cabe no prazo |
| Regra de agregação de M2.7.2 | Entendido por pelo menos 3 de 5 | Entendido pela maioria dos participantes válidos: 2 de 3 (ou 3 de 5, se houver cinco) | A ficha da Fase 2 fala em "maioria dos participantes"; 3 de 5 era a maioria para n = 5 |
| Condutor | João Felipe Oliveira ou quem fez o piloto | Qualquer integrante que tenha conduzido ou assistido ao piloto | Permite marcar sessões em horários diferentes, conforme a agenda de cada integrante |
| Observador | Obrigatório | Opcional; sem observador, o condutor preenche a ficha de uso pela gravação e outro integrante faz a segunda classificação (seção 3.2) | Sessões remotas à noite nem sempre têm dois integrantes livres; a gravação preserva tudo o que o observador anotaria |

**Alternativas consideradas e descartadas.**

1. **Manter o método e declarar as duas métricas não coletadas.** Era o que a versão 0.5 previa. Descartada porque deixaria Q2.5 sem resposta e Q2.7 só com a inspeção (M2.7.1), quando havia como coletar com o público certo.
2. **Fazer as sessões com estudantes de outros cursos.** Descartada porque viola o critério de inclusão e muda o que se mede: a ficha pede representantes do público-alvo, e um estudante de outro curso não reage a termos como PICO e Quality Score como o estudante de Medicina.
3. **Passar também o questionário de compreensão para o formulário.** Descartada porque a ficha de M2.7.2 exige que o elemento seja **usado** sem ajuda e explicado. Sem a observação do uso, a métrica mudaria de definição, e não só de forma de coleta.

**Ameaças à validade criadas pela adaptação.**

- **Amostra de três em M2.7.2.** Com n = 3, a classificação de cada elemento depende de um único participante (2 de 3 contra 1 de 3). O resultado é **indicativo**, não conclusivo, e a Fase 4 o apresenta com essa ressalva.
- **Estética sem uso prévio.** Em M2.5.1, o respondente julga a imagem da tela sem tê-la usado numa tarefa, diferente do que a ficha previa até a D13.
- **Ambiente não controlado na sessão remota.** Cada participante usa o próprio computador, navegador, tamanho de tela e rede. Essas diferenças são registradas em `sessoes.csv` (coluna `observacao`), e uma queda da chamada segue a regra da seção 7.4.

Os limiares de nível da [Fase 2](../fase-2/niveis-e-julgamento.md) não mudaram. Mudaram a regra de agregação de M2.7.2 (de "3 de 5" para "maioria dos participantes válidos") e a fonte dos dados de M2.5.1, e as duas fichas da [especificação](../fase-2/especificacao-das-metricas.md) foram atualizadas, como registra a [seção 5.5 de recursos e ambiente](recursos-e-ambiente.md#55-alteracoes-na-fase-2-durante-a-fase-3).

### 2.9 Ajustes feitos antes da primeira sessão

Antes da P01 (19/11/2026), a equipe mudou três pontos da sessão, mas só os registrou nestas páginas em 22/11/2026. Nenhum dado foi reinterpretado: os ajustes valeram igualmente para todos os participantes.

| O que mudou | Previsto | Feito nas sessões | Efeito |
|-------------|----------|-------------------|--------|
| Tema do cartão A | Tema T1 do G1 | "O uso de células-tronco para restauração de tecido", com um projeto já triado desse tema para a parte B | Nenhum nos 12 elementos, que não dependem do tema |
| Conta da parte A | Conta nova criada pelo participante, com 0 crédito | Conta da equipe com créditos, com login enviado pelo condutor; a parte B usa a mesma conta | A criação de conta (F01) saiu da sessão. Havia risco de gastar crédito se o participante iniciasse a triagem; nenhum iniciou |
| Piloto (seção 3.8) | Uma sessão piloto antes da P01 | Não houve | Os cartões não foram calibrados antes; o texto foi o mesmo para todos |

O registro de cada ajuste está em `M2.7.2/coleta.md`.

### 2.10 Execução das sessões e do formulário

As três sessões válidas foram feitas em 19/11 (P01) e 20/11/2026 (P02 e P03), sem chamar reservas. O registro de cada uma está em `M2.7.2/sessoes.csv`, e as ocorrências, em `M2.7.2/coleta.md`.

| O que aconteceu | Previsto | Feito | Efeito |
|-----------------|----------|-------|--------|
| Observador | Opcional (seção 3.2) | P01 com observador. P02 e P03 sem, com a segunda classificação das explicações feita por outro integrante, pela gravação | Nenhum: é o caminho previsto para sessão sem observador |
| Duração | 63 minutos estimados, com folga até 75 | 43, 19 e 24 minutos | Nenhum tempo-limite foi atingido, e nenhum elemento ficou sem uso por tempo |
| Registro das explicações | Resposta literal anotada pela gravação (seção 4.1, bloco 4) | P01 com a fala do participante. P02 e P03 com a classificação informada pelo condutor, que só detalhou as exceções; os elementos não citados foram marcados como sem ajuda e corretos por padrão, com `resposta_literal` vazia, e as anotações do condutor levam a etiqueta `[síntese]` | As duas classificações das explicações coincidiram nos 36 itens; o código de uso não teve segunda conferência. A gravação continua sendo a evidência de cada resposta |
| Objetivo no cartão A | Frase de objetivo fixada junto com o tema (seção 3.3) | Cartões lidos em voz alta pelo condutor, sem frase de objetivo junto com o tema novo; o chat trouxe só o tema e os dados de acesso (P01) ou só o link e os dados de acesso (P02 e P03). P01 e P02 deixaram o campo Objetivo vazio, e P03 escreveu um objetivo próprio | Uso de E02 de P01 e P02 marcado como incorreto pela gravação (seção 7.1), e M2.7.2 foi de 11/12 para 10/12. A frase deveria ter sido definida junto com o tema e precisa ser fixada numa próxima aplicação |
| Recortes dos 12 elementos | Feitos antes do piloto e guardados em `M2.7.2/elementos/` (seção 3.8) | Montados em 22/11, depois das sessões, com as capturas de produção da inspeção do G2 | Registram o que cada elemento mostra. As imagens exatas exibidas nas chamadas não foram guardadas |
| Respondentes da M2.5.1 | 5 respostas válidas; com menos de 5, a métrica não é calculada (seção 7.4) | 3 respostas, todas dos participantes das sessões, dadas depois da chamada | Pela D14, a métrica foi calculada com maioria de 2 de 3, com resultado indicativo. Os respondentes julgaram as telas depois de usá-las |
| Capturas do formulário | Guardadas em `M2.5.1/telas/`, com a data (seção 4.4) | Não guardadas | A imagem julgada em cada tela não pode ser conferida no repositório |

**Regra de agregação da M2.5.1 pela D14.** A regra de 2 de 3 repete a lógica que a D13 aplicou à M2.7.2: a ficha da Fase 2 fala em "maioria dos respondentes", e 3 de 5 era a maioria para cinco. A ficha da Fase 2 não foi alterada, porque a coleta já tinha acontecido: o desvio fica declarado aqui, em `M2.5.1/coleta.md` e na Fase 4, junto com a sensibilidade à regra (exigindo os três respondentes, nenhuma tela entraria em A).

## 3. Preparação

### 3.1 Recrutamento e critérios de inclusão

| Item | Definição |
|------|-----------|
| Quantos | **Sessão (M2.7.2):** 3 participantes válidos, mais 2 reservas convidados desde o início. Os titulares recebem os códigos P01 a P03, na ordem das sessões, e as reservas, P04 e P05, na ordem em que forem chamadas. Código de sessão interrompida ou retirada não é reaproveitado, de modo que as três sessões válidas podem ter, por exemplo, os códigos P01, P03 e P04. **Formulário (M2.5.1):** 5 respondentes válidos, com os códigos R01 a R05 na ordem de envio (seção 4.4). Uma mesma pessoa pode participar das duas coletas, desde que faça a sessão primeiro (seção 2.4); ela recebe um código P e um código R, sem ligação registrada entre os dois |
| Onde | Estudantes de Medicina da UnB (Faculdade de Medicina, campus Darcy Ribeiro), por contatos pessoais da equipe, ligas acadêmicas e centro acadêmico. Estudantes de Medicina de outras instituições do DF também são elegíveis |
| Convite | Mensagem curta com o objetivo, as duas formas de participar (formulário de cerca de 5 minutos e chamada de cerca de 1 hora), a gravação de tela e voz sem câmera na chamada e a ausência de remuneração. O termo completo é lido no início da chamada e aparece na primeira página do formulário |
| Inclusão | 18 anos ou mais (os Termos do VICKY restringem o uso a maiores de 18); matrícula ativa em Medicina; nunca ter usado o VICKY; aceitar o termo e, na sessão, também a gravação |
| Exclusão | Já ter acessado o VICKY, inclusive a página pública; ter vínculo com a Synaptha ou com a equipe de desenvolvimento do VICKY; ter visto as telas por colega da equipe; ser integrante desta equipe. Para a sessão, também: ter respondido antes ao formulário de estética |
| Pergunta de triagem | "Você já entrou no site do VICKY ou viu alguém usando?" Resposta sim exclui. Feita no convite e repetida no início da sessão e na página de triagem do formulário, onde a resposta "só na chamada com a equipe deste trabalho" não exclui |
| Perfil registrado (só na sessão) | Faixa do curso (1º ao 4º semestre, 5º ao 8º, internato), se já fez revisão sistemática ou de literatura e se já usou ferramenta de triagem. Esses dados não entram no cálculo; servem para interpretar o resultado na Fase 4, como prevê a abstraction sheet |

Não se exige conhecimento de metodologia científica: a promessa do VICKY, registrada na Fase 1, é que o estudante não precisa saber montar um PICO.

### 3.2 Papéis

| Papel | Quem | Responsabilidade | Não pode |
|-------|------|------------------|----------|
| Condutor (C) | Qualquer integrante que tenha conduzido ou assistido ao piloto (seção 3.8), escalado por sessão e registrado em `sessoes.csv` | Lê o termo, entrega os cartões, faz os lembretes neutros (as três frases fixas da [seção 4.1](#41-sessao-remota-com-o-participante-m272), que pedem ao participante que continue pensando em voz alta sem indicar o caminho), aplica os questionários e decide quando dar ajuda mínima | Explicar a interface, ler rótulos em voz alta, apontar a tela antes do limite de 3 minutos |
| Observador (O) | **Opcional.** Um integrante escalado por sessão, registrado em `sessoes.csv` (`-` quando não houver) | Preenche a ficha de uso de cada elemento com o momento da gravação, cuida da gravação e anota ocorrências | Falar com o participante durante as tarefas |
| Terceiro (A3) | Integrante que não esteve na sessão | Decide divergências de classificação que C e O não resolverem, olhando só a gravação e o gabarito | Ver a ficha de C ou de O antes de decidir |
| Avaliadores de teclado (K1, K2) | Dois integrantes | Executam M2.6.1 de forma independente | Consultar a ficha do outro antes de enviar a sua |
| Avaliadores de contraste (A1, A2) | Dois integrantes, pelo menos um sem ter lido o código | Executam M2.6.2 de forma independente | Consultar a ficha do outro antes de enviar a sua |

A relação entre os códigos (C, O, K1, K2, A1, A2, A3) e as pessoas fica em `coleta.md` de cada pasta, sem dado do participante.

**Sessão sem observador.** O condutor não preenche a ficha durante as tarefas, para não desviar a atenção do participante. No mesmo dia, ele preenche `observacao-uso.csv` a partir da gravação e cuida sozinho do hash, do envio ao Drive e de `sessoes.csv`. A segunda classificação das explicações (coluna `classificacao_o`) é feita por outro integrante, que não conduziu a sessão, a partir da gravação e do gabarito, sem ver a classificação de C. Esse segundo classificador não pode ser o A3 da mesma sessão.

**Conhecimento exigido dos condutores e avaliadores.** C, e O quando houver, leem esta página e os instrumentos, conduzem ou assistem ao piloto (ao vivo ou pela gravação) e conhecem o gabarito antes da primeira sessão. K1 e K2 sabem navegar por teclado no Chrome e conhecem os critérios 2.1.1, 2.4.7 e 2.5.8 da WCAG 2.2. A1 e A2 sabem rodar o axe, usar o seletor de cor do DevTools e conhecem o critério 1.4.3 da WCAG 2.2.

### 3.3 Tema dado ao participante

Nas sessões, o tema foi outro, pelo ajuste da [seção 2.9](#29-ajustes-feitos-antes-da-primeira-sessao). Pelo plano, o participante cria o projeto sobre o **tema T1 do G1** (fármaco com desfecho clínico bem estudado, definido no [Método do G1](metodo-g1.md)). Na parte B ele abre o projeto já triado desse mesmo tema. Assim as duas partes contam uma história só (o estudante prepara a busca e depois recebe o resultado), e a parte B não exige nenhuma triagem além das que o G1 já faz.

O tema vai no cartão da parte A escrito em uma frase, em linguagem de estudante, igual para todos os participantes, e o cartão também traz os requisitos que obrigam o uso dos 12 elementos (janela de anos, quantidade, bases, acesso aberto). O texto final do cartão é fixado em `M2.7.2/coleta.md` antes do piloto e não muda entre participantes. Se o T1 não estiver triado até a véspera da P01, usa-se o projeto triado mais antigo do G1, com o tema dele no cartão, e a troca é registrada em `coleta.md`.

### 3.4 Contas e créditos por parte da sessão

| Parte da sessão | Conta | Créditos | Cuidado |
|-----------------|-------|:--------:|---------|
| Parte A (F01 a F04) | Conta nova, criada pelo próprio participante durante a sessão, com nome "Participante P0x", e-mail de teste da equipe com sufixo do participante (ex.: `caixa+p01@...`) e senha enviada pelo chat da chamada junto com o cartão A | 0 | Nenhum dado pessoal do participante entra no VICKY. No código consultado (`c2ae570`), conta nova começa sem crédito, então "Criar e iniciar tudo direto" não gasta dinheiro mesmo se clicado por engano; isso é conferido em produção antes do piloto |
| Parte B (F06 a F09) | Conta de cortesia da equipe. Como o participante usa o próprio computador, o condutor envia pelo chat o e-mail da conta e uma senha temporária no início da parte B | 0 consumidos | O projeto triado do G1 só é usado depois que o Top 30 e o log desse projeto foram exportados e guardados em `dados/avaliacao/G1/`. Antes da parte B, o condutor pede que o participante não exclua nem renomeie projetos; se ele tentar, o condutor interrompe e registra a ocorrência. Duas sessões nunca usam a conta de cortesia ao mesmo tempo. Ao fim de cada sessão, o condutor desmarca os favoritos feitos pelo participante e troca a senha, para a próxima sessão começar do mesmo estado |
| M2.6.1 | Conta nova criada pelo próprio K1 (e por K2) no teste de F01, usada para F02 a F04; conta de cortesia para F06 a F09 | 0 | F05 é observada numa triagem já prevista no G1 |
| M2.6.2 | Janela anônima nas telas públicas; conta de cortesia nas internas | 0 | Nenhuma |

As sessões não consomem crédito. A dependência é um projeto triado do G1, como já previsto no [índice da Fase 3](index.md#cobertura-das-metricas).

A caixa de e-mail de teste é criada pela equipe antes do piloto; a senha dela e as senhas das contas ficam fora do repositório. Se a produção exigir confirmação de e-mail para gerar a prévia (o código consultado tem essa opção), o observador confirma o e-mail pela caixa de teste durante a sessão, e o tempo gasto é anotado como ocorrência, sem contar como ajuda.

### 3.5 Limite de prévias por conta e por IP (risco a checar)

No código consultado pela equipe (`c2ae570`), a prévia dos critérios tem limite de 20 por conta e 60 por origem (IP) em 24 horas. A sessão usa de 1 a 3 prévias, e o teste de teclado mais 1 ou 2 por avaliador, o que fica longe do limite por conta. O risco está no limite por IP:

- a etapa E08 da [inspeção](metodo-g2-inspecao.md#m222-e-m232-inventarios-de-mensagens) esgota de propósito a cota de uma conta e, se feita na mesma rede, consome cerca de 20 prévias da origem;
- redes da universidade costumam sair para a internet por poucos IPs compartilhados.

Por isso: (1) antes do piloto, o condutor confere em produção o limite vigente e anota em `M2.7.2/coleta.md`; (2) na sessão remota, o participante usa a própria rede, que não é a da universidade nem a da equipe, e por isso a regra da versão 0.5 de rotear pelo celular do condutor deixou de ser necessária; (3) no máximo três sessões por dia, sem sobreposição de horário, por causa da conta de cortesia (seção 3.4).

### 3.6 Termo, gravação e anonimização

| Item | Regra |
|------|-------|
| Termo | [Termo de consentimento](termo-de-consentimento.md), lido em voz alta pelo condutor no início da chamada, antes de qualquer acesso ao VICKY. O aceite, com a opção de gravação, é registrado num formulário online curto (nome, data, aceite e opção de gravação), enviado pelo chat; a resposta fica na pasta restrita, e o participante recebe uma cópia por e-mail. Sem aceite, inclusive da gravação, não há sessão. No formulário de estética, o termo aparece na primeira página e o aceite é uma caixa obrigatória, sem nome nem e-mail |
| O que se grava | Tela compartilhada pelo participante e voz, sem câmera. Gravador: a gravação do próprio Google Meet, se a conta usada permitir, ou o OBS Studio no computador do condutor, capturando a janela da chamada, o áudio do sistema e o microfone. O participante é orientado a manter a câmera desligada |
| Teste da gravação | 10 segundos gravados e reproduzidos pelo condutor antes do aceite, e conferência do arquivo no fim |
| Nome do arquivo | `P0x_AAAAMMDD`, com a extensão do gravador (`.mkv` no OBS, `.mp4` no Meet), sem nome de pessoa |
| Guarda | Logo após a sessão, o observador (ou o condutor, se não houver observador) calcula o hash (`shasum -a 256 P0x_AAAAMMDD.mkv`), envia o arquivo para a pasta restrita no Google Drive da equipe, compartilhada só com os seis integrantes e com a professora, e apaga a cópia local. Gravação feita pelo Meet é movida do Drive de quem gravou para a pasta restrita |
| Repositório público | Recebe só o registro: código do participante, data, duração e hash SHA-256 do arquivo (`M2.7.2/sessoes.csv`), mais as respostas e anotações anonimizadas. Nenhum vídeo, áudio ou aceite entra no repositório |
| Aceites | As respostas do formulário de aceite ficam numa subpasta separada da pasta das gravações, no mesmo Drive restrito. A ligação entre nome e código (P01 a P05) existe só no aceite. O formulário de estética não coleta nome, e por isso não há ligação entre pessoa e código R |
| Anonimato na tela | O participante usa o nome "Participante P0x" e o e-mail de teste, abre o VICKY numa janela anônima e compartilha só essa janela, quando o navegador permitir, para não expor favoritos, contas ou notificações. Voz não é anonimizável na gravação bruta, e por isso a gravação nunca sai da pasta restrita |
| Transcrição | Trechos citados no repositório e no relatório não trazem nome, instituição, semestre exato nem outro dado que identifique o participante |
| Prazo | Gravações, aceites e respostas brutas do formulário são excluídos ao fim do semestre 2026/2. A exclusão é registrada em `M2.7.2/coleta.md` |
| Desistência | Se o participante pedir, a gravação e as respostas dele são apagadas, e a linha em `sessoes.csv` fica só com o motivo `retirado`. No formulário de estética, que não tem nome, a resposta só pode ser apagada depois do envio se o respondente informar a data e a hora aproximadas do envio |

### 3.7 Ambiente da sessão

| Item | Valor |
|------|-------|
| Local | Remoto, pelo Google Meet, com o participante num lugar silencioso de sua escolha. Em `sessoes.csv`, `local = remoto` |
| Computador do participante | O próprio notebook ou desktop (celular e tablet não servem, porque a Fase 2 fixa a sessão em desktop), navegador atualizado em janela anônima, zoom de 100% e janela maximizada. Navegador, versão, sistema e resolução da tela vão para `sessoes.csv`, na coluna `observacao` |
| Computador do condutor | Conta do Meet usada pela equipe, gravador (seção 3.6), cartões, gabarito, ficha de uso e recortes abertos |
| Rede | A do participante (seção 3.5) |
| Produto | VICKY em produção, <https://vicky.synaptha.com/> |
| Cartões de tarefa | Enviados como texto pelo chat da chamada, no início de cada parte, e lidos em voz alta pelo condutor |
| Na tela, para o questionário | Recortes dos 12 elementos (`M2.7.2/elementos/`), mostrados pelo condutor ao compartilhar a tela dele, um de cada vez |

Se a sessão for feita fora desse ambiente (por exemplo, pelo celular), a diferença é registrada em `sessoes.csv` na coluna `observacao`.

### 3.8 Antes da primeira sessão

1. Conferir em produção os rótulos dos 12 elementos e as definições do [gabarito](instrumentos-g2-usuarios.md#4-gabarito-dos-12-elementos), em especial os itens marcados "a confirmar na interface" (E02, E05, E11 e E12), e registrar a conferência em `M2.7.2/coleta.md`. Se uma definição mudar, o gabarito é corrigido antes do piloto e não muda mais. Elemento que não existir em produção sai de B, com registro.
2. Fazer as capturas fixas das 5 telas de M2.5.1 e os recortes dos 12 elementos, na conta de cortesia, com a área visível de 1366 por 768 pixels.
3. Conferir que conta nova começa com 0 crédito e se a prévia exige e-mail confirmado.
4. Conferir o limite de prévias vigente (seção 3.5).
5. Fazer uma sessão piloto completa e remota, no formato da seção 4.1, com uma pessoa que não seja elegível (por exemplo, estudante de outro curso da saúde), gravada para que os condutores que não estiveram nela possam assistir. O piloto calibra o tempo e o texto dos cartões e testa a gravação pelo Meet; seus dados não entram em `dados/`. Mudança no cartão depois do piloto é registrada em `coleta.md`, e o texto fica congelado a partir da P01.
6. Montar o formulário de estética (seção 4.4), conferir que ele não coleta nome nem e-mail, respondê-lo uma vez como teste (resposta apagada depois) e registrar o link e a data de abertura em `M2.5.1/coleta.md`.

## 4. Passo a passo

### 4.1 Sessão remota com o participante (M2.7.2)

Tempo total estimado: 63 minutos, com folga até 75. Os 63 minutos somam os tempos estimados dos blocos, e é essa a duração informada no termo (cerca de 1 hora).

| Bloco | Tempo | Quem | O que acontece | Registro |
|:-----:|:-----:|:----:|----------------|----------|
| 0 | 8 min | C | Acolhida na chamada, pergunta de triagem (inclusive se já respondeu ao formulário de estética), teste da gravação, leitura do termo, dúvidas e aceite no formulário de aceite, com a opção de gravação | Aceite (fora do repositório) |
| 1 | 5 min | C | Início da gravação; o participante abre uma janela anônima e compartilha essa janela; explicação do pensar em voz alta com um exemplo neutro fora do VICKY (por exemplo, contar em voz alta as janelas da própria casa); perguntas do perfil (seção 3.1) | `perfil.csv` |
| 2 | 20 min | Participante | **Parte A**, com o cartão A enviado pelo chat: abrir <https://vicky.synaptha.com/>, criar a conta com os dados do cartão, criar o projeto do tema dado, ajustar o que o cartão pede, ver os critérios antes de gastar crédito e dizer se mudaria algum | Ficha de uso (`observacao-uso.csv`), por O na hora ou por C pela gravação |
| 3 | 15 min | Participante | **Parte B**, com o cartão B enviado pelo chat e a conta de cortesia (seção 3.4): abrir o projeto já triado, interpretar a lista, escolher e favoritar 3 artigos, encontrar onde o VICKY registra como a busca foi feita e por que artigos ficaram de fora, salvar o resultado num arquivo que abra em planilha | Ficha de uso |
| 4 | 12 min | C | Questionário de compreensão (M2.7.2): o condutor compartilha a tela dele e mostra os 12 recortes, um de cada vez, com a pergunta "Com suas palavras, o que é isto e para que serve?" A resposta é falada e gravada; O, ou C pela gravação, anota a resposta literal | `respostas-compreensao.csv` |
| 5 | 3 min | C | Fim da gravação, agradecimento e envio do link do formulário de estética (seção 4.4), que o participante pode responder depois. Depois que ele sai: troca da senha e limpeza dos favoritos da conta de cortesia, hash e envio ao Drive | `sessoes.csv` |

**Regras durante as partes A e B.**

1. O condutor envia o cartão pelo chat, lê o texto em voz alta e diz só: "Faça o que o cartão pede, falando o que você pensa. Eu não posso explicar o site, mas posso ler o cartão de novo."
2. Lembretes permitidos, e só eles: "O que você está pensando agora?", "Continue falando o que pensa", "O que você faria se estivesse sozinho?". Lembrete não é ajuda.
3. **Ajuda** é qualquer informação sobre a interface: apontar a tela, dizer um rótulo, confirmar se o caminho está certo. Só é dada se o participante ficar 3 minutos sem avanço no mesmo passo ou pedir para desistir dele. A ajuda é a mínima (dizer em que região da tela olhar, por exemplo "no alto, à direita") e todo elemento envolvido recebe `uso = com_ajuda`.
4. O observador marca (ou, sem observador, o condutor marca depois, pela gravação), para cada elemento, o código de uso e o momento da gravação (seção 5.2). Se o participante errar e corrigir sozinho, sem ajuda, o uso conta como `sem_ajuda`, com a correção anotada.
5. Tempo-limite: 25 minutos para a parte A e 20 para a parte B. O tempo da tabela (20 e 15 minutos) é o esperado; o limite é o teto, 5 minutos acima de cada estimativa. Se as duas partes chegarem ao limite, a sessão passa de 63 para 73 minutos, dentro da folga de 75; por isso o termo fala em duração aproximada. Esgotado o tempo, o condutor passa ao bloco seguinte, e os elementos não alcançados ficam com `uso = nao_usou`.
6. Se o participante clicar em "Criar e iniciar tudo direto" ou equivalente, ninguém interrompe: a conta não tem crédito. O elemento E08 recebe `uso = incorreto`.
7. Se o participante tentar excluir o projeto da conta de cortesia, o condutor interrompe e registra a ocorrência. Isso não conta como ajuda em nenhum dos 12 elementos.

**Regras do questionário de compreensão.** Os recortes mostram só o rótulo e o controle, sem o texto de ajuda que o VICKY exibe ao lado, para que o participante não leia a resposta. A ordem é a do fluxo (E01 a E12). O condutor pode pedir uma única vez "Pode explicar um pouco mais?". Não comenta se a resposta está certa.

### 4.2 Teste só com teclado (M2.6.1)

Feito por K1 e K2, cada um sozinho, no ambiente da [seção 2.2 da inspeção](metodo-g2-inspecao.md#22-ambiente) (Chrome em computador, 1366 por 768 pixels, zoom de 100%), com o mouse e o trackpad desconectados ou desativados. Teclas permitidas: Tab, Shift+Tab, Enter, Espaço e setas, como na ficha da Fase 2. Se um passo só puder ser feito com outra tecla (por exemplo, Esc para fechar um menu), isso é anotado e o passo conta como não acionável.

**Critério de sucesso.** Uma função conta em A só quando, em **todos** os passos do caminho abaixo:

1. **Acionável:** cada controle do caminho é alcançado e acionado só com as teclas permitidas (WCAG 2.2, critério 2.1.1);
2. **Foco visível:** depois de cada tecla, o avaliador consegue ver, sem procurar, qual controle tem o foco (critério 2.4.7). Foco que some, vai para um elemento invisível ou fica atrás de outro elemento é falha;
3. **Alvo mínimo:** cada controle clicável do caminho tem pelo menos 24 por 24 pixels, medidos no DevTools (seção 4.2.1), salvo as exceções do critério 2.5.8 (espaçamento suficiente, link dentro de frase, controle equivalente na mesma página, controle nativo do navegador sem estilo próprio, apresentação essencial).

| Função | Caminho testado (do início ao resultado) | Conta e momento |
|--------|------------------------------------------|-----------------|
| F01 | Abrir `/signup`, preencher nome, e-mail, senha e confirmação, marcar o aceite, enviar; sair; entrar por `/login`; abrir a recuperação de senha e enviar o pedido | Conta nova de K1 ou K2 |
| F02 | Abrir "Novo projeto", escolher o tipo de revisão, preencher tema e objetivo, escolher a janela de anos, salvar como rascunho | Conta nova |
| F03 | Gerar a prévia dos critérios, chegar aos critérios gerados e editar um deles | Conta nova; gasta 1 prévia |
| F04 | Em novo projeto, marcar e desmarcar cada base, ligar o filtro de acesso aberto e alterar a quantidade do Top | Conta nova |
| F05 | Iniciar a triagem completa, confirmar se houver confirmação e acompanhar o andamento até a lista | Triagem prevista do G1, feita por K1 com o teclado e K2 observando. Combinado com quem executa o G1 |
| F06 | Abrir a lista de artigos do projeto triado, ler o Quality Score de um artigo, abrir a ficha dele e o link da fonte | Conta de cortesia |
| F07 | Favoritar e desfavoritar um artigo na lista e na ficha | Conta de cortesia |
| F08 | Chegar ao registro da busca e dos critérios aplicados (log) do projeto triado | Conta de cortesia |
| F09 | Abrir o menu de exportação e baixar um arquivo em cada formato oferecido | Conta de cortesia |

F05 é observada uma única vez, porque cada triagem custa um crédito; por isso não há segunda execução independente dessa função, e a evidência é a gravação da tela de K1. As demais funções são executadas por K1 e K2.

#### 4.2.1 Como medir o alvo

Com o controle visível, abrir o DevTools (F12, que é tecla do avaliador e não do teste), escolher o controle com o seletor de elementos e ler largura e altura na aba *Computed*. O avaliador mede todo controle do caminho que pareça menor que um ícone comum (setas, estrelas de favorito, "x", links curtos). Abaixo de 24 por 24 pixels, verificar as exceções do critério 2.5.8 e anotar qual se aplica.

**Registro por função** (`M2.6.1/K1.md` e `K2.md`): `funcao`, `passo`, `acionavel (sim/nao)`, `foco_visivel (sim/nao)`, `alvos_abaixo_de_24px` (controle e tamanho), `excecao_2_5_8`, `concluida (sim/nao)`, `captura`.

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

### 4.4 Formulário de estética (M2.5.1)

Formulário online (Google Forms), respondido pelo próprio estudante, pelo celular ou pelo computador, no momento que preferir, do dia de abertura até a data da Fase 4. Leva cerca de 5 minutos. O link vai no convite e, para quem fez a sessão, no fim dela.

| Página | Conteúdo | Obrigatória |
|:------:|----------|:-----------:|
| 1 | Apresentação e texto do termo para o formulário ([termo, seção do formulário](termo-de-consentimento.md#formulario-de-estetica)), com a caixa de aceite | Sim |
| 2 | Triagem: tem 18 anos ou mais; tem matrícula ativa em Medicina; tem vínculo com a Synaptha ou com a equipe do VICKY (sim encerra); "Você já entrou no site do VICKY ou viu alguém usando?", com as opções "não", "sim, só na chamada com a equipe deste trabalho" e "sim, em outra situação" (esta encerra) | Sim |
| 3 a 7 | Uma captura por página, na ordem do fluxo, com a frase e a escala de 1 a 5 do [instrumento](instrumentos-g2-usuarios.md#5-questionario-de-estetica-m251) e um campo de comentário | Nota sim; comentário não |
| 8 | Bloco qualitativo (Q01 a Q10), fora do cálculo | Não |

**Regras.** As capturas são da página inteira, na ordem do fluxo (página inicial, novo projeto, detalhe do projeto, lista de artigos, ficha do artigo). A "página inicial" é o painel que o usuário logado vê (`/dashboard`), e não a página pública de apresentação (`/`): a medida avalia o produto em uso, e a página pública é material de divulgação. As capturas são tiradas da versão em produção antes da abertura do formulário, com a data registrada, porque a produção pode diferir do commit `c2ae570`. A escala do formulário só aceita inteiros de 1 a 5. O formulário não coleta nome nem e-mail; como, sem login, ele não impede duas respostas da mesma pessoa, a página 2 pede que cada um responda uma única vez, e respostas suspeitas de duplicidade (mesmo horário e mesmas notas) são examinadas e registradas em `M2.5.1/coleta.md`.

**Respostas válidas e códigos.** Uma resposta é válida quando tem o aceite, passa pela triagem e traz as cinco notas. As válidas recebem os códigos R01, R02 e assim por diante, na ordem de envio. O formulário é encerrado quando chega a cinco respostas válidas; válidas que chegarem antes do encerramento, além da quinta, ficam registradas em `M2.5.1/coleta.md` e fora do cálculo, que usa as cinco primeiras por ordem de envio. Respostas inválidas não recebem código e ficam só contadas em `coleta.md`.

**Registro.** A planilha de respostas do Forms fica na pasta restrita. Para o repositório vão só as linhas válidas, em `M2.5.1/respostas.csv` (uma linha por respondente e tela) e `M2.5.1/qualitativo.csv`, com o código R0x, sem carimbo de horário.

## 5. Registro

### 5.1 Arquivos de cada pasta

```text
dados/avaliacao/G2/
├── termo-de-consentimento.docx   # termo em branco para imprimir
├── M2.5.1/
│   ├── coleta.md                 # link e datas do formulário, data das capturas, respostas inválidas ou excedentes
│   ├── respostas.csv             # participante (R01 a R05), tela, nota (1 a 5), comentario
│   ├── qualitativo.csv           # bloco opcional, fora do cálculo
│   ├── consolidado.md            # tela agradável por respondente e cálculo (acrescentado com a D14)
│   └── telas/                    # as 5 capturas fixas mostradas aos participantes
├── M2.6.1/
│   ├── coleta.md                 # data, Chrome, área visível, papéis K1 e K2, projeto triado usado
│   ├── K1.md e K2.md             # ficha por função e passo
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
| `sessoes.csv` | `participante`, `data`, `inicio`, `fim`, `duracao_min`, `local`, `condutor`, `observador`, `arquivo_gravacao`, `sha256`, `termo_assinado`, `gravacao_autorizada`, `situacao`, `observacao` | `situacao`: `valida`, `interrompida`, `retirado` ou `piloto_descartado`; `local`: `remoto`; `observador`: `-` quando não houver; `termo_assinado`: `sim` quando o aceite foi registrado |
| `perfil.csv` | `participante`, `faixa_curso`, `fez_revisao`, `usou_ferramenta_triagem` | `faixa_curso`: `1-4`, `5-8` ou `internato` |
| `observacao-uso.csv` | `participante`, `elemento`, `uso`, `momento_gravacao`, `observacao` | `uso`: `sem_ajuda`, `com_ajuda`, `incorreto` ou `nao_usou` |
| `respostas-compreensao.csv` | `participante`, `elemento`, `resposta_literal`, `classificacao_c`, `classificacao_o`, `classificacao_final`, `decidido_por` | `classificacao_*`: `correta` ou `incorreta`; `decidido_por`: `consenso` ou `A3` |
| `M2.5.1/respostas.csv` | `participante`, `tela`, `nota`, `comentario` | `participante`: R01 a R05; `tela`: `inicial`, `novo_projeto`, `detalhe_projeto`, `lista_artigos`, `ficha_artigo`; `nota`: 1 a 5 |
| `M2.5.1/qualitativo.csv` | `participante`, `afirmacao`, `nota` | `afirmacao`: Q01 a Q10 |

`classificacao_c` e `classificacao_o` são preenchidas separadamente, depois da sessão, por C e por O (ou, sem observador, pelo segundo classificador da seção 3.2), cada um sem ver a do outro (seção 7).

## 6. Cálculo

As fórmulas estão nas [fichas da Fase 2](../fase-2/especificacao-das-metricas.md) e os níveis em [níveis de pontuação](../fase-2/niveis-e-julgamento.md). M2.7.2 usa só sessões com `situacao = valida` e é calculada com três sessões válidas, ou com cinco, se houver. Com quatro, usam-se as três primeiras em ordem cronológica, porque a maioria de quatro admite empate (2 a 2). M2.5.1 usa as cinco primeiras respostas válidas do formulário, na ordem dos códigos R01 a R05 (seção 4.4); o script `dados/avaliacao/G2/calcular_g2_usuarios.py` lê `M2.5.1/respostas.csv` e usa os cinco primeiros códigos, ou todos, quando há menos de cinco. Na coleta de 2026/2, que teve só três respostas, a M2.5.1 foi calculada com as três e com maioria de 2 de 3, pela [D14](../gestao/decisoes.md#d14-calcular-m251-com-as-tres-respostas-obtidas) (seção 2.10).

| Métrica | Regra por item | A | B | Regra especial nos níveis |
|---------|----------------|---|---|---------------------------|
| M2.5.1 | Tela agradável para o participante quando `nota` é 4 ou 5 | Telas agradáveis para pelo menos 3 dos 5 respondentes | 5 | - |
| M2.6.1 | Função com `concluida = sim` no `consolidado.md` | Funções concluídas | 9 | F01 não concluída leva a Insatisfatório |
| M2.6.2 | Par aprovado pelo axe ou aprovado na conferência manual | Soma, nas 8 telas, de `aprovados_axe` e `incertos_aprovados_manual` | Soma, nas 8 telas, de aprovados, violações e incertos | - |
| M2.7.2 | Elemento entendido pelo participante quando `uso = sem_ajuda` **e** `classificacao_final = correta` | Elementos entendidos pela maioria dos participantes válidos: pelo menos 2 de 3 (ou 3 de 5) | 12, menos elementos que não existam em produção (seção 3.8) | Quality Score (E10) não entendido pela maioria (2 de 3, ou 3 de 5) leva a Insatisfatório, qualquer que seja X |

A regra de M2.7.2 vem da proposta original do roteiro (respostas acertadas pela maioria compõem A, o que era 3 de 5 até a versão 0.5) e acrescenta a condição de uso sem ajuda que a ficha da Fase 2 exige.

Com três participantes, o resultado de M2.7.2 é **indicativo**: a decisão sobre cada elemento depende de um único participante, e a Fase 4 apresenta o valor com essa ressalva (seção 2.8).

Exemplo de leitura: se o Quality Score for entendido por 1 dos 3 participantes e outros 10 elementos por 2 ou mais, X = 10/12 = 83%, que cairia em Bom, mas a regra especial leva M2.7.2 a Insatisfatório.

O valor, o nível e a evidência são publicados na Fase 4. Os limiares não mudam depois da coleta. As hipóteses H2.5, H2.6 e H2.7 são comparadas com os valores medidos, sem efeito no julgamento.

## 7. Discordância e repetição

### 7.1 Classificação das explicações (M2.7.2)

1. Depois da sessão, C e O (ou C e o segundo classificador, seção 3.2) classificam sozinhos cada resposta como `correta` ou `incorreta`, usando só o gabarito. Correta é a resposta que traz o ponto essencial do elemento e não comete o erro que invalida, conforme o [gabarito](instrumentos-g2-usuarios.md#4-gabarito-dos-12-elementos). Vocabulário diferente do da tela não torna a resposta incorreta.
2. Se concordam, a classificação é final, com `decidido_por = consenso`.
3. Se divergem, os dois ouvem de novo o trecho da gravação e reaplicam o gabarito. Sem acordo, A3 ouve o trecho e decide, com `decidido_por = A3`.
4. Se a divergência vier de gabarito ambíguo, a interpretação adotada é escrita em `M2.7.2/coleta.md` e reaplicada às respostas de todos os participantes para aquele elemento.

O código de uso (`observacao-uso.csv`) é conferido pelo condutor com a gravação no mesmo dia, ou preenchido por ele pela gravação quando não houver observador; divergência entre o registro do observador e a gravação se resolve pela gravação.

### 7.2 Notas de estética (M2.5.1)

A nota é do respondente e não passa por classificação. No formulário a nota é obrigatória; se, por erro de configuração, alguma tela ficar sem nota, ela conta como "não agradável" para aquela tela, que é a leitura conservadora, e o caso fica registrado em `M2.5.1/coleta.md`.

### 7.3 Teclado e contraste (M2.6.1 e M2.6.2)

Seguem a [regra da inspeção](metodo-g2-inspecao.md#6-discordancia-e-repeticao): fichas enviadas ao repositório antes da comparação, divergência resolvida sobre a evidência, A3 sem consenso, resultado sim ou não por item, sem média.

Em M2.6.2, as contagens do axe-core devem coincidir entre A1 e A2, porque a ferramenta é determinística. Se não coincidirem, a causa é o estado da tela (menu aberto, aviso, conteúdo diferente). Os dois rodam de novo, juntos, no estado da tabela da seção 4.3, e vale essa execução. Nos pares incertos, a divergência se resolve medindo juntos no mesmo ponto do fundo.

Em M2.6.1, uma função em que K1 e K2 divergem é executada de novo pelos dois juntos, com gravação da tela, e vale o que a gravação mostra.

### 7.4 Quando a sessão não termina como previsto

| Situação | O que fazer |
|----------|-------------|
| Participante desiste no meio | A sessão para na hora, sem insistência. Pergunta-se se ele autoriza o uso do que foi gravado só como registro de ocorrência; os dados não entram no cálculo. `situacao = retirado` ou `interrompida`. Convida-se uma reserva |
| VICKY fora do ar ou prévia bloqueada antes do fim da parte A | Sessão interrompida. O participante já viu o produto e não pode repetir. Convida-se uma reserva, e a causa vai para `coleta.md` |
| Falha da gravação percebida no fim | Sessão interrompida, porque sem gravação as explicações não podem ser conferidas. Convida-se uma reserva |
| Tempo-limite de uma parte esgotado | A sessão continua; os elementos não alcançados ficam com `nao_usou` e contam como não entendidos para esse participante |
| Participante revela durante a sessão que já usou o VICKY ou já respondeu ao formulário de estética | Sessão interrompida por critério de exclusão; reserva |
| Queda da chamada ou da internet do participante | Antes da parte A, a sessão é remarcada. Depois, retoma-se na mesma chamada em até 10 minutos, do passo em que parou, com o tempo parado anotado em `observacao`; se não voltar, a sessão é interrompida e chama-se uma reserva |
| Mudança visível em produção entre sessões | Registrar a data em `coleta.md`. Se a mudança atingir um dos 12 elementos ou uma das 5 telas, as sessões anteriores e posteriores não são comparáveis naquele item, e o caso é declarado na Fase 4 |
| Menos de três sessões válidas até a data da Fase 4 | **Não calcular** M2.7.2. Não se aplica proporção sobre dois participantes. O desvio é registrado em `M2.7.2/coleta.md` e declarado na Fase 4 como métrica não coletada, sem nível por estimativa |
| Menos de cinco respostas válidas no formulário até a data da Fase 4 | **Não calcular** M2.5.1, pelo mesmo motivo. O desvio é registrado em `M2.5.1/coleta.md` e declarado na Fase 4. Exceção em 2026/2: a D14 calculou a métrica com três respostas (seção 2.10) |
| Falha no teste de teclado por causa externa | Repetir em outro horário. Persistindo, a função fica `nao_coletado`, sai de B e é declarada na Fase 4 |

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 04/11/2026 | Criação da página | Lucas Avelar | - |
| 0.2 | 09/11/2026 | Esqueleto com o que a Fase 2 define e os pontos em aberto para o responsável | Gabriel Fae | - |
| 0.3 | 14/11/2026 | Método completo: justificativa, recrutamento, papéis, contas, limite de prévias, termo e anonimização, roteiro da sessão com tempos, teste com teclado, passo a passo do axe, registro, cálculo e repetição. Incorpora o roteiro de M2.7.2 e o questionário qualitativo escritos por João Felipe Oliveira | Lucas Avelar e João Felipe Oliveira | - |
| 0.4 | 14/11/2026 | Códigos P06 e P07 para as reservas e relação entre o tempo estimado das partes A e B, o tempo-limite e a duração informada no termo | Lucas Avelar | - |
| 0.5 | 15/11/2026 | Definição dos lembretes neutros no papel do condutor e "Idem" trocado pelo texto, a partir da revisão do João Felipe | Lucas Avelar | - |
| 0.6 | 19/11/2026 | Adaptação pela D13, antes de qualquer sessão: M2.5.1 em formulário online assíncrono (seção 4.4); M2.7.2 em sessão remota pelo Meet, de cerca de 1 hora, com 3 participantes válidos e regra da maioria; condutor sem nome fixo e observador opcional; seção 2.8 com alternativas descartadas e ameaças à validade | Gabriel Fae | - |
| 0.7 | 22/11/2026 | Seção 2.9 com os ajustes feitos antes da primeira sessão: tema das células-tronco, conta da equipe com créditos nas partes A e B e sessões sem piloto | Gabriel Fae | - |
| 0.8 | 22/11/2026 | Seção 2.10 com a execução das três sessões e do formulário: sessões sem observador, durações, registro das explicações, recortes montados depois e M2.5.1 calculada com três respostas pela D14 | Gabriel Fae | - |
| 0.9 | 22/11/2026 | Seção 2.10 com as marcações por padrão das P02 e P03 e o cartão A sem frase de objetivo, com o uso de E02 de P01 e P02 corrigido pela gravação; seção 6 alinhada ao script quanto às respostas usadas na M2.5.1 (revisão do PR #40) | Gabriel Fae | - |
