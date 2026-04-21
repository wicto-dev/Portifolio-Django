from django.shortcuts import render,redirect
from core.models import Pessoal
from .models import Certificado,Projeto

def home(request):
    pessoal = Pessoal.objects.first()
    certificados = Certificado.objects.all()
    return render(request,'portfolio/home.html',{'pessoal':pessoal,'certificados':certificados})

def projetos(request):
    projetos = Projeto.objects.all()
    return render(request,'portfolio/projetos.html',{'projetos':projetos})

def contatos(request):
    pessoal = Pessoal.objects.first()
    return render(request,'portfolio/contatos.html',{'pessoal':pessoal})
