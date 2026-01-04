from django.shortcuts import render
from .models import Funcionario

def lista_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'lista.html', {'funcionarios': funcionarios})
