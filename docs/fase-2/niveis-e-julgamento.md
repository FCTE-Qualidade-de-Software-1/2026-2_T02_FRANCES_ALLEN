# Níveis de pontuação e critérios de julgamento

Os níveis são definidos **antes da coleta** para que a interpretação dos resultados não seja ajustada a posteriori. A rubrica (F2-C5) exige níveis para **todas** as métricas.

## 1. Níveis de pontuação por métrica

Cada métrica recebe um de quatro níveis: Insatisfatório (0 ponto), Aceitável (1), Bom (2) ou Excelente (3). Cada faixa inclui o limite inferior e exclui o superior, de modo que todo valor cai em exatamente um nível.

| Métrica | Insatisfatório | Aceitável | Bom | Excelente | Fonte do limiar |
|---------|:--------------:|:---------:|:---:|:---------:|-----------------|
| M1.1.1 | abaixo de 0,40 | de 0,40 a menos de 0,60 | de 0,60 a menos de 0,80 | 0,80 ou mais | Abaixo de 0,40 o estudante perde a maior parte da evidência; a hipótese H1.1 (0,40 a 0,60) corresponde à faixa Aceitável. |
| M1.1.2 | abaixo de 0,50 | de 0,50 a menos de 0,70 | de 0,70 a menos de 0,90 | 0,90 ou mais | Cada limiar fica 0,10 acima do de M1.1.1, o ganho previsto em H1.1 ao descontar os estudos que as fontes não indexam. Abaixo de 0,50 a VICKY deixa de fora estudos que as bases têm. |
| M1.2.1 | abaixo de 70% | de 70% a menos de 85% | de 85% a menos de 95% | 95% ou mais | Com nove funções, Excelente exige todas operantes; uma função parcial (94,4%) ou ausente (88,9%) leva a Bom, o que corresponde a H1.2; três ausentes (66,7%) levam a Insatisfatório. |
| M1.3.1 | abaixo de 50% | de 50% a menos de 70% | de 70% a menos de 85% | 85% ou mais | Abaixo de 50% mais da metade da lista é ruído; H1.3 (70% a 85%) corresponde a Bom. O resultado só vale com kappa de Cohen de 0,61 ou mais (Landis; Koch, 1977). |
| M1.3.2 | abaixo de 80% | de 80% a menos de 90% | de 90% a menos de 98% | 98% ou mais | Abaixo de 80% um em cada cinco itens exige correção antes de citar; o piso de Bom (90%) coincide com H1.3. |
| M1.4.1 | abaixo de 0,36 | de 0,36 a menos de 0,50 | de 0,50 a menos de 0,70 | 0,70 ou mais | O piso de Aceitável, 0,36, é o valor crítico de ρ com 30 itens a 5% de significância, em teste bilateral (Zar, 1972); abaixo dele o escore não se distingue de ordem aleatória frente à rubrica. Demais faixas por convenção da equipe; o piso de Bom (0,50) coincide com H1.4. |
| M1.5.1 | abaixo de 80% | de 80% a menos de 93% | de 93% a menos de 100% | 100% | Filtro é regra objetiva, então Excelente só vale sem nenhuma violação; o piso de Bom (93%) coincide com H1.5. |
| M1.5.2 | abaixo de 0,50 | de 0,50 a menos de 0,70 | de 0,70 a menos de 0,85 | 0,85 ou mais | Abaixo de 0,50 o registro da busca não permite replicar a revisão. |
| M2.1.1 | < 70% | 70% a menos de 90% | 90% a menos de 100% | 100% | O estudante decide sozinho, antes de pagar, se a ferramenta serve para o trabalho dele; com 10 cenários, "Bom" admite um cenário não descrito |
| M2.2.1 | < 70% | 70% a menos de 88% | 88% a menos de 100% | 100% | O VICKY não tem tutorial nem suporte em tempo real, e o estudante o usa poucas vezes por semestre; com 9 funções, "Bom" admite uma função sem orientação |
| M2.2.2 | < 50% | 50% a menos de 75% | 75% a menos de 90% | ≥ 90% | Os erros mais prováveis estão no cadastro e na criação do projeto, ou seja, no primeiro uso; mensagem sem solução ali leva ao abandono |
| M2.3.1 | < 0,70 | 0,70 a menos de 0,80 | 0,80 a menos de 0,90 | ≥ 0,90 | Com 10 padrões na lista, "Bom" admite até 2 inconsistências; a partir de 4, o estudante precisa reaprender telas do mesmo fluxo |
| M2.3.2 | < 70% | 70% a menos de 85% | 85% a menos de 95% | ≥ 95% | Texto técnico do servidor é a falha mais grave para quem não é da área de computação |
| M2.4.1 | < 70%, **ou** qualquer ação que consome crédito sem proteção | 70% a menos de 85% | 85% a menos de 100%, com todas as ações que consomem crédito protegidas | 100% | A triagem completa custa R$ 24,90 por execução, e o modelo de qualidade destaca que, na interface paga por crédito, um erro de configuração custa dinheiro e tempo |
| M2.4.2 | < 40% | 40% a menos de 60% | 60% a menos de 80% | ≥ 80% | Medida específica; os erros de entrada mais caros estão na configuração do projeto, que define a triagem paga |
| M2.5.1 | < 40% | 40% a menos de 60% | 60% a menos de 80% | ≥ 80% | Prioridade secundária no modelo de qualidade: a aparência influencia a satisfação, mas não decide se o estudante conclui a tarefa |
| M2.6.1 | < 75%, **ou** F01 (cadastro e login) não concluída | 75% a menos de 88% | 88% a menos de 100% | 100% | A Lei Brasileira de Inclusão (Lei nº 13.146/2015, art. 63) obriga sites de empresas com sede no país a serem acessíveis; com 9 funções, "Bom" admite uma falha, e sem F01 nenhuma outra função é alcançável |
| M2.6.2 | < 85% | 85% a menos de 95% | 95% a menos de 100% | 100% | Só 100% atende ao nível AA da WCAG 2.2, que é a referência de acessibilidade usada para cumprir o art. 63 da Lei nº 13.146/2015 |
| M2.7.1 | 1 de 4 ou menos | 2 de 4 | 3 de 4 | 4 de 4 | O estudante chega por link de colega, anúncio ou indicação do orientador, em qualquer uma das páginas de entrada |
| M2.7.2 | < 60%, **ou** Quality Score não entendido | 60% a menos de 75% | 75% a menos de 90% | ≥ 90% | O modelo de qualidade destaca que o VICKY usa termos técnicos (PICO, Quality Score) e promete que o estudante não precisa saber montar um PICO; se ele não entende o score, não consegue defender a lista diante do orientador |
| M3.1.1 | > 15 | de 10 a 15 | de 5 a 9 | < 5 | Diretrizes de design de software indicam que módulos com mais de 15 acoplamentos (dependências importadas) frequentemente violam o Princípio da Responsabilidade Única (SRP). |
| M3.1.2 | < 70% | 70% a 84% | 85% a 94% | ≥ 95% | A orquestração assíncrona exige alta previsibilidade. O piso de Bom (85%) reflete a expectativa de modularidade adequada, enquanto abaixo de 70% o risco de quebra ao modificar é crítico. |
| M3.2.1 | < 75% | 75% a 89% | 90% a 99% | 100% | O guia PEP8 é o padrão da comunidade. Menos de 75% de adequação indica ausência de automação de linting na esteira de desenvolvimento, causando alto atrito de leitura. |
| M3.2.2 | > 10% | 5,1% a 10% | 2% a 5% | < 2% | Princípio DRY (*Don't Repeat Yourself*). Acima de 10%, uma correção de *bug* precisará ser replicada em múltiplos arquivos, multiplicando o risco de omissão. |
| M3.2.3 | < 50% | 50% a 74% | 75% a 89% | ≥ 90% | Em integrações com IA e *scrapers* externos, falhas ocorrem fora do controle da aplicação. Menos de 50% de completude de logs deixa a equipe "cega" em produção. |
| M3.3.1 | < 50% | 50% a 69% | 70% a 89% | ≥ 90% | O piso de Bom (70%) coincide com a hipótese H3.3. Abaixo de 50% a cobertura é ilusória e modificar lógicas centrais torna-se uma operação de alto risco. |

Nas oito métricas de G1, quanto maior o valor, melhor.

Os limiares de G1 são proposta da equipe, a validar pelo grupo, exceto M1.4.1 (valor crítico de Zar, 1972).

## 2. Regras do G1 (adequação funcional)

### Da métrica para a questão

A pontuação de uma questão é a média dos pontos (0 a 3) de suas métricas, classificada em Insatisfatório (de 0,00 a menos de 1,00), Aceitável (de 1,00 a menos de 1,75), Bom (de 1,75 a menos de 2,50) ou Excelente (de 2,50 a 3,00). Duas métricas são críticas, M1.1.1 e M1.3.1: se qualquer uma ficar no nível Insatisfatório, a questão correspondente (Q1.1 ou Q1.3) não passa de Aceitável, porque uma lista que perde a evidência ou traz artigos irrelevantes não serve, por mais bem formatada que seja. Uma métrica que não puder ser coletada é declarada não aplicável, sai da média e não recebe nível por estimativa. Cada hipótese de H1.1 a H1.5 é comparada com o valor observado no relatório, mas não entra na pontuação.

### Da questão para o objetivo

O objetivo G1 é a média simples das pontuações das cinco questões (Q1.1 a Q1.5), com as mesmas faixas de classificação, e não passa de Bom se alguma questão ficar no nível Insatisfatório. O relatório informa sempre quantas das oito métricas foram medidas e o perfil das cinco questões, para que a nota global não esconda um ponto fraco.

### Do objetivo para o julgamento do produto

| Situação | Julgamento |
|----------|------------|
| G1 em Bom ou Excelente | Atende |
| G1 em Aceitável | Atende parcialmente |
| G1 em Insatisfatório | Não atende |

## 3. Regras do G2 (capacidade de interação)

A ISO/IEC 25023:2016 define como calcular cada medida, mas não diz qual valor é bom: a cláusula 1 declara que a norma não atribui faixas de valores a níveis de pontuação, porque isso depende do produto e da necessidade de quem o usa. Por isso cada limiar do G2 está justificado na coluna "Fonte do limiar" por uma necessidade do estudante de medicina ou por uma decisão registrada na Fase 1, e foi fixado antes da coleta.

As quatro faixas seguem a escala clássica de níveis de pontuação da ISO/IEC 14598-1:1999: **Excelente** = ultrapassa os requisitos, **Bom** = intervalo alvo, **Aceitável** = mínimo aceitável e **Insatisfatório** = inaceitável; os três primeiros são satisfatórios. A 14598-1 foi cancelada e substituída pela família SQuaRE; na ISO/IEC 25040:2024 o mesmo papel cabe aos níveis de classificação da qualidade (*quality rating levels*) definidos antes da medição. Cada faixa é um intervalo fechado à esquerda e aberto à direita, para que todo valor medido caia em exatamente um nível.

**1. Da medição para a hipótese.** A hipótese H2.x é **confirmada** quando os valores medidos caem na faixa que ela previu e **refutada** quando não caem. Confirmar ou refutar a hipótese não muda o julgamento do produto: mostra se a leitura preliminar da equipe estava certa.

**2. Da métrica para a questão.** O nível da questão é dado pela medida de referência indicada abaixo. As demais medidas da questão só interferem para baixo: se uma delas ficar em "Insatisfatório", a questão desce um nível.

| Questão | Medida de referência | Medidas que podem rebaixar |
|---------|----------------------|----------------------------|
| Q2.1 | M2.1.1 (UAp-1-G) | - |
| Q2.2 | M2.2.1 (ULe-1-G) | M2.2.2 (ULe-3-S) |
| Q2.3 | menor nível entre M2.3.1 e M2.3.2 (ambas genéricas) | - |
| Q2.4 | M2.4.1 (UEp-1-G) | M2.4.2 (UEp-2-S) |
| Q2.5 | M2.5.1 (UIn-1-S) | - |
| Q2.6 | M2.6.1 (UAc-1-G) | M2.6.2 (contraste) |
| Q2.7 | M2.7.2 (ULe-4-S), a medida com estudantes reais | M2.7.1 (UAp-3-S) |

**3. Da questão para o objetivo.** O julgamento usa as seis questões das subcaracterísticas principais (Q2.1 a Q2.4, Q2.6 e Q2.7). A Q2.5, de engajamento, tem prioridade secundária no modelo de qualidade: é relatada e pode gerar recomendação, mas não entra na contagem.

| Situação das seis questões principais | Julgamento do G2 |
|---------------------------------------|------------------|
| Nenhuma em "Insatisfatório" e pelo menos quatro em "Bom" ou "Excelente" | Atende |
| No máximo uma em "Insatisfatório" | Atende parcialmente |
| Duas ou mais em "Insatisfatório", **ou** Q2.4 em "Insatisfatório" por ação que consome crédito sem proteção | Não atende |

Quando mais de uma linha se aplica, vale a mais severa: "Não atende" prevalece sobre "Atende parcialmente". A regra da Q2.4 existe porque, entre os problemas de capacidade de interação, o único que tira dinheiro do estudante é o engano numa ação paga.

## 4. Regras do G3 (manutenibilidade)

### Da métrica para a questão

A pontuação de uma questão é a média dos pontos (0 a 3) de suas métricas, classificada em Insatisfatório (de 0,00 a menos de 1,00), Aceitável (de 1,00 a menos de 1,75), Bom (de 1,75 a menos de 2,50) ou Excelente (de 2,50 a 3,00). Duas métricas possuem caráter bloqueador, M3.1.2 e M3.3.1: se a adequação da complexidade ciclomática (M3.1.2) ficar no nível Insatisfatório, a questão correspondente (Q3.1) não passa de Aceitável, pois um baixo acoplamento não compensa funções intrinsecamente frágeis. A questão Q3.3 é ditada exclusivamente por sua única métrica (M3.3.1). Uma métrica que não puder ser coletada é declarada não aplicável, sai da média e não recebe nível por estimativa. Cada hipótese de H3.1 a H3.3 é comparada com o valor observado no relatório, mas não entra na pontuação.

### Da questão para o objetivo

O objetivo G3 é a média simples das pontuações das três questões (Q3.1 a Q3.3), com as mesmas faixas de classificação, e não passa de Aceitável se a questão de testabilidade (Q3.3) ficar no nível Insatisfatório, pois modificar código assíncrono complexo sem cobertura de testes automatizados é tecnicamente insustentável. O relatório informa sempre quantas das seis métricas foram medidas e o perfil das três questões, para que a nota global não esconda gargalos de dívida técnica.

### Do objetivo para o julgamento do produto

| Situação | Julgamento |
|----------|------------|
| G3 em Bom ou Excelente | Atende |
| G3 em Aceitável | Atende parcialmente |
| G3 em Insatisfatório | Não atende |

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 05/10/2026 | Criação da estrutura do documento | Gabriel Fae | - |
| 0.2 | 16/10/2026 | Reorganização da documentação por fases do processo de avaliação | Gabriel Fae | - |
| 0.3 | 18/10/2026 | Níveis de pontuação e regras de julgamento do G2 (capacidade de interação) | Lucas Avelar | Gabriel Fae |
| 0.4 | 18/10/2026 | Níveis das oito métricas de G1 e critérios de julgamento do objetivo G1 | Larissa Gomes Silva | - |
| 0.5 | 18/10/2026 | Níveis das métricas de G3 e regras de agregação e julgamento do objetivo de Manutenibilidade | Guilherme Moura | - |
| 0.6 | 18/10/2026 | Níveis e regras do G2 realinhados às sete subcaracterísticas de C2 | Lucas Avelar | Gabriel Fae |
| 0.7 | 25/10/2026 | G1: texto enxugado, repetição removida entre fichas | Larissa Gomes Silva | - |
