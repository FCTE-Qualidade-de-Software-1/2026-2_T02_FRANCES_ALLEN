# Etapa 11a de A1: conferência de M1.2.1 e revisão de M1.5.1

Feita em 19/11/2026, depois do envio das fichas de relevância e de rubrica (commit anterior desta pasta), como exige o [Método do G1](../../../../docs/fase-3/metodo-g1.md), seção 4.1, etapa 11a. Apoio de IA declarado no [README](README.md).

## 1. M1.2.1: funções declaradas operantes

A1 preencheu `classificacao_conferente` em [`../M1.2.1/casos_funcoes.csv`](../M1.2.1/casos_funcoes.csv), subpasso a subpasso, a partir dos registros de tela em `../M1.2.1/evidencias/` e da tabela da seção 4.3 do método. Cada linha recebeu uma nota iniciada por "A1 (19/11)" na coluna `observacao`. Quando executor e conferente coincidem, `classificacao_final` repete o valor.

| Função | Subpassos segundo A1 | Classificação de A1 |
|--------|----------------------|---------------------|
| F01 Cadastro e login | (a) sim, (b) sim, (c) não | Parcial |
| F02 Criação de projeto | (a) sim, (b) sim, (c) sim, (d) não | Parcial |
| F03 Protocolo PICO | (a) não, (b) sim, (c) não | Parcial |
| F04 Bases e quantidade | (a) não, (b) sim, (c) sim | Parcial |
| F05 Triagem completa | (a) a (d) sim | Operante |
| F06 Lista ranqueada | (a) a (c) sim | Operante |
| F07 Favoritos | (a) a (c) sim | Operante |
| F08 Log auditável | (a) a (c) sim | Operante |
| F09 Exportação | (a) sim, (b) sim, (c) não, (d) não | Parcial |

**Divergências a decidir com C** (`classificacao_final` em branco, pela regra da seção 4.3: C e A1 reabrem a evidência e aplicam a regra):

| Subpasso | Executor (C) | A1 | Motivo de A1 |
|----------|--------------|----|--------------|
| F02 (d) | com ressalva | não | Ao reabrir o projeto, objetivo e bases não aparecem; o subpasso pede ver os valores salvos |
| F03 (a) | discutível | não | A tela não apresenta P, I, C e O rotulados, apenas protocolo em estágios e strings de busca |
| F04 (a) | sim | não | A escolha de bases não é visível na tela ao reabrir o projeto; o registro no banco não é visto pelo estudante |

**Pontos para C conferir:**
- O registro do P0 #51 exibe meta do Top 0/25, e o do P0b #52, 0/10. O `execucoes.csv` anota Top 30 para P0.
- A captura citada em F04 (c), `capturas/E1_lista_tela.txt`, não está no repositório.
- F01 (a) e (b) não têm captura no repositório; foram aceitos pelo registro do condutor.

## 2. M1.5.1: itens não conformes de E1

A1 reviu, pela coluna `tipo_observado` (*Publication Type* do PubMed e resumo), os 29 itens de [`../M1.5.1/conferencia_E1.csv`](../M1.5.1/conferencia_E1.csv) marcados como não conformes. Todos são revisões sistemáticas, meta-análises, revisões narrativas ou revisão guarda-chuva. Nenhum é relato de ensaio randomizado ou análise secundária de ensaio, que é o que a E1 pede. **A1 concorda com os 29 julgamentos de C.** O único item conforme (posição 8, análise secundária do LoDoCo2) segue a mesma regra adotada por A1 em M1.3.1.

## 3. M1.3.2: itens incorretos

Pendente. A conferência de metadados de M1.3.2 (`../M1.3.2/conferencia_Tn.csv`) ainda não está no repositório. A1 revê os itens marcados como incorretos quando ela entrar.
