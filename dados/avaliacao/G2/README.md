# Dados brutos do objetivo G2 (capacidade de interação)

Cada métrica de G2 tem uma pasta própria, com o ID da métrica como nome. A ficha de cada uma está em [Especificação das métricas](../../../docs/fase-2/especificacao-das-metricas.md). Esta pasta só recebe dados reais de coleta; nada aqui é simulado.

| Pasta | Conteúdo esperado |
|-------|-------------------|
| `M2.1.1/` | Trechos e capturas das páginas públicas que descrevem cada cenário de uso, e a contagem dos dois avaliadores |
| `M2.2.1/` | Captura da orientação de uso de cada função (F01 a F09) e a classificação dos dois avaliadores |
| `M2.2.2/` | Inventário das mensagens de erro do código, capturas das mensagens disparadas em produção e a classificação causa e solução |
| `M2.3.1/` | Planilha dos 10 padrões de interação por tela, com capturas das inconsistências |
| `M2.3.2/` | Inventário das mensagens (erro, sucesso, aviso, andamento, saldo) e a classificação de clareza |
| `M2.4.1/` | Lista das ações caras ou destrutivas, a proteção encontrada em cada uma e o trecho de código que confirma |
| `M2.4.2/` | Roteiro de entradas inválidas e o comportamento do sistema em cada uma |
| `M2.5.1/` | Respostas anonimizadas (P01 a P05) do questionário de estética das 5 telas |
| `M2.6.1/` | Registro do teste só com teclado por função, com os alvos de clique abaixo de 24 por 24 pixels |
| `M2.6.2/` | Relatórios do axe DevTools por tela e a conferência manual dos pares incertos |
| `M2.7.1/` | Capturas da primeira tela visível de cada página de entrada |
| `M2.7.2/` | Gravações e anotações das sessões com estudantes (anonimizadas, P01 a P05) e as respostas do questionário de compreensão |

## Fichas da coleta por inspeção

As oito pastas da inspeção (M2.1.1, M2.2.1, M2.2.2, M2.3.1, M2.3.2, M2.4.1, M2.4.2 e M2.7.1) já trazem as fichas do [Método do G2 por inspeção](../../../docs/fase-3/metodo-g2-inspecao.md), com os itens listados e as colunas em branco:

| Arquivo | Quem preenche |
|---------|---------------|
| `coleta.md` | A1, antes da primeira captura |
| `A1.md` e `A2.md` | Cada avaliador, sem abrir a ficha do outro |
| `inventario.md` e `codigo-a1.md` (M2.2.2 e M2.3.2) | A1, na etapa 1. A2 só abre `codigo-a1.md` depois de enviar `A2.md` |
| `consolidado.md` | A1 e A2 juntos, na etapa 7. O valor da métrica sai daqui |
| `evidencias/` | Cada avaliador, com as capturas `AAAAMMDD_A1_<item>.png` |

**Como preencher pelo GitHub:** abra o arquivo, clique no lápis (*Edit this file*), escreva entre as barras `|` de cada linha e clique em *Commit changes*. Para as capturas, entre em `evidencias/` e use *Add file > Upload files*.

O arquivo `previa-ia.md` é uma prévia exploratória feita com IA, só com as páginas públicas. Não é dado de coleta, e A2 não deve lê-lo antes de enviar as próprias fichas.

Os dados de avaliadores e participantes devem ser anonimizados (A1, A2 e P01 a P05) antes de entrar no repositório, como pede o [README da pasta de dados](../../README.md). Registre em cada pasta a data da coleta e a versão do VICKY em produção.
