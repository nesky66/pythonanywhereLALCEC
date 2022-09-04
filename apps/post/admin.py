from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from .models import Categoria, Post

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('id','titulo','contenido',
                    'activo','created','updated','IMAGEN','usuario')
    
    readonly_fields  = ('created','updated')
    
    search_fields = ('titulo','descripcion')
    
    # list_filter = ('created','usuario_id')
    def IMAGEN(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="width: 100px; \ height: 100px" />',(obj.imagen.url))
        else:
            return ''
    
    

class AdminCategoria(admin.ModelAdmin):
    list_display =   ('id','categoria')
    readonly_fields  = ('created','updated')

# admin.site.register(Post,AdminPost)
admin.site.register(Categoria,AdminCategoria)