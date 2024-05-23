from django.contrib import admin
from soloFlix.models import Videos, Categoria

class Video(admin.ModelAdmin):
    list_display = ('id', 'categoria', 'titulo', 'descricao', 'url')
    list_display_links = ('id', 'titulo', 'categoria')
    search_fields = ('titulo', 'categoria')
    list_per_page = 10

admin.site.register(Videos, Video)

class Categorias(admin.ModelAdmin):
    list_display = ('id','titulo', 'cor')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_per_page = 10

admin.site.register(Categoria, Categorias)
