# Propósito da avaliação e uso pretendido

## 1. Propósito

Realizar uma avaliação em que medida o VICKY atende às necessidades dos estudantes de medicina na busca, triagem e consulta de artigos científicos, com o objetivo de indicar pontos para melhoria no produto, fornecendo evidências para orientar a priorização de melhorias no sistema.


## 2. Uso pretendido dos resultados

| Decisão apoiada pela avaliação | Quem toma a decisão | Como os resultados serão usados |
|--------------------------------|---------------------|---------------------------------|
| Priorizar correções e otimizações no pipeline de LLM e nas integrações (PubMed/Scholar) | Equipe de Desenvolvimento e Mantenedores do VICKY | Guiar a refatoração de código, correção de regras de negócio e melhorias na triagem de artigos |
| Garantir a evolução e facilidade de manutenção do código-fonte | Arquitetos de Software e Desenvolvedores do VICKY | Orientar melhorias na modularidade, analisabilidade da aplicação |
| Aprimorar a experiência de uso e a proteção contra erros do usuário no uso da interface | Designers de UX/UI e Desenvolvedores Frontend | Ajustar a capacidade de interação e operabilidade do sistema |
| Validar o nível de qualidade do produto frente às métricas GQM e ISO/IEC 25040 | Equipe Frances Allen | Fundamentar o relatório de avaliação e melhoras sugeridas pela equipe |

## 3. Perspectiva da avaliação

A avaliação do VICKY adota uma perspectiva dupla que integra visões externas e internas. A perspectiva externa examina o produto em uso via navegador web, focando na jornada do usuário, como autenticação, parametrização de buscas e exportação dos resultados. Essa visão orienta a análise de Adequação Funcional e Capacidade de Interação, garantindo uma triagem precisa, intuitiva e protegida contra erros.

Já a perspectiva interna examina a estrutura do código-fonte do backend, avaliando a orquestração de consultas e a integração com LLMs. Essa abordagem permite medir a Manutenibilidade, verificando modularidade e complexidade estrutural para assegurar a evolução sustentável do sistema.

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 16/10/2026 | Página criada a partir da seção "Propósito da avaliação" de Seleção e justificativa | Gabriel Fae | - |
| 0.2 | 18/10/2026 | Definição do propósito, uso pretendido e detalhamento da perspectiva | Guilherme Maciel | - |
