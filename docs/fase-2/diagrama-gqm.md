# Diagrama GQM

O diagrama representa a hierarquia completa, com os três níveis identificados formalmente (critério F2-C6). Atualizar sempre que um objetivo, questão ou métrica mudar.

```mermaid
flowchart LR
    subgraph N1["Nível conceitual - Objetivos"]
        G1["G1 - Adequação funcional"]
        G2["G2 - Capacidade de interação"]
        G3["G3 - Manutenibilidade"]
    end
    subgraph N2["Nível operacional - Questões"]
        Q11["Q1.1"]
        Q12["Q1.2"]
        Q21["Q2.1 - Operabilidade"]
        Q22["Q2.2 - Proteção contra<br/>erro do usuário"]
        Q23["Q2.3 - Autodescritividade"]
        Q31["Q3.1"]
    end
    subgraph N3["Nível quantitativo - Métricas"]
        M111["M1.1.1"]
        M121["M1.2.1"]
        M211["M2.1.1 · UOp-1-G"]
        M212["M2.1.2 · UOp-2-G"]
        M221["M2.2.1 · UEp-1-G"]
        M222["M2.2.2 · UEp-2-S"]
        M223["M2.2.3 · UEp-3-S"]
        M231["M2.3.1 · UAp-3-S"]
        M232["M2.3.2 · ULe-4-S"]
        M311["M3.1.1"]
    end
    G1 --> Q11 --> M111
    G1 --> Q12 --> M121
    G2 --> Q21 & Q22 & Q23
    Q21 --> M211 & M212
    Q22 --> M221 & M222 & M223
    Q23 --> M231 & M232
    G3 --> Q31 --> M311
```

_Figura 1 - Hierarquia GQM da avaliação do VICKY: os três objetivos (nível conceitual), as questões de cada um (nível operacional) e as métricas que respondem a cada questão (nível quantitativo), com o código da medida da ISO/IEC 25023:2016. Fonte: elaborada pela equipe._

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 05/10/2026 | Criação da estrutura do documento | Gabriel Fae | - |
| 0.2 | 16/10/2026 | Reorganização da documentação por fases do processo de avaliação | Gabriel Fae | - |
| 0.3 | 18/10/2026 | Ramo completo do G2 (capacidade de interação) no diagrama único | Lucas Avelar | Gabriel Fae |
