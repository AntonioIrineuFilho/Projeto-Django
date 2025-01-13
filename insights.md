# Insights do Django

## ambiente virtual

um espaço reservado para um projeto especifico, de modo a se isolar de configurações de outros projetos

## manage.py

controle de alterações no banco de dados, criação de apps, criação de superuser, roda o servidor, etc

## wsgi.py

especifica/define a configuração de como o servidor web vai se comunicar com o django

## urls.py

define as urls de cada página da aplicação web django

## settings.py

arquivo principal de configuração do projeto, controlando a conexão com o banco de dados, o idioma padrão, o fuso horário, etc

## app

agrupamento de funcionalidades de uma mesma natureza, possuindo models(representação do banco de dados dessa função), view(interação com o banco de dados) e templates(páginas HTML)

um app pode ter várias tabelas, conforme cada class no arquivo models.py

## admin.py

arquivo do painel administrativo, deve-se importar para esse arquivo todos os models para que possam ser visualizados pelo admin na interface

## templates/nome_do_app

pastas necessárias para armazenar as páginas HTML

## ideia geral

templates -> páginas HTML

models -> banco de dados

view -> renderiza as páginas HTML e manipula o banco de dados
