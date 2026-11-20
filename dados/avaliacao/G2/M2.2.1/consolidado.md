# M2.2.1 Completude da orientação ao usuário: consolidado

> Etapa 7. Preencher depois que `A1.md` e `A2.md` estiverem no repositório. Em cada divergência, reabrir a evidência e aplicar o critério do [método](../../../../docs/fase-3/metodo-g2-inspecao.md); sem consenso, A3 decide e a linha recebe `decidido_por = A3`. Na coluna `decidido_por`, use `consenso` quando A1 e A2 concordaram.

| item | valor_a1 | valor_a2 | valor_final | justificativa | decidido_por |
|---|---|---|---|---|---|
| F01 | sim | sim | sim |  | consenso |
| F02 | sim | sim | sim |  | consenso |
| F03 | sim | sim | sim |  | consenso |
| F04 | sim | sim | sim |  | consenso |
| F05 | sim | sim | sim |  | consenso |
| F06 | sim | sim | sim |  | consenso |
| F07 | sim | sim | sim |  | consenso |
| F08 | sim | nao | nao | Os painéis da tela do projeto só nomeiam o registro e listam as ações; nenhum texto diz como consultar o log nem como usá-lo para anexar ao trabalho, que é a função F08 na Fase 1. "Mostrando as 10 ações mais recentes (de 19 totais)" não diz como ver as demais. O texto do painel de desempenho explica como o sistema redistribui a busca entre as substrings, e não como executar F08. Divergência de julgamento: prevalece a leitura de A2 (`coleta.md`). | consenso (A1 adotou A2) |
| F09 | sim | nao | sim | A2 viu só o botão "Exportar" fechado e não abriu o menu; a frente do G1 confirmou em produção as três opções (resumo, PDF e XLSX). Cada opção descreve o que o arquivo traz ("Só os incluídos, com link pro artigo [...]", "Cada excluído com sua justificativa [...]", "Abas: Resumo, Top, Excluídos [...]"; código `templates/projects/detail.html:74-110`). Pela leitura que os dois avaliadores aplicaram a F04, a ajuda que explica cada opção da ação conta como orientação. Divergência de fato: a captura de A1 do menu aberto em produção confirma o item; se ela mostrar outro texto, F09 passa a `nao`. | A1, a ratificar por A2 com a captura |

**Rótulos de `decidido_por`.** `consenso`: A1 e A2 deram o mesmo valor. `consenso (A1 adotou A2)`: na consolidação, A1 reabriu a evidência e adotou o valor de A2. `A1, a ratificar por A2`: valor de A1 numa divergência de fato, ou item que A2 não classificou; espera a confirmação de A2. `regra de consolidação, a ratificar por A2`: item em que A1 e A2 concordavam e que mudou pela regra escrita em `coleta.md`. Se A2 discordar de um item a ratificar, A3 decide, e a linha recebe `decidido_por = A3`.

## Resultado

| Campo | Valor |
|---|---|
| A: funções com orientação | 8 |
| B: funções coletadas (de 9) | 9 |
| X = A / B | 0,889 |
| Nível | Bom |
| Itens fora de B e motivo | nenhum |

Nível pela tabela de [níveis de pontuação](../../../../docs/fase-2/niveis-e-julgamento.md). O valor sai somente deste arquivo e é publicado na Fase 4.
