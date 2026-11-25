# M2.7.2 Interface autoexplicativa: consolidado

> Calculado em 22/11/2026 com as três sessões válidas (P01, P02 e P03), pela [versão 0.6 do método](../../../../docs/fase-3/metodo-g2-usuarios.md) (D13): um elemento entra em A quando entendido por pelo menos 2 dos 3 participantes. Em cada célula, `1` quando o elemento foi entendido pelo participante (`uso = sem_ajuda` em `observacao-uso.csv` **e** `classificacao_final = correta` em `respostas-compreensao.csv`) e `0` nos demais casos. Conferência: `python3 dados/avaliacao/G2/calcular_g2_usuarios.py`.

| elemento | nome | P01 | P02 | P03 | entendido_por | entendido_por_2_ou_mais |
|---|---|---|---|---|---|---|
| E01 | Campo do tema | 1 | 1 | 1 | 3 | sim |
| E02 | Campo de objetivo | 0 | 0 | 1 | 1 | não |
| E03 | Tipo de revisão | 1 | 1 | 1 | 3 | sim |
| E04 | Janela de anos | 1 | 1 | 1 | 3 | sim |
| E05 | Quantidade do Top | 1 | 1 | 1 | 3 | sim |
| E06 | Escolha das bases | 1 | 1 | 1 | 3 | sim |
| E07 | Filtro de acesso aberto | 1 | 1 | 1 | 3 | sim |
| E08 | Rascunho, prévia e iniciar | 1 | 1 | 1 | 3 | sim |
| E09 | Critérios PICO gerados | 1 | 1 | 0 | 2 | sim |
| E10 | Quality Score | 1 | 1 | 1 | 3 | sim |
| E11 | Log auditável | 0 | 0 | 1 | 1 | não |
| E12 | Exportação | 0 | 1 | 1 | 2 | sim |

## Por que cada 0

| participante | elemento | uso | explicação | motivo |
|---|---|---|---|---|
| P01 | E02 | incorreto | correta | Deixou vazio o campo Objetivo (conferido na gravação em 22/11/2026); a ficha de uso dá "deixa vazio" como uso incorreto. O cartão A não trazia frase de objetivo junto com o tema |
| P01 | E11 | incorreto | incorreta | Explorou a tela do projeto, não encontrou o registro da busca e desistiu (36:30 a 40:32); no questionário, não soube dizer o que era |
| P01 | E12 | nao_usou | incorreta | Não encontrou o botão Exportar e desistiu (36:30 a 40:32); no questionário, também não o explicou |
| P02 | E02 | incorreto | correta | Deixou vazio o campo Objetivo (conferido na gravação em 22/11/2026), como P01 |
| P02 | E11 | incorreto | incorreta | Não encontrou como a busca foi feita e disse que não conseguiria explicar o elemento |
| P03 | E09 | sem_ajuda | incorreta | Usou sem ajuda, mas disse que o bloco é "um resumo dos artigos encontrados", que é o erro que invalida no gabarito |

## Resultado

| Campo | Valor |
|---|---|
| Sessões válidas (precisa ser 3, ou 5) | 3 (P01, P02 e P03) |
| A: elementos entendidos por pelo menos 2 de 3 | 10 |
| B: elementos (12, menos os ausentes em produção) | 12 |
| Resultado (A / B) | 10 / 12 = 83,3% |
| Quality Score (E10) entendido por pelo menos 2 de 3? | Sim, pelos 3 |
| Nível | Bom (75% a menos de 90%), **indicativo** por ser n = 3 (método, seção 2.8) |
| Elementos fora de B e motivo | Nenhum: os 12 existem em produção (conferência em `coleta.md`) |

**Margem.** E09 e E12 entraram em A por 2 de 3. Se um único participante tivesse errado um deles, X cairia para 9/12 = 75,0% (Bom); se errasse os dois, 8/12 = 66,7% (Aceitável). E02 e E11 ficaram fora por 1 de 3. Com o uso de E02 mantido como correto, como estava antes da conferência das gravações, X seria 11/12 = 91,7% (Excelente). As respostas de P01 lidas como corretas com interpretação (E02, E03 e E10, registradas em `coleta.md`) não mudam o resultado: E02 está fora de A pelo uso, e P02 e P03 acertaram E03 e E10.

Quality Score não entendido leva a Insatisfatório. Nível pela tabela de [níveis de pontuação](../../../../docs/fase-2/niveis-e-julgamento.md).
