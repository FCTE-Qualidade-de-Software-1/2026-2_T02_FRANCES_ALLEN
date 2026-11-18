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

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 05/10/2026 | Criação da estrutura do documento | Gabriel Fae | - |
| 0.2 | 16/10/2026 | Reorganização da documentação por fases do processo de avaliação | Gabriel Fae | - |
| 0.3 | 18/10/2026 | Declaração do uso de IA no objetivo G1 | Larissa Gomes Silva | - |
| 0.4 | 14/11/2026 | Declaração do uso de IA na Fase 3, linha do G2 marcada a confirmar e correções de texto | Lucas Avelar | - |
