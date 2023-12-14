from django.db import models


class InfoVideos (models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False,blank=False)
    url = models.CharField(max_length=100, null=False, blank=False)

