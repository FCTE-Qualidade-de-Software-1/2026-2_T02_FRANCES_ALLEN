# Instrumentos do G2 com usuários

Instrumentos aplicados aos estudantes conforme o [Método do G2 com usuários](metodo-g2-usuarios.md): na sessão remota, os cartões de tarefa e a ficha de uso (M2.7.2) e o questionário de compreensão com o gabarito (M2.7.2); no formulário online assíncrono, o questionário de estética (M2.5.1) e o bloco qualitativo opcional. Desde a versão 0.6 do método ([D13](../gestao/decisoes.md#d13-adaptar-a-coleta-com-usuarios-ao-prazo-da-entrega-2)), o questionário de estética não é mais aplicado na sessão. O texto dos cartões e das perguntas é lido igual para todos os participantes.

Os rótulos citados vêm das telas do VICKY no código-fonte do fork usado pela equipe (commit `c2ae570`, de 29/09/2026) e da descrição das funções na [Fase 1](../fase-1/objeto-de-avaliacao.md#3-principais-funcionalidades). Como a produção pode ter mudado desde esse commit, cada rótulo e cada definição do gabarito são conferidos em produção antes do piloto, e a conferência é registrada em `dados/avaliacao/G2/M2.7.2/coleta.md`.

## 1. Cartões de tarefa (M2.7.2)

Os cartões descrevem a necessidade do estudante sem usar o nome dos controles do VICKY. É isso que obriga o participante a encontrar e entender cada elemento sozinho. Na sessão remota, o condutor envia o texto de cada cartão pelo chat da chamada, já com o e-mail e a senha preenchidos, e o lê em voz alta.

### Cartão A: preparar a busca

> **Situação.** Você vai fazer o seu TCC, que será apresentado em banca, e precisa de uma primeira lista de artigos para mostrar ao orientador. Use o VICKY para preparar essa busca. Fale em voz alta o que está pensando.
>
> **Tema:** O uso de células-tronco para restauração de tecido.
>
> 1. Entre no VICKY com o e-mail e a senha que estão abaixo.
> 2. Crie um projeto para o seu tema. Você quer:
>     - registrar no projeto o que você quer descobrir com a revisão;
>     - só artigos publicados nos últimos 5 anos;
>     - no máximo 15 artigos na lista final;
>     - procurar só no PubMed e na SciELO;
>     - só artigos que você consiga ler inteiros sem pagar.
> 3. Antes de gastar qualquer crédito, veja quais critérios o VICKY vai usar para escolher os artigos e diga se você mudaria algum.
>
> E-mail: ______________________ Senha: ______________

Antes da primeira sessão (19/11/2026), o tema passou a ser o acima, e o passo 1, que pedia criar uma conta nova, passou a ser a entrada numa conta da equipe, a mesma da parte B ([método, seção 2.9](metodo-g2-usuarios.md#29-ajustes-feitos-antes-da-primeira-sessao)). A versão anterior do cartão trazia também uma frase de objetivo, a do desfecho do tema T1 do G1; com a troca de tema, nenhuma frase de objetivo foi fixada, e o chat das sessões trouxe só o tema e os dados de acesso (P01) ou só o link e os dados de acesso (P02 e P03). Sem a frase, o participante decide sozinho o que escrever no campo de objetivo (E02), e o efeito disso na marcação de uso está em [método, seção 2.10](metodo-g2-usuarios.md#210-execucao-das-sessoes-e-do-formulario).

Os valores pedidos (5 anos, 15 artigos, duas bases, só texto gratuito) foram escolhidos diferentes dos valores padrão da tela, para que o participante precise mexer em cada controle. No código consultado, o padrão é 10 anos, 20 artigos, as três bases marcadas e o filtro desligado.

### Cartão B: usar o resultado

> **Situação.** Um colega já rodou a busca completa sobre o mesmo tema e deixou o resultado nesta mesma conta, no projeto de nome igual ao seu tema anterior. Fale em voz alta o que está pensando.
>
> 1. Escolha os 3 artigos que você levaria primeiro ao orientador e diga por que escolheu esses. Marque os 3 para encontrá-los fácil depois.
> 2. Seu orientador quer saber como a busca foi feita e por que alguns artigos ficaram de fora. Mostre onde o VICKY registra isso.
> 3. Salve o resultado no computador, num arquivo que você consiga abrir numa planilha.

## 2. Ficha de uso dos 12 elementos (observador)

O observador registra, para cada elemento, um código de uso em `observacao-uso.csv`, com o momento da gravação. Quando não há observador, o condutor faz o mesmo registro depois da sessão, a partir da gravação. O uso é correto quando o participante faz o que a coluna "Uso correto" descreve.

| ID | Elemento (lista B da Fase 2) | Tarefa | Uso correto | Exemplo de uso incorreto |
|----|------------------------------|:------:|-------------|--------------------------|
| E01 | Campo do tema | A2 | Escreve o tema do cartão no campo do tema | Escreve o tema no campo de objetivo |
| E02 | Campo de objetivo | A2 | Escreve o que quer descobrir no campo de objetivo | Deixa vazio ou repete o tema por não saber o que é |
| E03 | Tipo de revisão (sistemática ou narrativa) | A2 | Escolhe revisão sistemática, coerente com TCC apresentado em banca | Escolhe narrativa ou não percebe a escolha |
| E04 | Janela de anos | A2 | Ajusta para os últimos 5 anos | Mantém o padrão sem perceber |
| E05 | Quantidade do Top | A2 | Ajusta para 15 | Mantém 20 ou entende como número de artigos buscados |
| E06 | Escolha das bases | A2 | Deixa marcados só PubMed e SciELO | Mantém o Google Acadêmico marcado |
| E07 | Filtro de acesso aberto | A2 | Liga o filtro de texto completo gratuito | Não liga, ou procura o filtro depois da triagem |
| E08 | Diferença entre salvar rascunho, gerar prévia e iniciar a triagem | A3 | Gera a prévia dos critérios, sem iniciar a triagem | Clica em iniciar a triagem, ou só salva o rascunho e acha que terminou |
| E09 | Critérios PICO gerados | A3 | Encontra os critérios gerados, lê e comenta se mudaria algum | Não encontra os critérios ou comenta outro conteúdo |
| E10 | Quality Score | B1 | Usa o número como medida de qualidade para ordenar ou escolher entre os incluídos | Trata o número como chance de o artigo ser relevante ou como o que decidiu a inclusão |
| E11 | Log auditável | B2 | Chega ao registro das buscas e dos critérios ou dos motivos de exclusão | Mostra só a lista de artigos ou desiste |
| E12 | Exportação | B3 | Baixa um arquivo do projeto num formato de planilha | Copia a tela, imprime ou baixa um formato que não abre em planilha sem perceber |

Códigos de uso: `sem_ajuda` (uso correto sem ajuda, inclusive depois de corrigir um erro sozinho), `com_ajuda`, `incorreto` (terminou a tarefa com o uso errado) e `nao_usou`.

## 3. Questionário de compreensão (M2.7.2)

Aplicado depois das partes A e B. Para cada elemento, o condutor compartilha a tela dele e mostra o recorte da tela (rótulo e controle, sem o texto de ajuda ao lado) e pergunta:

> **"Com suas palavras, o que é isto e para que serve?"**

Só para E08 a pergunta muda, porque o elemento é a diferença entre três botões, mostrados juntos:

> **"Qual é a diferença entre estes três botões?"**

O condutor pode pedir uma vez "Pode explicar um pouco mais?" e não diz se a resposta está certa. A resposta é falada; o observador (ou o condutor, pela gravação) anota a parte essencial em `respostas-compreensao.csv`, e a gravação é a evidência.

| Ordem | ID | Recorte mostrado (rótulo no código `c2ae570`) |
|:-----:|----|-----------------------------------------------|
| 1 | E01 | "Tema da pesquisa *" e o campo |
| 2 | E02 | "Objetivo (opcional)" e o campo |
| 3 | E03 | "1. Tipo de revisão" com as opções "Revisão sistemática" e "Revisão narrativa / artigo de resumo", só os títulos |
| 4 | E04 | "Janela temporal" e a lista |
| 5 | E05 | "Meta de artigos no Top final" e o campo, sem o texto explicativo |
| 6 | E06 | "3. Onde buscar" com as três bases, só os nomes |
| 7 | E07 | "Só artigos com texto completo gratuito", só o título |
| 8 | E08 | Os botões "Salvar como rascunho", "Pré-visualizar critérios" e "Criar e iniciar tudo direto", sem as legendas "grátis" e "consome 1 crédito" |
| 9 | E09 | Bloco dos critérios PICO gerados no projeto, mostrando os quatro rótulos |
| 10 | E10 | O número do Quality Score de um artigo na lista, sem a explicação do topo da lista |
| 11 | E11 | O lugar do registro das buscas e critérios no detalhe do projeto (a confirmar na interface, ver gabarito) |
| 12 | E12 | O botão "Exportar" fechado |

Os recortes estão em `dados/avaliacao/G2/M2.7.2/elementos/` (`E01.png` a `E12.png`). Foram montados em 22/11/2026, depois das sessões, com as capturas de produção da inspeção do G2, sem o texto de ajuda ao lado; a origem e o ajuste de cada um estão em `M2.7.2/coleta.md` ([método, seção 2.10](metodo-g2-usuarios.md#210-execucao-das-sessoes-e-do-formulario)). Em produção, o bloco de E09 é o painel "Critérios PICO + Strings de busca (geradas pela IA)", que mostra o protocolo de triagem sem os rótulos P, I, C e O, e o lugar de E11 são os painéis "Pipeline" e "Critérios PICO + Strings de busca" da tela do projeto.

## 4. Gabarito dos 12 elementos

Uma resposta é **correta** quando traz o ponto essencial e não comete o erro que invalida. Vocabulário diferente do da tela não torna a resposta errada; detalhe a mais também não, desde que não contradiga o ponto essencial.

| ID | Ponto essencial (precisa aparecer) | Erro que invalida | Base no VICKY |
|----|------------------------------------|-------------------|---------------|
| E01 | É o assunto da pesquisa, a partir do qual o VICKY monta os critérios e a busca | Dizer que é só o título ou nome do projeto, sem efeito na busca | Tela de novo projeto: "Seja específico. Quanto mais claro o tema, mais afiados ficam os critérios e melhores são os artigos retornados" |
| E02 | É o que o estudante quer descobrir ou avaliar com a revisão; orienta os critérios | Confundir com o tema ou dizer que é onde se escreve o resumo do trabalho | Tela de novo projeto: campo opcional com exemplo "Avaliar a eficácia clínica e segurança em humanos". Efeito exato sobre os critérios: a confirmar na interface |
| E03 | A escolha muda o rigor dos critérios: a sistemática é mais rigorosa (para trabalho apresentado em banca); a narrativa é mais flexível e aceita revisões e diretrizes | Dizer que muda só o formato do arquivo final ou que não muda nada na seleção | Tela de novo projeto: descrição das duas opções e aviso de que a IA gera critérios diferentes em cada modo |
| E04 | Define o período de publicação dos artigos considerados; mais antigos ficam de fora | Dizer que é o tempo que a busca vai levar | Tela de novo projeto: opções de 3 a 20 anos |
| E05 | É o número máximo de artigos que entram na lista final ranqueada | Dizer que é o número de artigos buscados ou analisados | Tela de novo projeto: "Limite de 30 artigos no Top final". No commit `c2ae570` o campo é numérico, de 1 a 30, com padrão 20 (`templates/projects/new.html`); a Fase 1 descrevia Top 10, 20 ou 30. **Limites do campo: conferir em produção** |
| E06 | Escolhe em quais bases o VICKY procura os artigos | Dizer que são as bases onde o resultado será publicado ou salvo | Tela de novo projeto: PubMed, SciELO e Google Scholar |
| E07 | Mantém só artigos com texto completo gratuito; o resultado fica menor | Dizer que traz mais artigos ou que libera artigos pagos | Tela de novo projeto: "Descarta o que está atrás de paywall antes mesmo da análise" |
| E08 | Só iniciar a triagem gasta crédito e faz a busca completa; a prévia mostra os critérios de graça antes; o rascunho só guarda o projeto. Precisa distinguir pelo menos a prévia gratuita da triagem que consome crédito | Dizer que a prévia gasta crédito, ou que os três fazem a mesma coisa | Tela de novo projeto: legendas "grátis; 0 créditos" e "consome 1 crédito" |
| E09 | São os critérios (população, intervenção, comparação e desfecho, mais inclusão e exclusão) que o VICKY usa para decidir se cada artigo entra ou sai; o estudante pode revisar antes de iniciar | Dizer que é um resumo dos artigos encontrados | Tela de novo projeto ("Esse protocolo é o filtro que o sistema usa em cada artigo") e detalhe do projeto ("Critérios PICO prontos. Revise antes de iniciar o pipeline") |
| E10 | É uma nota de 0 a 100 de qualidade metodológica, usada para ordenar os artigos incluídos | Dizer que a nota decide se o artigo entra, ou que mede a relevância para o tema, ou o fator de impacto da revista | Lista de artigos: "Ele não decide se o artigo entra ou sai [...] O Quality Score só serve para ranquear os incluídos" |
| E11 | É o registro de como a busca foi feita (termos de busca em cada base e critérios aplicados) e de por que cada artigo foi excluído, para prestar contas ao orientador | Dizer que é o histórico de login ou de acessos da conta | A Fase 1 descreve F08 como registro das buscas e dos critérios. No código `c2ae570` não há tela chamada "log": o conteúdo aparece no painel "Critérios PICO + Strings de busca" do detalhe do projeto e no PDF completo, descrito como "para auditoria". **Rótulo e local: a confirmar na interface** |
| E12 | Salva o resultado do projeto em arquivo para usar fora do VICKY (PDF ou planilha) | Dizer que envia o resultado para o orientador ou publica | Detalhe do projeto: no commit `c2ae570`, o menu "Exportar" (`templates/projects/detail.html`) oferece PDF resumo, PDF completo e XLSX, e o formato de planilha é o XLSX; a Fase 1 cita também CSV e JSON, que a rota de exportação aceita mas o menu não oferece. **Formatos oferecidos: conferir em produção** |

## 5. Questionário de estética (M2.5.1)

Aplicado por formulário online assíncrono ([método, seção 4.4](metodo-g2-usuarios.md#44-formulario-de-estetica-m251)). Cada captura fixa ocupa uma página do formulário, na ordem abaixo, com a frase e a escala.

> **"Olhando esta tela, quanto você concorda com a frase: esta tela é agradável e me convida a continuar usando o VICKY?"**
>
> 1 = discordo totalmente; 2 = discordo; 3 = nem concordo nem discordo; 4 = concordo; 5 = concordo totalmente

| Respondente: R0__ | Data: ___/___/2026 | | | | | |
|---|---|:-:|:-:|:-:|:-:|:-:|
| **Ordem** | **Tela (captura em `M2.5.1/telas/`)** | **1** | **2** | **3** | **4** | **5** |
| 1 | Página inicial, o painel após o login (`inicial.png`) | ( ) | ( ) | ( ) | ( ) | ( ) |
| 2 | Novo projeto (`novo_projeto.png`) | ( ) | ( ) | ( ) | ( ) | ( ) |
| 3 | Detalhe do projeto (`detalhe_projeto.png`) | ( ) | ( ) | ( ) | ( ) | ( ) |
| 4 | Lista de artigos (`lista_artigos.png`) | ( ) | ( ) | ( ) | ( ) | ( ) |
| 5 | Ficha do artigo (`ficha_artigo.png`) | ( ) | ( ) | ( ) | ( ) | ( ) |

Cada página tem um campo opcional de comentário, que vai para a coluna `comentario`. O formulário não pede justificativa da nota, para não alongar o preenchimento nem induzir a nota.

**Registro:** uma linha por participante e tela em `dados/avaliacao/G2/M2.5.1/respostas.csv`, com o cabeçalho:

```text
participante,tela,nota,comentario
```

**Contagem:** a tela é agradável para o participante quando a nota é 4 ou 5, e entra em A quando é agradável para pelo menos 3 dos 5 respondentes ([cálculo](metodo-g2-usuarios.md#6-calculo)).

Em 2026/2, o formulário foi respondido só pelos três participantes das sessões, depois da chamada. Pela [D14](../gestao/decisoes.md#d14-calcular-m251-com-as-tres-respostas-obtidas), as três respostas foram aceitas e a tela entra em A quando é agradável para pelo menos 2 dos 3.

## 6. Bloco qualitativo opcional

Fora do cálculo de M2.5.1. É a última página do formulário, de resposta opcional. Serve para explicar, na Fase 4, as notas de estética e para apoiar recomendações. As afirmações foram propostas por João Felipe Oliveira e valem para a interface como um todo, com a mesma escala de 1 a 5.

| ID | Afirmação |
|----|-----------|
| Q01 | A aparência do VICKY é agradável. |
| Q02 | Os menus e submenus são fáceis de encontrar e usar. |
| Q03 | Entendi o que cada elemento das telas faz. |
| Q04 | As telas são simples, sem excesso de informação. |
| Q05 | As cores são uniformes entre as telas e o contraste facilita a leitura. |
| Q06 | O tipo e o tamanho das letras facilitam a leitura. |
| Q07 | A disposição dos elementos é parecida de uma tela para outra. |
| Q08 | O visual é coerente com a marca do VICKY (logotipo e cores). |
| Q09 | Os elementos das telas estão alinhados e equilibrados. |
| Q10 | A interface parece fácil de adaptar a outros usos e tamanhos de tela. |

**Registro:** `dados/avaliacao/G2/M2.5.1/qualitativo.csv`, com o cabeçalho `participante,afirmacao,nota`.

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 14/11/2026 | Cartões de tarefa, ficha de uso, questionário de compreensão com gabarito, questionário de estética das 5 telas e bloco qualitativo. O questionário qualitativo e o roteiro de origem são de João Felipe Oliveira | Lucas Avelar e João Felipe Oliveira | - |
| 0.2 | 14/11/2026 | E05 com o campo de 1 a 30 (padrão 20) e E12 com os formatos do menu "Exportar", coerentes com o método do G1 | Lucas Avelar | - |
| 0.3 | 19/11/2026 | Adaptação pela D13: cartões e recortes passados pela chamada remota, ficha de uso preenchida pela gravação quando não houver observador, questionário de estética e bloco qualitativo em formulário online, com respondentes R01 a R05 | Gabriel Fae | - |
| 0.4 | 22/11/2026 | Cartões A e B como foram usados nas sessões: tema das células-tronco e entrada numa conta da equipe, a mesma da parte B | Gabriel Fae | - |
| 0.5 | 22/11/2026 | Local e origem dos recortes dos 12 elementos e contagem da M2.5.1 com três respondentes (D14) | Gabriel Fae | - |
| 0.6 | 22/11/2026 | Cartão A sem a frase de objetivo do tema T1, que não foi usada nas sessões (revisão do PR #40) | Gabriel Fae | - |
