from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Paciente

# Create your views here.
@login_required
def index(request):
    return render(request, "index.html")

@login_required
def novo_paciente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        data_nascimento = request.POST.get('data_nascimento')
        sintomas = request.POST.get('sintomas')

        Paciente.objects.create(
            nome=nome,
            cpf=cpf,
            data_nascimento=data_nascimento,
            sintomas=sintomas
        )
        return redirect('index')
    return render(request, 'novo_paciente.html')