# Modelo de qualidade

## 1. Norma de referência

Modelo de qualidade do produto da **ISO/IEC 25010:2023** (família SQuaRE - ISO/IEC 25000). A terminologia segue a edição de 2023, em que "usabilidade" passou a se chamar **capacidade de interação**.

## 2. Adaptação ao VICKY

_Explicar quais partes do modelo foram mantidas, quais foram descartadas e por quê, com base no contexto do produto e nas [partes interessadas](partes-interessadas.md)._

| Característica | Subcaracterísticas mantidas | Adaptação e justificativa |
|----------------|-----------------------------|---------------------------|
| Adequação funcional | _-_ | _-_ |
| Capacidade de interação | _-_ | _-_ |
| Manutenibilidade | _-_ | _-_ |

## 3. Representação gráfica

```mermaid
flowchart TD
    Q["Qualidade do produto VICKY<br/>(ISO/IEC 25010:2023)"]
    Q --> C1["C1 - Adequação funcional"]
    Q --> C2["C2 - Capacidade de interação"]
    Q --> C3["C3 - Manutenibilidade"]
    C1 --> S11["Completude funcional"]
    C1 --> S12["Correção funcional"]
    C1 --> S13["Aptidão funcional"]
    C2 --> S21["Subcaracterísticas a definir"]
    C3 --> S31["Subcaracterísticas a definir"]
```

_Figura 1 - Modelo de qualidade adaptado ao VICKY. Fonte: elaborada pela equipe com base na ISO/IEC 25010:2023._

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 16/10/2026 | Página criada a partir da seção "Norma de referência" de Seleção e justificativa | Gabriel Fae | - |
