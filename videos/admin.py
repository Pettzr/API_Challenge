from django.contrib import admin
from videos.models import InfoVideos

# Register your models here.

class ListandoVideos(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'url')

admin.site.register(InfoVideos, ListandoVideos)
