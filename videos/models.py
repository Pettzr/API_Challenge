from django.db import models

class Video (models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False,blank=False)
    url = models.CharField(max_length=100, null=False, blank=False)
    categoriaId = models.CharField(max_length=4, default='1', null=False, blank=False)

class CategoriaVideo (models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    cor = models.CharField(max_length=12, null=False, blank=False)

