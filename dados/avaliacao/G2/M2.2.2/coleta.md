# M2.2.2 Inteligibilidade das mensagens de erro: registro da coleta

> Preenchido por A1 antes da primeira captura e atualizado se algo mudar. Roteiro: [Método do G2 por inspeção](../../../../docs/fase-3/metodo-g2-inspecao.md).

| Campo | Valor |
|---|---|
| Métrica | M2.2.2 Inteligibilidade das mensagens de erro (ULe-3-S) |
| Avaliadores | A1, A2 (A3 só se houver desempate) |
| Data e hora de início | A1: 17/11/2026, 16:00. A2: 19/11/2026, 15:04 |
| Data e hora de fim | A1: 19/11/2026 (sessão principal em 17/11, das 16:00 às 19:00; complemento em 19/11). A2: 19/11/2026, 15:20 (disparos); E08 de cerca de 15:40 a 16:10 |
| Navegador e versão | A1: Brave 1.99.57 (Chromium 157.0.8103.79) em 17/11; Brave 1.100.58 sem interface (Chromium 158.0.8127.42) nas recapturas de 19/11. A2: Chrome 154.0.8037.97 sem interface, do Playwright, comandado por script (contexto novo, sem cookies; DPR 1); textos conferidos no Chrome 157.0.8103.79 do MacBook, cuja captura de tela falhou |
| Área visível | 1366 x 768 pixels, zoom de 100% (A1: modo responsivo do DevTools; A2: janela do navegador sem interface) |
| Versão dos Termos de Uso exibida no site | A1: 2026-09-29 (17/11 e 19/11). Menu lateral: v0.1.0 (registros do G1, 17/11). A2: não registrada; menu lateral v0.1.0 nas capturas de A2 (19/11) |
| Commit do código-fonte (só A1) | `c2ae570` |

## Decisões antes da coleta (17/11/2026)

- **E-mail inválido e e-mail sem domínio** (E02 e I01 a I03): `nome@gmail`, com @ e sem ponto depois dele. Decidido por A1 em 17/11, antes da coleta, e enviado a A2 junto com os inventários. O método v0.6 fixa `aluno` (E02) e `aluno@` (I01 a I03), que o navegador barra antes; `nome@gmail` passa pelo navegador e chega à validação do servidor. Desvio do método, declarado na Fase 4.
- **Mensagem que não aparece em produção:** fica de lado por enquanto, com `origem = nao_exibida` e a classificação vazia. A regra final (entra ou não em B) é decidida antes da consolidação, igual para todos os itens.
- **E08 (limite de pré-visualizações):** em aberto em 17/11. Em 19/11, A1 decidiu não executar (ver Ocorrências).

## Concordância entre A1 e A2

Preencher na etapa 7, só como informação; não muda o resultado.

| Itens comparados | Itens iguais | Concordância bruta |
|---|---|---|
| 33 | 30 | 90,9% (NAV02 a NAV04 estão só na ficha de A2 e ficam fora da comparação) |

## Interpretações adotadas

Critério que gerou dúvida, a interpretação escolhida e a confirmação de que ela foi reaplicada a todos os itens da métrica.

- **Regra de decisão das divergências (20/11/2026, todas as métricas).** Divergência de fato, sobre o que a tela mostra ou permite, é decidida pela evidência. Divergência de julgamento sobre a clareza ou a suficiência de um texto, sem fato novo na evidência, fica com a leitura de A2, que inspecionou sem ler o código: a seção 1 do método cria esse papel porque quem conhece o código tende a achar a interface mais clara do que ela é. A decisão de cada item está em `consolidado.md`, e os rótulos de `decidido_por` estão explicados abaixo da tabela.
- **`tem_causa` em mensagem que só manda fazer algo.** "Informe seu nome.", "Informe o e-mail da sua conta.", "Preencha este campo." e "Marque esta caixa se deseja continuar." ficam `nao`: dizem o que fazer, não o que estava errado. Mensagem que diz a regra violada ("A senha deve ter ao menos 8 caracteres.", "O valor deve ser menor ou igual a 30.") ou o estado que causou o erro continua `sim`. Reaplicada às 36 mensagens: muda ERR01, ERR12 e NAV01; as demais já seguiam essa leitura nas duas fichas.
- **Mensagens do navegador ausentes do inventário.** NAV02, NAV03 e NAV04, vistas por A2, entram no inventário com o mesmo critério da NAV01 (seção 3 do método: a validação do navegador conta como mensagem). O balão da senha curta, que A1 tinha anotado como observação da ERR03, passa a ser a NAV03.
- **Mensagens que não chegam à tela** (decisão adiada em 17/11 e tomada na consolidação, igual para M2.2.2 e M2.3.2). Vale o que a tela mostra quando a mensagem é provocada em produção (seção 6 do método). (a) Se o navegador barra antes e mostra a própria mensagem, a do servidor sai de B e a do navegador conta no lugar: ERR03 (NAV03) e ERR05 (NAV02). (b) Se nada aparece, a mensagem fica em B sem causa e sem solução, porque o estudante não recebe explicação: ERR18, pelo E08 de A2. (c) Mensagem que nenhum avaliador provocou é classificada pelo texto do inventário, como manda a seção 3 do método; o que o código indica sobre a exibição dela vai para os achados da Fase 4 (ERR10, ERR11, ERR12, ERR17, ERR19 e ERR20). A regra muda três linhas em que A1 e A2 concordavam (ERR03, ERR05 e ERR18), ratificadas por A2 em 20/11.

## Ocorrências

Mudança em produção durante a coleta, falha do site, cota esgotada, captura refeita ou item `nao_coletado`.

| Data | Ocorrência | Itens afetados | O que foi feito |
|---|---|---|---|
| 17/11/2026 | A1 usou o Brave 1.99.57 (Chromium 157.0.8103.79), e não o Google Chrome previsto no método | Todos os itens de A1 | Desvio registrado. O Brave usa o mesmo motor do Chrome, e as mensagens do navegador saíram em português |
| 17/11/2026 | Capturas de A1 com área maior que a do método (1572 x 1296 pixels) | Capturas de A1 de 17/11 | Sem efeito no julgamento fora da M2.7.1; na M2.7.1, E1 a E3 refeitas em 19/11 em 1366 x 768 |
| 17/11/2026 | Capturas de A1 com nome ou e-mail pessoal do avaliador | Ver a lista em cada ficha de A1 | Não sobem. Refeitas com nome fictício ou com a conta de teste, sem editar as imagens (seção 6 do método) |
| 19/11/2026 | Recapturas de páginas públicas com o navegador sem interface (Brave 1.100.58, Chromium 158.0.8127.42), em 1366 x 768 e zoom de 100%, comandado por script com apoio de IA e sem login: 7 aberturas de página e 3 envios de formulário recusados pelo servidor, sem criar conta | M2.7.1 (E1 a E3), M2.1.1 (C08 e C09), M2.2.2 e M2.4.2 (E02, E04, I01, I02 e I05), M2.3.1 (P03 e P06 no cadastro) | Desvio da coleta manual da seção 2.2 do método, a pedido de A1. Volume equivalente ao de uma pessoa, sem sobrecarga |
| 19/11/2026 | E08 (limite de prévias) não executado | E08, ERR18 | ERR18 classificada pelo texto do inventário (`origem = inventario`) |
| 19/11/2026 | A2 coletou com o Chrome 154.0.8037.97 sem interface, do Playwright, comandado por script (contexto novo, sem cookies; 1366 x 768, zoom de 100%, DPR 1), e não com o Chrome com interface; os textos foram conferidos no Chrome 157.0.8103.79 do MacBook, cuja captura de tela falhou | Todos os itens de A2 | Desvio da coleta manual da seção 2.2 do método, declarado na Fase 4 |
| 19/11/2026 | Mensagens do navegador de A2 em inglês (idioma en-US do navegador sem interface) | NAV01 a NAV04 | Classificação pelo texto em português, que é o que o estudante vê num navegador em português; NAV01 e NAV02 conferidos em português no Chrome do MacBook |
| 19/11/2026 | A2 também digitou `nome@gmail` (E02 e I01 a I03), pela decisão de A1 de 17/11 | E02, I01 a I03 | As duas fichas são comparáveis nesses itens |
| 19/11/2026 | E08 executado por A2: 20 prévias aceitas nos projetos de teste #61 a #80, sem gastar crédito, e a 21ª recusada (mais 5 tentativas também recusadas); o texto da ERR18 só foi para o endereço da página, e a tela não mostrou mensagem | E08, ERR18 | Captura `20261119_A2_E08.png`. Vale a evidência de A2 sobre a ficha de A1, que tinha o E08 como não executado |
| 19/11/2026 | No E07 (tema vazio), A2 capturou o balão "Preencha este campo."; em 17/11, A1 não viu balão nenhum | E07, NAV01 | Vale a captura de A2 (`20261119_A2_E07.png`) |
| 20/11/2026 | Consolidação (etapa 7) feita por A1, sem reunião com A2, pela regra de decisão desta página | Linhas de `consolidado.md` com `decidido_por` diferente de `consenso` | Em 20/11/2026, A2 ratificou todas as linhas que não seguiam o valor dela; nenhuma foi recusada, e A3 não foi acionado |
