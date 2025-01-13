from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # o atributo 'name' é importante para definir o nome da pagina no momento de redirecionar no HTML
    path('topicos', views.topicos, name='topicos'),
    path('topico/<id_topico>', views.topico, name='topico')
]