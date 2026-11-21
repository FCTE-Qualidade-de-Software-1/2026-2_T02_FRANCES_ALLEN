# Respostas de A1 no G1

Fichas do avaliador A1 (relação entre papel e integrante em [`M1.3.1/coleta.md`](../M1.3.1/coleta.md)), preenchidas em 19/11/2026 conforme o [Método do G1](../../../../docs/fase-3/metodo-g1.md), seções 4.4 e 4.6. A pasta reúne as respostas de A1 num só lugar, como combinado com o condutor (C).

## Arquivos

| Arquivo | Métrica | Conteúdo |
|---------|---------|----------|
| `julgamento_A1_T1.csv` a `julgamento_A1_T4.csv` | M1.3.1 | Relevância de cada item da ficha cega contra o PICO de referência: `relevante` (sim ou nao), primeiro componente não atendido e justificativa |
| `rubrica_A1_T1.csv` e `rubrica_A1_T2.csv` | M1.4.1 | Nota da rubrica por componente (desenho, amostra, comparador e revisão por pares), soma e justificativa |
| `revisao_11a.md` | M1.2.1 e M1.5.1 | Etapa 11a, feita depois do envio das fichas: conferência de M1.2.1 e revisão dos itens não conformes de M1.5.1 |

**Para o cálculo.** O `calcular_g1.py` lê as fichas em caminhos fixos. Antes de rodar, copiar `julgamento_A1_Tn.csv` para `../M1.3.1/` e `rubrica_A1_Tn.csv` para `../M1.4.1/`; os nomes já seguem o método. A leitura dos arquivos pelo script foi conferida numa cópia da pasta.

**Resumo.** Itens julgados relevantes: 5 de 30 em T1, 9 de 30 em T2, 7 de 25 em T3 e 6 de 30 em T4.

## Procedimento

O julgamento usou apenas as fichas cegas (`../M1.3.1/ficha_cega_Tn.csv`): título, resumo, ano, periódico e DOI, sem posição nem Quality Score. Cada item foi comparado com o PICO da seção 3.2 do método. Foi considerado relevante apenas quando população, intervenção (ou exposição), desfecho e desenho eram atendidos, e o comparador não foi exigido. Componente não mencionado no resumo não reprovou o artigo; componente contradito pelo resumo reprovou. O desenho foi identificável pelo resumo em todos os itens, e não foi necessário consultar o *Publication Type* do PubMed. Na rubrica, quando o trecho inicial do resumo não trazia o tamanho da amostra, o resumo foi lido por inteiro. Sem número de participantes no resumo, a amostra recebeu 0, como define a escala.

## Interpretações adotadas

1. **Análise secundária de ensaio randomizado.** Conta como ensaio randomizado quando preserva a comparação randomizada da intervenção do tema sobre o desfecho do tema (T1-04, T1-30, T2-22 e T2-30). O critério coincide com o de `tipo_ok` da M1.5.1. Extensão aberta e análise de início tardio não preservam essa comparação e não contam (T4-02 e T4-12).
2. **Artigo de desenho de ensaio.** Artigo de racional e características basais, sem resultado de desfecho, equivale a protocolo e não atende ao desenho em M1.3.1 (T1-10). Na rubrica, que independe da relevância, recebe a pontuação do desenho descrito.
3. **População mais ampla que a do tema.** Estudo cuja população contém a do tema, mas não se limita a ela, não atende à população (T1-06, T1-11 e T4-22).
4. **Intervenção em T2.** O pranayama, prática respiratória da ioga, conta como ioga (T2-17). A ioga combinada com exercício e dieta, sem efeito isolado, é cointervenção (T2-18). A comparação randomizada de lembretes por e-mail após a ioga não avalia a ioga (T2-24).
5. **Desfecho em T3.** Estudo restrito a gestantes que já têm diabetes gestacional, ou com amostra pareada por diagnóstico, não estima prevalência e não atende ao desfecho. Estudo que relata a frequência de diabetes gestacional numa amostra de gestantes atende (T3-17 e T3-21).
6. **Desfecho em T4.** Medidas de desempenho funcional (teste de nove pinos, marcha cronometrada) e escalas de ataxia atendem. Imagem, biomarcador, farmacocinética e aptidão cardiopulmonar isolada não atendem (T4-11 e T4-15).
7. **Rubrica.** Revisão sistemática que inclui ensaios não randomizados recebe 2 no desenho, por analogia com o nível 3 da tabela do OCEBM (T2-29). Revisão narrativa recebe 0 em desenho, amostra e comparador (T1-22 e T2-19).

## Desvios do método e limitações

- **Apoio de IA.** O julgamento, a rubrica e a etapa 11a foram executados com apoio de IA (Claude Opus 5.5), a pedido de A1, pela aplicação dos critérios das seções 4.4 e 4.6 a cada item. O método prevê avaliador humano. A independência em relação a A2 se mantém, porque A2 julga sem acesso a estas fichas. O uso está registrado na [declaração de uso de IA](../../../../docs/sobre/uso-de-ia.md).
- **Contato prévio com dados do G1.** Antes do julgamento, o assistente teve contato com registros do G1 usados na inspeção do G2: os registros de texto das telas do projeto T1 (`../M1.2.1/evidencias/`), que exibem os dez primeiros títulos com Quality Score, e `../M1.2.1/casos_funcoes.csv`. O risco de viés recai sobretudo na rubrica de T1 (M1.4.1). Ele foi mitigado porque a nota é a soma de componentes objetivos extraídos do resumo: desenho, número de participantes, presença de comparador e revisão por pares. Os arquivos `chave_Tn.csv` e `top30_Tn.csv` não foram abertos antes do envio das fichas.
- **Piloto de calibração.** O piloto conjunto de A1 e A2 (etapa 9) não foi realizado. A ausência é declarada como limitação da M1.3.1 e dá mais peso ao kappa como verificação de consistência.

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 19/11/2026 | Fichas de relevância (T1 a T4) e rubrica (T1 e T2) de A1 | Gabriel Fae | - |
