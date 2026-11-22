# M2.4.1 Prevenção de erro de operação: registro da coleta

> Preenchido por A1 antes da primeira captura e atualizado se algo mudar. Roteiro: [Método do G2 por inspeção](../../../../docs/fase-3/metodo-g2-inspecao.md).

| Campo | Valor |
|---|---|
| Métrica | M2.4.1 Prevenção de erro de operação (UEp-1-G) |
| Avaliadores | A1, A2 (A3 só se houver desempate) |
| Data e hora de início | A1: 17/11/2026, 16:00. A2: 19/11/2026, 15:04 |
| Data e hora de fim | A1: 19/11/2026 (sessão principal em 17/11, das 16:00 às 19:00; complemento em 19/11). A2: 19/11/2026, 15:25; A03 na triagem completa do G1 por volta das 20:20, por intermédio da frente do G1 |
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
| 6 | 6 | 100% |

## Interpretações adotadas

Critério que gerou dúvida, a interpretação escolhida e a confirmação de que ela foi reaplicada a todos os itens da métrica.

- Nenhuma. A1 e A2 deram o mesmo valor a todos os itens, e o consolidado foi preenchido pelo `calcular_g2_inspecao.py` sem decisão adicional.
- **Regra do crédito.** A ficha de A1 marca só a A01 como ação que consome crédito; A2 marcou A01 como "Sim" e A03 e A04 como "A verificar". Nas duas leituras, nenhuma ação que consome crédito ficou sem proteção: A01 tem aviso no rótulo do botão ("CONSOME 1 CRÉDITO"), A03 tem confirmação em duas etapas, e A04 não cobra crédito (A1) nem mostra cobrança na tela (A2).

## Ocorrências

Mudança em produção durante a coleta, falha do site, cota esgotada, captura refeita ou item `nao_coletado`.

| Data | Ocorrência | Itens afetados | O que foi feito |
|---|---|---|---|
| 17/11/2026 | A1 usou o Brave 1.99.57 (Chromium 157.0.8103.79), e não o Google Chrome previsto no método | Todos os itens de A1 | Desvio registrado. O Brave usa o mesmo motor do Chrome, e as mensagens do navegador saíram em português |
| 17/11/2026 | Capturas de A1 com área maior que a do método (1572 x 1296 pixels) | Capturas de A1 de 17/11 | Sem efeito no julgamento fora da M2.7.1; na M2.7.1, E1 a E3 refeitas em 19/11 em 1366 x 768 |
| 17/11/2026 | Capturas de A1 com nome ou e-mail pessoal do avaliador | Ver a lista em cada ficha de A1 | Não sobem. Refeitas com nome fictício ou com a conta de teste, sem editar as imagens (seção 6 do método) |
| 19/11/2026 | Recapturas de páginas públicas com o navegador sem interface (Brave 1.100.58, Chromium 158.0.8127.42), em 1366 x 768 e zoom de 100%, comandado por script com apoio de IA e sem login: 7 aberturas de página e 3 envios de formulário recusados pelo servidor, sem criar conta | M2.7.1 (E1 a E3), M2.1.1 (C08 e C09), M2.2.2 e M2.4.2 (E02, E04, I01, I02 e I05), M2.3.1 (P03 e P06 no cadastro) | Desvio da coleta manual da seção 2.2 do método, a pedido de A1. Volume equivalente ao de uma pessoa, sem sobrecarga |
| 19/11/2026 | A03 conferida no código antes de qualquer clique (janela de confirmação em 2 etapas); botão visto em produção no registro do G1 | A03 | Janela observada numa triagem do G1, clicando em Cancelar |
| 19/11/2026 | A2 coletou com o Chrome 154.0.8037.97 sem interface, do Playwright, comandado por script (contexto novo, sem cookies; 1366 x 768, zoom de 100%, DPR 1), e não com o Chrome com interface; os textos foram conferidos no Chrome 157.0.8103.79 do MacBook, cuja captura de tela falhou | Todos os itens de A2 | Desvio da coleta manual da seção 2.2 do método, declarado na Fase 4 |
| 19/11/2026 | A03 observada por A2 na prévia da conta de teste (com captura, clicando em Cancelar) e, por intermédio da frente do G1, numa triagem completa em andamento (T1-B, projeto #81), só pelo texto da tela, cancelando na segunda etapa | A03 | A triagem do G1 seguiu sem interrupção. Desvio registrado |
| 20/11/2026 | Consolidação (etapa 7): A1 e A2 deram o mesmo valor a todos os itens | Todos | Consolidado preenchido pelo `calcular_g2_inspecao.py` |
