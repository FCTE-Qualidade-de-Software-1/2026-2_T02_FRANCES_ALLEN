# Níveis de pontuação e critérios de julgamento

Os níveis são definidos **antes da coleta** para que a interpretação dos resultados não seja ajustada a posteriori. A rubrica (F2-C5) exige níveis para **todas** as métricas.

## 1. Níveis de pontuação por métrica

| Métrica | Insatisfatório | Aceitável | Bom | Excelente | Fonte do limiar |
|---------|:--------------:|:---------:|:---:|:---------:|-----------------|
| M1.1.1 | _-_ | _-_ | _-_ | _-_ | _literatura, norma, benchmark ou decisão justificada da equipe_ |
| M1.2.1 | _-_ | _-_ | _-_ | _-_ | _-_ |
| M2.1.1 | < 0,70 | 0,70 a 0,79 | 0,80 a 0,89 | ≥ 0,90 | Com 10 padrões na lista, "Bom" admite até 2 inconsistências; a partir de 4, o estudante precisa reaprender telas do mesmo fluxo |
| M2.1.2 | < 70% | 70% a 84% | 85% a 94% | ≥ 95% | Texto técnico do servidor é a falha mais grave para quem não é da área de computação, e o estudante não tem suporte em tempo real |
| M2.2.1 | < 70%, **ou** qualquer ação que consome crédito sem proteção | 70% a 84% | 85% a 99%, com todas as ações que consomem crédito protegidas | 100% | A triagem completa custa R$ 24,90 por execução ([Objeto de avaliação](../fase-1/objeto-de-avaliacao.md#25-restricoes)), e a Fase 1 escolheu C2 justamente para evitar erros no uso dos créditos pagos |
| M2.2.2 | < 40% | 40% a 59% | 60% a 79% | ≥ 80% | Medida específica; os erros de entrada mais caros estão na configuração do projeto, que define a triagem paga |
| M2.2.3 | < 40% | 40% a 59% | 60% a 79% | ≥ 80% | Medida específica; erro irrecuperável na configuração do projeto obriga a criar outro projeto e pagar de novo |
| M2.3.1 | 1 de 4 ou menos | 2 de 4 | 3 de 4 | 4 de 4 | O estudante chega por link de colega, anúncio ou indicação do orientador, em qualquer uma das páginas de entrada |
| M2.3.2 | < 60%, **ou** Quality Score não entendido | 60% a 74% | 75% a 89% | ≥ 90% | O VICKY não tem tutorial nem suporte em tempo real, e a Fase 1 justificou C2 pela configuração do PICO e pela leitura do Quality Score; se o estudante não entende o score, não consegue defender a lista diante do orientador |
| M3.1.1 | _-_ | _-_ | _-_ | _-_ | _-_ |

## 2. Critérios de julgamento

### Da métrica para a questão

_Regra explícita, ex.: a hipótese H1.1 é confirmada se M1.1.1 atingir o nível "Bom" ou superior._

### Da questão para o objetivo

_Regra explícita, ex.: G1 é considerado atingido se todas as questões tiverem hipótese confirmada; parcialmente atingido se ao menos metade; não atingido nos demais casos._

### Do objetivo para o julgamento do produto

| Situação | Julgamento |
|----------|------------|
| _-_ | Atende |
| _-_ | Atende parcialmente |
| _-_ | Não atende |

## 3. Regras do G2 (capacidade de interação)

A ISO/IEC 25023:2016 define como calcular cada medida, mas não diz qual valor é bom: a cláusula 1 declara que a norma não atribui faixas de valores a níveis de pontuação, porque isso depende do produto e da necessidade de quem o usa. Por isso cada limiar do G2 está justificado na coluna "Fonte do limiar" por uma necessidade do estudante de medicina ou por uma decisão registrada na Fase 1, e foi fixado antes da coleta.

As quatro faixas da tabela correspondem aos níveis de pontuação da ISO/IEC 14598-1:1999 (subcláusula 8.2): **Excelente** = ultrapassa os requisitos, **Bom** = intervalo alvo, **Aceitável** = mínimo aceitável e **Insatisfatório** = inaceitável. Os três primeiros são satisfatórios.

**1. Da medição para a hipótese.** A hipótese H2.x é **confirmada** quando os valores medidos caem na faixa que ela previu e **refutada** quando não caem. Confirmar ou refutar a hipótese não muda o julgamento do produto: mostra se a leitura preliminar da equipe estava certa.

**2. Da métrica para a questão.** O nível da questão é dado pela medida de referência indicada abaixo. As demais medidas da questão só interferem para baixo: se uma delas ficar em "Insatisfatório", a questão desce um nível.

| Questão | Medida de referência | Medidas que podem rebaixar |
|---------|----------------------|----------------------------|
| Q2.1 | menor nível entre M2.1.1 e M2.1.2 (ambas genéricas) | - |
| Q2.2 | M2.2.1 (UEp-1-G, genérica) | M2.2.2 (UEp-2-S), M2.2.3 (UEp-3-S) |
| Q2.3 | M2.3.2 (ULe-4-S), a única medida com estudantes reais | M2.3.1 (UAp-3-S) |

**3. Da questão para o objetivo.**

| Situação das três questões | Julgamento do G2 |
|----------------------------|------------------|
| Nenhuma em "Insatisfatório" e pelo menos duas em "Bom" ou "Excelente" | Atende |
| No máximo uma em "Insatisfatório" | Atende parcialmente |
| Duas ou mais em "Insatisfatório", **ou** Q2.2 em "Insatisfatório" por ação que consome crédito sem proteção | Não atende |

A última regra existe porque, entre os problemas de capacidade de interação, o único que tira dinheiro do estudante é o engano numa ação paga.

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 05/10/2026 | Criação da estrutura do documento | Gabriel Fae | - |
| 0.2 | 16/10/2026 | Reorganização da documentação por fases do processo de avaliação | Gabriel Fae | - |
| 0.3 | 18/10/2026 | Níveis de pontuação e regras de julgamento do G2 (capacidade de interação) | Lucas Avelar | Gabriel Fae |
