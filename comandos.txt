# Comandos Importantes do Django

## COMANDOS NECESSÁRIOS PARA CRIAÇÃO DE PROJETO DJANGO

python -m venv nome -> criação de ambiente virtual

nome\Scripts\activate -> ativa o ambiente virtual especificado no terminal do Windows

deactivate -> sai do ambiente virtual

pip install Django==VERSÃO -> instala uma versão específica do Django

django-admin --version -> verifica a versão

django-admin startproject nome . -> cria um projeto

code . -> abre o projeto no VSCode

## COMANDOS IMPORTANTES PARA O DESENVOLVIMENTO

python manage.py makemigrations nome -> cria um arquivo com o que deve ser alterado no banco de dados

python manage.py migrate -> realiza as alterações presentes no arquivo criado no banco de dados real

python manage.py runserver -> cria uma URL para acessar a página incial do projeto

python manage.py startapp nome -> cria um novo app no projeto

python manage.py createsuperuser -> cria os dados do admin

## COMANDOS PARA O MODELS

class Tabela(Model.models) -> cria uma tabela

### DENTRO DA CLASS	

campo = models.CharField(max_length=x) -> campo do BD do tipo varchar
campo = models.TextField() -> campo do BD do tipo string longa
campo = models.IntegerField() -> campo do BD do tipo num inteiro
campo = models.FloatField() -> campo do BD do tipo decimal
campo = models.DecimalField(max_digits=x, decimal_places=y) -> campo do BD do tipo decimal, com especificação do total de digitos e do total de digitos após a virgula
campo = models.BooleanField() -> campo do BD do tipo true ou false
campo = models.DateField() -> campo do BD do tipo data
campo = models.DatetTmeField() -> campo do BD do tipo data + horas, caso queira preencher com o datetime do momento da adição de algo no BD, basta passar como parametro "auto_now_add=True"
campo = models.EmailField() -> campo do BD do tipo email
campo = models.URLField() -> campo do BD dque armazena uma URL
campo = models.FileField(upload_to='documentos/') -> campo do BD que armazena o link de um arquivo, deve ser especificado o diretorio
campo = models.ImageField(upload_to='documentos/') -> campo do BD que armazena o link de uma imagem, deve ser especificado o diretorio
campo = models.ForeignKey(Modelo, on_delete=models.CASCADE/NULL/PROTECT/etc) -> define o id de uma instância de outra tabela como chave estrangeira, definindo, em caso de exclusão da instância, o que fazer com os objetos da tabela filha.

### COMANDOS PARA MANIPULAÇÃO DOS MODELOS

Modelo.objects.all() -> retorna uma lista com todas as instâncias do modelo
Modelo.objects.get(id=valor) -> retorna um objeto especifico
Objeto.modeloFilho_set.all() -> retorna uma lista com os objetos de uma tabela filha do objeto em questão(relação de chave estrangeira)

## COMANDOS PYTHON DENTRO DO HTML

{% %} -> estrutura para escrever comandos do django no html

{% extends 'dir/base.html' %} -> herda as características fixas de uma página base, diminuindo a repetição de codigo

{% block content %} {% endblock content} -> define o espaço que vai ser diferente entre as páginas, o código efetivamente deve ser escrito nesse bloco

{% url 'nome' %} -> pega o link de uma página com base no nome dela(atributo name='' do path) 

{% load static %} -> carrega a pasta de arquivos estáticos(css, imagens, etc)

{% static 'dir/arquivo.css ou arquivo.png' %} -> carrega o css ou a imagem dentro da pasta do diretório static
