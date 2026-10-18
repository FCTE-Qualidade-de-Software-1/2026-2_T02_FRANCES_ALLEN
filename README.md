# Qualidade de Software 1 - 2026.2 - T02 - Frances Allen

## Sobre o projeto

Esta página é dedicada à documentação de todos os artefatos criados pela equipe Frances Allen  no segundo semestre de 2026, na disciplina de Qualidade de Software da Faculdade de Ciências e Tecnologias em Engenharia da Universidade de Brasília (FCTE-UnB).

O produto avaliado é o **VICKY**, um website voltado a **estudantes de medicina**, que permite buscar e consultar informações sobre artigos científicos e conteúdos acadêmicos da área da saúde.

O objetivo do trabalho é **avaliar o produto à luz de modelos e métricas de qualidade**, identificando pontos fortes, oportunidades de melhoria e evidências mensuráveis que sustentem as conclusões. A avaliação segue o processo de avaliação de produto da família **SQuaRE** (ISO/IEC 25040). Ela usa o modelo de qualidade da **ISO/IEC 25010**, define as métricas pelo método **GQM (Goal-Question-Metric)** e acompanha a gestão do projeto com métricas **PSM/CID**.

| Item | Descrição |
|------|-----------|
| Nome | VICKY |
| Tipo | Aplicação web (SaaS) de triagem de literatura científica assistida por IA, acessada pelo navegador |
| URL | <https://vicky.synaptha.com/> |
| Organização responsável | Synaptha Inc Ltda (CNPJ 63.642.396/0001-90), Brasília-DF |
| Versão avaliada / data de acesso | Versão em produção acessada em 17/10/2026 (Termos de Uso e Política de Privacidade na versão 2026-09-29) |
| Público-alvo | Estudantes de medicina (foco declarado) em iniciação científica, TCC, monografia e artigo de resumo; uso restrito a maiores de 18 anos |
| Plataformas | Navegador web, desktop e mobile |
| Exige cadastro ou login | Sim, com nome, e-mail e senha. |
| Modelo de acesso | Gratuito ou por assinatura |
| Acesso ao código-fonte | Sim, código-fonte completo, liberado pela equipe de desenvolvimento (ativa no projeto) |
| Repositório do código | Não pode ser exibido de forma aberta. |

### Características de qualidade selecionadas (ISO/IEC 25010)

| # | Característica | Justificativa |
|---|----------------|---------------|
| C1 | **Adequação funcional** |  O VICKY promete poupar o tempo de pesquisa filtrando artigos metodologicamente relevantes. Avaliar a correção e completude garante que o pipeline de LLM e as integrações (PubMed/Scholar) entregam o valor prometido sem falhas nas regras de negócio |
| C2 | **Capacidade de interação** | Operabilidade, Proteção contra erro do usuário e Autodescritividade | Estudantes de medicina precisam configurar critérios complexos (PICO) para iniciar uma revisão. A interface deve guiar o usuário na parametrização correta e na interpretação clara do "Quality Score" para evitar erros no uso dos créditos pagos. |
| C3 | **Manutenibilidade** | Modularidade, Analisabilidade e Modificabilidade | O sistema possui um orquestrador assíncrono complexo (`pipeline.py`) e integrações externas instáveis por natureza (LLMs, scrapers). Avaliar a modularidade e analisabilidade do código Python garante que os desenvolvedores consigam atualizar as fontes de busca e os prompts facilmente no futuro.  |

Detalhes em [Fase 1 - Seleção e priorização das características](docs/fase-1/caracteristicas.md).

## Link da página de documentação

[https://fcte-qualidade-de-software-1.github.io/2026-2_T02_FRANCES_ALLEN/](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_FRANCES_ALLEN/)

> A documentação é escrita em Markdown na pasta [`docs/`](docs/) e publicada via **MkDocs + GitHub Pages**.

## Integrantes

<center>
<table style="margin-left: auto; margin-right: auto;">
    <tr>
        <td align="center">
            <a href="link do github">
                <img style="border-radius: 50%; width: 100px; heigth: 100px" src="https://github.com/Faehzin" />
                <h5 class="text-center">Gabriel Sampaio Fae</h5>
                <h5 class="text-center">231011382</h5>
            </a>
        </td>
        <td align="center">
            <a href="link do github">
                <img style="border-radius: 50%;  width: 100px; heigth: 100px" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAUi3wIxO1RToN_FhwNdon8Xhiz53UFneKSg&s"/>
                <h5 class="text-center">Nome do integrante</h5>
                <h5 class="text-center">Matrícula</h5>
            </a>
        </td><td align="center">
            <a href="link do github">
                <img style="border-radius: 50%;  width: 80px;heigth: 100px" src="https://www.giantbomb.com/a/uploads/scale_small/13/139866/2783526-roberta.jpg" />
                <h5 class="text-center">Nome do integrante</h5>
                <h5 class="text-center">Matrícula</h5>
            </a>
        </td><td align="center">
            <a href="link do github">
                <img style="border-radius: 50%;  width: 150px;heigth: 100px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Katherine_Johnson_at_NASA%2C_in_1966.jpg/250px-Katherine_Johnson_at_NASA%2C_in_1966.jpg"/>
                <h5 class="text-center">Nome do integrante</h5>
                <h5 class="text-center">Matrícula</h5>
            </a>
        </td><td align="center">
            <a href="link do github">
                <img style="border-radius: 50%;  width: 150px;heigth: 100px" src="https://s2.glbimg.com/M7i2Eovi6zB-rywedhQc355033E=/e.glbimg.com/og/ed/f/original/2019/08/09/hedy_lamarr_-_1940_1.jpg"/>
                <h5 class="text-center">Larissa Gomes Silva</h5>
                <h5 class="text-center">211031092</h5>
            </a>
        </td><td align="center">
            <a href="link do github">
                <img style="border-radius: 50%;  width: 150px;heigth: 100px" src="https://ik.imagekit.io/smdxc0e2g3/userscontent2-endpoint/images/ef3ac225-0a27-4267-b19c-390ac862caeb/80e4d68dd69eefb7d6fe2d41a0038293.jpg?tr=w-160,rt-0"/>
                <h5 class="text-center">Nome do integrante</h5>
                <h5 class="text-center">Matrícula</h5>
            </a>
        </td>
</table>
 <! -- ## :email: Site -->
<hr/>


## Documentação

A documentação é organizada em abas pelas fases do processo de avaliação de produto da SQuaRE (ISO/IEC 25040).

- [Página inicial](docs/index.md)
- **Fase 1 - Estabelecer os requisitos da avaliação**: [Propósito](docs/fase-1/proposito.md) · [Partes interessadas](docs/fase-1/partes-interessadas.md) · [Objeto de avaliação](docs/fase-1/objeto-de-avaliacao.md) · [Modelo de qualidade](docs/fase-1/modelo-de-qualidade.md) · [Características](docs/fase-1/caracteristicas.md) · [Escopo](docs/fase-1/escopo.md) · [ODS](docs/fase-1/ods.md)
- **Fase 2 - Especificar a avaliação (GQM)**: [Objetivos, questões e hipóteses](docs/fase-2/objetivos-questoes-hipoteses.md) · [Especificação das métricas](docs/fase-2/especificacao-das-metricas.md) · [Níveis e julgamento](docs/fase-2/niveis-e-julgamento.md) · [Diagrama GQM](docs/fase-2/diagrama-gqm.md)
- **Fase 3 - Projetar a avaliação**: [futuramente](docs/fase-3/index.md)
- **Fase 4 - Executar e concluir a avaliação**: [futuramente](docs/fase-4/index.md)
- **Gestão do projeto (PSM/CID)**: [Plano de medição](docs/gestao/plano-de-medicao.md) · [Registro de medições](docs/gestao/registro-de-medicoes.md) · [Decisões](docs/gestao/decisoes.md) · [Atas](docs/gestao/atas.md)
- **Sobre**: [Equipe](docs/sobre/equipe.md) · [Declaração de uso de IA](docs/sobre/uso-de-ia.md) · [Referências](docs/sobre/referencias.md) · [Dados](dados/README.md)

### Rodar a documentação localmente

```bash
pip install -r requirements.txt
GIT_DATES=false mkdocs serve   # http://127.0.0.1:8000 (GIT_DATES=false só enquanto não houver commits)
```


## :octocat: Histórico de versão 
| Versão | Data | Descrição  |  Autor(a) |
|--------|------|------------|-----------|
| 0.1 | 05/10/2026 | Inicialização do projeto no github | Gabriel Fae |
| 0.2 | 05/10/2026 | Contexto do projeto (VICKY), características selecionadas e estrutura da documentação | Gabriel Fae |
| 0.3 | 16/10/2026 | Documentação reorganizada em abas por fase do processo de avaliação | Gabriel Fae |
