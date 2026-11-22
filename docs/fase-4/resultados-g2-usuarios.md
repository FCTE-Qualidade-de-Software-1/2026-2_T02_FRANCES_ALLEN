# Resultados do G2 com usuários (capacidade de interação)

!!! note "Situação em 22/11/2026"
    M2.7.2 e M2.5.1 foram calculadas com as três sessões válidas (19 e 20/11/2026) e as três respostas ao formulário de estética. Com n = 3, os dois valores são **indicativos**. Em M2.7.2, a marcação de E02 para P01 e P02 está pendente de decisão (seção 8). A M2.5.1 só pôde ser calculada pela [D14](../gestao/decisoes.md#d14-calcular-m251-com-as-tres-respostas-obtidas), que aceitou três respostas no lugar de cinco. M2.6.1 e M2.6.2, executadas pelos avaliadores e não por estudantes, não foram coletadas até esta data: as fichas estão em branco, e a Q2.6 fica sem nível. Os valores saem dos `consolidado.md` de M2.7.2 e M2.5.1, conferidos com `dados/avaliacao/G2/calcular_g2_usuarios.py`.

Esta página reúne o resultado das métricas do G2 que dependem de estudantes de Medicina, conforme o [Método do G2 com usuários](../fase-3/metodo-g2-usuarios.md) e os [instrumentos](../fase-3/instrumentos-g2-usuarios.md). As oito métricas de inspeção estão em [Resultados do G2 por inspeção](resultados-g2-inspecao.md). Os níveis seguem a tabela de [níveis de pontuação](../fase-2/niveis-e-julgamento.md), fixada antes da coleta.

## 1. Execução da coleta

| Campo | Valor |
|-------|-------|
| Período | Sessões em 19/11/2026 (P01) e 20/11/2026 (P02 e P03). Formulário de estética respondido depois de cada sessão. Cálculo em 22/11/2026 |
| Produto | VICKY em produção, <https://vicky.synaptha.com/> |
| Formato | Sessão remota e individual pelo Google Meet, com tela e voz gravadas, no dispositivo do participante: P01 num iPad com Safari, P02 num Mac com Safari e P03 num computador com navegador não identificado na gravação |
| Tarefas | Cartão A: entrar numa conta da equipe e criar um projeto sobre "O uso de células-tronco para restauração de tecido", com os requisitos que obrigam o uso de E01 a E08, e ver os critérios antes de gastar crédito (E09). Cartão B: no projeto já triado do mesmo tema, escolher artigos (E10), mostrar onde o VICKY registra a busca (E11) e salvar o resultado em planilha (E12). Questionário de compreensão no fim |
| Participantes | 3 válidos (P01 a P03), sem reservas chamadas. Nenhuma sessão interrompida ou retirada |
| Respondentes do formulário | 3 (R01 a R03), os mesmos três participantes. Ninguém mais respondeu |
| Gravações | Pasta restrita do Drive da equipe. Hash SHA-256 de cada arquivo em `M2.7.2/sessoes.csv` |
| Dados brutos | [M2.7.2/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G2/M2.7.2) e [M2.5.1/](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G2/M2.5.1) |

### Sessões e perfil

O perfil não entra no cálculo; serve para interpretar o resultado, como prevê a abstraction sheet do G2.

| Participante | Data | Duração | Condutor | Observador | Segunda classificação | Faixa do curso | Já fez revisão | Já usou ferramenta de triagem |
|--------------|------|:-------:|----------|------------|-----------------------|----------------|:--------------:|:-----------------------------:|
| P01 | 19/11/2026 | 43 min | João Felipe Oliveira | Gabriel Fae | Observador | 1º ao 4º semestre | Sim | Não |
| P02 | 20/11/2026 | 19 min | Gabriel Fae | - | Lucas Avelar, pela gravação | Internato | Sim | Não |
| P03 | 20/11/2026 | 24 min | Gabriel Fae | - | Lucas Avelar, pela gravação | Internato | Sim | Não |

As duas classificações das explicações coincidiram nos 36 itens (12 elementos por 3 participantes), e o terceiro avaliador (A3) não foi acionado.

### Desvios do método

| Data | Desvio | Efeito na medida |
|------|--------|------------------|
| Antes da P01 | Tema das células-tronco no lugar do tema T1 do G1; parte A numa conta da equipe com créditos, e não numa conta nova com 0 crédito; sem sessão piloto ([método, seção 2.9](../fase-3/metodo-g2-usuarios.md#29-ajustes-feitos-antes-da-primeira-sessao)) | Os 12 elementos não dependem do tema nem da conta. Ninguém iniciou a triagem, e nenhum crédito foi gasto. Sem piloto, o texto dos cartões não foi calibrado, mas foi o mesmo para todos |
| 19 e 20/11 | Sessões de 19 a 43 minutos, contra 63 previstos | Nenhum tempo-limite atingido; nenhum elemento ficou sem uso por falta de tempo |
| 19/11 | P01 fez a sessão num iPad, e não num computador | A Fase 2 fixa a sessão em desktop; o desvio foi visto na gravação em 22/11 e está em `sessoes.csv` |
| 20/11 | P02 e P03 sem observador | Caminho previsto no método: ficha de uso pelo condutor, a partir da gravação, e segunda classificação por outro integrante |
| 20/11 | Nas P02 e P03, o condutor informou a classificação de cada explicação e só detalhou as exceções; os elementos não citados foram marcados como sem ajuda e corretos por padrão | A coluna `resposta_literal` fica vazia nos 21 elementos sem transcrição; as anotações do condutor levam a etiqueta `[síntese]`. A gravação é a evidência (ver as limitações) |
| 19 a 22/11 | Formulário de estética com 3 respostas, e não 5, todas de quem tinha feito a sessão | M2.5.1 calculada pela D14 com maioria de 2 de 3, com resultado indicativo |
| 22/11 | Recortes dos 12 elementos montados depois das sessões, com capturas da inspeção; capturas do formulário não guardadas | O repositório mostra o que cada elemento é, mas não a imagem exata exibida a cada participante |

## 2. M2.7.2: interface autoexplicativa

Um elemento conta como entendido pelo participante quando ele o **usou sem ajuda** nas tarefas **e o explicou corretamente** no questionário, comparado com o [gabarito](../fase-3/instrumentos-g2-usuarios.md#4-gabarito-dos-12-elementos). O elemento entra em A quando é entendido por pelo menos 2 dos 3 participantes.

| Elemento | P01 | P02 | P03 | Entendido por |
|----------|:---:|:---:|:---:|:-------------:|
| E01 Campo do tema | 1 | 1 | 1 | 3 |
| E02 Campo de objetivo | 1 | 1 | 1 | 3 |
| E03 Tipo de revisão | 1 | 1 | 1 | 3 |
| E04 Janela de anos | 1 | 1 | 1 | 3 |
| E05 Quantidade do Top | 1 | 1 | 1 | 3 |
| E06 Escolha das bases | 1 | 1 | 1 | 3 |
| E07 Filtro de acesso aberto | 1 | 1 | 1 | 3 |
| E08 Rascunho, prévia e iniciar | 1 | 1 | 1 | 3 |
| E09 Critérios PICO gerados | 1 | 1 | **0** | 2 |
| E10 Quality Score | 1 | 1 | 1 | 3 |
| E11 Log auditável | **0** | **0** | 1 | **1** |
| E12 Exportação | **0** | 1 | 1 | 2 |
| **Entendidos pelo participante** | 10 | 11 | 11 | |

| Métrica | Medida | A | B | Valor | Quality Score (E10) | Nível |
|---------|--------|:-:|:-:|:-----:|---------------------|:-----:|
| M2.7.2 | ULe-4-S | 11 | 12 | 91,7% | Entendido pelos 3 | **Excelente** (indicativo) |

**Os quatro zeros.**

- **P01, E11 e E12.** Na parte B, explorou a tela do projeto por cerca de quatro minutos (36:30 a 40:32 da gravação) sem encontrar onde a busca fica registrada nem o botão Exportar, e desistiu das duas tarefas sem pedir ajuda. No questionário, também não soube explicar os dois elementos.
- **P02, E11.** Não encontrou como a busca foi feita e disse que não conseguiria explicar o elemento.
- **P03, E09.** Usou o bloco sem ajuda, mas o explicou como "um resumo dos artigos encontrados", exatamente o erro que invalida no gabarito: o bloco traz os critérios que decidem se cada artigo entra ou sai.

**Margem do resultado.** Oito elementos foram entendidos pelos três participantes. E09 e E12 entraram em A por 2 de 3: se um único participante tivesse errado um deles, X iria a 10/12 (83,3%, Bom); se errasse os dois, a 9/12 (75,0%, Bom). Três respostas de P01 foram aceitas como corretas com interpretação (E02, E03 e E10, registradas em `M2.7.2/coleta.md`); como P02 e P03 acertaram esses elementos, a leitura delas não muda o resultado. Já a marcação de uso de E02 para P01 e P02 está pendente de decisão (seção 8): se mudar, X vai a 10/12 (83,3%, Bom).

## 3. M2.5.1: estética da interface

A tela é agradável para o respondente com nota 4 ou 5. Pela D14, entra em A quando é agradável para pelo menos 2 dos 3 respondentes; a Fase 2 pedia 3 de 5.

| Tela | R01 | R02 | R03 | Agradável para |
|------|:---:|:---:|:---:|:--------------:|
| Página inicial (painel) | 5 | 3 | 5 | 2 |
| Novo projeto | 5 | 4 | 3 | 2 |
| Detalhe do projeto | 5 | 3 | 2 | 1 |
| Lista de artigos | 5 | 2 | 1 | 1 |
| Ficha do artigo | 4 | 3 | 3 | 1 |

| Métrica | Medida | A | B | Valor | Nível |
|---------|--------|:-:|:-:|:-----:|:-----:|
| M2.5.1 | UIn-1-S | 2 | 5 | 40,0% | **Aceitável** (indicativo, D14) |

O valor está no limite inferior de Aceitável: uma tela a menos levaria a 20% (Insatisfatório). Se a regra exigisse os três respondentes, o mesmo número absoluto de "3 de 5", nenhuma tela entraria em A (0%). Os códigos R foram atribuídos sem seguir a ordem das sessões.

**Bloco qualitativo (fora do cálculo).** Escala de 1 a 5; resumo pela mediana e pela concordância (nota 4 ou 5), porque a escala é ordinal.

| Afirmação | Notas | Mediana | Concordam |
|-----------|:-----:|:-------:|:---------:|
| Q01 A aparência do VICKY é agradável | 3, 3, 3 | 3 | 0 de 3 |
| Q02 Menus e submenus fáceis de encontrar e usar | 5, 3, 3 | 3 | 1 de 3 |
| Q03 Entendi o que cada elemento das telas faz | 5, 2, 5 | 5 | 2 de 3 |
| Q04 Telas simples, sem excesso de informação | 3, 2, 1 | 2 | 0 de 3 |
| Q05 Cores uniformes e contraste que facilita a leitura | 5, 3, 4 | 4 | 2 de 3 |
| Q06 Tipo e tamanho das letras facilitam a leitura | 5, 4, 2 | 4 | 2 de 3 |
| Q07 Disposição dos elementos parecida entre telas | 5, 3, 3 | 3 | 1 de 3 |
| Q08 Visual coerente com a marca | 4, 3, 4 | 4 | 2 de 3 |
| Q09 Elementos alinhados e equilibrados | 5, 4, 3 | 4 | 2 de 3 |
| Q10 Fácil de adaptar a outros usos e tamanhos de tela | 5, 2, 1 | 2 | 1 de 3 |

Nas sessões, um participante achou o VICKY "mediano" ("nada leva a querer usar, mas também não é feio"), outro apontou excesso de informação em todas as telas, e o terceiro disse que gostou de tudo e que usaria o produto num TCC.

## 4. Principais achados

São os achados que alimentam a ação de melhoria (#29). Onde há achado da inspeção sobre o mesmo ponto, ele aparece na última coluna: as duas fontes são independentes, porque os participantes não conheciam o resultado da inspeção.

| Ponto | O que os estudantes mostraram | Convergência com a inspeção |
|-------|-------------------------------|-----------------------------|
| Registro da busca (E11) | É o elemento menos entendido: 2 dos 3 participantes não encontraram onde o VICKY registra como a busca foi feita e por que artigos ficaram de fora. Em produção, esse registro não tem nome próprio: está nos painéis "Pipeline (sequência de ações executadas)" e "Critérios PICO + Strings de busca", e o motivo da exclusão fica no detalhe de cada artigo | M2.2.1: F08 só tem títulos de painel, sem texto que diga como consultar ou usar o registro. M2.3.2: 28 linhas do painel Pipeline usam termos de implementação (substring, iter, fallback) |
| Exportação (E12) | P01 não encontrou o botão Exportar e desistiu. P02 baixou o XLSX, mas o arquivo não abriu no computador usado na sessão (macOS). P03 exportou e abriu sem problema | M2.2.1: o menu Exportar descreve bem os três formatos (F09) depois de aberto. A falha de abertura no macOS não foi testada na inspeção e precisa ser reproduzida |
| Critérios PICO (E09) | Dois participantes explicaram o bloco corretamente, como os critérios usados para selecionar os artigos. O terceiro, do internato e com revisão de literatura já feita, o leu como "um resumo dos artigos encontrados". Em produção, o painel mostra o protocolo de triagem e as strings de busca, sem os rótulos P, I, C e O | M2.3.2: duas mensagens mandam editar os critérios PICO, o que a tela do projeto não permite |
| Quality Score (E10) | Entendido pelos três participantes, como a nota que o VICKY dá a cada artigo. A regra especial da Fase 2 (Quality Score não entendido leva a Insatisfatório) não foi acionada | M2.2.1: a lista de artigos explica o número no topo ("Ele não decide se o artigo entra ou sai [...] só serve para ranquear os incluídos"). A explicação parece cumprir o papel |
| Configuração do projeto (E01 a E08) | Os oito elementos da parte A foram usados e explicados corretamente pelos três, inclusive a diferença entre a prévia gratuita e a triagem que gasta crédito (E08). Nenhum participante iniciou a triagem por engano | M2.4.1: a ação paga traz aviso explícito no rótulo do botão ("CONSOME 1 CRÉDITO") |
| Aparência | Só a página inicial e o Novo projeto foram agradáveis para a maioria. As telas de resultado (detalhe do projeto, lista de artigos e ficha do artigo) foram agradáveis para um respondente só. Ninguém concordou que as telas são simples, sem excesso de informação (Q04), e um participante disse que estudantes do começo do curso não entenderiam a interface | M2.3.1: seis dos oito padrões comparáveis variam entre telas; só um respondente achou a disposição parecida entre telas (Q07) |
| Perfil | O único participante do 1º ao 4º semestre perdeu os dois elementos da parte B (E11 e E12); os dois do internato perderam um cada. Os três já tinham feito revisão de literatura, e nenhum tinha usado ferramenta de triagem | Com três participantes, não é possível separar o efeito do perfil do efeito da pessoa |

## 5. Hipóteses

| Hipótese | Previsão | Medido | Resultado |
|----------|----------|--------|-----------|
| H2.5 | A maioria dos participantes considera agradáveis pelo menos 4 das 5 telas | Um respondente achou as 5 telas agradáveis; os outros dois, uma cada | Refutada |
| H2.7 | As quatro páginas de entrada explicam o propósito; só de 60% a 75% dos elementos são entendidos no primeiro uso; o Quality Score está entre os não entendidos | M2.7.1 = 3 de 4 (a tela de login não explica); M2.7.2 = 91,7%; Quality Score entendido pelos três | Refutada nas três partes |

A equipe esperava que o Quality Score e o PICO fossem os pontos fracos. Para estes três estudantes, o ponto fraco foi o registro da busca, que é justamente o que o VICKY promete para "prestar contas ao orientador".

## 6. Respostas às questões

As regras são as da seção 3 de [níveis e julgamento](../fase-2/niveis-e-julgamento.md#3-regras-do-g2-capacidade-de-interacao): a medida de referência dá o nível, e uma medida complementar em Insatisfatório rebaixa a questão em um nível.

| Questão | Como o nível é obtido | Nível | Resposta |
|---------|-----------------------|:-----:|----------|
| Q2.5 | Nível de M2.5.1 | Aceitável (indicativo) | A aparência convida a continuar no painel e no Novo projeto, mas não nas três telas de resultado (detalhe do projeto, lista e ficha do artigo). Prioridade secundária: não entra no julgamento do G2 |
| Q2.6 | Nível de M2.6.1, um nível abaixo se M2.6.2 for Insatisfatório | Sem nível | M2.6.1 e M2.6.2 não foram coletadas até 22/11/2026 |
| Q2.7 | Nível de M2.7.2, um nível abaixo se M2.7.1 for Insatisfatório | Excelente (indicativo) | Sem ajuda, os três estudantes entenderam 11 dos 12 elementos pela maioria, incluindo o Quality Score e a diferença entre prévia e triagem paga. M2.7.1 = Bom (3 de 4) não rebaixa a questão. O ponto fraco é o registro da busca, entendido por 1 dos 3 |

**Efeito no julgamento do G2.** As seis questões principais ficam assim: Q2.1 Bom, Q2.2 Aceitável, Q2.3 Insatisfatório, Q2.4 Insatisfatório, Q2.6 sem nível e Q2.7 Excelente. Pela regra da Fase 2, duas ou mais questões em Insatisfatório levam o G2 a "Não atende". Como Q2.3 e Q2.4 já estão em Insatisfatório pela inspeção, o resultado com usuários não muda o julgamento do G2, qualquer que venha a ser o nível de Q2.6. O julgamento é registrado em [Julgamento e conclusões](julgamento-e-conclusoes.md) (#30).

## 7. Recomendações

| Ponto | Recomendação | Base |
|-------|--------------|------|
| Registro da busca | Dar ao registro um nome que o estudante reconheça (por exemplo, "Como a busca foi feita") e uma frase dizendo que ele serve para mostrar ao orientador as buscas, os critérios e os motivos de exclusão; reescrever as linhas do painel Pipeline em linguagem de estudante | E11 entendido por 1 de 3; M2.2.1 (F08) e M2.3.2 |
| Exportação | Conferir se o XLSX exportado abre no Numbers e no Excel para macOS e, se não abrir, corrigir o arquivo; avaliar repetir o botão Exportar na lista de artigos | E12 de P01 e P02 |
| Critérios PICO | Pôr no topo do painel uma frase que diga que aqueles são os critérios que decidem se cada artigo entra ou sai, e mostrar os rótulos P, I, C e O | E09 de P03 |
| Telas de resultado | Reduzir a densidade de texto no detalhe do projeto e na lista de artigos | M2.5.1 (telas de resultado agradáveis para 1 de 3); Q04 com 0 de 3; comentário de P02 |

## 8. Limitações

- **Amostra de três.** Cada elemento de M2.7.2 e cada tela de M2.5.1 dependem de um único participante para entrar ou sair de A. Os dois valores são indicativos (método, seção 2.8), e a margem está nas seções 2 e 3.
- **M2.5.1 fora da regra da Fase 2.** Três respostas no lugar de cinco, com maioria de 2 de 3 (D14), e respondentes que já tinham usado o produto na sessão. Com a regra de unanimidade, o valor seria 0%. As duas amostras (sessão e formulário) são as mesmas pessoas, e por isso não são independentes.
- **Sem piloto e com cartões ajustados antes da P01.** O tempo e o texto dos cartões não foram calibrados. As sessões duraram de 19 a 43 minutos, abaixo dos 63 previstos, e nenhuma foi interrompida.
- **Marcações por padrão nas P02 e P03.** A ficha do condutor dessas duas sessões citou só as exceções, e os elementos não citados foram marcados como `sem_ajuda` e `correta` por padrão. Das 22 marcações 1 dessas sessões, 19 vêm inteiramente dessa regra (nem o uso nem a explicação foram descritos), 2 têm o uso descrito e a explicação por padrão (E12 de P02 e de P03) e só 1 tem uso e explicação descritos (E11 de P03). A única checagem independente é a segunda classificação das explicações, feita por outro integrante pela gravação, que coincidiu nos 36 itens; o código de uso não teve segunda conferência.
- **Campo Objetivo (E02) pendente.** Uma conferência parcial das gravações, em 22/11, mostrou que P01 e P02 deixaram vazio o campo Objetivo, marcado como uso correto, e que o chat das sessões não trouxe frase de objetivo. A ficha de uso trata "deixa vazio" como uso incorreto, mas o texto lido em voz alta não foi conferido. Se E02 for reclassificado para P01 e P02, ele sai de A, e M2.7.2 vai a 10/12 = 83,3% (Bom). A decisão está registrada como pendente em `M2.7.2/coleta.md`.
- **Leitura de três respostas de P01.** E02, E03 e E10 de P01 foram aceitas como corretas com interpretação, registrada em `M2.7.2/coleta.md`. A leitura não muda o resultado.
- **Ambiente não registrado.** Versão do navegador, sistema e resolução não foram anotados; o dispositivo e o navegador foram identificados depois, pelas gravações. Também não foi anotado o momento de uso de cada elemento (só o trecho de E11 e E12 da P01). A falha do XLSX no macOS vem do relato da sessão e não foi reproduzida.
- **Recortes e capturas.** Os recortes dos 12 elementos foram montados depois das sessões, com capturas da inspeção, e as capturas do formulário não foram guardadas.
- **Conta com créditos.** A parte A usou uma conta da equipe com créditos, e não uma conta nova com 0 crédito. Ninguém iniciou a triagem, mas o participante via um saldo positivo, o que pode ter influenciado a leitura de E08.

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 22/11/2026 | Resultados de M2.7.2 e M2.5.1 com as três sessões e as três respostas ao formulário: execução, desvios, valores, achados com a convergência da inspeção, hipóteses, respostas Q2.5 a Q2.7, recomendações e limitações | Gabriel Fae | - |
| 0.2 | 22/11/2026 | Marcações por padrão das P02 e P03 com números, campo Objetivo (E02) pendente de decisão e dispositivos vistos nas gravações, a partir da revisão do PR #40 | Gabriel Fae | - |
