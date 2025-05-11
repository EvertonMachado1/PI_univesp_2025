from agenda import urls
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from core.models import agendamento_de_aula,Matricula
from datetime import time
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


#render tela inicial
@login_required
def tela_principal(request):
    dias_da_semana = [2, 3, 4, 5, 6, 7]  # Seg a Sáb
    horarios = range(8, 18)  # Das 08h às 17h

    agendamentos = {} # Dicionario vazio pra guardar os agendamentos organizados por horario

    for hora in horarios:
        hora_inicio = time(hora, 0)
        hora_fim = time(hora + 1, 0)
        linha = []

        for dia in dias_da_semana:
            agendamento = agendamento_de_aula.objects.filter(
                data_agendamento__week_day=dia,
                hora__gte=hora_inicio,
                hora__lt=hora_fim
            ).first()
            linha.append(agendamento)

        agendamentos[f"{hora:02d}:00"] = linha

    return render(request, 'tela_principal.html', {'agendamentos': agendamentos})

def matriculasubmit(request) :
    if request.POST:
      nome_completo = request.POST.get('nome_completo')
      idade  = request.POST.get('idade')
      instrumento = request.POST.get('instrumento')
      email = request.POST.get('email')
      telefone= request.POST.get('telefone')
      observacao =  request.POST.get('observacoes')
      instrutor = request.user
      Matricula.objects.create(nome_completo= nome_completo ,idade = idade ,instrumento = instrumento, email = email, telefone = telefone,observacao = observacao, instrutor = instrutor)
    return redirect('tela_principal')

def tela_login(request):
   if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tela_principal')
        else:
            messages.error(request, 'Usuário ou senha incorretos!')
   return render(request, 'tela_login.html')

def sair(request):
    logout(request)
    return redirect('tela_login')