# M2.2.2: Inventário das mensagens de erro

> Etapa 1, feita por A1 em 17/11/2026. Mensagens de erro do fluxo de F01 a F09. Fora: compra de créditos (F10) e configurações (F11). Este arquivo é o texto entregue a A2: **sem caminho de arquivo nem trecho de código**. Os caminhos ficam em `codigo-a1.md`, que A2 só abre depois de enviar `A2.md`.
>
> Textos iguais em lugares diferentes contam uma vez (os lugares vão em `gatilho`). Texto com variável conta uma vez. Se produção e código divergirem, vale produção e a diferença é anotada em `observacao`.
>
> A2 recebeu este inventário em 17/11 como `inventario.csv` (branch `docs/fase-3-cronograma-e-correcoes-e1`), com os mesmos `id`, textos e gatilhos.

`tipo`: `erro`. `origem`: `servidor`, `navegador` ou `inventario`.

Na coluna `texto`, `//` separa linhas da mesma caixa, `{...}` marca parte variável e `[...]` descreve botão ou trecho omitido. `origem` diz de onde vem o texto: `servidor` (VICKY) ou `navegador` (validação nativa do Chrome).

| id | tipo | texto | funcao | gatilho | origem | observacao |
|---|---|---|---|---|---|---|
| ERR01 | erro | Informe seu nome. | F01 | Cadastro com o nome preenchido só com espaços (nome vazio é barrado antes pelo navegador) | servidor |  |
| ERR02 | erro | E-mail inválido. | F01 | Cadastro com e-mail que tem @ mas não tem ponto depois dele (ex.: nome@gmail) | servidor |  |
| ERR03 | erro | A senha deve ter ao menos 8 caracteres. | F01 | Cadastro ou redefinição de senha com menos de 8 caracteres | servidor | Em produção (17/11) quem responde é o navegador, com o balão "Aumente este texto para 8 caracteres ou mais. No momento, você está usando 5 caracteres)."; o texto do servidor não chega a aparecer |
| ERR04 | erro | As senhas não coincidem. | F01 | Cadastro com senha e confirmação diferentes | servidor |  |
| ERR05 | erro | Para criar a conta e preciso aceitar os Termos de Uso e a Politica de Privacidade. | F01 | Cadastro sem marcar a caixa de aceite dos Termos | servidor |  |
| ERR06 | erro | Este e-mail já está cadastrado. | F01 | Cadastro com e-mail de uma conta que já existe | servidor |  |
| ERR07 | erro | E-mail ou senha incorretos. | F01 | Login com senha errada ou com e-mail sem conta | servidor |  |
| ERR08 | erro | Esse link de confirmação expirou. Entre e peca um novo. | F01 | Abrir o link de confirmação de e-mail depois de 48 horas (aparece na tela de login) | servidor |  |
| ERR09 | erro | Link de confirmação inválido. | F01 | Abrir um link de confirmação adulterado ou de um e-mail que foi trocado (aparece na tela de login) | servidor |  |
| ERR10 | erro | Já mandei alguns links agora há pouco. Confira a caixa de entrada e o spam, e tente de novo daqui a uma hora. | F01 | Painel: pedir o reenvio do link de confirmação mais de 3 vezes em 1 hora | servidor |  |
| ERR11 | erro | Não consegui enviar o e-mail agora. Tente de novo em alguns minutos. | F01 | Painel: pedir o reenvio do link quando o envio de e-mail falha | servidor |  |
| ERR12 | erro | Informe o e-mail da sua conta. | F01 | Esqueci minha senha com e-mail sem @ | servidor |  |
| ERR13 | erro | Muitos pedidos de redefinição em pouco tempo. Espere uma hora e tente de novo. | F01 | Esqueci minha senha: mais de 3 pedidos para o mesmo e-mail (ou 10 da mesma rede) em 1 hora | servidor |  |
| ERR14 | erro | Esse link de redefinição expirou. Ele vale por 60 minutos. [botão: Pedir um link novo] | F01 | Abrir o link de redefinição de senha depois de 60 minutos | servidor |  |
| ERR15 | erro | Esse link de redefinição não vale mais: ele já foi usado, a senha foi trocada depois que ele saiu, ou o endereço chegou incompleto. [botão: Pedir um link novo] | F01 | Abrir um link de redefinição já usado, antigo ou incompleto | servidor |  |
| ERR16 | erro | A confirmação não é igual à senha nova. | F01 | Redefinir senha com confirmação diferente da senha nova | servidor |  |
| ERR17 | erro | Confirme seu e-mail para gerar a pré-visualização. Reenviamos o link se você pedir no painel. | F03 | Pré-visualizar critérios com o e-mail ainda não confirmado, quando o VICKY exige confirmação | servidor |  |
| ERR18 | erro | Limite de 20 pré-visualizações por dia atingido. Inicie o pipeline ou tente amanhã. | F03 | Pedir a 21ª pré-visualização de critérios em 24 horas (é o E08 do roteiro) | servidor |  |
| ERR19 | erro | Você já gerou muitas pré-visualizações hoje. Inicie o pipeline ou tente amanhã. | F03 | Pedir mais de 60 pré-visualizações em 24 horas na mesma conta, contando as de projetos já excluídos | servidor |  |
| ERR20 | erro | Limite de pré-visualizações por dia atingido nesta rede. Inicie o pipeline ou tente amanhã. | F03 | Mais de 60 pré-visualizações em 24 horas vindas da mesma rede, somando todas as contas | servidor |  |
| ERR21 | erro | ⚠️ Sem créditos // Se continuar, escreva para vickyangel@gmail.com. [botão: Comprar créditos] | F05 | Iniciar a triagem completa (ou "Criar e iniciar tudo direto") com saldo zero | servidor |  |
| ERR22 | erro | ⚠️ Erro no pipeline: Sem créditos | F05 | Triagem ou prévia interrompida porque o serviço de IA usado pelo próprio VICKY ficou sem saldo (não é o saldo do estudante) | servidor |  |
| ERR23 | erro | ⚠️ Erro no pipeline: Discovery falhou: {nome técnico do erro} | F03 | Falha interna na geração dos critérios PICO | servidor |  |
| ERR24 | erro | ⚠️ Erro no pipeline: Análise falhou em {x}/{total} artigos. Último erro: {texto técnico do erro} | F05 | Triagem interrompida quando a análise falha em todos os artigos | servidor |  |
| ERR25 | erro | ⚠️ Erro no pipeline: {texto técnico do erro} | F05 | Qualquer outra falha não prevista durante a triagem | servidor |  |
| ERR26 | erro | ⚠️ Erro no pipeline: Workspace não encontrado | F05 | Triagem iniciada num projeto cujo espaço de trabalho não existe mais | servidor |  |
| ERR27 | erro | ⚠️ {texto técnico do erro} // Se continuar, escreva para vickyangel@gmail.com. | F05 | Falha ao parar a triagem | servidor |  |
| ERR28 | erro | Não passou: {lista das verificações reprovadas} | F08 | Painel "Pipeline" do projeto: a etapa "Verificação final (checklist)" reprova | servidor |  |
| ERR29 | erro | {TipoDoErro}: {mensagem técnica} | F08 | Painel "Pipeline": uma etapa da triagem falha | servidor |  |
| ERR30 | erro | iter{n} {base}: erro {mensagem técnica} | F08 | Painel "Pipeline": falha numa rodada de expansão da busca | servidor |  |
| ERR31 | erro | Página não encontrada // Esta página não existe // O endereço que você acessou não existe ou foi removido. Pode ser um link antigo ou um typo. [botões: Voltar ao Dashboard, Ver projetos] | F02 | Abrir projeto ou artigo que não existe, foi excluído ou é de outra conta | servidor |  |
| ERR32 | erro | Acesso negado // Você não tem permissão // Esta área é restrita. Se você acredita que deveria ter acesso, fale com o administrador do workspace. [botão: Voltar ao Dashboard] | F02 | Ação que a conta não tem permissão de fazer | servidor |  |
| NAV01 | erro | Preencha este campo. | F01 | Balão do navegador ao enviar um formulário com campo obrigatório em branco (visto no cadastro, no E01) | navegador | Acrescentada por A1 na etapa 4: mensagem do navegador vista em produção, que não vem do código do VICKY |
