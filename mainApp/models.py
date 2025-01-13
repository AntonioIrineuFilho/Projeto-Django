from django.db import models

class Topico(models.Model):
    nome_topico = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        # util para representar o modelo em string no painel de controle do Django
        return self.nome_topico

class Note(models.Model):
    descricao = models.TextField()
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE) # id do topico, se o topico for deletado, as anotações também serão
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if (len(self.descricao) > 45):
            return self.descricao[:45] + '...'
        return self.descricao