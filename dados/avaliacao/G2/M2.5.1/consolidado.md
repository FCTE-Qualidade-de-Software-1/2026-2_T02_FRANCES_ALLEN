# M2.5.1 Estética da interface: consolidado

> Calculado em 22/11/2026 com as três respostas obtidas (R01 a R03), pela [D14](../../../../docs/gestao/decisoes.md): a tela é agradável para o respondente com nota 4 ou 5 e entra em A quando é agradável para a maioria, 2 de 3. A Fase 2 pedia 3 de 5. Conferência: `python3 dados/avaliacao/G2/calcular_g2_usuarios.py`.

| tela | R01 | R02 | R03 | agradavel_para | agradavel_para_2_ou_mais |
|---|---|---|---|---|---|
| inicial | 5 | 3 | 5 | 2 | sim |
| novo_projeto | 5 | 4 | 3 | 2 | sim |
| detalhe_projeto | 5 | 3 | 2 | 1 | não |
| lista_artigos | 5 | 2 | 1 | 1 | não |
| ficha_artigo | 4 | 3 | 3 | 1 | não |

## Resultado

| Campo | Valor |
|---|---|
| Respostas válidas (a Fase 2 pede 5) | 3 (R01 a R03), aceitas pela D14 |
| A: telas agradáveis para pelo menos 2 de 3 | 2 (inicial e novo_projeto) |
| B: telas avaliadas | 5 |
| Resultado (A / B) | 2 / 5 = 40,0% |
| Nível | Aceitável (40% a menos de 60%), **indicativo** |

**Sensibilidade.** O valor está no limite inferior de Aceitável: uma tela a menos levaria a 20% (Insatisfatório). Se a regra exigisse os três respondentes (o mesmo número absoluto de "3 de 5"), nenhuma tela entraria em A, e X seria 0%.

**Hipótese H2.5** ("a maioria dos participantes considera agradáveis pelo menos 4 das 5 telas"): só um dos três respondentes achou 4 ou mais telas agradáveis (5 de 5); os outros dois, uma tela cada. Refutada.

## Bloco qualitativo (fora do cálculo)

| afirmação | notas (R01, R02, R03) | mediana | concordam (4 ou 5) |
|---|---|---|---|
| Q01 A aparência do VICKY é agradável | 3, 3, 3 | 3 | 0 de 3 |
| Q02 Menus e submenus fáceis de encontrar e usar | 5, 3, 3 | 3 | 1 de 3 |
| Q03 Entendi o que cada elemento das telas faz | 5, 2, 5 | 5 | 2 de 3 |
| Q04 Telas simples, sem excesso de informação | 3, 2, 1 | 2 | 0 de 3 |
| Q05 Cores uniformes e contraste que facilita a leitura | 5, 3, 4 | 4 | 2 de 3 |
| Q06 Tipo e tamanho das letras facilitam a leitura | 5, 4, 2 | 4 | 2 de 3 |
| Q07 Disposição dos elementos parecida entre telas | 5, 3, 3 | 3 | 1 de 3 |
| Q08 Visual coerente com a marca (logotipo e cores) | 4, 3, 4 | 4 | 2 de 3 |
| Q09 Elementos alinhados e equilibrados | 5, 4, 3 | 4 | 2 de 3 |
| Q10 Interface fácil de adaptar a outros usos e tamanhos de tela | 5, 2, 1 | 2 | 1 de 3 |

A escala é ordinal; por isso o resumo usa a mediana e a contagem de concordância, e não a média.
