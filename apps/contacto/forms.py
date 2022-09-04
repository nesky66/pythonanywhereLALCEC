
from .models import Comentarios
from django import forms

class FormContacto(forms.ModelForm):
   
    class Meta:#Le decimos que modelo utilizar para crear formulario
        model = Comentarios
        fields = ('nombre', 'telefono','domicilio','comentario')