# Respostas de A2 no G1

Fichas do avaliador A2 (relação entre papel e integrante em [`M1.3.1/coleta.md`](../M1.3.1/coleta.md)), preenchidas em 20/11/2026 conforme o [Método do G1](../../../../docs/fase-3/metodo-g1.md), seções 4.4 e 4.6.

## Arquivos

| Arquivo | Métrica | Conteúdo |
|---------|---------|----------|
| `julgamento_A2_T1.csv` a `julgamento_A2_T4.csv` | M1.3.1 | Relevância de cada item da ficha cega contra o PICO de referência: `relevante` (sim ou nao), primeiro componente não atendido e justificativa |
| `rubrica_A2_T1.csv` e `rubrica_A2_T2.csv` | M1.4.1 | Nota da rubrica por componente (desenho, amostra, comparador e revisão por pares), soma e justificativa |

**Para o cálculo.** Mesmo procedimento de A1: copiar `julgamento_A2_Tn.csv` para `../M1.3.1/` e `rubrica_A2_Tn.csv` para `../M1.4.1/` antes de rodar o `calcular_g1.py`.

**Resumo.** Itens julgados relevantes: 5 de 30 em T1, 8 de 30 em T2, 8 de 25 em T3 e 6 de 30 em T4.

## Procedimento e independência

O julgamento usou só as fichas cegas (`../M1.3.1/ficha_cega_Tn.csv`), o PICO da seção 3.2 e as seções 2.3, 4.4, 4.6 e 5 do método, copiados para uma pasta separada. Não foram abertos os arquivos `chave_*`, as respostas de A1, as listas de referência, o Top 30, M1.1.1 nem M1.2.1, e não houve busca na web pelos estudos incluídos nas revisões. As justificativas estão sem acento, como nas fichas de A1.

## Interpretações de critério

### T1 e T2
- Revisão sistemática e metanálise reprovam em desenho, porque o PICO pede ECR.
- Análise secundária de ECR conta como ECR quando mantém a comparação randomizada (T1-04, T1-30, T2-22); não conta quando a análise fica dentro de um braço só (T2-30).
- Artigo de desenho de ensaio (T1-10) foi tratado como protocolo e reprova em desenho; na rubrica recebeu a nota do ECR que descreve, leitura que pode ser contestada.
- População mais ampla que a do PICO reprova (T1-06 e T1-11, com pericardite e fibrilação atrial). Pranayama sozinho conta como ioga (T2-17); pacote de exercício, pranayama e dieta (T2-18) e ioga nos dois braços (T2-24) reprovam em intervenção.
- Rubrica: amostra vale 0 quando o resumo não informa o total de participantes; em revisão de ECR, comparador vale 2.

### T3 e T4
- T3: prevalência conta só quando o denominador são gestantes não selecionadas pelo status de DMG; amostra só de DMG, caso-controle ou grupos pareados reprova em desfecho. País não citado no resumo não reprova (T3-19); T3-07 reprova em população por indicar Portugal.
- T4: escala de ataxia ou medida funcional conta como desfecho, mesmo secundário; VO2 pico, imagem de medula, farmacocinética e frataxina não contam. Extensão aberta de ECR reprova em desenho (T4-02 e T4-12, casos de borda). População mista reprova (T4-22).

Notas completas de cada tema: `notas_A2_T1T2.md` e `notas_A2_T3T4.md`.

## Limitação declarada

As fichas de A2, como as de A1, foram preenchidas com apoio de IA (ver [Uso de IA](../../../../docs/sobre/uso-de-ia.md)). Por isso o kappa de M1.3.1 mede a concordância entre dois julgamentos assistidos por IA feitos em sessões independentes, e não entre dois avaliadores humanos. Isso deve constar nas limitações da Fase 4. A2 também participou da pesquisa das revisões de referência na Fase 3 (seção 2.3, item 4); o julgamento não teve acesso à lista de incluídos, mas o conflito fica declarado.
