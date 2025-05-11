from agenda import urls
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from core.models import agendamento_de_aula,Matricula
from datetime import time
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


#render tela inicial
@login_required
def tela_principal(request):  # função que renderiza a tela
    dias_da_semana = [2, 3, 4, 5, 6, 7]  # lista de dias de seg a sab
    horarios = range(8, 18)  # cria um intervalo de horas (das 8 as 17h)

    agendamentos = {}  # cria dicionário que vai armazenar os agendamentos

    for hora in horarios:  # loop pra cada hora
        hora_inicio = time(hora, 0)  # define o começo da aula (ex: 8h00)
        hora_fim = time(hora + 1, 0)  # define o fim da aula (ex: 9h00)
        linha = []  # lista que vai armazenar os agendamentos daquela hora

        for dia in dias_da_semana:  # loop para cada dia
            agendamento = agendamento_de_aula.objects.filter(  # busca agendamentos na hora e dia especificado
                data_agendamento__week_day=dia,  # filtra pelo dia da semana
                hora__gte=hora_inicio,  # verifica se o horário da aula é maior ou igual ao 'hora_inicio'
                hora__lt=hora_fim  # verifica se o horário da aula é menor que o 'hora_fim'
            ).first()  # pega o primeiro agendamento que corresponde aos critérios

            linha.append(agendamento)  # adiciona o agendamento encontrado à linha

        agendamentos[f"{hora:02d}:00"] = linha  # adiciona a linha (agendamentos daquela hora) no dicionário

    return render(request, 'tela_principal.html', {'agendamentos': agendamentos})  # renderiza a pagina passando os agendamentos encontrados


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