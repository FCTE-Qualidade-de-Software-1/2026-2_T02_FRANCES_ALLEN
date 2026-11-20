# Artigo v2: Resultados, Conclusão e pendências da E1 (rascunho para o Overleaf)

Rascunho da #31, escrito em 20/11/2026 a partir do que está no repositório. Não é publicado (fora de `docs/`). Cada número cita o arquivo de onde saiu. O que ainda não existe está marcado com `[PENDENTE: ...]` e não deve ir para o PDF assim.

Os blocos em LaTeX estão prontos para colar no modelo da SBC. Os textos não usam travessão; nas faixas numéricas, usar "a" (nunca `--` nem `---`, que viram travessão no PDF).

**Fontes usadas**

| Conteúdo | Arquivo |
|----------|---------|
| Valores do G3 | `dados/avaliacao/G3/resultados.csv` (main) |
| Pontos, questões, hipóteses e julgamento do G3 | `docs/fase-4/resultados-g3.md` (PR #35, branch `docs/resultados-g3`) |
| Repetição independente do G3 | `dados/avaliacao/G3/repeticao.md` (PR #35) |
| Achados por métrica do G3 | `dados/avaliacao/G3/M3.*/` |
| Situação do G2 por inspeção | `dados/avaliacao/G2/M2.*/A2.md` e `consolidado.md` (PR #34, branch `larissa/g2-a2`) |
| Situação do G1 | `docs/fase-4/resultados-g1.md` (branch `larissa/g1-dia1`, em andamento) |
| Regras de agregação e julgamento | `docs/fase-2/niveis-e-julgamento.md` |
| Rastreabilidade Fase 1 para Fase 2 | `docs/fase-1/caracteristicas.md`, `docs/fase-1/partes-interessadas.md`, `docs/fase-1/proposito.md`, `docs/fase-2/objetivos-questoes-hipoteses.md` |
| Calendário | `docs/gestao/index.md` (seção 3.2), `docs/gestao/registro-de-medicoes.md` (painel dos ciclos), `docs/fase-3/cronograma.md` (marcos), milestones do GitHub |

---

## 1. Resultados

```latex
\section{Resultados}

Esta seção apresenta os valores medidos na Fase 4, o nível de cada métrica, a resposta
às questões do GQM e o julgamento do VICKY em cada característica. Os níveis, as regras
de agregação e os critérios de julgamento são os definidos na Fase 2, antes da coleta,
e não foram alterados. Os dados brutos e os scripts de cálculo estão no repositório da
equipe, em \texttt{dados/avaliacao/}.

\subsection{Adequação funcional (G1)}

[PENDENTE: kappa e cálculo do G1. Inserir aqui a Tabela de valores de M1.1.1 a M1.5.2,
o kappa de Cohen de T1 a T4, a pontuação de Q1.1 a Q1.5 e o julgamento do G1, a partir de
\texttt{docs/fase-4/resultados-g1.md} depois do fechamento da \#26.]

A coleta do G1 executou as triagens T1 a T4 no VICKY em produção, com repetição de T1
(T1-B) para a medida de estabilidade e a execução E1 para a conformidade com os filtros.
Em todas as triagens executadas até 19/11/2026, apenas o PubMed retornou artigos: o
SciELO e o Google Acadêmico retornaram zero itens mesmo quando marcados na configuração
do projeto. [PENDENTE: confirmar com a condutora do G1 se esse achado entra no artigo e
com qual arquivo de \texttt{dados/avaliacao/G1/} como fonte.]

\subsection{Capacidade de interação (G2)}

[PENDENTE: consolidação da inspeção do G2 (etapa 7) e coleta com usuários. Inserir aqui
a Tabela de valores de M2.1.1 a M2.7.2, a concordância entre A1 e A2, a resposta de Q2.1 a
Q2.7 e o julgamento do G2, a partir de \texttt{docs/fase-4/resultados-g2-inspecao.md} e
da página do G2 com usuários.]

A inspeção do G2 foi feita por dois avaliadores independentes no VICKY em produção. As
fichas do segundo avaliador, com as capturas de tela, foram registradas em 19/11/2026. A
coleta com usuários foi adaptada ao prazo da entrega pela decisão D13: a métrica de
estética (M2.5.1) passou a um formulário online com cinco respondentes, e a de
compreensão (M2.7.2) passou a sessões remotas com três participantes válidos, com
resultado apresentado como indicativo.

\subsection{Manutenibilidade (G3)}

A coleta do G3 foi feita em 14/11/2026 no commit \texttt{c2ae570} do VICKY, sobre o pacote
\texttt{src/vicky/} (38 arquivos) e a suíte \texttt{tests/} (1.034 testes), com as
ferramentas fixadas por arquivo de dependências com hash. Em 18/11/2026, um segundo
avaliador repetiu a coleta em outra máquina e outro sistema operacional e obteve
exatamente os mesmos valores de A, B e nível nas seis métricas. A
Tabela~\ref{tab:g3-valores} apresenta os valores medidos.

\begin{table}[ht]
\centering
\caption{Valores medidos do G3 no commit \texttt{c2ae570}}
\label{tab:g3-valores}
\small
\begin{tabular}{llrrrll}
\hline
\textbf{Métrica} & \textbf{Nome} & \textbf{A} & \textbf{B} & \textbf{Valor} & \textbf{Nível} & \textbf{Pontos} \\
\hline
M3.1.1 & Acoplamento de componentes & 78 & 38 & 2,05 & Excelente & 3 \\
M3.1.2 & Adequação da complexidade ciclomática & 11 & 47 & 76,6\% & Aceitável & 1 \\
M3.2.1 & Conformidade de estilo PEP 8 & 2 & 38 & 5,3\% & Insatisfatório & 0 \\
M3.2.2 & Densidade de código duplicado & 28 & 18.927 & 0,15\% & Excelente & 3 \\
M3.2.3 & Completude de logs do sistema & 0 & 33 & 0,0\% & Insatisfatório & 0 \\
M3.3.1 & Completude de testes automatizados & 4.750 & 7.519 & 63,17\% & Aceitável & 1 \\
\hline
\end{tabular}

\smallskip
\footnotesize Fonte: elaborada pela equipe a partir de \texttt{dados/avaliacao/G3/resultados.csv}.
\end{table}

O acoplamento entre arquivos é baixo, com média de 2,05 dependências internas distintas
por módulo, e a duplicação é residual: 28 linhas em 18.927, restritas a dois blocos. Os
problemas se concentram em três métricas. Em complexidade (M3.1.2), 11 das 47 funções de
\texttt{pipeline.py} passam do limite de complexidade ciclomática 10, com pico em
\texttt{run\_full\_pipeline}, de complexidade 84. Em registro de eventos (M3.2.3), nenhuma
das 33 funções críticas de \texttt{pipeline.py} usa a biblioteca \texttt{logging}, que não
aparece em nenhum arquivo do pacote; o diagnóstico depende de chamadas a \texttt{print} e
\texttt{traceback.print\_exc()}. Em testes (M3.3.1), a suíte executa sem falhas (1.002
aprovados, 27 pulados por dependência externa e 5 falhas esperadas), mas cobre 63,17\% das
linhas executáveis: a camada web chega a 87,8\%, enquanto \texttt{pipeline.py} fica em 24\%
e responde sozinho por 905 das 2.769 linhas não cobertas. A conformidade com o PEP 8
(M3.2.1) ficou em 5,3\%, mas 1.777 das 1.916 violações (92,7\%) são linhas acima de 79
caracteres.

A Tabela~\ref{tab:g3-questoes} mostra a agregação das métricas em questões e no objetivo,
pelas regras da Fase 2: a pontuação de cada questão é a média dos pontos das suas
métricas, e o objetivo é a média das três questões.

\begin{table}[ht]
\centering
\caption{Respostas às questões do G3 e julgamento do objetivo}
\label{tab:g3-questoes}
\small
\begin{tabular}{llcl}
\hline
\textbf{Questão} & \textbf{Cálculo} & \textbf{Pontuação} & \textbf{Nível} \\
\hline
Q3.1 Modularidade & (3 + 1) / 2 & 2,00 & Bom \\
Q3.2 Analisabilidade & (0 + 3 + 0) / 3 & 1,00 & Aceitável \\
Q3.3 Testabilidade & 1 / 1 & 1,00 & Aceitável \\
\hline
G3 & (2,00 + 1,00 + 1,00) / 3 & 1,33 & Aceitável \\
\hline
\end{tabular}

\smallskip
\footnotesize Fonte: elaborada pela equipe a partir de \texttt{docs/fase-4/resultados-g3.md}.
\end{table}

Nenhuma regra bloqueadora foi acionada: M3.1.2 ficou em Aceitável, e Q3.3 também. Com o
G3 em Aceitável, a manutenibilidade do VICKY \textbf{atende parcialmente}. Quanto às
hipóteses, H3.1 foi parcialmente confirmada (o acoplamento ficou melhor que o previsto,
mas a concentração de complexidade se confirmou), H3.2 foi parcialmente confirmada (a
duplicação baixa e a falta de \textit{logs} se confirmaram, e a conformidade ao PEP 8 não)
e H3.3 foi refutada, com cobertura 6,83 pontos percentuais abaixo dos 70\% previstos.

\subsection{Ação de melhoria}

Os três problemas do G3 convergem no mesmo arquivo, \texttt{src/vicky/pipeline.py}. Por
isso, a ação de melhoria escolhida é a decomposição de \texttt{run\_full\_pipeline} e a
troca de \texttt{print} por \texttt{logging} nas funções críticas, com testes para as
funções extraídas. A verificação usa o mesmo método do G3, trocando só o commit
avaliado. [PENDENTE: commit da melhoria e valores depois de M3.1.2, M3.2.3 e M3.3.1 (\#29).
Inserir uma tabela antes e depois.]

\subsection{Relação entre as características}

[PENDENTE: julgamento do G1 e do G2 (\#30). Sugestão para discutir na \#30, a confirmar
com os dados do G1: a cobertura de testes de \texttt{sources/scholar.py} é de 13\%
(\texttt{dados/avaliacao/G3/M3.3.1/pytest-cov.txt}), e na coleta do G1 o Google Acadêmico
retornou zero itens em todas as triagens. Os dados são compatíveis com uma relação entre
manutenibilidade e adequação funcional nas integrações com as fontes, mas não a
estabelecem: a equipe não mediu a causa do retorno vazio.]
```

---

## 2. Conclusão

```latex
\section{Conclusão}

Este trabalho avaliou a qualidade do VICKY, ferramenta de triagem de literatura para
revisões de estudantes de medicina, pelo processo da ISO/IEC 25040:2024, com objetivos,
questões e métricas definidos pelo GQM e níveis de julgamento fixados antes da coleta.
Foram avaliadas três características da ISO/IEC 25010:2023: adequação funcional,
capacidade de interação e manutenibilidade.

[PENDENTE: julgamento do G1. Uma ou duas frases: o que o G1 mostra sobre a lista
ranqueada que o estudante recebe.]

[PENDENTE: julgamento do G2. Uma ou duas frases: se o estudante entende e opera o VICKY
sem gastar crédito por engano.]

Na manutenibilidade, o VICKY atende parcialmente. O código tem baixo acoplamento e quase
nenhuma duplicação, mas a dívida técnica se concentra no orquestrador
\texttt{pipeline.py}, que reúne a função mais complexa do pacote, nenhum registro
estruturado de eventos e a menor cobertura de testes. Para a equipe de desenvolvimento,
isso indica onde começar: uma mudança no orquestrador é, hoje, a mais difícil de analisar
e a menos protegida contra regressão.

Em relação ao propósito definido na Fase 1, de indicar pontos de melhoria com evidências
para orientar a priorização, os resultados apontam [PENDENTE: prioridades depois do G1 e
do G2; pelo G3, a primeira é o orquestrador].

Como limitações, a avaliação mede o produto em produção numa janela de uma semana, sem
controle sobre mudanças feitas pelo fornecedor nesse período; a coleta com usuários teve
amostra reduzida (três participantes válidos na compreensão e cinco respondentes na
estética), e por isso o resultado de M2.7.2 é indicativo; e a cobertura de testes foi
medida por linhas, não por ramos. [PENDENTE: limitações do G1, como o número de temas e
o kappa obtido.]

Como trabalhos futuros, a equipe sugere repetir a avaliação depois das correções nas
integrações com as fontes de busca e estender a coleta com usuários a uma amostra maior.
```

---

## 3. Quadro de rastreabilidade da Fase 1 para a Fase 2 (pendência da #5)

Entra na seção de definição da avaliação (Fase 2), logo depois do GQM ou antes dele.

```latex
\begin{table}[ht]
\centering
\caption{Rastreabilidade das características da Fase 1 para os objetivos GQM da Fase 2}
\label{tab:rastreabilidade}
\footnotesize
\begin{tabular}{p{2.2cm}p{1.6cm}p{3.4cm}p{2.2cm}p{1.6cm}p{3.2cm}}
\hline
\textbf{Característica (Fase 1)} & \textbf{Prioridade} & \textbf{Subcaracterísticas} & \textbf{Parte interessada} & \textbf{Objetivo e questões} & \textbf{Decisão apoiada} \\
\hline
C1 Adequação funcional & Must Have (15) & Completude e correção; pertinência acrescida no G1 & Estudantes de medicina & G1, Q1.1 a Q1.5 & Priorizar correções no pipeline e nas integrações \\
C2 Capacidade de interação & Must Have (15) & Reconhecimento da adequação, aprendizado, operabilidade, proteção contra erro, engajamento, assistência (contraste e motricidade) e autodescritividade & Estudantes de medicina (usuário) & G2, Q2.1 a Q2.7 & Aprimorar a experiência de uso e a proteção contra erros \\
C3 Manutenibilidade & Should Have (12) & Modularidade, analisabilidade e testabilidade & Equipe de desenvolvimento & G3, Q3.1 a Q3.3 & Orientar a evolução e a manutenção do código \\
\hline
\end{tabular}

\smallskip
Fonte: elaborada pela equipe a partir das páginas da Fase 1 (características, partes
interessadas e propósito) e da Fase 2 (objetivos, questões e hipóteses).
\end{table}
```

Frase de chamada para o texto:

```latex
A Tabela~\ref{tab:rastreabilidade} liga cada característica selecionada na Fase 1 ao
objetivo GQM que a mede: o foco de qualidade de cada objetivo vem das subcaracterísticas
escolhidas, e o ponto de vista vem da parte interessada correspondente. As características
cortadas no MoSCoW (compatibilidade, eficiência de desempenho, flexibilidade, segurança,
confiabilidade e segurança operacional) não geram objetivo.
```

Nota de conferência: a página `docs/fase-2/objetivos-questoes-hipoteses.md` dizia, no parágrafo do G3, que a Fase 1 apontou "modificabilidade"; a Fase 1 (versão 0.7 de `caracteristicas.md`) trocou por testabilidade. A worktree corrige isso em commit separado; o artigo deve usar testabilidade.

---

## 4. Calendário da equipe para a metodologia (pendência da #8)

```latex
A equipe trabalhou em ciclos semanais de domingo a domingo, no modelo Kanban do PSM CID:
planejamento das issues do ciclo no domingo, ponto de controle com coleta parcial das
medidas na quarta-feira e revisão com coleta completa no domingo seguinte. Cada entrega
da disciplina corresponde a uma \textit{milestone} e a uma \textit{release} no GitHub. A
Tabela~\ref{tab:calendario} resume o calendário.

\begin{table}[ht]
\centering
\caption{Calendário da equipe por ciclo de trabalho}
\label{tab:calendario}
\footnotesize
\begin{tabular}{lp{2.6cm}p{8cm}}
\hline
\textbf{Ciclo} & \textbf{Período (2026)} & \textbf{Marcos} \\
\hline
0 & 05/10 a 18/10 & Estruturação do repositório e produção das Fases 1 e 2 \\
1 & 19/10 a 25/10 & Milestone E1 aberta em 19/10, com vencimento em 25/10; artigo v1 no Overleaf \\
2 & 26/10 a 01/11 & Entrega 1 e \textit{release} v0.1 (26/10) \\
3 & 02/11 a 08/11 & Abertura da Entrega 2: milestones e issues das Fases 3 e 4 (04/11) \\
4 & 09/11 a 15/11 & Ponto de controle interno (11/11); redistribuição do trabalho pela D12 (13/11); métodos da Fase 3 fechados (14/11); \textit{release} v0.2 (15/11) \\
5 & 16/11 a 22/11 & Ponto de controle da disciplina (16/11); coleta da Fase 4 (14/11 a 20/11); artigo v2 e revisão cruzada (21/11); entrega final (22/11) \\
\hline
\end{tabular}

\smallskip
Fonte: elaborada pela equipe a partir do registro de medições e do cronograma da avaliação.
\end{table}
```

Conferir antes de colar: a release v0.1 está datada de 26/10/2026 no GitHub e a v0.2 de 15/11/2026 (`gh release list`). A coleta do G3 começou em 14/11, ainda no ciclo 4, por isso a linha do ciclo 5 diz "14/11 a 20/11".

---

## 5. Tabela de contribuição do artigo (soma 99,7%)

No Overleaf, trocar a coluna de esforço da tabela de contribuição para o mesmo arredondamento da GitPage (`docs/sobre/equipe.md`, versão 0.5):

| Integrante | Esforço |
|------------|:-------:|
| Gabriel Sampaio Fae | 16,7% |
| Guilherme Maciel de Meneses | 16,7% |
| Guilherme Moura da Silva Neto | 16,7% |
| João Felipe Oliveira Alves e Silva | 16,7% |
| Larissa Gomes Silva | 16,6% |
| Lucas Antunes de Avelar | 16,6% |
| **Total** | **100,0%** |

Nota de rodapé sugerida: `Divisão igual declarada pela equipe (1/6 por integrante), arredondada pelo método dos maiores restos para somar 100,0\%.`

Se o artigo v2 trouxer também a tabela da Entrega 2 pelas horas de `dados/gestao/esforco.csv`, ver o alerta no fim deste arquivo antes de calcular.

---

## 6. Correções de idioma no Overleaf (legendas e bibliografia)

Hoje o PDF sai com "Table", "Figure" e "References". Lista para o Lucas aplicar:

1. **Preâmbulo**, logo depois de `\usepackage{sbc-template}`:
   ```latex
   \usepackage[T1]{fontenc}
   \usepackage[utf8]{inputenc}
   \usepackage[brazilian]{babel}
   ```
   Se já existir `\usepackage[english]{babel}` ou `\usepackage[brazil]{babel}`, trocar pela linha acima (uma só chamada ao `babel`). Se o documento tiver mais de um idioma, o principal é o último da lista: `\usepackage[english,brazilian]{babel}`.
2. **Recompilar do zero** (no Overleaf: menu Recompile, "Recompile from scratch"), porque os rótulos antigos ficam no `.aux`.
3. **Se ainda aparecer "Table", "Figure" ou "References"** depois do passo 2 (o estilo da SBC pode redefinir os nomes), forçar os nomes no preâmbulo, depois do `babel`:
   ```latex
   \addto\captionsbrazilian{%
     \renewcommand{\tablename}{Tabela}%
     \renewcommand{\figurename}{Figura}%
     \renewcommand{\refname}{Referências}%
   }
   ```
4. **Bibliografia:** com `sbc.bst`, os conectivos das entradas ("and", "In", "pages") vêm em inglês do próprio estilo. Para os autores, trocar "and" por "e" não é feito pelo `babel`; se a professora cobrar, a saída é usar `\bibliographystyle{abnt}` (pacote abnTeX2) ou editar uma cópia local do `sbc.bst`. Conferir com a rubrica antes de mexer (a confirmar).
5. **Títulos em inglês no `.bib`:** nomes de normas e livros em inglês ficam como estão; só os rótulos do LaTeX mudam.
6. **Legendas:** toda tabela com `\caption` acima e "Fonte: ..." abaixo; toda figura com `\caption` abaixo e fonte logo depois. Conferir as chamadas no texto com `\ref` (Tabela~\ref{...}).
7. **Travessão:** buscar no Overleaf por `--` e `---` e pelo caractere colado; trocar por vírgula, dois-pontos ou parênteses.

---

## 7. Alertas para o Lucas

- **Horas da E2:** em 20/11, `dados/gestao/esforco.csv` somando main e os branches #34, #35 e `larissa/g1-dia1` tem 33,8 h, de Faehzin (18,0 h), larigs (11,8 h) e Guilherme-Moura (4,0 h). Lucas, Guilherme Maciel e João Felipe têm 0 h lançadas, apesar de o Lucas ter escrito os métodos da Fase 3 pela D12 e feito a coleta do G3. Uma tabela de contribuição da E2 calculada hoje pelas horas daria 0% para ele. Lançar as horas antes de calcular.
- **Travessões no PR #35:** `docs/fase-4/resultados-g3.md` usa o caractere de travessão em várias linhas (títulos das questões Q3.1 a Q3.3, faixas de nível e o achado de M3.2.2). Vale pedir a troca na revisão do PR.
