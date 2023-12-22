from django.contrib import admin
from videos.models import Video, CategoriaVideo

# Register your models here.

class ListandoVideos(admin.ModelAdmin):
   list_display = ('id', 'titulo', 'descricao', 'url')

class ListandoCategorias(admin.ModelAdmin):
   list_display = ('id', 'titulo', 'cor')

admin.site.register(Video, ListandoVideos)
admin.site.register(CategoriaVideo, ListandoCategorias)
