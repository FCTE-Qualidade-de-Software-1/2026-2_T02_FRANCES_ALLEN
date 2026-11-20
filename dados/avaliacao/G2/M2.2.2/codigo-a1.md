# M2.2.2: caminhos no código (só A1)

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
| NAV01 | - | navegador | validação nativa do navegador (atributo required) |
