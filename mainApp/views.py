from django.shortcuts import render
from .models import Topico

def index(request): # parametro padrão, indicando uma requisição da página
    return render(request, 'mainApp/index.html') # retorna a página renderizada, não precisa especificar a pasta templates

def topicos(request):
    topicos = Topico.objects.order_by('date_added')
    context = {'topicos': topicos}
    return render(request, 'mainApp/topicos.html', context)

def topico(request, id_topico):
    topicoEsp = Topico.objects.get(id=id_topico)
    notes = topicoEsp.note_set.order_by('-date_added')
    context = {'topico': topicoEsp, 'notes': notes}
    return render(request, 'mainApp/topico.html', context)