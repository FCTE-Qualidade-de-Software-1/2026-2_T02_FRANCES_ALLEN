# Método do G2 por inspeção (capacidade de interação)

Este método cobre as oito métricas do G2 obtidas por inspeção das telas e do código. As métricas que dependem de participantes ou de teste de acessibilidade (M2.5.1, M2.6.1, M2.6.2 e M2.7.2) estão no [Método do G2 com usuários](metodo-g2-usuarios.md). Definição, fórmula e níveis são os da [Fase 2](../fase-2/especificacao-das-metricas.md); esta página diz como executar a coleta.

## 1. Métricas cobertas

| Métrica | Medida | O que é inspecionado | Denominador (B) | Pasta em `dados/avaliacao/G2/` |
|---------|--------|----------------------|-----------------|--------------------------------|
| [M2.1.1](../fase-2/especificacao-das-metricas.md#m211) | UAp-1-G | Páginas públicas | 10 cenários | `M2.1.1/` |
| [M2.2.1](../fase-2/especificacao-das-metricas.md#m221) | ULe-1-G | Orientação dentro das telas | 9 funções | `M2.2.1/` |
| [M2.2.2](../fase-2/especificacao-das-metricas.md#m222) | ULe-3-S | Mensagens de erro | Inventário de erros | `M2.2.2/` |
| [M2.3.1](../fase-2/especificacao-das-metricas.md#m231) | UOp-1-G | Padrões de interação repetidos | 10 padrões (lista inicial) | `M2.3.1/` |
| [M2.3.2](../fase-2/especificacao-das-metricas.md#m232) | UOp-2-G | Todas as mensagens do sistema | Inventário ampliado | `M2.3.2/` |
| [M2.4.1](../fase-2/especificacao-das-metricas.md#m241) | UEp-1-G | Ações caras ou destrutivas | 6 ações (lista inicial) | `M2.4.1/` |
| [M2.4.2](../fase-2/especificacao-das-metricas.md#m242) | UEp-2-S | Erros de entrada nos formulários | Erros detectados pelo sistema | `M2.4.2/` |
| [M2.7.1](../fase-2/especificacao-das-metricas.md#m271) | UAp-3-S | Primeira tela das páginas de entrada | 4 páginas | `M2.7.1/` |

## 2. Preparação

### 2.1 Papéis

A Fase 2 exige dois avaliadores independentes, com pelo menos um que não tenha lido o código. O método separa os papéis para que essa condição se mantenha até o fim da classificação.

| Papel | Pode ver | Responsabilidade |
|-------|----------|------------------|
| A1 | Telas e código-fonte | Monta os inventários a partir do código, faz a inspeção e confirma as proteções no código |
| A2 | Telas e inventários em texto, sem caminho de arquivo nem trecho de código | Faz a inspeção apenas pelo produto. Só pode abrir o código depois que `A2.csv` estiver no repositório |
| A3 | Evidências e critério | Decide apenas as divergências que A1 e A2 não resolverem. Não pode ser A1 nem A2 |

Quem leu o código na inspeção preliminar que gerou as hipóteses H2.1 a H2.7 não pode ser A2.

### 2.2 Ambiente

| Item | Valor |
|------|-------|
| Produto | VICKY em produção, <https://vicky.synaptha.com/> |
| Navegador | Google Chrome em computador, versão anotada em `coleta.md` |
| Área visível | 1366 x 768 pixels, zoom de 100%, definida pelo modo responsivo do DevTools. O valor fixo é necessário porque M2.7.1 depende do que aparece sem rolar |
| Sessão | Janela anônima para as páginas públicas, para não reaproveitar login nem cache |
| Código-fonte (só A1) | Fork privado `LucasAvelar2711/Vicky`, commit `c2ae570` (29/09/2026). Se produção e código divergirem, vale o que aparece em produção, e a diferença é anotada |
| Forma de coleta | Manual. Os Termos de Uso proíbem *scraping* abusivo e sobrecarga, por isso nenhuma etapa usa automação contra a produção |

### 2.3 Contas e dependências

| Recurso | Uso | Cuidado |
|---------|-----|---------|
| Conta de cortesia | Telas internas e projeto já triado | Nome fictício. Senha fora do repositório |
| Conta descartável | Roteiro de erros de cadastro e login, incluindo "e-mail já cadastrado" | E-mail de teste criado para a coleta |
| Projeto rascunho | Excluir projeto (M2.4.1) e preencher formulários | Criado só para o teste; não usar projeto do G1 |
| Projeto triado do G1 (#26) | F05 a F09 em M2.2.1 e padrões das telas de resultado em M2.3.1 | Depende da primeira triagem do G1 |
| Triagem prevista do G1 (#26) | Observar "iniciar triagem" e "parar triagem" em M2.4.1 | Combinar o horário com quem executa o G1. A inspeção não gasta crédito extra |

### 2.4 Organização de cada pasta

```text
dados/avaliacao/G2/M2.x.y/
├── coleta.md            # data, hora, navegador, versão em produção, papéis A1/A2
├── A1.csv               # classificação independente de A1
├── A2.csv               # classificação independente de A2
├── consolidado.csv      # resultado único, com a justificativa das divergências
└── evidencias/          # AAAAMMDD_A1_<item>.png
```

Só entram dados reais de coleta. Antes de enviar uma captura, confira que ela não mostra nome ou e-mail de pessoa real, senha ou saldo de outra conta. A relação entre A1, A2 e A3 e as pessoas fica fora do repositório.

## 3. Passo a passo

A coleta segue esta ordem, para que nenhuma etapa gaste a cota de prévias antes da hora nem dependa de dado que ainda não existe.

| Etapa | Quem | Atividade | Métricas |
|:-----:|:----:|-----------|----------|
| 1 | A1 | Monta os inventários de mensagens e entrega o texto a A2 | M2.2.2, M2.3.2 |
| 2 | A1 e A2, separados | Inspeciona as páginas públicas e de entrada | M2.1.1, M2.7.1 |
| 3 | A1 e A2, separados | Inspeciona a orientação e os padrões das telas sem resultado de triagem | M2.2.1, M2.3.1 |
| 4 | A1 e A2, separados | Aplica os roteiros de entradas inválidas, com o limite de prévias por último | M2.2.2, M2.4.2 |
| 5 | A1 e A2, separados | Classifica os inventários | M2.2.2, M2.3.2 |
| 6 | A1 e A2, separados | Durante a triagem do G1 e no projeto triado, completa as telas de resultado e as ações caras | M2.2.1, M2.3.1, M2.4.1 |
| 7 | A1, A2 e, se preciso, A3 | Sobe `A1.csv` e `A2.csv`, consolida e calcula | Todas |

**Regra comum.** Sem evidência, o item não conta. Se um item não puder ser observado por causa externa (produto fora do ar ou triagem indisponível), ele é marcado como `nao_coletado`, sai do denominador e é declarado na Fase 4.

### M2.1.1: completude da descrição

Abra `/` (incluindo o FAQ) e `/termos`. Para cada cenário, procure um trecho que diga o que aquilo entrega ao estudante. Citar o nome da função de passagem não conta.

| ID | Cenário | Conta como descrito quando a página diz |
|----|---------|------------------------------------------|
| C01 | F01 Cadastro e login | Que o estudante cria uma conta e entra nela para usar o produto |
| C02 | F02 Criação de projeto | Que o estudante informa o tema e pode ajustar o recorte |
| C03 | F03 Protocolo PICO | Que o sistema gera o PICO e os critérios a partir do tema |
| C04 | F04 Bases e quantidade | Quais bases são consultadas e qual o tamanho do resultado |
| C05 | F05 Triagem completa | Que os artigos são buscados e triados automaticamente, com o consumo de crédito |
| C06 | F06 Lista ranqueada | Que o resultado é uma lista ordenada por qualidade, com acesso à fonte |
| C07 | F07 Favoritos | Que o estudante pode marcar artigos |
| C08 | F08 Log auditável | Que existe registro das buscas e dos critérios aplicados |
| C09 | F09 Exportação | Que os resultados podem ser exportados e em quais formatos |
| C10 | Limite do produto | Que o VICKY não substitui a leitura crítica dos artigos |

**Registro:** `item`, `pagina`, `trecho_literal`, `descrito (sim/nao)`, `captura`.

### M2.7.1: autodescrição dos pontos de entrada

Abra cada página com a área visível definida na seção 2.2 e capture a tela sem rolar. A página conta quando o texto visível diz que o VICKY busca e tria artigos científicos sobre um tema. Logotipo, nome do produto ou slogan genérico não contam.

| ID | Página | Condição |
|----|--------|----------|
| E1 | `/` | Janela anônima |
| E2 | `/signup` | Janela anônima |
| E3 | `/login` | Janela anônima |
| E4 | `/dashboard` | Logo depois do login, com a conta de cortesia |

**Registro:** `pagina`, `trecho_literal`, `explica_proposito (sim/nao)`, `captura`.

### M2.2.1: completude da orientação ao usuário

Para cada função, localize dentro do produto uma orientação sobre como executá-la: texto explicativo, dica, exemplo no campo ou ajuda contextual. Só o nome do campo não conta, assim como orientação que diz apenas que a função existe. Vídeo, e-mail e conversa com a equipe do VICKY também não contam.

| Função | Onde observar | Depende de |
|--------|---------------|------------|
| F01 | Cadastro, login e recuperação de senha | - |
| F02 | Novo projeto | - |
| F03 | Geração e revisão do PICO | Cota de prévias |
| F04 | Escolha de bases e do Top | - |
| F05 | Início e acompanhamento da triagem | Triagem do G1 |
| F06 | Lista de artigos e Quality Score | Projeto triado |
| F07 | Favoritos na lista | Projeto triado |
| F08 | Log auditável | Projeto triado |
| F09 | Exportação | Projeto triado |

**Registro:** `funcao`, `tela`, `orientacao_literal`, `diz_como_executar (sim/nao)`, `captura`.

### M2.2.2 e M2.3.2: inventários de mensagens

**Etapa 1 (A1).** Em `src/vicky/web/` e nos demais módulos chamados pelas rotas de F01 a F09, A1 lista os textos que chegam ao estudante. Ficam de fora as mensagens exclusivas de compra de créditos (F10) e configurações (F11).

| Inventário | Conteúdo | Pasta |
|------------|----------|-------|
| Erros | Mensagens de erro do fluxo do escopo | `M2.2.2/inventario.csv` |
| Ampliado | Os erros, mais sucesso, aviso, andamento da triagem e saldo de créditos antes de executar | `M2.3.2/inventario.csv` |

Colunas: `id`, `tipo`, `texto`, `funcao`, `gatilho`. Textos iguais em lugares diferentes contam uma vez, e os lugares ficam em `gatilho`. Um texto com variável conta uma vez. A1 mantém o caminho no código em arquivo separado, que A2 só abre depois de terminar.

**Etapa 4 (A1 e A2).** Cada avaliador dispara as mensagens abaixo em produção e guarda a captura.

| ID | Entrada | Formulário | Observação |
|----|---------|------------|------------|
| E01 | Campos vazios | Cadastro | |
| E02 | E-mail inválido | Cadastro | |
| E03 | Senha curta | Cadastro | |
| E04 | Senhas diferentes | Cadastro | |
| E05 | E-mail já cadastrado | Cadastro | Usa a conta descartável |
| E06 | Senha errada | Login | |
| E07 | Tema vazio | Novo projeto | |
| E08 | Limite de pré-visualizações | Geração do PICO | Sempre por último, pois esgota a cota do dia |

A validação nativa do navegador conta como mensagem, porque é o que o estudante vê, e fica marcada como `origem = navegador`. Mensagem que não pode ser disparada sem gastar crédito é classificada pelo texto do inventário, com `origem = inventario`.

**Etapa 5 (A1 e A2).** Cada mensagem é classificada pelos critérios:

| Métrica | Critério | Sim quando | Não quando |
|---------|----------|------------|------------|
| M2.2.2 | `tem_causa` | O texto diz por que o erro aconteceu | Só diz que algo falhou |
| M2.2.2 | `tem_solucao` | O próprio texto sugere o que fazer | Só existe um botão ao lado da mensagem |
| M2.3.2 | `clara` | Diz em linguagem do estudante o que aconteceu ou o que fazer, e o resultado informado é o correto | Traz texto técnico do servidor, não diz o resultado ou informa resultado errado |

Em M2.2.2, a mensagem só entra em A quando `tem_causa` e `tem_solucao` são ambos "sim".

### M2.3.1: consistência operacional

Para cada padrão, registre como ele é resolvido em cada tela do escopo onde aparece. Compare os atributos da tabela. O padrão é inconsistente quando duas ou mais telas o resolvem de forma visual ou comportamental diferente.

| ID | Padrão | Atributos comparados |
|----|--------|----------------------|
| P01 | Acionar a ação principal | Rótulo, cor, posição e formato do botão |
| P02 | Confirmar ação irreversível | Janela própria ou caixa nativa do navegador, texto dos botões |
| P03 | Exibir erro | Posição, cor, ícone e permanência |
| P04 | Exibir sucesso | Posição, cor, ícone e permanência |
| P05 | Exibir lista vazia | Ícone, cor, texto e presença de ação sugerida |
| P06 | Indicar o campo em foco | Estilo do contorno ou destaque |
| P07 | Navegar pelo menu | Itens, ordem e indicação da página atual |
| P08 | Reabrir um projeto anterior | Caminho e tela de destino |
| P09 | Acompanhar processo longo | Indicador, texto e atualização |
| P10 | Preencher formulário | Rótulos, obrigatoriedade e momento da validação |

Um padrão observado em uma única tela não tem o que comparar: sai de B e fica registrado com o motivo.

**Registro:** `padrao`, `tela`, `como_aparece`, `captura`, e por padrão `consistente (sim/nao)` e `justificativa`.

### M2.4.1: prevenção de erro de operação

| ID | Ação | Consome crédito? | Proteção procurada |
|----|------|:----------------:|--------------------|
| A01 | Iniciar a triagem completa | Sim | Confirmação ou aviso explícito de que 1 crédito será consumido |
| A02 | Excluir projeto | Não | Confirmação antes de excluir |
| A03 | Parar a triagem em andamento | A verificar | Confirmação ou aviso do efeito sobre a execução e o crédito |
| A04 | Definir a quantidade do Top | A verificar | Aviso de que o valor não pode ser alterado depois |
| A05 | Ativar o filtro de acesso aberto | Não | Aviso do efeito sobre o resultado |
| A06 | Gerar pré-visualização | Não (cota diária) | Aviso do consumo da cota ou do saldo restante |

1. Antes da coleta, A1 e A2 conferem em produção se a lista está completa, como pede a ficha. Uma ação nova entra na lista e a mudança é registrada em `coleta.md`.
2. A2 verifica cada ação pela tela. A1 verifica pela tela e localiza o trecho que confirma no código.
3. A01 é observada numa triagem já prevista no G1.
4. **A03 pode desperdiçar a triagem do G1.** A1 confere no código, antes, se há confirmação. Se houver, A2 clica e cancela. Se não houver, ninguém clica durante uma triagem do G1: A03 é registrada como desprotegida com a evidência do código e a tela do botão.
5. Se uma ação que consome crédito estiver sem proteção, anote em destaque em `consolidado.csv`: pela Fase 2, isso leva M2.4.1 a Insatisfatório e pode levar o G2 a "Não atende".

**Registro:** `acao`, `consome_credito`, `protecao_encontrada`, `tipo (confirmacao/aviso/bloqueio/nenhuma)`, `protegida (sim/nao)`, `captura`. Somente em A1: `arquivo_e_linha`.

### M2.4.2: correção de erro de entrada

| ID | Entrada inválida | Formulário |
|----|------------------|------------|
| I01 | E-mail sem domínio | Cadastro |
| I02 | E-mail sem domínio | Login |
| I03 | E-mail sem domínio | Recuperação de senha |
| I04 | Senha curta | Cadastro |
| I05 | Senhas diferentes | Cadastro |
| I06 | Tema vazio | Novo projeto |
| I07 | Quantidade do Top fora dos valores permitidos | Novo projeto |

Só valem entradas possíveis pela interface normal, sem alterar a página pelo DevTools.

| Comportamento observado | `detectado` | `sugeriu_valor` | Efeito na métrica |
|-------------------------|:-----------:|:---------------:|-------------------|
| Recusa e indica o valor ou formato correto | sim | sim | Entra em A e B |
| Recusa sem indicar o valor correto | sim | não | Entra só em B |
| Troca o valor sem avisar | sim | não | Entra só em B |
| Aceita a entrada e segue | não | não | Sai de B, com registro |
| A interface impede a entrada (ex.: lista fechada) | não se aplica | não se aplica | Sai de B, com registro |

**Registro:** `id`, `formulario`, `entrada`, `comportamento`, `detectado`, `sugeriu_valor`, `mensagem_literal`, `captura`.

## 4. Registro

| Arquivo | Quem produz | Quando |
|---------|-------------|--------|
| `coleta.md` | A1 | Antes da primeira captura, atualizado se algo mudar |
| `inventario.csv` | A1 | Etapa 1 (M2.2.2 e M2.3.2) |
| `A1.csv` e `A2.csv` | Cada avaliador | Ao terminar a classificação, com as colunas da métrica |
| `evidencias/` | Cada avaliador | Durante a inspeção |
| `consolidado.csv` | A1 e A2 | Etapa 7, com `valor_a1`, `valor_a2`, `valor_final`, `justificativa` e `decidido_por` |

`coleta.md` traz data e hora de início e fim, versão do Chrome, área visível, commit do código e a versão em produção. Como a tela do VICKY pode não exibir número de versão, a referência é a data e a hora de acesso, junto com a versão dos Termos de Uso exibida no site.

## 5. Cálculo

| Métrica | A | B | Regra especial nos níveis |
|---------|---|---|---------------------------|
| M2.1.1 | Cenários com `descrito = sim` | 10 | - |
| M2.2.1 | Funções com `diz_como_executar = sim` | 9 | - |
| M2.2.2 | Erros com causa **e** solução | Erros do inventário coletados | - |
| M2.3.1 | Padrões inconsistentes; X = 1 - A / B | Padrões observados em duas ou mais telas | - |
| M2.3.2 | Mensagens com `clara = sim` | Mensagens do inventário ampliado coletadas | - |
| M2.4.1 | Ações com `protegida = sim` | Ações da lista conferida | Ação que consome crédito sem proteção leva a Insatisfatório |
| M2.4.2 | Erros com `sugeriu_valor = sim` | Erros com `detectado = sim` | - |
| M2.7.1 | Páginas com `explica_proposito = sim` | 4 | - |

O valor é calculado somente sobre `consolidado.csv`, e o nível sai da tabela de [níveis de pontuação](../fase-2/niveis-e-julgamento.md). Valor, nível e evidência são publicados na [Fase 4](../fase-4/index.md). Os limiares não mudam depois da coleta.

## 6. Discordância e repetição

**Como A1 e A2 chegam a um resultado único:**

1. Cada um classifica sozinho. `A1.csv` e `A2.csv` são enviados ao repositório antes da conversa, o que deixa no histórico o julgamento independente.
2. As duas planilhas são comparadas item a item, e a concordância bruta é registrada em `coleta.md`, apenas como informação.
3. Em cada divergência, A1 e A2 reabrem a evidência e aplicam o critério desta página. A decisão e o motivo vão para `consolidado.csv`.
4. Sem consenso, A3 decide olhando somente a evidência e o critério, e a linha recebe `decidido_por = A3`.
5. Se a divergência vier de um critério ambíguo, a interpretação adotada é escrita em `coleta.md` e reaplicada a todos os itens da métrica, não só ao item discutido.
6. O resultado é sempre sim ou não por item. Não se faz média entre avaliadores.

**Quando repetir a coleta:**

| Situação | O que fazer |
|----------|-------------|
| Falha momentânea do site | Tentar de novo em outro horário. Persistindo, marcar `nao_coletado` |
| Mudança visível em produção durante a coleta | Refazer os itens afetados e anotar a data da mudança em `coleta.md` |
| Texto diferente entre produção e código | Vale produção. Anotar a diferença em `inventario.csv` |
| Cota de prévias esgotada | Continuar no dia seguinte |
| Captura perdida ou com dado pessoal | Refazer a captura. Não editar a imagem para esconder o problema |

## 7. Pendências antes da coleta

- [ ] Definir quem são A1, A2 e A3
- [ ] Confirmar a conta de cortesia e o número de créditos com a equipe do VICKY
- [ ] Conferir em produção a lista de ações de M2.4.1
- [ ] Combinar com o G1 (#26) o horário da triagem observada

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 04/11/2026 | Criação da página | Lucas Avelar | - |
| 0.2 | 09/11/2026 | Método completo de inspeção: papéis, ambiente, roteiro e checklist por métrica, registro, cálculo e regra de discordância | Gabriel Fae | - |
