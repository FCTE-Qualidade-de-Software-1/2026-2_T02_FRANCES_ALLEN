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
| `M2.5.1/` | Respostas anonimizadas (códigos R01 a R05) do formulário de estética das 5 telas e registro do formulário (`coleta.md`) |
| `M2.6.1/` | Registro do teste só com teclado por função, com os alvos de clique abaixo de 24 por 24 pixels |
| `M2.6.2/` | Relatórios do axe DevTools por tela e a conferência manual dos pares incertos |
| `M2.7.1/` | Capturas da primeira tela visível de cada página de entrada |
| `M2.7.2/` | Registro de cada sessão com estudantes (código do participante, data, duração e hash SHA-256 da gravação), anotações anonimizadas (P01 a P05) e respostas do questionário de compreensão. As gravações não ficam aqui (ver abaixo) |

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

**Etapa 7 (consolidação).** Depois que `A1.md` e `A2.md` estiverem no repositório, a partir da raiz:

```bash
python3 dados/avaliacao/G2/calcular_g2_inspecao.py comparar   # preenche valor_a1, valor_a2 e os consensos; lista as divergências
python3 dados/avaliacao/G2/calcular_g2_inspecao.py calcular   # lê só valor_final e escreve o "Resultado" de cada consolidado.md
```

Em cada divergência, A1 e A2 preenchem `valor_final`, `justificativa` e `decidido_por` no `consolidado.md` antes de rodar `calcular`. Os inventários foram entregues a A2 em 17/11 também como planilhas (`modelo.csv` e `inventario.csv`, no branch `docs/fase-3-cronograma-e-correcoes-e1`); se a ficha de A2 vier como `A2.csv` nesse modelo, o script lê a planilha no lugar de `A2.md`.

## Fichas da coleta com usuários e de acessibilidade

As quatro pastas do [Método do G2 com usuários](../../../docs/fase-3/metodo-g2-usuarios.md) (M2.5.1, M2.6.1, M2.6.2 e M2.7.2) trazem as fichas em branco e os modelos CSV só com o cabeçalho:

| Arquivo | Quem preenche |
|---------|---------------|
| `M2.7.2/sessoes.csv` | Observador (ou o condutor, se não houver observador), ao fim de cada sessão: código do participante, data, duração, local e hash SHA-256 da gravação |
| `M2.7.2/perfil.csv`, `observacao-uso.csv` e `respostas-compreensao.csv` | Condutor e observador, durante e depois da sessão; sem observador, o condutor pela gravação e um segundo classificador para `classificacao_o` |
| `M2.5.1/coleta.md`, `respostas.csv`, `qualitativo.csv` e `consolidado.md` | Quem montou o formulário, a partir das respostas válidas exportadas do Google Forms; `consolidado.md` com o cálculo (acrescentado com a D14) |
| `M2.7.2/coleta.md` e `consolidado.md` | Condutor, antes do piloto e depois das três sessões válidas |
| `M2.6.1/K1.md`, `K2.md` e `consolidado.md` | Avaliadores do teste com teclado (K1 e K2) |
| `M2.6.2/A1.md`, `A2.md`, `consolidado.md` e `relatorios/` | Avaliadores de contraste |
| `termo-de-consentimento.docx` | Texto do termo da sessão, lido no início da chamada |

**Cálculo de M2.7.2 e M2.5.1.** Depois que os CSVs estiverem preenchidos, a partir da raiz:

```bash
python3 dados/avaliacao/G2/calcular_g2_usuarios.py   # imprime as tabelas dos dois consolidado.md, para conferência
```

Em 22/11/2026, as três sessões válidas (P01 a P03) e as três respostas ao formulário (R01 a R03) já estão nas pastas, com os recortes dos 12 elementos em `M2.7.2/elementos/`.

**Gravações, aceites e a planilha bruta do formulário nunca entram neste repositório, que é público.** Eles ficam na pasta restrita do Google Drive da equipe, compartilhada só com os integrantes e com a professora, e são apagados ao fim do semestre 2026/2. Aqui fica só o registro de cada arquivo (participante anonimizado, data, duração e hash).

Só os participantes (P01 a P05) e os respondentes do formulário (R01 a R05) são anonimizados antes de entrar no repositório, como pede o [README da pasta de dados](../../README.md). Integrantes da equipe podem ser nomeados nos papéis (A1, A2, C, O, K1, K2) em `coleta.md`, porque o histórico do git já os identifica. Registre em cada pasta a data da coleta e a versão do VICKY em produção.
