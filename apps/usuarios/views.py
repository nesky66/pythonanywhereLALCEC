from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Usuario


# Create your views here.

class RegistroLogin(UserCreationForm):
        class Meta:
            model = Usuario
            fields = UserCreationForm.Meta.fields
    
class VRegistro(LoginRequiredMixin, View):
    
    def get(self, request):
        
        form = RegistroLogin()
        return render(request,'usuarios/registro.html',{'form':form})
    
    def post(self,request):
        form = RegistroLogin(request.POST)
        
        if form.is_valid():
           
            usuario=form.save()
            login(request, usuario)
            return redirect('inicio')
        
        else:
          
            return render(request,'usuarios/registro.html',{'form':form})
        
   