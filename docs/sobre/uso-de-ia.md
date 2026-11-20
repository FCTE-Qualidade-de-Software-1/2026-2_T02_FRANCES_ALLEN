# Declaração de uso de IA

A rubrica da disciplina exige declarar **a ferramenta**, **a tarefa** e **como o resultado foi conferido ou ajustado**.

| Ferramenta | Tarefa | Como foi conferido / ajustado | Responsável |
|------------|--------|-------------------------------|-------------|
| Claude (Anthropic) | Estruturação inicial dos arquivos da documentação e da GitPage | Usou meu modelo de Docs para montar a estrutura básica | Gabriel Fae |
| Claude (Anthropic) | Inventário das telas, mensagens e ações do código-fonte do VICKY e rascunho do GQM de capacidade de interação (G2) | _A confirmar por Lucas Avelar._ O histórico do repositório registra a revisão do GQM do G2 em 18/10/2026 (commits `51dce2b`, `8c048e1` e `ef7af41`), com o realinhamento às sete subcaracterísticas de C2; o que foi conferido nas fontes não está registrado | Lucas Avelar |
| Claude (Anthropic) | Rascunho do GQM de adequação funcional (G1) | Todo o conteúdo foi lido, ajustado e adaptado pela Larissa, para conferir a veracidade dos fatos | Larissa Gomes Silva |
| Claude (Anthropic) | Diagrama de modelo de qualidade | Escrevi todas as qualidades analisadas e suas subcaracterísticas e pedi o diagrama desenhado após anexar um desenho feito à mão no caderno | Gabriel Fae |
| Claude (Anthropic) | Revisão do método do G2 por inspeção, fichas de coleta em Markdown, estrutura da página de resultados do G2 por inspeção e prévia exploratória das páginas públicas (não incluída no repositório) | Basicamente pedi para a IA analisar minha entrega da Fase 3, me dizer as pendências e estruturar uma ficha para que eu completasse com os resultados da Fase 4 | Gabriel Fae |
| Claude (Anthropic) | Redação dos métodos do G1, do G2 com usuários e do G3, da página de recursos e ambiente, do cronograma, da tabela de consistência, dos instrumentos do G2 com usuários e do termo de consentimento (Fase 3) | Lucas Avelar conferiu cada método contra as fichas da Fase 2 e contra o código do VICKY. Cada dono original revisa a sua página em 15/11/2026; até essa revisão, as páginas constam como escritas, não revisadas | Lucas Avelar |
| Claude (Anthropic) | Scripts `coletar.sh`, `extrair.py` e `calcular.py` (G3) e `calcular_g1.py` (G1) | Os números do G3 foram conferidos contra as saídas brutas das ferramentas. O `calcular_g1.py` foi testado contra o scipy e o scikit-learn | Lucas Avelar |
| Claude (Anthropic) | Execução das ferramentas do G3 sobre o commit `c2ae570` do VICKY | Os valores foram conferidos contra as saídas brutas, e a coleta foi rodada duas vezes, com os mesmos resultados (`dados/avaliacao/G3/repeticao-autor-2026-11-14.md`) | Lucas Avelar |
| Claude (Anthropic) | Pesquisa das revisões sistemáticas de referência do G1 | DOI, PMID, PMCID e número de incluídos de cada revisão conferidos no PubMed e no PMC em 14/11/2026 (`dados/avaliacao/G1/referencias/referencias.md`) | Lucas Avelar |
| Claude (Anthropic) | Montagem das fichas cegas dos testes do G1 (`ficha_cega_Tn.csv`, em ordem aleatória, sem posição nem Quality Score) | A ordem vem do `calcular_g1.py`, com a semente do método, e foi conferida pela Larissa contra o Top 30 de cada tema | Larissa Gomes Silva |
| Claude (Anthropic) | Montagem das planilhas de avaliação entregues a A1 e A2 (uma por avaliador, com uma aba por tema e por julgamento), a partir das fichas cegas `ficha_cega_Tn.csv` já geradas: copia item, título, resumo, ano, periódico e DOI, acrescenta as instruções, o PICO do tema e as colunas em branco a preencher, com listas de opções nas colunas de resposta | A IA não julgou relevância nem rubrica e não preencheu nenhuma coluna de resposta. O script usa só as fichas cegas, sem ler as chaves `chave_Tn.csv` nem abrir o VICKY, então as planilhas não trazem posição nem Quality Score. A Larissa conferiu as planilhas contra as fichas cegas antes do envio | Larissa Gomes Silva |
| Claude (Anthropic) | Fichas de A1 do G1: julgamento de relevância de T1 a T4 (M1.3.1), rubrica de T1 e T2 (M1.4.1) e etapa 11a (conferência de M1.2.1 e revisão dos não conformes de M1.5.1) | Aplicação dos critérios das seções 4.4 e 4.6 do método a cada item da ficha cega, com justificativa por item e interpretações registradas em `dados/avaliacao/G1/respostas-A1/README.md`, a pedido de A1. O contato prévio do assistente com registros de tela de T1 está declarado como limitação no mesmo arquivo | Gabriel Fae |
| Claude (Anthropic) | Apoio a A2 nas fichas do G1: relevância de T1 a T4 (M1.3.1) e rubrica de T1 e T2 (M1.4.1) | IA usada como auxílio na aplicação dos critérios das seções 4.4 e 4.6, em sessão separada da de A1 e sem acesso às chaves nem às respostas de A1. A2 revisou as fichas e assume cada julgamento; interpretações registradas em `dados/avaliacao/G1/respostas-A2/README.md` | Lucas Avelar |

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 05/10/2026 | Criação da estrutura do documento | Gabriel Fae | - |
| 0.2 | 16/10/2026 | Reorganização da documentação por fases do processo de avaliação | Gabriel Fae | - |
| 0.3 | 18/10/2026 | Declaração do uso de IA no objetivo G1 | Larissa Gomes Silva | - |
| 0.4 | 14/11/2026 | Declaração do uso de IA na Fase 3, linha do G2 marcada a confirmar e correções de texto | Lucas Avelar | - |
| 0.6 | 19/11/2026 | Declaração do uso de IA nas fichas de A1 do G1 | Gabriel Fae | - |
| 0.7 | 20/11/2026 | Declaração do uso de IA como auxílio nas fichas de A2 do G1 | Lucas Avelar | - |
| 0.8 | 20/11/2026 | Declaração do uso de IA na montagem das planilhas de avaliação de A1 e A2 do G1 | Larissa Gomes Silva | - |
