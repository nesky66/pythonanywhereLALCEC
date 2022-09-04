from django.db import models

# Create your models here.
class Date(models.Model):
    created = models.DateTimeField(auto_now_add=True,null=True,blank=False)
    updated = models.DateTimeField(auto_now=True,null=True,blank=False)
    
    class Meta:
        abstract = True
        
class Comentarios(Date):
    nombre = models.CharField(max_length=100, blank=False, null=True)
    domicilio = models.CharField(max_length=100,blank=True,default='')
    telefono = models.CharField(max_length=100,blank=True,default='')
    comentario = models.TextField(max_length=100,blank=False,null=True)