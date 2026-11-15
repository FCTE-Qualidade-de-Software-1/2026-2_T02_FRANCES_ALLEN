# Dados

Pasta de dados brutos e consolidados (Premissa 5 - rastreabilidade dos dados).

- `gestao/` - medições de acompanhamento do projeto (Premissa 3).
- `avaliacao/` - dados de coleta das métricas do VICKY, uma pasta por objetivo e, dentro dela, uma pasta por métrica, com os scripts de cálculo do objetivo:

```text
avaliacao/
├── G1/            # adequação funcional: calcular_g1.py, modelos/, referencias/ e M1.1.1/ a M1.5.2/
├── G2/            # capacidade de interação: termo em branco e M2.1.1/ a M2.7.2/
└── G3/            # manutenibilidade: coletar.sh, extrair.py, calcular.py, lockfiles e M3.1.1/ a M3.3.1/
```

O passo a passo de cada objetivo e o nome de cada arquivo estão nos métodos da [Fase 3](../docs/fase-3/index.md) e no `README.md` de cada pasta.

## Identificação de pessoas

- **Integrantes da equipe** podem ser nomeados nos papéis de cada método (C, O, A1, A2, A3, K1, K2), no `coleta.md` da pasta. O histórico do git já identifica quem enviou cada arquivo.
- **Participantes** (estudantes das sessões do G2 com usuários) são sempre anonimizados, com os códigos P01 a P07, antes de entrar no repositório. Nenhum nome, e-mail, matrícula, instituição, semestre exato ou outro dado que identifique o participante entra aqui.

## Condições de acesso aos dados de participantes

| Dado | Onde fica | Quem acessa |
|------|-----------|-------------|
| Respostas, anotações e perfil anonimizados (P01 a P07) | Este repositório, em `avaliacao/G2/M2.5.1/` e `avaliacao/G2/M2.7.2/` | Público |
| Registro de cada gravação (código, data, duração e hash SHA-256) | `avaliacao/G2/M2.7.2/sessoes.csv` | Público |
| Gravações de tela e voz e termos assinados | Pasta restrita no Google Drive da equipe, com subpastas separadas para gravações e termos | Só os seis integrantes e a professora |
| Ligação entre o nome do participante e o código | Só no termo assinado, na pasta restrita | Só os seis integrantes e a professora |

As gravações e os termos digitalizados são excluídos ao fim do semestre 2026/2, como informa o termo de consentimento, e a exclusão é registrada em `avaliacao/G2/M2.7.2/coleta.md`. O hash permite conferir, enquanto a gravação existir, que o arquivo da pasta restrita é o da sessão registrada.
