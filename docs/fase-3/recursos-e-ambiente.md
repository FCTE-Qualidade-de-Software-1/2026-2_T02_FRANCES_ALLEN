# Recursos, ambiente e consistência

Esta página reúne o que a execução da avaliação precisa para acontecer: máquinas, sistemas, programas e versões, contas e créditos no VICKY, acesso ao código, massa de dados e conhecimento exigido de avaliadores e participantes. Cada requisito vem do método que o usa ([G1](metodo-g1.md), [G2 por inspeção](metodo-g2-inspecao.md), [G2 com usuários](metodo-g2-usuarios.md) e [G3](metodo-g3.md)); aqui ele aparece consolidado, para que a equipe prepare tudo de uma vez e veja onde um método depende de outro. A última parte é a [tabela de consistência](#5-tabela-de-consistencia-entre-a-fase-2-e-a-fase-3), que liga cada uma das 26 métricas da Fase 2 ao método, ao recurso, ao ambiente e ao critério de julgamento.

Na ISO/IEC 25040:2024, projetar a avaliação inclui definir os recursos e as condições em que cada medida é obtida, antes da execução. Onde um recurso depende de uma decisão que a equipe ainda não tomou, a página registra o requisito e o responsável, sem antecipar a decisão; a lista dessas decisões está na [seção 6](#6-decisoes-pendentes-antes-da-coleta).

## 1. Hardware e software

### 1.1 Produto avaliado

| Item | Valor | Usado por |
|------|-------|-----------|
| VICKY em produção | <https://vicky.synaptha.com/>, acessado em navegador de computador. A tela não mostra número de versão; a versão é identificada pela data e hora de acesso e pela versão dos Termos de Uso exibida no site | G1, G2 por inspeção, G2 com usuários |
| Código-fonte do VICKY | Fork privado `LucasAvelar2711/Vicky`, commit `c2ae5704b9770fbc33156fb3f457c4e8c63e5007` (`c2ae570`), de 29/09/2026 20:51 (horário de Brasília). Escopo: `src/vicky/` (38 arquivos `.py`) e `tests/` | G2 por inspeção (só A1), G3 |
| Versão móvel | Fora do escopo, como decidido na [Fase 1](../fase-1/escopo.md). Nenhuma coleta usa celular ou tablet | - |

Produção e código não são a mesma coisa: o commit é de setembro e a produção pode ter mudado desde então. Os métodos tratam isso do mesmo jeito: o que o estudante vê é medido em produção, o código serve para o inventário de mensagens e a confirmação das proteções no G2 e para todas as medidas do G3, e qualquer diferença observada é anotada no arquivo de coleta da métrica.

### 1.2 Requisitos por método

**G1 e G2 (coleta em produção).**

| Item | Requisito | Onde a versão é registrada |
|------|-----------|----------------------------|
| Computador | Notebook ou desktop com macOS, Windows ou Linux que rode a versão estável atual do Google Chrome; tela de pelo menos 1366 x 768 pixels | - |
| Navegador | Google Chrome de computador, canal estável, versão anotada no início de cada coleta. O mesmo navegador em todos os métodos, porque a Fase 2 fixa navegador de computador e o axe DevTools é extensão do Chrome | `execucoes.csv` (G1), `coleta.md` de cada pasta do G2 |
| Área visível | 1366 x 768 pixels, zoom de 100%, pelo modo responsivo do DevTools na inspeção e no teste de acessibilidade; janela maximizada nas sessões com participantes | `coleta.md` |
| Perfil do navegador | Perfil limpo, sem favoritos, contas, extensões de bloqueio ou notificações; janela anônima nas páginas públicas | - |
| Extensão axe DevTools (Deque) | Versão gratuita, da Chrome Web Store, configurada com o padrão WCAG 2.2 AA e as boas práticas desligadas (M2.6.2) | `M2.6.2/coleta.md`, versão lida em `chrome://extensions` |
| axe-core | 4.10.2, arquivo `axe.min.js` de <https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.10.2/axe.min.js>, colado no Console do DevTools (M2.6.2) | Fixa |
| Teclado | Mouse e trackpad desconectados ou desativados durante o teste de M2.6.1 | - |
| Leitores de arquivo | Leitor de PDF, editor de planilhas que abra CSV e XLSX (LibreOffice Calc, Excel ou Google Planilhas) e editor de texto para JSON, para conferir a exportação em F09 (M1.2.1) e abrir as planilhas de coleta. Planilhas salvas em UTF-8 | - |
| Python | 3.9 ou superior, só a biblioteca padrão, para `calcular_g1.py` (fichas cegas, amostra de M1.3.2 e cálculo) | Saída do script |
| Bases de consulta | Acesso a PubMed, SciELO (<https://search.scielo.org/>), Google Acadêmico e à página oficial de cada artigo (DOI), para M1.1.2, M1.3.2 e M1.5.1; acesso ao texto completo das revisões de referência na Cochrane Library, para a lista de estudos incluídos de T1, T2 e T4 | `consulta_fontes_Tn.csv` (data da consulta) |

**G2 com usuários (sessões com participantes).**

| Item | Requisito | Onde é registrado |
|------|-----------|-------------------|
| Computador da sessão | Notebook da equipe com tela de pelo menos 1366 x 768 pixels, Chrome atualizado com perfil limpo e zoom de 100%, mouse externo à disposição do participante | `sessoes.csv` (`observacao`, se houver diferença) |
| Gravador de tela | OBS Studio, com a fonte "Captura de tela" e o microfone; nenhuma webcam configurada. Teste de 10 segundos antes de cada sessão | Versão do OBS anotada em `M2.7.2/coleta.md` |
| Microfone | O do notebook ou externo, conferido no teste de gravação | - |
| Hash da gravação | `shasum -a 256` (macOS e Linux); no Windows, `certutil -hashfile <arquivo> SHA256` dá o mesmo valor | `sessoes.csv` (`sha256`) |
| Rede | Roteamento pelo celular do condutor, e não a rede da universidade, por causa do limite de prévias por IP ([seção 2.3](#23-limites-de-uso-do-vicky)) | `M2.7.2/coleta.md` |
| Material impresso | Termo em duas vias (`dados/avaliacao/G2/termo-de-consentimento.docx`), cartões de tarefa A e B, folha com a escala de 1 a 5 | - |
| Material na tela | Capturas fixas das 5 telas (`M2.5.1/telas/`) e recortes dos 12 elementos (`M2.7.2/elementos/`), abertos no visualizador de imagens | Data da captura em `M2.7.2/coleta.md` |
| Guarda das gravações | Pasta restrita no Google Drive da equipe, compartilhada só com os seis integrantes e com a professora, com subpastas separadas para gravações e termos digitalizados | - |
| Local | Sala reservada e silenciosa no campus Darcy Ribeiro, próxima à Faculdade de Medicina, ou outra sala combinada com o participante | `sessoes.csv` (`local`) |

**G3 (análise estática e testes).** Os requisitos e as versões estão na [seção 3.2 do método do G3](metodo-g3.md#32-hardware-e-software); a tabela resume o que a máquina precisa ter. A coleta de 14/11/2026 usou exatamente essas versões.

| Item | Requisito | Versão fixada |
|------|-----------|---------------|
| Computador | macOS ou Linux com bash, 4 GB de RAM livres, 1 GB de disco livre. No Windows, WSL (não testado) | Referência: Apple M4, 16 GB, macOS 26.6.2 (arm64) |
| git | 2.x, com acesso de leitura ao fork privado | - |
| uv | 0.12 ou mais recente | 0.12.5 |
| Python | Série 3.12, a mesma da imagem de produção do VICKY | 3.12.13 |
| radon | Complexidade ciclomática (M3.1.2) e linhas (M3.2.2) | 6.0.1 |
| flake8 | Estilo PEP 8 (M3.2.1), com pycodestyle, pyflakes e mccabe | 7.5.0 (pycodestyle 2.15.0, pyflakes 4.1.0, mccabe 0.7.0) |
| pylint | Duplicação (M3.2.2), só `duplicate-code` | 4.1.4 (astroid 4.3.4) |
| pytest e pytest-cov | Cobertura (M3.3.1) | pytest 9.2.0, pytest-cov 7.1.0 (coverage 7.17.3) |
| Dependências do VICKY | As 58 do `requirements.lock` do commit avaliado, instaladas com hash | As do lockfile |
| Restrições | Sem Postgres escutando em `localhost:5433` e sem chave `sk_test_` da Stripe no Keychain; `DATABASE_URL` vazia | - |
| Rede | Só para clonar e instalar; a suíte roda offline | - |

As versões com hash estão em `dados/avaliacao/G3/ferramentas.lock` e `testes.lock`, e a versão realmente usada em cada coleta é gravada em `ambiente.txt` de cada pasta.

### 1.3 Repositório e registro

Todos os métodos registram os dados brutos em `dados/avaliacao/` do [repositório do trabalho](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN), com permissão de escrita para os seis integrantes. As fichas do G2 são preenchidas direto no GitHub, pelo navegador, e o histórico de commits prova que cada avaliador enviou a sua ficha antes de ver a do outro, que é a condição de independência dos quatro métodos. Data e hora são registradas no horário de Brasília.

## 2. Contas, créditos e acesso

### 2.1 Contas no VICKY

| Conta | Para que serve | Método | Créditos que consome | Cuidado |
|-------|----------------|--------|:--------------------:|---------|
| Conta de cortesia da equipe | As oito triagens do G1 e o projeto rascunho P0; telas internas e `/dashboard` na inspeção; parte B das sessões; F06 a F09 no teste com teclado; telas S4 a S8 do contraste | G1, G2 por inspeção, G2 com usuários | 8 (só as triagens do G1) | Nome fictício; senha fora do repositório; nenhum participante exclui projeto; favoritos desmarcados ao fim de cada sessão |
| Conta de teste do G1 | Cadastro e recuperação de senha em M1.2.1 (F01) | G1 | 0 | E-mail criado só para a coleta |
| Conta descartável da inspeção | Roteiro de erros de cadastro e login, inclusive "e-mail já cadastrado" (E05) e o limite de prévias (E08) | G2 por inspeção | 0 | Esgota de propósito a cota de prévias dela; não é a conta de cortesia |
| Contas novas dos participantes | Parte A das sessões, criadas pelo próprio participante como "Participante P0x" | G2 com usuários | 0 (conta nova começa sem crédito, a conferir em produção antes do piloto) | E-mail de teste da equipe com sufixo do participante; nenhum dado pessoal entra no VICKY |
| Contas novas de T1 e T2 | F01 a F04 no teste com teclado | G2 com usuários | 0 | Criadas pelo próprio avaliador |

**E-mail de teste.** As contas de teste usam uma caixa de e-mail criada pela equipe só para a avaliação, que aceite endereço com sufixo (`caixa+p01@...`), como o Gmail aceita. A mesma caixa serve para confirmar e-mail, se a produção exigir isso para gerar a prévia, e para receber a recuperação de senha em F01. A senha da caixa e das contas fica fora do repositório.

### 2.2 Créditos

| Item | Valor | Fonte |
|------|-------|-------|
| Triagens completas necessárias | 8 (T1, T2, T3, T4, E1, E2, T1-B e T3-B), 1 crédito cada | [Método do G1, seção 3.5](metodo-g1.md#35-contas-creditos-e-divisao-das-triagens) |
| Triagens extras de outros métodos | Nenhuma. A inspeção observa "iniciar triagem" (M2.4.1) e o teste com teclado observa F05 (M2.6.1) em triagens já previstas no G1; as sessões usam o projeto já triado de T1 | Métodos do G2 |
| Créditos de cortesia disponíveis | A confirmar com a equipe do VICKY antes da etapa 3 do G1 | [Seção 6](#6-decisoes-pendentes-antes-da-coleta) |
| Custo de referência | R$ 24,90 por triagem completa, valor usado na Fase 2 (M2.4.1). Se faltarem créditos de cortesia, a compra de créditos é decisão da equipe; o método não pressupõe compra | [Níveis de pontuação](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica) |
| Com menos de 8 créditos | Ordem de prioridade do G1: T1, T2, T3, T4, T1-B, E1, T3-B, E2. Execução não feita torna a métrica "não coletada" naquele tema, sem estimativa | Método do G1, seção 3.5 |

A estimativa de cerca de oito triagens da Fase 2 se confirmou no método: cada lista de T1 a T4 alimenta até cinco métricas, e só M1.5.1 e M1.5.2 exigem execuções próprias.

### 2.3 Limites de uso do VICKY

No código consultado (`c2ae570`), a prévia dos critérios tem limite de **20 por conta** e **60 por origem (IP)** em 24 horas, e o condutor do G2 com usuários confere o limite vigente em produção antes do piloto. A tabela estima o consumo de cada método para mostrar que o ambiente suporta a massa de dados prevista.

| Método | Prévias previstas | Conta | Regra que evita estourar o limite |
|--------|-------------------|-------|-----------------------------------|
| G1 | Uma por triagem (8) e as de F03 no projeto P0; no máximo cerca de 6 no dia 1 | Cortesia | Se o limite da conta for atingido, as triagens restantes passam para o dia seguinte (método do G1, seção 4.1) |
| G2 por inspeção | Cerca de 20 em E08, que esgota a cota de propósito, e as de F03 em M2.2.1 | Descartável | E08 sempre por último e nunca no mesmo dia nem na mesma rede de uma sessão com participante |
| G2 com usuários | De 1 a 3 por sessão e 1 ou 2 por avaliador de teclado | Contas novas | No máximo três sessões por dia, em rede do celular do condutor |
| G3 | Nenhuma | - | Não usa a produção |

Os Termos de Uso do VICKY proíbem *scraping* abusivo e sobrecarga. Por isso nenhuma coleta em produção é automatizada: o axe é rodado à mão, uma vez por tela e por avaliador.

### 2.4 Acesso ao código e aos dados restritos

| Recurso | Quem precisa | Como obter |
|---------|--------------|------------|
| Fork privado `LucasAvelar2711/Vicky` | A1 do G2 por inspeção (inventário de mensagens e proteções); A1 e A2 do G3 | Acesso de leitura concedido por Lucas Avelar, dono do fork. O A2 da inspeção **não** recebe o código antes de enviar `A2.md` |
| Repositório do trabalho | Os seis integrantes | Já concedido (organização da disciplina) |
| Pasta restrita no Google Drive | Os seis integrantes e a professora | Criada pelo condutor do G2 com usuários antes do piloto |
| Relação entre papéis e pessoas (A1, A2, A3, C, O, T1, T2) | Equipe | Fora do repositório nos métodos G1, G2 por inspeção e G3; em `coleta.md`, sem dado de participante, no G2 com usuários |
| Relação entre participante e código (P01 a P05) | Aluno responsável pelas sessões | Existe só no termo assinado |

## 3. Massa de dados

A avaliação usa dados de exemplo definidos antes da coleta. Isso tem dois motivos: tornar a medição repetível, porque quem refaz a coleta digita a mesma entrada e compara com o mesmo gabarito, e agilizar a execução, porque uma mesma triagem alimenta várias métricas e o número de créditos fica no que a Fase 2 estimou.

| Método | Massa de dados | Onde está definida | Por que esta massa |
|--------|----------------|--------------------|--------------------|
| G1 | Quatro temas de teste, um por perfil exigido pela Fase 2: T1 colchicina na prevenção secundária cardiovascular; T2 ioga para fadiga em pessoas com câncer; T3 prevalência de diabetes gestacional no Brasil; T4 tratamento farmacológico da ataxia de Friedreich. Texto do tema e do objetivo digitado literalmente, configuração fixa das triagens e uma reserva por perfil | [Método do G1, seções 3.2 e 3.4](metodo-g1.md#32-temas-de-teste-e-pico) | Cada perfil expõe um fator de variação do abstraction sheet do G1: caso favorável no PubMed (T1), vocabulário variado (T2), peso do SciELO e PICO sem intervenção (T3), literatura escassa (T4) |
| G1 | Revisões de referência: Ebrahimi et al., Cochrane 2025 (T1, 12 estudos); Messer et al., Cochrane 2025 (T2, 21 ECR); Mocellin et al., Cad. Saúde Pública 2024 (T3, 32 estudos); Lyons et al., Cochrane 2026 (T4, 8 ECR). A lista de estudos incluídos de cada uma é o gabarito de M1.1.1 e M1.1.2, e o PICO de cada uma é o critério de relevância de M1.3.1 | [Método do G1, seção 3.3](metodo-g1.md#33-revisoes-de-referencia-e-regra-do-gabarito) | Gabarito externo, feito por especialistas com protocolo publicado, em vez de um gabarito montado pela equipe. A regra do gabarito fixa o que entra em Ref na data da coleta |
| G1 | Execuções E1 (texto de T1, só PubMed, 5 anos, ensaios randomizados) e E2 (texto de T3, só SciELO, 5 anos, observacionais primários); T1-B e T3-B repetidos de 24 a 72 horas depois | Método do G1, seções 3.5 e 4.7 | Reaproveitam textos já fixados; E1 e E2 restringem as três dimensões de filtro da ficha de M1.5.1 com fontes diferentes |
| G2 por inspeção | Listas fechadas: 10 cenários (M2.1.1), 9 funções (M2.2.1), 10 padrões (M2.3.1), 6 ações (M2.4.1), 4 páginas de entrada (M2.7.1); roteiros de entradas inválidas com valores fixos (E01 a E08 e I01 a I07, por exemplo `aluno@` e `abc12`); projeto rascunho criado só para o teste; projeto triado de T1 do G1 | [Método do G2 por inspeção, seção 3](metodo-g2-inspecao.md#3-passo-a-passo) | Os dois avaliadores digitam os mesmos valores e veem as mesmas mensagens. O valor `aluno@` foi escolhido porque o Chrome aceita `aluno@unb` como e-mail válido. O projeto rascunho isola a exclusão de projeto das listas medidas no G1 |
| G2 com usuários | Tema T1 do G1, escrito em uma frase no cartão A, igual para os cinco; requisitos do cartão (5 anos, no máximo 15 artigos, PubMed e SciELO, só texto gratuito); projeto já triado de T1 na conta de cortesia para a parte B; capturas fixas das 5 telas e recortes dos 12 elementos | [Método do G2 com usuários, seção 3.3](metodo-g2-usuarios.md#33-tema-dado-ao-participante) e [Instrumentos](instrumentos-g2-usuarios.md) | Uma história só (preparar a busca e usar o resultado) sem triagem extra. Os requisitos diferem dos valores padrão da tela para obrigar o participante a mexer em cada controle. As capturas fixas fazem os cinco julgarem o mesmo objeto |
| G2 com usuários | As 9 funções no teste com teclado e as 8 telas no contraste, com o estado de cada tela fixado (S1 a S8) | Método do G2 com usuários, seções 4.2 e 4.3 | As mesmas funções e telas que as fichas da Fase 2 listam |
| G3 | Código do commit `c2ae570`, exportado com `git archive`: 38 arquivos `.py` em `src/vicky/` e a suíte `tests/` (1.034 testes). A suíte usa banco SQLite descartável e credenciais falsas | [Método do G3, seções 3.4 e 3.6](metodo-g3.md#34-versao-do-codigo) | É o commit lido nas hipóteses do G3 e na inspeção do G2, o que mantém os objetivos comparáveis; nenhum dado externo ou de produção entra na medição |

**Dependência entre métodos.** O projeto triado de T1 é a peça de massa de dados compartilhada: alimenta M1.1.1 a M1.4.1 e F05 a F09 do G1, a etapa 6 da inspeção do G2, a parte B das sessões, F06 a F09 do teste com teclado e as telas S6 a S8 do contraste. Por isso a triagem T1 é a primeira coleta do G1, e o Top 30 e o log desse projeto são exportados para `dados/avaliacao/G1/` antes da primeira sessão com participante.

## 4. Conhecimento exigido

A rubrica pede o nível de conhecimento em informática e no domínio da aplicação. O domínio do VICKY é a revisão de literatura em Medicina; a equipe é de Engenharia de Software. Cada método foi escrito para que o julgamento dependa de critério escrito, e não de formação clínica.

### 4.1 Avaliadores

| Método e papel | Informática | Domínio da aplicação | Preparação antes da coleta |
|----------------|-------------|----------------------|----------------------------|
| G1, condutor (C) | Usuário avançado de navegador; consulta a PubMed, SciELO e Google Acadêmico; rodar um script Python pelo terminal | Familiaridade com a interface do VICKY; não precisa de formação clínica | Ler o método do G1 inteiro |
| G1, A1 e A2 | Usuário de planilha e de GitHub pelo navegador | Ler resumo científico em inglês e português; saber o que é PICO; distinguir os desenhos de estudo dos critérios; achar tamanho da amostra e comparador num resumo | Ler as seções 4.4 e 4.6 do método (cerca de 20 minutos) e fazer o piloto de calibração |
| G1, A3 | Usuário de planilha | O mesmo de A1 e A2 | Ler a seção 4.4 |
| G2 por inspeção, A1 | Ler templates HTML e Python para montar o inventário de mensagens e achar a proteção no código; usar o DevTools | Saber o que o estudante faz no VICKY (funções F01 a F09) | Ler o método da inspeção |
| G2 por inspeção, A2 | Usuário de navegador e do modo responsivo do DevTools; **não** pode ter lido o código | O mesmo de A1 | Ler o método da inspeção |
| G2 com usuários, condutor e observador | Operar o OBS Studio, o Chrome e o visualizador de imagens; calcular hash | Conhecer o gabarito dos 12 elementos; não precisa de formação clínica | Ler o método e os instrumentos e fazer a sessão piloto juntos |
| G2 com usuários, T1 e T2 (teclado) | Navegar só por teclado no Chrome; medir elemento no DevTools | Critérios 2.1.1, 2.4.7 e 2.5.8 da WCAG 2.2 | Ler a seção 4.2 do método |
| G2 com usuários, A1 e A2 (contraste) | Rodar o axe, colar script no Console, usar o seletor de cor do DevTools | Critério 1.4.3 da WCAG 2.2 | Ler a seção 4.3 do método |
| G3, A1 e A2 | Terminal com bash, git básico, leitura de Python (função, `try`/`except`, `logging`, `print`) | Noção de complexidade ciclomática e de cobertura de testes no nível das fichas; não precisa conhecer o domínio do VICKY | Ler o método do G3 |

Os papéis de cada método são independentes, mas há restrições cruzadas: no G1, quem conduz as triagens não julga; na inspeção do G2, quem leu o código na preparação das hipóteses não pode ser A2; em todos os métodos, A3 não pode ser A1 nem A2.

### 4.2 Participantes das sessões

| Item | Exigência |
|------|-----------|
| Perfil | Estudante de Medicina com matrícula ativa, 18 anos ou mais, que nunca usou nem viu o VICKY |
| Informática | Uso comum de computador e navegador: criar conta em site, preencher formulário, baixar arquivo. Nenhum conhecimento técnico além disso |
| Domínio | Nenhum conhecimento de metodologia científica é exigido, porque a promessa do VICKY, registrada na Fase 1, é que o estudante não precisa saber montar um PICO. Faixa do curso, experiência com revisão e com ferramenta de triagem são registradas em `perfil.csv` para interpretar o resultado, sem entrar no cálculo |
| Quantidade | 5 participantes válidos e 2 reservas convidados desde o início |

## 5. Tabela de consistência entre a Fase 2 e a Fase 3

A tabela liga cada métrica da [especificação da Fase 2](../fase-2/especificacao-das-metricas.md) ao método que a coleta, aos recursos e ao ambiente desta página e ao nível de pontuação e à regra de julgamento da [Fase 2](../fase-2/niveis-e-julgamento.md). A coluna "Coerência" diz por que o método mede exatamente o que a ficha define. Nenhuma fórmula, limiar ou regra de agregação muda na Fase 3: os métodos fixam só o que a Fase 2 deixou para esta fase. Nas faixas, "Bom" é o limite inferior do nível Bom; em M3.1.1 e M3.2.2, em que menor é melhor, é o limite superior.

### 5.1 G1 (adequação funcional)

Recursos comuns: Chrome de computador, conta de cortesia, triagens da [seção 2.2](#22-creditos), Python 3.9 para `calcular_g1.py`, planilhas em `dados/avaliacao/G1/`. Julgamento: média dos pontos por questão e do objetivo, com M1.1.1 e M1.3.1 críticas ([regras do G1](../fase-2/niveis-e-julgamento.md#2-regras-do-g1-adequacao-funcional)).

| Métrica | Questão | Método | Recursos e ambiente | Nível e julgamento | Coerência |
|---------|:-------:|--------|---------------------|--------------------|-----------|
| M1.1.1 | Q1.1 | [G1, 4.9](metodo-g1.md#49-m111-e-m112-cruzamento-e-consulta-as-fontes) | Triagens T1 a T4; listas de incluídos das quatro revisões (Cochrane Library e PMC) | [Bom a partir de 0,60](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica); crítica em Q1.1 | A ficha define R como estudos da revisão presentes no Top 30 sobre min(Ref, 30); o método cruza exatamente esses dois conjuntos por DOI, PMID e título, e só tira de Ref o que não estava publicado na data da coleta, mantendo o que as fontes não indexam, como a ficha manda |
| M1.1.2 | Q1.1 | [G1, 4.9](metodo-g1.md#49-m111-e-m112-cruzamento-e-consulta-as-fontes) | As mesmas listas; consulta manual a PubMed, SciELO e Google Acadêmico | [Bom a partir de 0,70](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica); média em Q1.1 | A ficha restringe Ref aos estudos que as três fontes indexam; o método consulta cada estudo nas três fontes, com regra escrita de "encontrado", o que separa falha de triagem de limite da base |
| M1.2.1 | Q1.2 | [G1, 4.3](metodo-g1.md#43-m121-funcoes-declaradas-operantes) | Conta de teste do G1, projeto rascunho P0, projeto T1, execução E1; leitores de PDF, XLSX, CSV e JSON | [Bom a partir de 85%](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica); única em Q1.2 | A ficha pede um caso de teste por função anunciada e a classificação em operante, parcial ou ausente; o método tira os subpassos da descrição da Fase 1 e aplica uma regra mecânica, conferida por um segundo avaliador |
| M1.3.1 | Q1.3 | [G1, 4.4](metodo-g1.md#44-m131-precisao30) | Ficha cega gerada pelo script; A1 e A2 sem acesso à VICKY; A3 para discordâncias | [Bom a partir de 70%](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica), válida com kappa de 0,61 ou mais; crítica em Q1.3 | A ficha exige título e resumo sem posição nem Quality Score e julgamento de dois avaliadores contra o PICO; o método entrega a ficha cega, fixa o critério por componente do PICO e verifica o kappa antes de aceitar o valor |
| M1.3.2 | Q1.3 | [G1, 4.5](metodo-g1.md#45-m132-metadados-e-links-corretos) | Amostra de 10 itens por tema; página oficial de cada artigo (DOI, PubMed ou SciELO) | [Bom a partir de 90%](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica); média em Q1.3 | A ficha compara cinco campos com a página oficial e só aceita o item com os cinco corretos; o método fixa a amostra sistemática que a ficha deixou em aberto e a regra de igualdade de cada campo |
| M1.4.1 | Q1.4 | [G1, 4.6](metodo-g1.md#46-m141-quality-score-e-rubrica) | Top 30 de T1 e T2 com o Quality Score exibido; ficha cega; rubrica de A1 e A2 | [Bom a partir de 0,50](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica); única em Q1.4 | A ficha pede ρ de Spearman entre o Quality Score e a média de uma rubrica dada sem ver o escore; o método usa a mesma ficha cega, fixa os pesos dos quatro componentes da ficha e calcula ρ por tema e a média |
| M1.5.1 | Q1.5 | [G1, 4.7](metodo-g1.md#47-m151-conformidade-com-filtros) | Execuções E1 e E2; página oficial, *Publication Type* do PubMed e busca no SciELO | [Bom a partir de 93%](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica); média em Q1.5 | A ficha pede duas execuções que restrinjam janela, tipo de estudo e fonte e a conferência item a item; E1 e E2 restringem as três dimensões, e cada uma tem evidência registrada por item |
| M1.5.2 | Q1.5 | [G1, 4.8](metodo-g1.md#48-m152-estabilidade-entre-execucoes) | Execuções T1-B e T3-B, de 24 a 72 horas depois de T1 e T3, com a mesma entrada | [Bom a partir de 0,70](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica); média em Q1.5 | A ficha pede o mesmo tema repetido com 24 horas ou mais e o índice de Jaccard entre os dois Top 30; o método respeita o mínimo, limita o máximo a 72 horas para reduzir a chance de mudança de versão e usa a mesma regra de identidade de M1.1.1 |

### 5.2 G2 (capacidade de interação)

Recursos comuns: Chrome de computador em 1366 x 768 pixels e zoom de 100%, contas da [seção 2.1](#21-contas-no-vicky), fichas em `dados/avaliacao/G2/`, dois avaliadores independentes com pelo menos um sem ter lido o código. Julgamento: medida de referência por questão, medidas que só rebaixam e regra das seis questões principais, com Q2.5 fora da contagem ([regras do G2](../fase-2/niveis-e-julgamento.md#3-regras-do-g2-capacidade-de-interacao)).

| Métrica | Questão | Método | Recursos e ambiente | Nível e julgamento | Coerência |
|---------|:-------:|--------|---------------------|--------------------|-----------|
| M2.1.1 | Q2.1 | [Inspeção, M2.1.1](metodo-g2-inspecao.md#m211-completude-da-descricao) | Janela anônima; páginas `/`, `/termos` e `/privacidade` | [Bom a partir de 90%](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica); referência de Q2.1 | A ficha mede os cenários descritos nas páginas que o estudante vê antes de criar conta; o método procura os 10 cenários exatamente nessas três páginas, sem login, e só aceita trecho que diga o que o cenário entrega |
| M2.2.1 | Q2.2 | [Inspeção, M2.2.1](metodo-g2-inspecao.md#m221-completude-da-orientacao-ao-usuario) | Conta de cortesia; projeto triado de T1 para F05 a F09 | [Bom a partir de 88%](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica); referência de Q2.2 | A ficha conta só a orientação dentro do produto que diz como executar a função; o método procura essa orientação nas telas de cada uma das 9 funções e exclui nome de campo e material externo |
| M2.2.2 | Q2.2 | [Inspeção, M2.2.2 e M2.3.2](metodo-g2-inspecao.md#m222-e-m232-inventarios-de-mensagens) | Código no commit `c2ae570` (só A1); conta descartável; roteiro E01 a E08 | [Bom a partir de 75%](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica); pode rebaixar Q2.2 | A ficha pede o inventário do código, o disparo em produção com o roteiro de entradas inválidas e a classificação por causa e solução; o método segue os três passos, com os oito disparos que a ficha lista e valores fixos |
| M2.3.1 | Q2.3 | [Inspeção, M2.3.1](metodo-g2-inspecao.md#m231-consistencia-operacional) | Conta de cortesia; telas com e sem resultado de triagem | [Bom a partir de 0,80](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica); menor nível de Q2.3 | A ficha define padrão inconsistente como resolvido de forma diferente em duas ou mais telas; o método compara atributos fixos de 10 padrões em todas as telas onde aparecem e tira de B o padrão visto numa tela só |
| M2.3.2 | Q2.3 | [Inspeção, M2.2.2 e M2.3.2](metodo-g2-inspecao.md#m222-e-m232-inventarios-de-mensagens) | Inventário ampliado (erro, sucesso, aviso, andamento, saldo) | [Bom a partir de 85%](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica); menor nível de Q2.3 | A ficha amplia o inventário de M2.2.2 e classifica a clareza pela linguagem do estudante; o método usa esse inventário e o mesmo critério, contando texto técnico do servidor como não claro |
| M2.4.1 | Q2.4 | [Inspeção, M2.4.1](metodo-g2-inspecao.md#m241-prevencao-de-erro-de-operacao) | Código (A1); projeto rascunho; triagem do G1 observada, sem crédito extra | [Bom a partir de 85%](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica), Insatisfatório se ação paga estiver sem proteção; referência de Q2.4 e regra de "Não atende" | A ficha pede verificação pela tela, confirmação no código e "iniciar triagem" observada numa triagem do G1; o método faz isso e destaca a ação paga sem proteção, que a Fase 2 leva a Insatisfatório |
| M2.4.2 | Q2.4 | [Inspeção, M2.4.2](metodo-g2-inspecao.md#m242-correcao-de-erro-de-entrada) | Formulários de cadastro, login, recuperação de senha e novo projeto; roteiro I01 a I07 | [Bom a partir de 60%](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica); pode rebaixar Q2.4 | A ficha pede o roteiro fixo de entradas inválidas e conta a correção silenciosa como detectada e não sugerida; o método aplica as mesmas entradas e a mesma regra de classificação |
| M2.5.1 | Q2.5 | [Usuários, 4.1](metodo-g2-usuarios.md#41-sessao-com-o-participante-m272-e-m251) | 5 participantes; notebook com OBS; capturas fixas das 5 telas; termo | [Bom a partir de 60%](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica); Q2.5 fora da contagem do G2 | A ficha pede representantes do público-alvo, as 5 telas listadas, escala de 1 a 5 com 4 e 5 como agradável e maioria de 3 de 5; o método aplica isso no fim da sessão, sobre capturas iguais para todos, e não calcula com menos de cinco sessões válidas |
| M2.6.1 | Q2.6 | [Usuários, 4.2](metodo-g2-usuarios.md#42-teste-so-com-teclado-m261) | Mouse e trackpad desativados; DevTools para medir alvos; contas novas e de cortesia | [Bom a partir de 88%](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica), Insatisfatório se F01 falhar; referência de Q2.6 | A ficha mede as funções usáveis sem mouse, registrando foco, acionamento e alvos menores que o mínimo; o método transforma esses três registros nas três condições de sucesso, verificadas em cada passo das 9 funções |
| M2.6.2 | Q2.6 | [Usuários, 4.3](metodo-g2-usuarios.md#43-axe-devtools-m262) | Extensão axe DevTools e axe-core 4.10.2; seletor de cor do DevTools; 8 telas em estado fixo | [Bom a partir de 95%](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica); pode rebaixar Q2.6 | A ficha pede o axe nas 8 telas, versão registrada e conferência manual dos incertos; o método usa a extensão para as violações, o axe-core para obter o denominador que a extensão não mostra e o limiar de 4,5:1 (ou 3:1) da WCAG 2.2 |
| M2.7.1 | Q2.7 | [Inspeção, M2.7.1](metodo-g2-inspecao.md#m271-autodescricao-dos-pontos-de-entrada) | Área visível fixa de 1366 x 768 pixels; `/`, `/signup`, `/login` e `/dashboard` | [Bom com 3 de 4](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica); pode rebaixar Q2.7 | A ficha mede o que a primeira tela visível diz, sem rolar, nas 4 páginas de entrada; a área visível fixa torna "sem rolar" igual para os dois avaliadores, e o critério exige dizer o que é tratado e o que é feito |
| M2.7.2 | Q2.7 | [Usuários, 4.1](metodo-g2-usuarios.md#41-sessao-com-o-participante-m272-e-m251) | 5 participantes; cartões A e B; ficha de uso; questionário com gabarito; gravação | [Bom a partir de 75%](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica), Insatisfatório se o Quality Score não for entendido; referência de Q2.7 | A ficha considera entendido o elemento usado sem ajuda e explicado corretamente; o método mede as duas metades separadamente (ficha de uso e questionário contra gabarito escrito antes) e combina as duas para os 12 elementos da lista da ficha |

### 5.3 G3 (manutenibilidade)

Recursos comuns: máquina macOS ou Linux, Python 3.12, ferramentas com versão fixada por lockfile, fork no commit `c2ae570`, script `coletar.sh`. Julgamento: média dos pontos por questão e do objetivo, M3.1.2 bloqueadora em Q3.1 e Q3.3 limitando o G3 ([regras do G3](../fase-2/niveis-e-julgamento.md#4-regras-do-g3-manutenibilidade)).

| Métrica | Questão | Método | Recursos e ambiente | Nível e julgamento | Coerência |
|---------|:-------:|--------|---------------------|--------------------|-----------|
| M3.1.1 | Q3.1 | [G3, 4.2](metodo-g3.md#42-m311-acoplamento-de-componentes) | `extrair.py` (AST da biblioteca padrão) sobre `src/vicky/` | [Bom abaixo de 10](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica) (de 5 a menos de 10); média em Q3.1 | A ficha divide os imports internos pelo número de arquivos de `src/vicky/`; o método lê os imports pela AST, o que pega imports relativos e de várias linhas, e fixa por escrito o que conta como uma dependência |
| M3.1.2 | Q3.1 | [G3, 4.3](metodo-g3.md#43-m312-adequacao-da-complexidade-ciclomatica) | radon 6.0.1 sobre `src/vicky/pipeline.py` | [Bom a partir de 85%](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica); média e bloqueadora em Q3.1 | A ficha manda rodar `radon cc` em `pipeline.py` e contar as funções com complexidade acima de 10; o método roda o mesmo comando e define quais linhas da saída são funções |
| M3.2.1 | Q3.2 | [G3, 4.4](metodo-g3.md#44-m321-conformidade-de-estilo-pep-8) | flake8 7.5.0 com `--isolated` | [Bom a partir de 90%](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica); média em Q3.2 | A ficha pede o flake8 com configuração padrão e a contagem de arquivos com violação; `--isolated` garante a configuração padrão em qualquer máquina, e a lista por violação dá os arquivos distintos |
| M3.2.2 | Q3.2 | [G3, 4.5](metodo-g3.md#45-m322-densidade-de-codigo-duplicado) | pylint 4.1.4 (`duplicate-code`) e radon raw | [Bom até 5%](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica) (de 2% a 5%); média em Q3.2 | A ficha divide as linhas acusadas pelo pylint pelo total do `radon raw`; o método usa os dois comandos e fixa a soma das linhas (união das ocorrências) e o total (linhas físicas), que a ficha não detalhava |
| M3.2.3 | Q3.2 | [G3, 4.6](metodo-g3.md#46-m323-completude-de-logs-do-sistema) | `extrair.py` sobre `pipeline.py`; inspeção de A1 e A2 | [Bom a partir de 75%](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica); média em Q3.2 | A ficha conta as funções críticas do orquestrador que usam a biblioteca `logging`; o método transforma "crítica" em três critérios verificáveis (integração externa, banco, orquestração) e conta só `logging`, como a ficha exige |
| M3.3.1 | Q3.3 | [G3, 4.7](metodo-g3.md#47-m331-completude-de-testes-automatizados) | pytest 9.2.0 e pytest-cov 7.1.0; suíte offline, sem Postgres e sem Stripe | [Bom a partir de 70%](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica); única em Q3.3 e limita o G3 | A ficha pede `pytest --cov=src/vicky/ tests/` e a cobertura de linhas; o método roda o mesmo comando, num ambiente sem recursos externos para que qualquer integrante obtenha a mesma suíte, e lê o valor sem arredondamento |

### 5.4 Verificação da cobertura

| Método | Métricas | Quantidade |
|--------|----------|:----------:|
| [G1](metodo-g1.md) | M1.1.1, M1.1.2, M1.2.1, M1.3.1, M1.3.2, M1.4.1, M1.5.1, M1.5.2 | 8 |
| [G2 por inspeção](metodo-g2-inspecao.md) | M2.1.1, M2.2.1, M2.2.2, M2.3.1, M2.3.2, M2.4.1, M2.4.2, M2.7.1 | 8 |
| [G2 com usuários](metodo-g2-usuarios.md) | M2.5.1, M2.6.1, M2.6.2, M2.7.2 | 4 |
| [G3](metodo-g3.md) | M3.1.1, M3.1.2, M3.2.1, M3.2.2, M3.2.3, M3.3.1 | 6 |
| **Total** | | **26** |

O resumo da [especificação das métricas](../fase-2/especificacao-das-metricas.md#resumo) lista 26 métricas, e as 26 aparecem nas tabelas acima, cada uma em um único método. **Nenhuma métrica fica sem método.** Cada um dos quatro métodos cobre só métricas da Fase 2, sem medida própria fora da especificação. **Nenhum método fica sem métrica.** As 15 questões (Q1.1 a Q1.5, Q2.1 a Q2.7, Q3.1 a Q3.3) têm pelo menos uma métrica com método, e as métricas com regra especial na Fase 2 (críticas M1.1.1 e M1.3.1, bloqueadoras M3.1.2 e M3.3.1, e as regras de M2.4.1, M2.6.1 e M2.7.2) têm essa regra aplicada no cálculo do método correspondente.

## 6. Decisões pendentes antes da coleta

Itens que dependem de decisão da equipe. Cada um tem o requisito que precisa ser cumprido e quem responde por ele; a data limite segue o [cronograma](cronograma.md). Pela [D12](../gestao/decisoes.md), parte que não for entregue no prazo é assumida por outro integrante e comunicada à professora.

| Item | Requisito | Responsável | Até |
|------|-----------|-------------|-----|
| Créditos de cortesia | Confirmar com a equipe do VICKY quantos créditos a conta de cortesia tem; são necessários 8. Com menos, vale a ordem de prioridade do G1 e a decisão de comprar ou não fica com a equipe | Condutor do G1 (#26) | 16/11, antes da etapa 3 do G1 |
| Avaliadores do G1 | Definir C, A1, A2 e A3, com C fora do julgamento | Equipe, combinado pelo WhatsApp (D12) | 15/11 |
| Avaliadores do G2 por inspeção | Definir A1, A2 e A3, com A2 sem ter lido o código | Responsável pela #27 | Já em andamento; registrar em `coleta.md` |
| Avaliadores do G2 com usuários | Definir C, O e A3 das sessões, T1 e T2 do teclado e A1 e A2 do contraste | Responsável pela #28 | 15/11 |
| Repetição do G3 | Definir o A2 que repete a coleta em outra máquina e o A3 da inspeção de M3.2.3 | Responsável pela #29 | 16/11 |
| Recrutamento | 5 estudantes de Medicina e 2 reservas que cumpram os critérios de inclusão | Responsável pela #28 | 16/11 |
| Local das sessões | Sala reservada e silenciosa, registrada por sessão | Responsável pela #28 | Antes do piloto |
| Notebook e gravador | Notebook da equipe com Chrome atualizado e OBS Studio testado | Responsável pela #28 | Antes do piloto |
| Caixa de e-mail de teste | Caixa que aceite sufixo `+`, usada pelas contas de teste | Responsável pela #28, com o condutor do G1 | Antes do piloto e da etapa 3 do G1 |
| Pasta restrita no Drive | Compartilhada só com os seis integrantes e a professora, com subpastas para gravações e termos | Responsável pela #28 | Antes do piloto |
| E-mail de contato no termo | Preencher o e-mail do aluno responsável antes de imprimir | Lucas Avelar | Antes do piloto |
| Acesso ao fork | Leitura para o A1 da inspeção e para A1 e A2 do G3 | Lucas Avelar | Assim que os avaliadores forem definidos |
| Listas de incluídos | Baixar da Cochrane Library a lista nominal de estudos incluídos de T1, T2 e T4; se não for possível, trocar pelo tema reserva | Condutor do G1 | Etapa 1 do G1, antes da primeira triagem |

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 04/11/2026 | Criação da página | Lucas Avelar | - |
| 0.2 | 09/11/2026 | Esqueleto com os pontos em aberto e a tabela de consistência das 26 métricas, com recurso e ambiente a definir | Gabriel Fae | - |
| 0.3 | 14/11/2026 | Página completa, assumida pela D12: hardware e software por método com versões, contas, créditos e limites de uso, acesso ao código, massa de dados justificada, conhecimento exigido, tabela de consistência das 26 métricas com a coerência de cada uma, verificação da cobertura e decisões pendentes com responsável | Lucas Avelar | - |
