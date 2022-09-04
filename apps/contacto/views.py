from django.shortcuts import render, redirect,get_object_or_404

from django.conf import settings
from django.contrib import messages

# Create your views here.
from .forms import FormContacto
from .models import Comentarios

def contacto(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        miFormulario = FormContacto(request.POST)
        # check whether it's valid:
        if miFormulario.is_valid():
            # process the data in form.cleaned_data as required
            miFormulario.save()
            return redirect('contacto')
            # infoFormulario = miFormulario.cleaned_data
            # send_mail(infoFormulario['asunto'],infoFormulario['mensaje'],infoFormulario.get('email',''),['nesky66@gmail.com'],)
            
            # redirect to a new URL:
        
        else:
            pass
            # for msg in miFormulario.error_messages:
            #     messages.error(request,  miFormulario.error_messages[msg])
        

    # if a GET (or any other method) we'll create a blank form
    else:
       
        miFormulario = FormContacto()

    return render(request, 'contacto.html', {'form': miFormulario})

def comentarios(request):
    if request.method=='POST':
        if request.POST:
            id = request.POST.getlist('eliminar')
            for x in id:
                c = Comentarios.objects.get(id=x)
                c.delete()
            
            return redirect('comentarios')
    
    com = Comentarios.objects.all()
    comen = {}
    for x in com:
        comen[x.id]=x
   
    return render(request, 'comentarios.html', {'comentarios':comen})