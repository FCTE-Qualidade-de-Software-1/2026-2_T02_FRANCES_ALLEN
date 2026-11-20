# M2.3.2: caminhos no código (só A1)

> **A2 não abre este arquivo antes de `A2.md` estar no repositório.** Commit do código: `c2ae570` do fork `LucasAvelar2711/Vicky`. Caminhos relativos a `src/vicky/`.
>
> `exibicao_segundo_o_codigo` é o que o código indica sobre a mensagem chegar à tela; o que vale é produção. "PROVAVELMENTE NÃO EXIBIDA": o sistema manda a mensagem na URL para uma tela que não a lê.

| id | arquivo_e_linha | exibicao_segundo_o_codigo | observacao |
|---|---|---|---|
| ERR01 | web/app.py:1132-1133 | exibida (signup.html:31) |  |
| ERR02 | web/app.py:1134-1135 | exibida | e-mail sem @ é barrado antes pelo navegador |
| ERR03 | web/app.py:1136-1137 e 1358-1359 | provavelmente encoberta | campo tem minlength=8: o Chrome barra antes e mostra a mensagem dele |
| ERR04 | web/app.py:1138-1139 | exibida |  |
| ERR05 | web/app.py:1142-1147 | provavelmente encoberta | caixa tem required: o Chrome barra antes. Texto sem acentos no código ("e preciso", "Politica") |
| ERR06 | web/app.py:1150-1152 | exibida |  |
| ERR07 | web/app.py:1086-1088 | exibida | mesma mensagem para e-mail inexistente e senha errada (de propósito, por segurança) |
| ERR08 | web/app.py:1186-1189 | exibida (login.html:35) | "peca" sem cedilha no código. Só existe se o envio de e-mail estiver ligado |
| ERR09 | web/app.py:1190-1200 | exibida | difícil de provocar sem adulterar URL |
| ERR10 | web/app.py:1246-1250 | PROVAVELMENTE NÃO EXIBIDA | redireciona para /dashboard?error=...; dashboard.html não lê msg/error da URL |
| ERR11 | web/app.py:1255-1257 | PROVAVELMENTE NÃO EXIBIDA | mesmo caso de ERR10 |
| ERR12 | web/app.py:1279-1282 | provavelmente encoberta | campo type=email required: o Chrome barra e-mail sem @ antes |
| ERR13 | web/app.py:1285-1291 | exibida |  |
| ERR14 | templates/redefinir_senha.html:24-35 | exibida |  |
| ERR15 | templates/redefinir_senha.html:24-35 | exibida |  |
| ERR16 | web/app.py:1360-1361 | exibida |  |
| ERR17 | web/app.py:1468-1473 | PROVAVELMENTE NÃO EXIBIDA | exigência desligada por padrão (config.py:63). Redireciona para /projetos?error=...; projects/list.html não lê msg/error |
| ERR18 | web/app.py:1474-1481 (teto em app.py:65) | PROVAVELMENTE NÃO EXIBIDA | redireciona para /projetos?error=...; projects/list.html não lê msg/error. Conta só projetos ainda parados na prévia |
| ERR19 | web/app.py:1492-1501 (teto em app.py:82) | PROVAVELMENTE NÃO EXIBIDA | mesmo caso de ERR18 |
| ERR20 | web/app.py:1506-1515 (teto em app.py:78) | PROVAVELMENTE NÃO EXIBIDA | mesmo caso de ERR18 |
| ERR21 | web/app.py:1545-1549, 1858-1865, 1901-1908; tarja em components/aviso_de_erro.html | exibida (detail.html:303-315) | botão Comprar só aparece se a venda estiver ligada |
| ERR22 | pipeline.py:563-565 e 2404-2405; exibido em detail.html:327-331 | exibida | mesmo texto do saldo do estudante (ERR21) para uma causa diferente |
| ERR23 | pipeline.py:2406-2407 | exibida | nome da exceção Python (ex.: TimeoutError) |
| ERR24 | pipeline.py:1418-1421 -> 566-568 | exibida | texto cru da exceção |
| ERR25 | pipeline.py:566-568 (str(e)) | exibida | texto cru da exceção |
| ERR26 | pipeline.py:187 e 2390 | exibida | improvável para o estudante |
| ERR27 | web/app.py:1959-1960 | exibida | texto cru da exceção na URL |
| ERR28 | pipeline.py:2140-2147; exibido em detail.html:714-716 | exibida | linha com X vermelho no painel |
| ERR29 | pipeline.py:2171-2174 (_job_fail) | exibida | nome da exceção Python + mensagem crua |
| ERR30 | pipeline.py:1011 | exibida |  |
| ERR31 | templates/errors/404.html; app.py:848, 1017-1025, 2033 | exibida |  |
| ERR32 | templates/errors/403.html; app.py:736, 817 | exibida | improvável para conta de estudante (perfil operacional) |
| MSG01 | web/app.py:421-425, 1216-1218 | exibida |  |
| MSG02 | web/app.py:1206-1209 | PROVAVELMENTE NÃO EXIBIDA | o código manda ok=email-ja-confirmado+Pode+entrar..., que não bate com a chave do dicionário (app.py:422): a caixa não aparece |
| MSG03 | web/app.py:424, 1374-1375 | exibida |  |
| MSG04 | templates/esqueci_senha.html:28-34 | exibida |  |
| MSG05 | templates/esqueci_senha.html:35-40 | exibida | MSG04 ou MSG05: só uma das duas existe em produção |
| MSG06 | web/app.py:1237-1239 | PROVAVELMENTE NÃO EXIBIDA | dashboard.html não lê msg da URL |
| MSG07 | web/app.py:1251-1254 | PROVAVELMENTE NÃO EXIBIDA | dashboard.html não lê msg da URL |
| MSG08 | templates/app_layout.html:103-116 | exibida | só com envio de e-mail ligado. "voce" sem acento |
| MSG09 | templates/app_layout.html:188-204 | exibida |  |
| MSG10 | templates/projects/new.html:5 | exibida |  |
| MSG11 | templates/projects/new.html:227 | exibida |  |
| MSG12 | templates/projects/new.html:212-219 | exibida | não menciona o limite diário de 20 prévias |
| MSG13 | templates/projects/new.html:220-224; detail.html:123-127, 164-168 | exibida |  |
| MSG14 | templates/app_layout.html:36-57 | exibida |  |
| MSG15 | templates/projects/new.html:105-122 | exibida |  |
| MSG16 | templates/projects/new.html:186-199 | exibida |  |
| MSG17 | templates/projects/new.html:200; components/pipeline_banner.html:70 | exibida | o pipeline roda no servidor (pipeline.py:2437-2455, schedule_pipeline); pelo código, fechar a aba não interrompe |
| MSG18 | web/app.py:1733 | PROVAVELMENTE NÃO EXIBIDA | redireciona para /projetos?msg=...; projects/list.html não lê msg |
| MSG19 | templates/projects/detail.html:262-294 | exibida |  |
| MSG20 | web/app.py:1539-1542; detail.html:297-302 | exibida | some sozinha depois de 8 segundos |
| MSG21 | templates/projects/detail.html:591-604 | exibida | a tela do projeto não tem formulário para editar os critérios (a rota POST /criterios existe, app.py:1962, mas nenhum template a chama) |
| MSG22 | templates/projects/detail.html:151-154 | exibida | caixa nativa do navegador (confirm) |
| MSG23 | web/app.py:1554-1557, 1911-1915 | PROVAVELMENTE NÃO EXIBIDA | detail.html:297 só mostra msg com status draft/discovering; aqui o status já é searching |
| MSG24 | web/app.py:1868-1871 | exibida | status discovering |
| MSG25 | web/app.py:1848-1852 | exibida |  |
| MSG26 | web/app.py:1878-1882, 1890-1894 | PROVAVELMENTE NÃO EXIBIDA | status searching/analyzing |
| MSG27 | templates/projects/detail.html:179-224 | exibida | não diz que o crédito da rodada se perde: parar zera rodada_paga (app.py:1946-1954) e reiniciar cobra outro crédito |
| MSG28 | templates/projects/detail.html:225-254 | exibida | o projeto volta a criteria_ready e pode ser reiniciado (app.py:1953) |
| MSG29 | web/app.py:1955-1958 | PROVAVELMENTE NÃO EXIBIDA | status vira criteria_ready; detail.html:297 só mostra msg em draft/discovering. E não há tela de edição dos critérios |
| MSG30 | web/app.py:1927-1931 | só se o projeto estiver em rascunho |  |
| MSG31 | templates/components/pipeline_banner.html:24-45 | exibida |  |
| MSG32 | templates/components/pipeline_banner.html:50-69 | exibida | não há notificação de fim no código (nenhum e-mail ou aviso ao terminar; só recarrega a página se a aba estiver aberta) |
| MSG33 | pipeline_banner.html:57-61; web/progresso.py | exibida |  |
| MSG34 | pipeline_banner.html:62-66 | exibida |  |
| MSG35 | templates/components/pipeline_banner.html:96-250 (window.__livePhrases) | exibida | texto fixo no navegador; não reflete o que o servidor está fazendo |
| MSG36 | templates/components/pipeline_banner.html:96-250 (window.__livePhrases) | exibida | texto fixo no navegador; não reflete o que o servidor está fazendo |
| MSG37 | templates/components/pipeline_banner.html:96-250 (window.__livePhrases) | exibida | texto fixo no navegador; não reflete o que o servidor está fazendo |
| MSG38 | templates/components/pipeline_banner.html:96-250 (window.__livePhrases) | exibida | texto fixo no navegador; não reflete o que o servidor está fazendo |
| MSG39 | templates/components/pipeline_banner.html:96-250 (window.__livePhrases) | exibida | texto fixo no navegador; não reflete o que o servidor está fazendo |
| MSG40 | templates/components/pipeline_banner.html:96-250 (window.__livePhrases) | exibida | texto fixo no navegador; não reflete o que o servidor está fazendo |
| MSG41 | templates/components/pipeline_banner.html:96-250 (window.__livePhrases) | exibida | texto fixo no navegador; não reflete o que o servidor está fazendo |
| MSG42 | templates/components/pipeline_banner.html:96-250 (window.__livePhrases) | exibida | texto fixo no navegador; não reflete o que o servidor está fazendo |
| MSG43 | templates/components/pipeline_banner.html:96-250 (window.__livePhrases) | exibida | texto fixo no navegador; não reflete o que o servidor está fazendo |
| MSG44 | pipeline.py:718-728; exibido em detail.html:714-716 (job.message \|\| job.error) | exibida |  |
| MSG45 | pipeline.py:695-702; exibido em detail.html:714-716 (job.message \|\| job.error) | exibida |  |
| MSG46 | pipeline.py:804; exibido em detail.html:714-716 (job.message \|\| job.error) | exibida |  |
| MSG47 | pipeline.py:833; exibido em detail.html:714-716 (job.message \|\| job.error) | exibida |  |
| MSG48 | pipeline.py:871-877; exibido em detail.html:714-716 (job.message \|\| job.error) | exibida |  |
| MSG49 | pipeline.py:969; exibido em detail.html:714-716 (job.message \|\| job.error) | exibida |  |
| MSG50 | pipeline.py:1009; exibido em detail.html:714-716 (job.message \|\| job.error) | exibida |  |
| MSG51 | pipeline.py:1015-1016; exibido em detail.html:714-716 (job.message \|\| job.error) | exibida |  |
| MSG52 | pipeline.py:1316; exibido em detail.html:714-716 (job.message \|\| job.error) | exibida |  |
| MSG53 | pipeline.py:1339; exibido em detail.html:714-716 (job.message \|\| job.error) | exibida |  |
| MSG54 | pipeline.py:1347; exibido em detail.html:714-716 (job.message \|\| job.error) | exibida |  |
| MSG55 | pipeline.py:1404, 1497; exibido em detail.html:714-716 (job.message \|\| job.error) | exibida |  |
| MSG56 | pipeline.py:1423-1427; exibido em detail.html:714-716 (job.message \|\| job.error) | exibida |  |
| MSG57 | pipeline.py:1453; exibido em detail.html:714-716 (job.message \|\| job.error) | exibida |  |
| MSG58 | pipeline.py:1522; exibido em detail.html:714-716 (job.message \|\| job.error) | exibida |  |
| MSG59 | pipeline.py:1572; exibido em detail.html:714-716 (job.message \|\| job.error) | exibida |  |
| MSG60 | pipeline.py:1734; exibido em detail.html:714-716 (job.message \|\| job.error) | exibida |  |
| MSG61 | pipeline.py:1743-1747; exibido em detail.html:714-716 (job.message \|\| job.error) | exibida |  |
| MSG62 | pipeline.py:1814-1816; exibido em detail.html:714-716 (job.message \|\| job.error) | exibida |  |
| MSG63 | pipeline.py:1897; exibido em detail.html:714-716 (job.message \|\| job.error) | exibida |  |
| MSG64 | pipeline.py:2129-2131; exibido em detail.html:714-716 (job.message \|\| job.error) | exibida | lista JSON crua exibida como texto quando a verificação final passa |
| MSG65 | web/app.py:1941; pipeline.py:558; exibido em detail.html:714-716 (job.message \|\| job.error) | exibida |  |
| MSG66 | pipeline.py:2178; exibido em detail.html:714-716 (job.message \|\| job.error) | exibida |  |
| MSG67 | templates/projects/detail.html:730-732; exibido em detail.html:714-716 (job.message \|\| job.error) | exibida |  |
| MSG68 | templates/projects/detail.html:794-796; exibido em detail.html:714-716 (job.message \|\| job.error) | exibida |  |
| MSG69 | templates/projects/detail.html:497-503 | exibida |  |
| MSG70 | templates/projects/detail.html:499-500 | exibida |  |
| MSG71 | templates/projects/detail.html:505-515 | exibida |  |
| MSG72 | templates/projects/detail.html:516-519 | exibida |  |
| MSG73 | templates/projects/detail.html:520-522 | exibida |  |
| MSG74 | templates/projects/detail.html:524-534 | exibida |  |
| MSG75 | templates/projects/detail.html:535-538 | exibida |  |
| MSG76 | templates/projects/detail.html:539-541 | exibida |  |
| MSG77 | templates/projects/detail.html:563-569 | exibida |  |
| MSG78 | templates/records/list.html:289 | exibida |  |
| MSG79 | templates/records/detail.html:72-76 | exibida |  |
| MSG80 | templates/favorites/index.html:47-58 | exibida |  |
| MSG81 | templates/favorites/project.html:63-67 | exibida |  |
| MSG82 | templates/projects/list.html:68-83 | exibida |  |
| MSG83 | templates/dashboard.html:134-147 | exibida |  |
| NAV01 | - | navegador | validação nativa do navegador (atributo required) |
