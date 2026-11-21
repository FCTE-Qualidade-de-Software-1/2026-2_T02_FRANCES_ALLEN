# Resultados do G2 por inspeção (capacidade de interação)

!!! note "Situação em 20/11/2026"
    Os valores desta página saem dos `consolidado.md` de 20/11/2026, calculados com `dados/avaliacao/G2/calcular_g2_inspecao.py`. A consolidação foi feita por A1, e A2 ratificou em 20/11/2026 as 13 linhas que não seguiam o valor dela (M2.2.1, M2.2.2 e M2.3.2): nenhuma foi recusada, e A3 não foi acionado. As capturas de A1 que faltavam foram incluídas em 20/11/2026, entre elas a do menu Exportar aberto, que confirma o item F09 da M2.2.1.

Esta página reúne o resultado das oito métricas do G2 coletadas por inspeção, conforme o [Método do G2 por inspeção](../fase-3/metodo-g2-inspecao.md). As métricas com participantes (M2.5.1, M2.6.1, M2.6.2 e M2.7.2) vêm da #28. Os níveis seguem a tabela de [níveis de pontuação](../fase-2/niveis-e-julgamento.md), fixada antes da coleta.

## 1. Execução da coleta

| Campo | Valor |
|-------|-------|
| Período | A1: 17/11/2026 (16:00 às 19:00) e 19/11/2026 (complemento). A2: 19/11/2026 (15:04 às 16:10, e por volta das 20:20 na triagem do G1). Consolidação: 20/11/2026 |
| Produto | VICKY em produção, <https://vicky.synaptha.com/> |
| Versão de referência | Termos de Uso versão 2026-09-29, acessados de 17 a 19/11/2026; menu lateral com `v0.1.0` nas telas vistas por A1 e por A2 |
| Navegador | A1: Brave 1.99.57 (Chromium 157.0.8103.79) em 17/11 e Brave 1.100.58 sem interface (Chromium 158.0.8127.42) nas recapturas de 19/11. A2: Chrome 154.0.8037.97 sem interface (Playwright), com os textos conferidos no Chrome 157.0.8103.79. Área visível de 1366 x 768 e zoom de 100% |
| Código-fonte (só A1) | Fork `LucasAvelar2711/Vicky`, commit `c2ae570` |
| Avaliadores | A1 e A2. A3 não foi acionado até 20/11/2026 |
| Itens não coletados | Nenhum, de A1 nem de A2. A1 não executou o E08 (limite de prévias); A2 executou, e a evidência dela vale para a mensagem correspondente (ERR18) |
| Desvios do método | Ver a tabela abaixo |

### Desvios do método

| Data | Desvio | Motivo | Efeito na medida |
|------|--------|--------|------------------|
| 17/11/2026 | A1 seguiu a versão 0.2 deste método (planilhas CSV, sem valores digitados fixos), que estava num branch desatualizado, e não a 0.6 publicada | Branch local do avaliador desatualizado | Em 19/11, as anotações foram passadas para as fichas `.md` da versão 0.6 sem mudar o conteúdo. Os valores digitados divergem do roteiro na linha abaixo |
| 17/11/2026 | E02 e I01 a I03 com `nome@gmail`, e não `aluno` e `aluno@` | Decisão de A1 antes da coleta, registrada em `coleta.md` e enviada a A2 com os inventários: o valor passa pelo navegador e chega à validação do servidor | Mede a mensagem do servidor em vez do balão do navegador. A2 usou o mesmo valor, e as duas fichas são comparáveis nesses itens |
| 17/11/2026 | A1 usou o Brave, e não o Google Chrome | Navegador da máquina do avaliador | Nenhum esperado: o Brave usa o mesmo motor do Chrome, e os balões do navegador saíram em português |
| 17/11/2026 | Capturas de A1 com área maior que 1366 x 768 | Configuração do modo responsivo | A M2.7.1, que depende do que aparece sem rolar, foi refeita em 19/11 em 1366 x 768, com os mesmos julgamentos |
| 19/11/2026 | Etapa 6 de A1 sem acompanhar a triagem ao vivo: telas de resultado pelos registros de texto feitos pelo G1 em produção (17/11) e pelo código | A1 não estava na triagem do G1 | Atinge F05 a F09 (M2.2.1), P02, P04 e P07 a P09 (M2.3.1), A01 e A03 (M2.4.1) e as mensagens do pipeline (M2.3.2) |
| 19/11/2026 | Recapturas de páginas públicas com navegador sem interface comandado por script, com apoio de IA | Corrigir a área visível da M2.7.1 e refazer capturas que mostravam dado pessoal do avaliador | 7 aberturas de página e 3 envios de formulário recusados pelo servidor, sem login e sem criar conta. Foge da coleta manual da seção 2.2 do método, sem sobrecarga ao site |
| 19/11/2026 | A2 coletou com o Chrome 154 sem interface, do Playwright, comandado por script | A captura de tela pelo Chrome com interface (MacBook, tela Retina) falhou | Foge da coleta manual da seção 2.2 do método. Os balões do navegador saíram em inglês e foram classificados pelo texto em português, que é o que o estudante vê |
| 19/11/2026 | F06 a F09 (M2.2.1), A03 (M2.4.1) e parte da P09 (M2.3.1) observados por A2 por intermédio da frente do G1, só pelo texto da tela, no projeto #53 (concluído) e numa triagem em andamento (projeto #81) | A2 não acompanhou a triagem do G1 ao vivo | O julgamento é de A2. Nas imagens tiradas depois, o nome e o e-mail da titular da conta foram substituídos na página antes da captura, e não na imagem. A2 não abriu o menu Exportar (F09) |
| 17 a 20/11/2026 | Transcrição das anotações, classificação da etapa 5, complemento da etapa 6 e consolidação (etapa 7) feitos por A1 com apoio de IA, a pedido de A1 | Prazo da coleta | O método prevê dois avaliadores humanos. A independência de A2 se mantém, porque A2 classificou sem ver nada de A1; as decisões da consolidação que não seguem o valor de A2 foram ratificadas por ela |
| 20/11/2026 | Consolidação feita por A1, sem reunião com A2, pela regra de decisão escrita em cada `coleta.md`: divergência de fato vai pela evidência; divergência de julgamento sobre a clareza de um texto fica com a leitura de A2, que inspecionou sem ler o código | Prazo da E2 | 21 das 25 divergências ficaram com o valor de A2, e 4 com o de A1 (F09, MSG21, MSG29 e a NAV01 da M2.3.2). Com as 6 linhas mudadas pela regra das mensagens que não chegam à tela e as 3 mensagens do navegador acrescentadas na M2.3.2, 13 linhas foram ratificadas por A2 em 20/11/2026, sem nenhuma recusa |

### Concordância entre os avaliadores

A concordância bruta é só informativa: o resultado vem do consolidado. Itens que estão numa só ficha ficam fora da comparação: NAV02 a NAV04 na M2.2.2, vistas só por A2, e NAV01 na M2.3.2, classificada só por A1.

| Métrica | Itens comparados | Itens iguais | Concordância | Decididos por A3 |
|---------|:----------------:|:------------:|:------------:|:----------------:|
| M2.1.1 | 10 | 10 | 100% | 0 |
| M2.2.1 | 9 | 7 | 77,8% | 0 |
| M2.2.2 | 33 | 30 | 90,9% | 0 |
| M2.3.1 | 10 | 7 | 70,0% | 0 |
| M2.3.2 | 115 | 106 | 92,2% | 0 |
| M2.4.1 | 6 | 6 | 100% | 0 |
| M2.4.2 | 7 | 3 | 42,9% | 0 |
| M2.7.1 | 4 | 4 | 100% | 0 |

A menor concordância, na M2.4.2, veio da leitura de "sugeriu o valor": A1 contou o exemplo fixo do campo, e A2, só a resposta ao erro. Prevaleceu a leitura de A2, que é a literal da Fase 2 ("sugere ao estudante o valor correto, em vez de só recusar"). As interpretações adotadas em cada métrica estão no `coleta.md` da pasta, e a decisão de cada item, no `consolidado.md`.

## 2. Valores medidos

| Métrica | Medida | A | B | Valor | Nível | Dados brutos |
|---------|--------|:-:|:-:|:-----:|:-----:|--------------|
| M2.1.1 | UAp-1-G | 9 | 10 | 90,0% | Bom | [M2.1.1/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G2/M2.1.1) |
| M2.2.1 | ULe-1-G | 8 | 9 | 88,9% | Bom | [M2.2.1/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G2/M2.2.1) |
| M2.2.2 | ULe-3-S | 10 | 34 | 29,4% | Insatisfatório | [M2.2.2/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G2/M2.2.2) |
| M2.3.1 | UOp-1-G | 6 | 8 | 0,25 (1 - A / B) | Insatisfatório | [M2.3.1/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G2/M2.3.1) |
| M2.3.2 | UOp-2-G | 77 | 117 | 65,8% | Insatisfatório | [M2.3.2/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G2/M2.3.2) |
| M2.4.1 | UEp-1-G | 4 | 6 | 66,7% | Insatisfatório | [M2.4.1/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G2/M2.4.1) |
| M2.4.2 | UEp-2-S | 2 | 6 | 33,3% | Insatisfatório | [M2.4.2/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G2/M2.4.2) |
| M2.7.1 | UAp-3-S | 3 | 4 | 3 de 4 | Bom | [M2.7.1/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G2/M2.7.1) |

**Itens fora de B.** M2.2.2 e M2.3.2: ERR03 e ERR05, que o balão do navegador encobre (NAV03 e NAV02 contam no lugar). M2.3.1: P02 e P09, observados numa só tela. M2.4.2: I03, porque a recuperação de senha aceita `nome@gmail` e segue.

**Regra do crédito (M2.4.1).** Alguma ação que consome crédito ficou sem proteção? Não. A única ação que consome crédito, iniciar a triagem completa (A01), traz aviso explícito no rótulo do botão ("CONSOME 1 CRÉDITO"), no Novo projeto e na tela do projeto. Não há caixa de confirmação, mas o aviso explícito do efeito conta como proteção pela Fase 2, e a regra não se aplica.

## 3. Principais achados

São os achados que alimentam a ação de melhoria (#29).

| Métrica | Achado | Evidência |
|---------|--------|-----------|
| M2.1.1 | As páginas públicas descrevem 9 dos 10 cenários, incluindo o limite do produto. Favoritos (F07) não aparece em nenhuma delas. | C07 no consolidado; busca de A2 no texto das três páginas, com o FAQ aberto |
| M2.7.1 | A página inicial, o cadastro e o painel dizem o que o VICKY faz. A tela de login traz "Volte para sua bancada" e "Triagem PICO com IA, feita pra IC, TCC, monografia e artigo de resumo", sem dizer o que é triado. | E3; `20261119_A1_E3.png` e `20261119_A2_E3.png` |
| M2.2.1 | A orientação cobre cadastro, novo projeto, PICO, bases, triagem, lista e favoritos. O log auditável (F08) só tem títulos de painel: nenhum texto diz como consultar o registro ou usá-lo no trabalho, e "Mostrando as 10 ações mais recentes (de 19 totais)" não diz como ver as demais. | F08; `20261119_A2_F08.png` |
| M2.2.2 | Só 10 das 34 mensagens de erro dizem a causa e o que fazer. As da tela de acesso nomeiam o problema sem dizer o que fazer ("E-mail inválido.", "As senhas não coincidem.", "E-mail ou senha incorretos."), e as falhas da triagem mostram texto técnico cru ("Erro no pipeline: {texto técnico do erro}"). Ao atingir o limite de 20 prévias por dia, o VICKY recusa a prévia e volta para a lista de projetos sem mensagem: o texto vai só no endereço da página. | ERR02, ERR04, ERR07, ERR23 a ERR25, ERR29, ERR30 e ERR18; `20261119_A2_E08.png` |
| M2.2.2 e M2.3.2 | Pelo código, outras mensagens seguem o mesmo caminho da ERR18 e também não chegariam à tela: os limites de prévias por conta e por rede (ERR19 e ERR20), a confirmação de e-mail exigida para a prévia (ERR17), o reenvio do link de confirmação (ERR10, ERR11, MSG06 e MSG07), a exclusão de projeto (MSG18), o início e a repetição da triagem (MSG23 e MSG26) e o e-mail já confirmado (MSG02). Como ninguém as provocou, foram classificadas pelo texto do inventário e precisam ser conferidas em produção. | `codigo-a1.md` das pastas M2.2.2 e M2.3.2 |
| M2.3.1 | Seis dos oito padrões comparáveis variam entre telas: o botão principal (rótulo, gradiente ou cor sólida, raio), o erro (caixa rosa ou balão do navegador), o sucesso (caixa que fica ou faixa que some), a lista vazia (ícone e rótulo), o foco (halo ou anel) e os rótulos dos formulários (caixa alta sem marca de obrigatório ou caixa normal com "*"). Na tela do projeto, as três confirmações de ação irreversível usam três formas (aviso no menu, janela em duas etapas e caixa nativa do navegador); a medida não as conta porque estão numa só tela. | P01, P03 a P06, P10 e P02 |
| M2.3.2 | As mensagens de acesso, de sucesso e de saldo são claras. As 40 não claras estão em três grupos: as falhas da triagem, com texto técnico cru ou enganoso (ERR22 a ERR30); 28 linhas do painel Pipeline e da faixa de andamento, com termos de implementação (substring, iter, fallback, cap, JSON cru) e frases que giram sem informar o andamento real; e duas mensagens que mandam editar os critérios PICO, o que a tela do projeto não permite. A ERR18, que não aparece, completa as 40. | ERR22 a ERR30; MSG35 a MSG51, MSG53 a MSG55, MSG57, MSG60 a MSG64, MSG66 e MSG68; MSG21 e MSG29 |
| M2.4.1 | Iniciar a triagem, excluir o projeto, parar a triagem e o filtro de acesso aberto estão protegidos. A quantidade do Top não avisa que fica fixa depois de criado o projeto, e a pré-visualização não mostra a cota diária nem quantas prévias restam. | A04 e A06 |
| M2.4.2 | O VICKY detecta seis das sete entradas inválidas, mas só indica o valor aceito nas duas em que o balão do navegador diz o limite (senha curta e Top acima de 30). As mensagens do servidor nomeiam o erro sem dizer o formato, e a recuperação de senha aceita `nome@gmail` e segue. | I01, I02, I05, I06 e I03 |

## 4. Hipóteses

Uma hipótese é confirmada quando o valor medido cai na faixa que ela previu. Isso não muda o julgamento: mostra se a leitura preliminar da equipe estava certa.

| Hipótese | Previsão (parte coberta por inspeção) | Medido | Resultado |
|----------|----------------------------------------|--------|-----------|
| H2.1 | M2.1.1 de pelo menos 90%, incluindo o limite do produto | 90,0%, com o limite do produto descrito (C10) | Confirmada |
| H2.2 | M2.2.1 de pelo menos 85%; M2.2.2 entre 50% e 75% | M2.2.1 = 88,9%; M2.2.2 = 29,4% | Refutada: M2.2.1 caiu na faixa, mas M2.2.2 ficou bem abaixo |
| H2.3 | M2.3.1 entre 0,6 e 0,8; M2.3.2 entre 85% e 95%, com as falhas em texto técnico do servidor | M2.3.1 = 0,25; M2.3.2 = 65,8%, com as falhas concentradas em texto técnico | Refutada: os dois valores ficaram abaixo da faixa, embora a natureza das falhas de M2.3.2 tenha sido a prevista |
| H2.4 | M2.4.1 entre 50% e 70%, sem confirmação ao iniciar a triagem; M2.4.2 de 40% ou menos, com correção silenciosa | M2.4.1 = 66,7%, com aviso no botão e sem caixa de confirmação ao iniciar a triagem; M2.4.2 = 33,3% | Confirmada pelos valores. A correção silenciosa não foi observada: as entradas inválidas foram recusadas |
| H2.7 (parte) | As quatro páginas de entrada explicam o propósito (M2.7.1 = 4 de 4) | 3 de 4: a tela de login não explica | Refutada |

## 5. Respostas às questões

As regras são as da seção 3 de [níveis e julgamento](../fase-2/niveis-e-julgamento.md#3-regras-do-g2-capacidade-de-interacao): a medida de referência dá o nível, e uma medida complementar em Insatisfatório rebaixa a questão em um nível.

| Questão | Como o nível é obtido | Nível | Resposta |
|---------|-----------------------|:-----:|----------|
| Q2.1 | Nível de M2.1.1 | Bom | Antes de criar a conta, o estudante encontra o que o VICKY entrega em 9 dos 10 cenários, incluindo o limite do produto; só Favoritos não é descrito |
| Q2.2 | Nível de M2.2.1, um nível abaixo se M2.2.2 for Insatisfatório | Aceitável | A orientação dentro do produto cobre 8 das 9 funções (Bom), mas as mensagens de erro raramente dizem a causa e o que fazer (M2.2.2 Insatisfatório), o que rebaixa a questão |
| Q2.3 | Menor nível entre M2.3.1 e M2.3.2 | Insatisfatório | As telas resolvem de formas diferentes seis dos oito padrões comparáveis, e cerca de um terço das mensagens não é claro, sobretudo no acompanhamento da triagem |
| Q2.4 | Nível de M2.4.1, um nível abaixo se M2.4.2 for Insatisfatório; Insatisfatório se ação paga estiver desprotegida | Insatisfatório | A ação paga está protegida por aviso, mas duas das seis ações sem proteção deixam M2.4.1 abaixo de 70%, e o VICKY raramente indica o valor aceito depois de um erro de entrada |
| Q2.7 | Nível de M2.7.2 (#28), um nível abaixo se M2.7.1 for Insatisfatório | Depende da #28 | M2.7.1 = Bom (3 de 4): não rebaixa a Q2.7 |

Q2.5 e Q2.6 dependem só das métricas com participantes (#28). O julgamento do G2 é feito na #30, com as seis questões principais.

## 6. Limitações

- A1 julgou as telas de resultado pelos registros de texto do G1 e pelo código, sem ver a triagem ao vivo; A2 viu parte delas por intermédio da frente do G1, só pelo texto da tela (ver os desvios).
- A consolidação foi feita por A1, sem reunião com A2, que depois ratificou as 13 linhas que não seguiam o valor dela. Mesmo que todas tivessem ficado com o valor de A2, M2.2.2 iria a 13/36 (36,1%) e M2.3.2 a 78/115 (67,8%), sem mudar o nível; só F09 mudaria um nível.
- F09 (M2.2.1) conta pelo texto do menu Exportar, que A2 não abriu; a captura de A1 do menu aberto em produção (`20261120_A1_F09.png`) confirma as três descrições. Sem F09, M2.2.1 iria a 7 de 9 (77,8%, Aceitável), e a Q2.2 a Insatisfatório.
- Mensagens que nenhum avaliador provocou foram classificadas pelo texto do inventário, como manda o método. Pelo código, onze delas não chegam à tela (ver os achados). Se a regra aplicada à ERR18 fosse estendida a elas, M2.2.2 iria a 6/34 (17,6%) e M2.3.2 a 66/117 (56,4%), sem mudar o nível.
- Na M2.3.1, a regra de tela única deixa fora da medida a inconsistência entre as três confirmações da tela do projeto (P02), registrada como achado.
- Os balões do navegador de A2 saíram em inglês. NAV03 foi classificada pelo texto em português visto por A1; a versão em português da NAV04 não foi observada.
- A1 não viu os balões do tema vazio e do Top acima de 30 em 17/11, e A2 os capturou em 19/11; vale a captura.
- O e-mail sem @ na recuperação de senha (ERR12) não foi provocado, porque os dois avaliadores usaram `nome@gmail`, que passa pelo navegador. Pelo código, o navegador barra antes, com uma mensagem própria que não entrou no inventário.

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 13/11/2026 | Estrutura da página de resultados do G2 por inspeção, a preencher com a coleta da #27 | Gabriel Fae | - |
| 0.2 | 19/11/2026 | Execução da coleta de A1, desvios do método e limitações conhecidas antes da consolidação | Gabriel Fae | - |
| 0.3 | 20/11/2026 | Consolidação de A1 e A2: concordância, valores, níveis, achados, hipóteses, respostas Q2.1 a Q2.4 e parte da Q2.7, desvios de A2 e limitações | Gabriel Fae | - |
| 0.4 | 20/11/2026 | Ratificação de A2 nas 13 linhas decididas por A1, sem recusa | Gabriel Fae | - |
| 0.5 | 20/11/2026 | Capturas de A1 incluídas; F09 confirmado pela captura do menu Exportar | Gabriel Fae | - |
