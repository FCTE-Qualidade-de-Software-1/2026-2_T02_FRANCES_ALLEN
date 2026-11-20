# M2.4.2 Correção de erro de entrada: consolidado

> Etapa 7. Preencher depois que `A1.md` e `A2.md` estiverem no repositório. Em cada divergência, reabrir a evidência e aplicar o critério do [método](../../../../docs/fase-3/metodo-g2-inspecao.md); sem consenso, A3 decide e a linha recebe `decidido_por = A3`. Na coluna `decidido_por`, use `consenso` quando A1 e A2 concordaram.

| item | valor_a1 | valor_a2 | valor_final | justificativa | decidido_por |
|---|---|---|---|---|---|
| I01 | sim/sim | sim/nao | sim/nao | A recusa diz só "E-mail inválido." e mantém o e-mail errado no campo, o que esconde o exemplo voce@exemplo.com. Interpretação adotada na consolidação (`coleta.md`): `sugeriu_valor = sim` só quando a resposta ao erro indica o valor ou o formato aceito; exemplo e ajuda fixos do campo são orientação (M2.2.1), não correção do erro. | consenso (A1 adotou A2) |
| I02 | sim/sim | sim/nao | sim/nao | "E-mail ou senha incorretos." não indica o formato do e-mail. Mesma interpretação da I01. | consenso (A1 adotou A2) |
| I03 | nao_se_aplica/nao_se_aplica | nao_se_aplica/nao_se_aplica | nao_se_aplica/nao_se_aplica | Aceita `nome@gmail` e segue para a tela de pedido recebido: sai de B. | consenso |
| I04 | sim/sim | sim/sim | sim/sim | O balão do navegador diz o mínimo aceito (8 caracteres) e quantos foram digitados. | consenso |
| I05 | sim/sim | sim/nao | sim/nao | "As senhas não coincidem." nomeia o problema, mas não indica o valor, e o formulário limpa as senhas. Mesma interpretação da I01. | consenso (A1 adotou A2) |
| I06 | sim/sim | sim/nao | sim/nao | Em produção aparece o balão "Preencha este campo." (captura de A2; A1 não o viu em 17/11), que manda preencher sem sugerir um tema. Mesma interpretação da I01. | consenso (A1 adotou A2) |
| I07 | sim/sim | sim/sim | sim/sim | O balão do navegador diz o limite aceito (menor ou igual a 30), na captura de A2. A1 não viu o balão em 17/11 e chegou ao mesmo valor pela ajuda do campo; vale a captura. | consenso |

**Rótulos de `decidido_por`.** `consenso`: A1 e A2 deram o mesmo valor. `consenso (A1 adotou A2)`: na consolidação, A1 reabriu a evidência e adotou o valor de A2. `A1, a ratificar por A2`: valor de A1 numa divergência de fato, ou item que A2 não classificou; espera a confirmação de A2. `regra de consolidação, a ratificar por A2`: item em que A1 e A2 concordavam e que mudou pela regra escrita em `coleta.md`. Se A2 discordar de um item a ratificar, A3 decide, e a linha recebe `decidido_por = A3`.

## Resultado

| Campo | Valor |
|---|---|
| A: erros com valor sugerido | 2 |
| B: erros detectados | 6 |
| X = A / B | 0,333 |
| Nível | Insatisfatório |
| Itens fora de B e motivo | I03 (motivo na justificativa de cada item) |

Nível pela tabela de [níveis de pontuação](../../../../docs/fase-2/niveis-e-julgamento.md). O valor sai somente deste arquivo e é publicado na Fase 4.
