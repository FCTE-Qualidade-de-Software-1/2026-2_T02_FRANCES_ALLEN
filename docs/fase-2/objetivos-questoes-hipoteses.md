# Objetivos, questões e hipóteses

Cada objetivo deriva de uma característica selecionada na [Fase 1](../fase-1/caracteristicas.md) (critério F2-C11: rastreabilidade entre Fases 1 e 2).

## Rastreabilidade com a Fase 1

O **foco de qualidade** de cada objetivo vem da característica selecionada, e o **ponto de vista** vem das [partes interessadas](../fase-1/partes-interessadas.md).

| Característica (Fase 1) | Parte interessada | Objetivo GQM |
|-------------------------|-------------------|--------------|
| C1 - Adequação funcional | Estudantes de medicina | [G1](#g1) |
| C2 - Capacidade de interação | Estudantes de medicina (usuário) | [G2](#g2) |
| C3 - Manutenibilidade | Equipe de desenvolvimento | [G3](#g3) |

## G1

**Característica de origem:** C1 - Adequação funcional · **Parte interessada:** Estudantes de medicina

A [Fase 1](../fase-1/caracteristicas.md) classificou a adequação funcional como Must Have, com 15 pontos no MoSCoW com pesos (impacto 3, viabilidade 3): o estudante só confia no Top N se a lista trouxer a evidência certa, e a equipe tem acesso a estudantes para os testes. O ponto de vista é o dos estudantes de medicina, usuários listados nas [partes interessadas](../fase-1/partes-interessadas.md). A Fase 1 apontou completude e correção como subcaracterísticas candidatas; G1 mede também a pertinência funcional (Q1.4 e Q1.5), porque a ordem do ranking e o cumprimento dos filtros decidem se o resultado serve à tarefa que o estudante configurou. As três subcaracterísticas seguem a ISO/IEC 25010:2023: completude, correção e pertinência funcional.

| Elemento do template | Definição |
|----------------------|-----------|
| Analisar | o website VICKY (<https://vicky.synaptha.com/>), versão em produção na data da coleta, com foco na lista ranqueada (Top 30) e nas funções que a produzem |
| com o propósito de | entender |
| com respeito a | adequação funcional (completude, correção e pertinência funcional) |
| do ponto de vista de | estudantes de medicina que montam a revisão de literatura de um trabalho de conclusão |
| no contexto de | triagem de literatura clínica e de saúde pública em português e inglês, com busca em PubMed, SciELO e Google Acadêmico, em navegador de computador |

O propósito é entender porque a Fase 4 precisa conhecer o nível atual de adequação funcional antes de indicar melhorias. O VICKY declara que não escreve a revisão nem faz avaliação crítica dos artigos, e por isso essas limitações não contam como falha.

### Rastreabilidade com a Fase 1

| Elemento do G1 | Origem na Fase 1 |
|----------------|------------------|
| Foco de qualidade: completude, correção e pertinência funcional | Subcaracterísticas selecionadas para C1 em [Seleção e priorização das características](../fase-1/caracteristicas.md#2-caracteristicas-selecionadas) (completude e correção); a pertinência funcional é acréscimo do G1, justificado acima |
| Ponto de vista: estudantes de medicina | [Partes interessadas](../fase-1/partes-interessadas.md) |
| Contexto: navegador desktop, funções F01 a F09 e testes de cenário | Objetos, profundidade e limites de validade em [Escopo e profundidade](../fase-1/escopo.md); a triagem completa (F05) entrou no escopo por decisão do grupo em 18/10/2026, porque a lista ranqueada, os favoritos, o log e a exportação só existem depois de uma triagem |
| Ênfase na lista ranqueada (Top 30) | Justificativa da escolha de C1 em [Seleção e priorização das características](../fase-1/caracteristicas.md#2-caracteristicas-selecionadas): o estudante só confia no Top N se a lista trouxer a evidência certa |

### Abstraction sheet do G1

| Objeto | Propósito | Foco da qualidade | Ponto de vista |
|--------|-----------|-------------------|----------------|
| Website VICKY, lista ranqueada (Top 30) e funções que a produzem | Entender | Completude, correção e pertinência funcional | Estudantes de medicina |

| Foco da qualidade (o que será contado) | Fatores de variação |
|----------------------------------------|---------------------|
| Estudos da revisão de referência recuperados e não recuperados; funções declaradas operantes, parciais e ausentes; artigos relevantes e não relevantes ao PICO; itens com metadados e link corretos e incorretos; concordância entre a ordem do Quality Score e a rubrica metodológica; itens que cumprem e que violam os filtros; artigos repetidos entre duas execuções do mesmo tema | Tema de teste (T1 a T4: fármaco, intervenção não farmacológica, saúde pública brasileira e tema estreito); idioma e base que indexa cada estudo; versão em produção na data da coleta; execução, porque a triagem usa modelos de linguagem e pode variar; avaliador que julga relevância e rubrica |

| Hipóteses de referência | Impacto dos fatores de variação |
|-------------------------|---------------------------------|
| As hipóteses H1.1 a H1.5 abaixo, formuladas antes da coleta como baseline | Tema estreito tem poucos estudos e tende a puxar o recall para baixo; estudo que as bases não indexam não é falha da VICKY, por isso M1.1.2 desconta esses casos; duas execuções do mesmo tema podem trazer listas diferentes, o que M1.5.2 mede com intervalo de 24 horas ou mais; avaliadores divergem no julgamento de relevância, por isso M1.3.1 e M1.4.1 usam dois avaliadores e M1.3.1 só vale com kappa de 0,61 ou mais |

### Questões, hipóteses e métricas

Pelo método Goal-Question-Metric (Basili; Caldiera; Rombach, 1994), cinco questões desdobram o objetivo. Duas tratam da completude: se a lista contém os estudos que uma revisão de referência incluiria e se o estudante consegue executar o fluxo prometido, do protocolo PICO ao registro da busca. Uma trata da correção: se os artigos respondem ao PICO e vêm com metadados e links corretos. Duas tratam da pertinência: se a ordem do Quality Score acompanha um critério metodológico explícito e se o resultado obedece aos filtros e se repete quando a configuração é repetida. Filtros e repetibilidade entram na pertinência porque determinam se o resultado serve à tarefa configurada e se a busca pode ser registrada e replicada na revisão. Cada hipótese é um baseline, formulado antes da coleta.

!!! info "Por que o G1 adapta as medidas da ISO/IEC 25023"
    As medidas de adequação funcional da ISO/IEC 25023:2016 (subcláusula 8.2) contam funções: a cobertura funcional (FCp-1-G, *Functional coverage*), a correção funcional (FCr-1-G, *Functional correctness*) e a pertinência ao objetivo de uso e ao sistema (FAp-1-G e FAp-2-G, *Functional appropriateness*). Na VICKY, porém, o que o estudante usa é a lista ranqueada, e saber que a função de triagem "funciona" não diz se a lista traz a evidência certa. Por isso o G1 mantém M1.2.1 como contagem de funções, no molde da FCp-1-G, e adapta as demais para o nível do artigo da lista: recall a partir da FCp-1-G, precisão e metadados a partir da FCr-1-G, e ordem do ranking, filtros e estabilidade (adaptação própria do G1) a partir da FAp-1-G. A cláusula 2 da norma admite modificar uma medida desde que a mudança seja justificada. A FAp-2-G, que olha a pertinência do conjunto de funções do sistema, não é medida à parte: o ponto de vista do G1 é o da tarefa do estudante, coberto pela FAp-1-G, e a cláusula 2 pede justificativa para excluir uma medida genérica, que é esta.

| Questão | Hipótese | Métricas |
|---------|----------|----------|
| Q1.1 - A lista contém os estudos que uma revisão de referência sobre o mesmo tema incluiria? (completude funcional) | H1.1 - A VICKY recupera de 40% a 60% dos estudos da revisão dentro do teto de 30 posições; descontados os estudos que as fontes não indexam, o valor sobe 10 pontos percentuais ou mais | [M1.1.1](especificacao-das-metricas.md#m111), [M1.1.2](especificacao-das-metricas.md#m112) |
| Q1.2 - Que partes do fluxo prometido, do PICO ao registro da busca, o estudante consegue executar? (completude funcional) | H1.2 - No máximo uma das 9 funções declaradas está parcial ou ausente | [M1.2.1](especificacao-das-metricas.md#m121) |
| Q1.3 - Os artigos respondem ao PICO e vêm descritos de modo que o estudante possa citá-los? (correção funcional) | H1.3 - De 70% a 85% dos 30 artigos são relevantes e 90% ou mais têm metadados e link corretos | [M1.3.1](especificacao-das-metricas.md#m131), [M1.3.2](especificacao-das-metricas.md#m132) |
| Q1.4 - A ordem do ranking acompanha um critério explícito de qualidade metodológica? (pertinência funcional) | H1.4 - Há correlação positiva de moderada a forte (0,50 ou mais) entre o Quality Score e uma rubrica metodológica | [M1.4.1](especificacao-das-metricas.md#m141) |
| Q1.5 - O resultado obedece ao que o estudante configurou e se mantém quando a configuração é repetida? (pertinência funcional) | H1.5 - Os filtros são cumpridos em 93% ou mais dos itens; duas execuções do mesmo tema repetem 70% ou mais dos artigos, sem repetir todos | [M1.5.1](especificacao-das-metricas.md#m151), [M1.5.2](especificacao-das-metricas.md#m152) |

## G2

**Característica de origem:** C2 - Capacidade de interação · **Parte interessada:** estudantes de medicina (usuário)

| Elemento do template | Definição |
|----------------------|-----------|
| Analisar | o website VICKY |
| com o propósito de | avaliar |
| com respeito a | capacidade de interação: reconhecimento da adequação, facilidade de aprendizado, operabilidade, proteção contra erro do usuário, engajamento do usuário, assistência ao usuário (contraste e motricidade) e autodescritividade |
| do ponto de vista de | estudantes de medicina |
| no contexto de | uso do VICKY em produção, em navegador desktop, no fluxo que vai do cadastro à exportação dos resultados, por inspeção da equipe e por testes de cenário com estudantes de medicina |

### Rastreabilidade com a Fase 1

| Elemento do G2 | Origem na Fase 1 |
|----------------|------------------|
| Foco de qualidade: as sete subcaracterísticas mantidas para C2, com engajamento em prioridade secundária e assistência ao usuário reduzida a contraste e motricidade | [Modelo de qualidade, seção 2.2](../fase-1/modelo-de-qualidade.md#22-capacidade-de-interacao-c2) e [Seleção e priorização das características](../fase-1/caracteristicas.md#2-caracteristicas-selecionadas) |
| Ponto de vista: estudantes de medicina | [Partes interessadas](../fase-1/partes-interessadas.md) |
| Contexto: desktop, funções F01 a F09, testes de cenário e questionários com estudantes | Objetos, profundidade e limites de validade em [Escopo e profundidade](../fase-1/escopo.md) |
| Ênfase na configuração do PICO, na leitura do Quality Score e no uso dos créditos pagos | Justificativa da escolha de C2 em [Seleção e priorização das características](../fase-1/caracteristicas.md#2-caracteristicas-selecionadas) e adaptação em [Modelo de qualidade](../fase-1/modelo-de-qualidade.md#22-capacidade-de-interacao-c2) |

### Abstraction sheet do G2

| Objeto | Propósito | Foco da qualidade | Ponto de vista |
|--------|-----------|-------------------|----------------|
| Website VICKY, fluxo do cadastro à exportação | Avaliar | As sete subcaracterísticas de capacidade de interação mantidas no modelo | Estudantes de medicina |

| Foco da qualidade (o que será contado) | Fatores de variação |
|----------------------------------------|---------------------|
| Cenários de uso descritos e não descritos; funções com e sem orientação; mensagens com e sem causa e solução; padrões de interação consistentes e inconsistentes; ações caras com e sem proteção; erros de entrada com e sem sugestão de correção; telas consideradas agradáveis ou não; funções utilizáveis só com teclado; pares de cor com contraste suficiente; elementos entendidos ou não no primeiro uso | Versão em produção na data da coleta; semestre do estudante e experiência prévia com revisão de literatura; avaliador que conhece ou não o código |

| Hipóteses de referência | Impacto dos fatores de variação |
|-------------------------|---------------------------------|
| As hipóteses H2.1 a H2.7 abaixo, formuladas a partir de uma inspeção preliminar do código-fonte (fork do VICKY, commit `c2ae570`, de 29/09/2026) | Estudante que já fez revisão sistemática tende a entender mais os campos do PICO. Avaliador que conhece o código tende a achar a interface mais clara do que ela é, por isso as métricas de inspeção são coletadas por dois avaliadores, e pelo menos um não leu o código |

### Questões, hipóteses e métricas

As métricas são medidas da **ISO/IEC 25023:2016**, a norma da família SQuaRE que define como medir as características da ISO/IEC 25010. As medidas de capacidade de interação estão na cláusula 8.5, e o código de cada uma (ex.: UOp-1-G) é o da própria norma. **G** indica medida genérica, que a norma recomenda usar para toda subcaracterística selecionada, exigindo justificativa para excluir alguma; **S** indica medida específica, de uso opcional quando relevante (ISO/IEC 25023:2016, cláusula 2). Toda subcaracterística que tem medida genérica na norma usa todas elas.

!!! info "Subcaracterísticas de 2023 e medidas de 2016"
    A ISO/IEC 25023:2016 segue o modelo de 2011 da ISO/IEC 25010, e a edição de 2023 renomeou, dividiu e criou subcaracterísticas (Foreword). A equipe associa as medidas assim, como a cláusula 2 da norma admite desde que justificado: **engajamento do usuário**, que substituiu a estética da interface, usa a medida de estética (UIn-1-S); **assistência ao usuário**, que herdou a definição da antiga acessibilidade, usa a medida de acessibilidade (UAc-1-G) e uma medida adicional de contraste; **autodescritividade**, nova em 2023, usa as duas medidas da norma cuja definição coincide com a dela (UAp-3-S e ULe-4-S).

| Questão | Hipótese | Métricas |
|---------|----------|----------|
| Q2.1 - Antes de criar conta, o estudante consegue saber o que o VICKY faz e o que ele não faz? (reconhecimento da adequação) | H2.1 - As páginas públicas descrevem pelo menos 90% dos cenários de uso, incluindo o limite de que o VICKY não substitui a leitura crítica dos artigos. | [M2.1.1](especificacao-das-metricas.md#m211) (UAp-1-G) |
| Q2.2 - Um estudante sem formação em metodologia aprende a montar o primeiro projeto sozinho? (facilidade de aprendizado) | H2.2 - A orientação dentro das telas cobre pelo menos 85% das funções, mas só entre 50% e 75% das mensagens de erro dizem como resolver o problema. | [M2.2.1](especificacao-das-metricas.md#m221) (ULe-1-G), [M2.2.2](especificacao-das-metricas.md#m222) (ULe-3-S) |
| Q2.3 - O VICKY se comporta de forma previsível de uma tela para outra e informa com clareza o resultado de cada ação? (operabilidade) | H2.3 - A consistência operacional fica entre 0,6 e 0,8, porque botões, estados vazios e confirmações são resolvidos de formas diferentes conforme a tela, e entre 85% e 95% das mensagens comunicam o resultado certo; as que falham mostram texto técnico do servidor. | [M2.3.1](especificacao-das-metricas.md#m231) (UOp-1-G), [M2.3.2](especificacao-das-metricas.md#m232) (UOp-2-G) |
| Q2.4 - Um engano ao configurar o projeto ou ao acionar uma ação paga pode custar crédito ao estudante? (proteção contra erro do usuário) | H2.4 - Entre 50% e 70% das ações caras ou destrutivas têm proteção, e iniciar a triagem completa, que consome um crédito, não pede confirmação. O sistema corrige valores inválidos em silêncio em vez de sugerir o correto (40% ou menos). | [M2.4.1](especificacao-das-metricas.md#m241) (UEp-1-G), [M2.4.2](especificacao-das-metricas.md#m242) (UEp-2-S) |
| Q2.5 - A aparência do VICKY convida o estudante a continuar usando? (engajamento do usuário, prioridade secundária) | H2.5 - A maioria dos participantes considera agradáveis pelo menos 4 das 5 telas avaliadas. | [M2.5.1](especificacao-das-metricas.md#m251) (UIn-1-S) |
| Q2.6 - Uma pessoa com dificuldade motora ou baixa visão consegue usar o fluxo principal? (assistência ao usuário) | H2.6 - Pelo menos 7 das 9 funções podem ser usadas só com o teclado, e entre 85% e 99% dos pares de texto e fundo têm contraste suficiente; os que falham são textos secundários em cinza claro. | [M2.6.1](especificacao-das-metricas.md#m261) (UAc-1-G), [M2.6.2](especificacao-das-metricas.md#m262) (medida adicional) |
| Q2.7 - Sem ajuda externa, o estudante entende os termos e elementos do VICKY, como o PICO e o Quality Score? (autodescritividade) | H2.7 - As quatro páginas de entrada explicam para que serve o produto, mas só entre 60% e 75% dos elementos do fluxo são entendidos no primeiro uso, e o Quality Score está entre os não entendidos. | [M2.7.1](especificacao-das-metricas.md#m271) (UAp-3-S), [M2.7.2](especificacao-das-metricas.md#m272) (ULe-4-S) |

!!! note "Por que as hipóteses têm números"
    Os valores vêm de uma leitura preliminar do código-fonte, feita só para formular as hipóteses. A medição da Fase 4 é feita no VICKY em produção e pode confirmar ou refutar cada uma.

## G3

**Característica de origem:** C3 - Manutenibilidade · **Parte interessada:** Equipe de desenvolvimento

A [Fase 1](../fase-1/caracteristicas.md) classificou a manutenibilidade como Should Have, com 12 pontos no MoSCoW com pesos (impacto 2, viabilidade 3): a facilidade de manter e evoluir o sistema afeta diretamente a equipe de desenvolvimento, e a viabilidade de medição é alta pelo acesso total ao código-fonte. O ponto de vista é o da equipe de desenvolvimento (desenvolvedores e arquitetos). A Fase 1 apontou analisabilidade, modularidade e modificabilidade como subcaracterísticas foco, fundamentais para um sistema com integrações externas instáveis e orquestração assíncrona. As três subcaracterísticas seguem a ISO/IEC 25010:2023.

| Elemento do template | Definição |
|----------------------|-----------|
| Analisar | o código-fonte do backend em Python do VICKY (diretórios `src/vicky/` e `tests/`), com foco nas lógicas centrais e no orquestrador `pipeline.py` |
| com o propósito de | avaliar |
| com respeito a | manutenibilidade (analisabilidade, modularidade e testabilidade) |
| do ponto de vista de | equipe de desenvolvimento e arquitetos de software |
| no contexto de | orquestração do pipeline de triagem e das integrações na versão atual do código |

O propósito é avaliar o código para que a Fase 4 consiga diagnosticar potenciais gargalos técnicos ("dívida técnica") que possam dificultar a implementação de melhorias futuras ou a correção de *bugs*.

### Rastreabilidade com a Fase 1

| Elemento do G3 | Origem na Fase 1 |
|----------------|------------------|
| Foco de qualidade: analisabilidade, modularidade e testabilidade | Subcaracterísticas selecionadas para C3 em [Seleção e priorização das características](../fase-1/caracteristicas.md#2-caracteristicas-selecionadas) |
| Ponto de vista: equipe de desenvolvimento | [Partes interessadas](../fase-1/partes-interessadas.md) |
| Contexto: backend em Python (`src/vicky/` e `tests/`), análise estática automatizada | Objetos, profundidade e limites de validade em [Escopo e profundidade](../fase-1/escopo.md) |
| Ênfase na complexidade, padrões de código, estruturação e cobertura | Justificativa da escolha de C3 em [Seleção e priorização das características](../fase-1/caracteristicas.md#2-caracteristicas-selecionadas) |

### Abstraction sheet do G3

| Objeto | Propósito | Foco da qualidade | Ponto de vista |
|--------|-----------|-------------------|----------------|
| Código-fonte do backend em Python (VICKY) | Avaliar | Analisabilidade, modularidade e testabilidade | Equipe de desenvolvimento |

| Foco da qualidade (o que será contado) | Fatores de variação |
|----------------------------------------|---------------------|
| Chamadas de dependências internas (acoplamento); funções que excedem o limiar de complexidade ciclomática; violações de estilo e formatação (PEP8); blocos de código ou lógicas estruturais duplicadas; funções críticas que registram logs de execução; proporção de linhas cobertas por testes automatizados. | Versão do código-fonte (commit analisado na data da coleta); ferramentas de análise escolhidas (`radon`, `flake8`, `pylint`, `pytest-cov`) e suas configurações de rigor; exclusão de arquivos gerados automaticamente. |

| Hipóteses de referência | Impacto dos fatores de variação |
|-------------------------|---------------------------------|
| As hipóteses H3.1 a H3.3 abaixo, formuladas a partir de uma inspeção preliminar da arquitetura do código-fonte. | Ferramentas de *linting* diferem nas regras padrão. Para estabilizar a medição, as métricas definirão o uso da configuração *default* das ferramentas mais adotadas na comunidade Python, limitando o escopo estritamente à pasta principal `src/vicky/`. |

### Questões, hipóteses e métricas

Pelo método Goal-Question-Metric, três questões desdobram o objetivo. A primeira foca na modularidade, investigando o acoplamento e se o sistema concentra lógica excessiva em poucas funções. A segunda foca na analisabilidade: a adesão a padrões comuns da linguagem, a ausência de duplicação que confunda a leitura e a presença de logs que permitam rastrear falhas. A terceira fecha o ciclo focando na testabilidade, verificando se o sistema possui testes para suportar refatorações.

!!! info "A Manutenibilidade e a ISO/IEC 25023"
    A edição de 2016 da ISO/IEC 25023 provê medidas diretas para a avaliação estrutural do software. O G3 adota estritamente o catálogo normativo: MMo-1-G (acoplamento) e MMo-2-S (complexidade) para modularidade; MRe-2-S (regras de codificação), MRe-1-G (duplicação) e MAn-1-G (logs do sistema) cobrindo analisabilidade e reusabilidade interna; e MTe-1-G garantindo a completude de testes da subcaracterística de testabilidade.

| Questão | Hipótese | Métricas |
|---------|----------|----------|
| Q3.1 - Qual é o grau de acoplamento entre os componentes e a adequação da complexidade estrutural do orquestrador? (modularidade) | H3.1 - O sistema possui acoplamento moderado, mas uma porção significativa das funções centrais de orquestração não atinge a adequação, excedendo o limite aceitável de complexidade ciclomática. | [M3.1.1](especificacao-das-metricas.md#m311), [M3.1.2](especificacao-das-metricas.md#m312) |
| Q3.2 - Qual é o nível de adesão aos padrões da linguagem Python (PEP8), a densidade de duplicação e a completude de logs no sistema? (analisabilidade) | H3.2 - O código não possui duplicação estrutural significativa e cumpre as diretrizes PEP8 na maior parte do pacote, porém apresenta baixa completude de registros de log nas integrações principais. | [M3.2.1](especificacao-das-metricas.md#m321), [M3.2.2](especificacao-das-metricas.md#m322), [M3.2.3](especificacao-das-metricas.md#m323) |
| Q3.3 - O código-fonte possui uma suíte de testes abrangente que garanta o funcionamento sistêmico? (testabilidade) | H3.3 - A cobertura de testes automatizados abrange 70% ou mais das linhas de código testáveis do backend (`src/vicky/`). | [M3.3.1](especificacao-das-metricas.md#m331) |

!!! tip "Cuidados apontados pela rubrica"
    - As questões não devem ser a própria métrica em forma de pergunta (F2-C2).
    - Toda questão precisa de uma hipótese clara (F2-C3).

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 05/10/2026 | Criação da estrutura do documento | Gabriel Fae | - |
| 0.2 | 16/10/2026 | Reorganização da documentação por fases do processo de avaliação | Gabriel Fae | - |
| 0.3 | 18/10/2026 | GQM de capacidade de interação (G2): objetivo, rastreabilidade com a Fase 1, abstraction sheet, questões e hipóteses | Lucas Avelar | Gabriel Fae |
| 0.4 | 18/10/2026 | GQM de adequação funcional (G1): objetivo, rastreabilidade com a Fase 1, abstraction sheet, questões e hipóteses | Larissa Gomes Silva | - |
| 0.5 | 18/10/2026 | GQM de manutenibilidade (G3): objetivo, rastreabilidade com a Fase 1, abstraction sheet, questões e hipóteses | Guilherme Moura | - |
| 0.6 | 19/10/2026 | G2 realinhado às sete subcaracterísticas de C2 do modelo de qualidade | Lucas Avelar | Gabriel Fae |
