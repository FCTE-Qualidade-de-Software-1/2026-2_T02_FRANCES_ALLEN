# M2.3.1 Consistência operacional: consolidado

> Etapa 7. Preencher depois que `A1.md` e `A2.md` estiverem no repositório. Em cada divergência, reabrir a evidência e aplicar o critério do [método](../../../../docs/fase-3/metodo-g2-inspecao.md); sem consenso, A3 decide e a linha recebe `decidido_por = A3`. Na coluna `decidido_por`, use `consenso` quando A1 e A2 concordaram.

| item | valor_a1 | valor_a2 | valor_final | justificativa | decidido_por |
|---|---|---|---|---|---|
| P01 | nao | nao | nao |  | consenso |
| P02 | nao | fora_de_b | fora_de_B | As três confirmações (Excluir, Parar e Iniciar durante a prévia) ficam na mesma tela, a do projeto, em estados diferentes. A seção 3 do método tira de B o padrão observado numa só tela; A1 tinha contado os estados como telas. Prevalece a leitura literal do método, e a diferença entre as três confirmações fica como achado na Fase 4. | consenso (A1 adotou A2) |
| P03 | nao | nao | nao |  | consenso |
| P04 | nao | nao | nao |  | consenso |
| P05 | nao | nao | nao |  | consenso |
| P06 | sim | nao | nao | O foco é resolvido com estilos diferentes: borda rosa com halo translúcido de 3 pixels nos formulários públicos e anel sólido de 1 pixel no Novo projeto (capturas de A1 e de A2). Diferença visual no atributo comparado conta como inconsistência, como os dois avaliadores fizeram na P01 e na P05. | consenso (A1 adotou A2) |
| P07 | sim | sim | sim |  | consenso |
| P08 | sim | sim | sim |  | consenso |
| P09 | sim | fora_de_b | fora_de_B | A prévia e a triagem completa mostram o andamento na mesma tela, a do projeto, e nenhuma outra tela acompanha processo longo. Sai de B pela mesma leitura da P02. | consenso (A1 adotou A2) |
| P10 | nao | nao | nao |  | consenso |

**Rótulos de `decidido_por`.** `consenso`: A1 e A2 deram o mesmo valor. `consenso (A1 adotou A2)`: na consolidação, A1 reabriu a evidência e adotou o valor de A2. `A1, a ratificar por A2`: valor de A1 numa divergência de fato, ou item que A2 não classificou; espera a confirmação de A2. `regra de consolidação, a ratificar por A2`: item em que A1 e A2 concordavam e que mudou pela regra escrita em `coleta.md`. Se A2 discordar de um item a ratificar, A3 decide, e a linha recebe `decidido_por = A3`.

## Resultado

| Campo | Valor |
|---|---|
| A: padrões inconsistentes | 6 |
| B: padrões observados em duas ou mais telas | 8 |
| X = 1 - A / B | 0,250 |
| Nível | Insatisfatório |
| Padrões fora de B e motivo | P02, P09 (motivo na justificativa de cada item) |

Nível pela tabela de [níveis de pontuação](../../../../docs/fase-2/niveis-e-julgamento.md). O valor sai somente deste arquivo e é publicado na Fase 4.
