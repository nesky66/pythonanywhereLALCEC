from django.contrib import admin

# Register your models here.
from apps.contacto.models import Comentarios

class AdminComentarios(admin.ModelAdmin):
    list_display =   ('id','nombre','domicilio','telefono','comentario','created','updated')

admin.site.register(Comentarios,AdminComentarios)