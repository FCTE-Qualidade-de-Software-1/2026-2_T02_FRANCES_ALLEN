# Objetivos, questões e hipóteses

Cada objetivo deriva de uma característica selecionada na [Fase 1](../fase-1/caracteristicas.md) (critério F2-C11: rastreabilidade entre Fases 1 e 2).

## Rastreabilidade com a Fase 1

O **foco de qualidade** de cada objetivo vem da característica selecionada, e o **ponto de vista** vem das [partes interessadas](../fase-1/partes-interessadas.md).

| Característica (Fase 1) | Parte interessada | Objetivo GQM |
|-------------------------|-------------------|--------------|
| C1 - Adequação funcional | _-_ | [G1](#g1) |
| C2 - Capacidade de interação | Estudantes de medicina (usuário) | [G2](#g2) |
| C3 - Manutenibilidade | _-_ | [G3](#g3) |

## G1

**Característica de origem:** C1 - Adequação funcional · **Parte interessada:** _a definir_

| Elemento do template | Definição |
|----------------------|-----------|
| Analisar | o website VICKY |
| com o propósito de | _avaliar / caracterizar / compreender_ |
| com respeito a | _foco de qualidade (subcaracterística)_ |
| do ponto de vista de | _ex.: estudantes de medicina_ |
| no contexto de | _ex.: busca de artigos para estudo, em desktop e mobile_ |

| Questão | Hipótese | Métricas |
|---------|----------|----------|
| Q1.1 - _a definir_ | H1.1 - _resultado esperado, com valor de referência_ | [M1.1.1](especificacao-das-metricas.md#m111) |
| Q1.2 - _a definir_ | H1.2 - _-_ | M1.2.1 |

## G2

**Característica de origem:** C2 - Capacidade de interação · **Parte interessada:** estudantes de medicina (usuário)

| Elemento do template | Definição |
|----------------------|-----------|
| Analisar | o website VICKY |
| com o propósito de | avaliar |
| com respeito a | capacidade de interação: operabilidade, proteção contra erro do usuário e autodescritividade |
| do ponto de vista de | estudantes de medicina |
| no contexto de | uso do VICKY em produção, em navegador desktop, no fluxo que vai do cadastro à exportação dos resultados, por inspeção da equipe e por testes de cenário com estudantes de medicina |

### Rastreabilidade com a Fase 1

| Elemento do G2 | Origem na Fase 1 |
|----------------|------------------|
| Foco de qualidade: operabilidade, proteção contra erro do usuário e autodescritividade | Subcaracterísticas selecionadas para C2 em [Seleção e priorização das características](../fase-1/caracteristicas.md#2-caracteristicas-selecionadas) |
| Ponto de vista: estudantes de medicina | [Partes interessadas](../fase-1/partes-interessadas.md) |
| Contexto: desktop, funções F01 a F04 e F06 a F09, testes de cenário e questionários com estudantes | Objetos, profundidade e limites de validade em [Escopo e profundidade](../fase-1/escopo.md) |
| Ênfase na parametrização do PICO, na leitura do Quality Score e no uso dos créditos pagos | Justificativa da escolha de C2 em [Seleção e priorização das características](../fase-1/caracteristicas.md#2-caracteristicas-selecionadas) |

### Abstraction sheet do G2

| Objeto | Propósito | Foco da qualidade | Ponto de vista |
|--------|-----------|-------------------|----------------|
| Website VICKY, fluxo do cadastro à exportação | Avaliar | Operabilidade, proteção contra erro do usuário e autodescritividade | Estudantes de medicina |

| Foco da qualidade (o que será contado) | Fatores de variação |
|----------------------------------------|---------------------|
| Padrões de interação consistentes e inconsistentes; mensagens claras e confusas; ações caras ou destrutivas com e sem proteção; erros de entrada com e sem sugestão de correção; erros recuperáveis e irrecuperáveis; páginas de entrada que explicam ou não o produto; elementos da interface que o estudante entende ou não no primeiro uso | Versão em produção na data da coleta; semestre do estudante e experiência prévia com revisão de literatura; avaliador que conhece ou não o código |

| Hipóteses de referência | Impacto dos fatores de variação |
|-------------------------|---------------------------------|
| As hipóteses H2.1 a H2.3 abaixo, formuladas a partir de uma inspeção preliminar do código-fonte (fork do VICKY, commit `c2ae570`, de 29/09/2026) | Estudante que já fez revisão sistemática tende a entender mais os campos do PICO. Avaliador que conhece o código tende a achar a interface mais clara do que ela é, por isso as métricas de inspeção são coletadas por dois avaliadores, e pelo menos um não leu o código |

### Questões, hipóteses e métricas

As métricas são medidas da **ISO/IEC 25023:2016**, a norma da família SQuaRE que define como medir as características da ISO/IEC 25010. As medidas de capacidade de interação estão na cláusula 8.5, e o código de cada uma (ex.: UOp-1-G) é o da própria norma. **G** indica medida genérica, que a norma recomenda usar para toda subcaracterística selecionada, exigindo justificativa para excluir alguma; **S** indica medida específica, de uso opcional quando relevante (ISO/IEC 25023:2016, cláusula 2). Operabilidade e proteção contra erro do usuário usam todas as suas medidas genéricas.

!!! info "Autodescritividade e a ISO/IEC 25023"
    A autodescritividade entrou no modelo na edição de 2023 da ISO/IEC 25010 (Foreword), e a ISO/IEC 25023:2016 ainda segue o modelo de 2011, por isso não tem medida própria para ela. A equipe usa duas medidas da 25023 cuja definição coincide com a da subcaracterística, que é apresentar a informação necessária para tornar o uso do produto imediatamente óbvio: **UAp-3-S** (*Entry point self-descriptiveness*) e **ULe-4-S** (*Self-explanatory user interface*). A cláusula 2 da norma admite usar e adaptar medidas desde que a escolha seja justificada.

| Questão | Hipótese | Métricas |
|---------|----------|----------|
| Q2.1 - O VICKY se comporta de forma previsível de uma tela para outra e informa com clareza o resultado de cada ação? | H2.1 - A consistência operacional fica entre 0,6 e 0,8, porque botões, estados vazios e confirmações são resolvidos de formas diferentes conforme a tela, e entre 85% e 95% das mensagens comunicam o resultado certo; as que falham mostram texto técnico do servidor. | [M2.1.1](especificacao-das-metricas.md#m211) (UOp-1-G), [M2.1.2](especificacao-das-metricas.md#m212) (UOp-2-G) |
| Q2.2 - Um engano do estudante ao configurar o projeto ou ao acionar uma ação paga pode custar crédito ou trabalho? | H2.2 - Entre 50% e 70% das ações caras ou destrutivas têm proteção, e iniciar a triagem completa, que consome um crédito, não pede confirmação. O sistema corrige valores inválidos em silêncio em vez de sugerir o correto (40% ou menos), e menos da metade dos erros possíveis pode ser desfeita depois. | [M2.2.1](especificacao-das-metricas.md#m221) (UEp-1-G), [M2.2.2](especificacao-das-metricas.md#m222) (UEp-2-S), [M2.2.3](especificacao-das-metricas.md#m223) (UEp-3-S) |
| Q2.3 - Sem ajuda externa, o estudante entende o que o VICKY faz, como configurar o PICO e como ler o Quality Score? | H2.3 - As quatro páginas de entrada explicam para que serve o produto, mas só entre 60% e 75% dos elementos do fluxo são entendidos no primeiro uso, e o Quality Score está entre os não entendidos. | [M2.3.1](especificacao-das-metricas.md#m231) (UAp-3-S), [M2.3.2](especificacao-das-metricas.md#m232) (ULe-4-S) |

!!! note "Por que as hipóteses têm números"
    Os valores vêm de uma leitura preliminar do código-fonte, feita só para formular as hipóteses. A medição da Fase 4 é feita no VICKY em produção e pode confirmar ou refutar cada uma.

## G3

**Característica de origem:** C3 - Manutenibilidade · **Parte interessada:** _a definir_

| Elemento do template | Definição |
|----------------------|-----------|
| Analisar | o website VICKY |
| com o propósito de | _-_ |
| com respeito a | _-_ |
| do ponto de vista de | _-_ |
| no contexto de | _-_ |

| Questão | Hipótese | Métricas |
|---------|----------|----------|
| Q3.1 - _a definir_ | H3.1 - _-_ | M3.1.1 |

!!! tip "Cuidados apontados pela rubrica"
    - As questões não devem ser a própria métrica em forma de pergunta (F2-C2).
    - Toda questão precisa de uma hipótese clara (F2-C3).

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 05/10/2026 | Criação da estrutura do documento | Gabriel Fae | - |
| 0.2 | 16/10/2026 | Reorganização da documentação por fases do processo de avaliação | Gabriel Fae | - |
| 0.3 | 18/10/2026 | GQM de capacidade de interação (G2): objetivo, rastreabilidade com a Fase 1, abstraction sheet, questões e hipóteses | Lucas Avelar | Gabriel Fae |
