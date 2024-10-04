# Aplicativo de Segurança com Sistema de Login e Inventário

## Acesse o aplicativo
Para utilizar o aplicativo, entre na seguinte URL:  
[http://localhost:5000/login/](http://localhost:5000/login/)

---

## Estrutura do Projeto

- **Pasta `templates`:** Contém os arquivos HTML utilizados no projeto.
- **Pasta `static`:** Contém o arquivo JavaScript do framework `cru.js`.
- **Pasta `styles`:** Contém os arquivos CSS responsáveis pelo estilo visual.
- **Pasta `database`:** Contém o arquivo `contas.py`, onde estão definidos os logins de acesso.

---

## Executando o Aplicativo

O aplicativo deve ser executado utilizando o arquivo `server.py`. Para iniciar o servidor local, execute o seguinte comando no terminal:
python server.py

## Rotas do Flask
As rotas do aplicativo estão localizadas na pasta routes.

## Linguagens Utilizadas
Python
JavaScript
HTML/CSS
Framework Flask (Python)
Observação
Antes de utilizar o aplicativo, acesse o arquivo contas.py na pasta database, onde estão definidos os logins de acesso:

## python

[{"login": "adm", "senha": "senha", "tipo": "administrador"},
 {"login": "funcionario", "senha": "senha", "tipo": "funcionario"},
 {"login": "gerente", "senha": "senha", "tipo": "gerente"}]


## Créditos
Este projeto foi desenvolvido como parte do projeto de conclusão de curso da Infinity School. Agradecimentos ao canal do YouTube Programador Python pelo suporte e tutoriais.

