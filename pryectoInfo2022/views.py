# from http.client import HTTPResponse
from django.shortcuts import render


def inicio(request):
    return render(request,'inicio.html')

def campañas(request):
    return render(request,'campanias.html')

def mision(request):
    return render(request,'mision.html')

def canma(request):
    return render(request,'canma.html')

def canute(request):
    return render(request,'canute.html')

def canpros(request):
    return render(request,'canpros.html')

def canpul(request):
    return render(request,'canpul.html')

def canpiel(request):
    return render(request,'canpiel.html')

def canhab(request):
    return render(request,'canhab.html')

def profesionales(request):
    return render(request,'profesionales.html')
