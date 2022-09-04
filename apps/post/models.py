
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
# from django.utils import timezone
from django.conf import settings


# Create your models here.
class Date(models.Model):
    created = models.DateTimeField(auto_now_add=True,null=True,blank=False)
    updated = models.DateTimeField(auto_now=True,null=True,blank=False)
    
    class Meta:
        abstract = True

class Categoria(Date):
    categoria = models.CharField(max_length=30, blank=False,null=True)
    
    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
     
    def __str__(self):
        return self.categoria

class Post(Date):
    titulo = models.CharField(max_length=200, blank=False, null=True)
    introduccion = models.CharField(max_length=200, blank=False, null=True)
    contenido = models.TextField(null=True)
    imagen = models.ImageField(upload_to='post/',max_length=200, null=True,blank=True)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,blank=False,null=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'
    
    def __str__(self):
        return self.titulo
    
