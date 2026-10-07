from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Paciente

# Create your views here.
@login_required
def index(request):
    pacientes = Paciente.objects.all()
    return render(request, "index.html", {'pacientes':pacientes})

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

@login_required
def alterar_dados(request, codigo_paciente):
    paciente = Paciente.objects.get(codigo_paciente=codigo_paciente)

    if request.method == "POST":
        paciente.nome = request.POST.get('nome')
        paciente.cpf = request.POST.get('cpf')
        paciente.data_nascimento = request.POST.get('data_nascimento')
        paciente.sintomas = request.POST.get('sintomas')

        paciente.save()

        return redirect('index')

    return render(request, 'alterar_dados.html', {'paciente':paciente})

@login_required
def deletar_paciente(request, codigo_paciente):
    paciente = Paciente.objects.get(codigo_paciente=codigo_paciente)
    paciente.delete()
    return redirect('index')