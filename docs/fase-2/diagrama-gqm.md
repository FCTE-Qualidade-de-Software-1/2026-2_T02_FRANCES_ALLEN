# Diagrama GQM

O diagrama representa a hierarquia completa, com os três níveis identificados formalmente (critério F2-C6). Atualizar sempre que um objetivo, questão ou métrica mudar.

```mermaid
flowchart TD
    subgraph N1["Nível conceitual - Objetivos"]
        G1["G1 - Adequação funcional"]
        G2["G2 - Capacidade de interação"]
        G3["G3 - Manutenibilidade"]
    end
    subgraph N2["Nível operacional - Questões"]
        Q11["Q1.1"]
        Q12["Q1.2"]
        Q21["Q2.1"]
        Q31["Q3.1"]
    end
    subgraph N3["Nível quantitativo - Métricas"]
        M111["M1.1.1"]
        M121["M1.2.1"]
        M211["M2.1.1"]
        M311["M3.1.1"]
    end
    G1 --> Q11 --> M111
    G1 --> Q12 --> M121
    G2 --> Q21 --> M211
    G3 --> Q31 --> M311
```

_Figura 1 - Hierarquia GQM da avaliação do VICKY. Fonte: elaborada pela equipe._

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 05/10/2026 | Criação da estrutura do documento | Gabriel Fae | - |
| 0.2 | 16/10/2026 | Reorganização da documentação por fases do processo de avaliação | Gabriel Fae | - |
