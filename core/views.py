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
    #08am - 09am
    ag_8h_seg = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=2, # Segunda-feira
        hora__gte=time(8, 0),
        hora__lt=time(9, 0)
    ).first()  # Pega apenas o primeiro, se houver

    ag_8h_ter = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=3, # Terça-feira
        hora__gte=time(8, 0),
        hora__lt=time(9, 0)
    ).first()  # Pega apenas o primeiro, se houver

    ag_8h_qua = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=4, # Quarta-feira
        hora__gte=time(8, 0),
        hora__lt=time(9, 0)
    ).first()

    ag_8h_qui = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=5, # Quinta-feira
        hora__gte=time(8, 0),
        hora__lt=time(9, 0)
    ).first()

    ag_8h_sex = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=6, # Sexta-feira
        hora__gte=time(8, 0),
        hora__lt=time(9, 0)
    ).first()

    ag_8h_sab = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=7, # Sábado-feira
        hora__gte=time(8, 0),
        hora__lt=time(9, 0)
    ).first()

    #09am - 10am
    ag_9h_seg = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=2, # Segunda-feira
        hora__gte=time(9, 0),
        hora__lt=time(10, 0)
    ).first()  # Pega apenas o primeiro, se houver

    ag_9h_ter = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=3, # Terça-feira
        hora__gte=time(9, 0),
        hora__lt=time(10, 0)
    ).first()  # Pega apenas o primeiro, se houver

    ag_9h_qua = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=4, # Quarta-feira
        hora__gte=time(9, 0),
        hora__lt=time(10, 0)
    ).first()

    ag_9h_qui = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=5, # Quinta-feira
        hora__gte=time(9, 0),
        hora__lt=time(10, 0)
    ).first()

    ag_9h_sex = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=6, # Sexta-feira
        hora__gte=time(9, 0),
        hora__lt=time(10, 0)
    ).first()

    ag_9h_sab = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=7, # Sábado-feira
        hora__gte=time(9, 0),
        hora__lt=time(10, 0)
    ).first()

    #010am - 11am
    ag_10h_seg = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=2, # Segunda-feira
        hora__gte=time(9, 0),
        hora__lt=time(10, 0)
    ).first()  # Pega apenas o primeiro, se houver

    ag_10h_ter = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=3, # Terça-feira
        hora__gte=time(9, 0),
        hora__lt=time(10, 0)
    ).first()  # Pega apenas o primeiro, se houver

    ag_10h_qua = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=4, # Quarta-feira
        hora__gte=time(9, 0),
        hora__lt=time(10, 0)
    ).first()

    ag_10h_qui = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=5, # Quinta-feira
        hora__gte=time(9, 0),
        hora__lt=time(10, 0)
    ).first()

    ag_10h_sex = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=6, # Sexta-feira
        hora__gte=time(9, 0),
        hora__lt=time(10, 0)
    ).first()

    ag_10h_sab = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=7, # Sábado-feira
        hora__gte=time(9, 0),
        hora__lt=time(10, 0)
    ).first()

    #11am - 12pm
    ag_11h_seg = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=2, # Segunda-feira
        hora__gte=time(10, 0),
        hora__lt=time(11, 0)
    ).first()  # Pega apenas o primeiro, se houver

    ag_11h_ter = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=3, # Terça-feira
        hora__gte=time(10, 0),
        hora__lt=time(11, 0)
    ).first()  # Pega apenas o primeiro, se houver

    ag_11h_qua = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=4, # Quarta-feira
        hora__gte=time(10, 0),
        hora__lt=time(11, 0)
    ).first()

    ag_11h_qui = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=5, # Quinta-feira
        hora__gte=time(10, 0),
        hora__lt=time(11, 0)
    ).first()

    ag_11h_sex = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=6, # Sexta-feira
        hora__gte=time(10, 0),
        hora__lt=time(11, 0)
    ).first()

    ag_11h_sab = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=7, # Sábado-feira
        hora__gte=time(10, 0),
        hora__lt=time(11, 0)
    ).first()

    #12pm - 13pm
    ag_12h_seg = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=2, # Segunda-feira
        hora__gte=time(11, 0),
        hora__lt=time(12, 0)
    ).first()  # Pega apenas o primeiro, se houver

    ag_12h_ter = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=3, # Terça-feira
        hora__gte=time(11, 0),
        hora__lt=time(12, 0)
    ).first()  # Pega apenas o primeiro, se houver

    ag_12h_qua = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=4, # Quarta-feira
        hora__gte=time(11, 0),
        hora__lt=time(12, 0)
    ).first()

    ag_12h_qui = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=5, # Quinta-feira
        hora__gte=time(11, 0),
        hora__lt=time(12, 0)
    ).first()

    ag_12h_sex = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=6, # Sexta-feira
        hora__gte=time(11, 0),
        hora__lt=time(12, 0)
    ).first()

    ag_12h_sab = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=7, # Sábado-feira
        hora__gte=time(11, 0),
        hora__lt=time(12, 0)
    ).first()

    #13pm - 14pm
    ag_13h_seg = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=2, # Segunda-feira
        hora__gte=time(12, 0),
        hora__lt=time(13, 0)
    ).first()  # Pega apenas o primeiro, se houver

    ag_13h_ter = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=3, # Terça-feira
        hora__gte=time(12, 0),
        hora__lt=time(13, 0)
    ).first()  # Pega apenas o primeiro, se houver

    ag_13h_qua = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=4, # Quarta-feira
        hora__gte=time(12, 0),
        hora__lt=time(13, 0)
    ).first()

    ag_13h_qui = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=5, # Quinta-feira
        hora__gte=time(12, 0),
        hora__lt=time(13, 0)
    ).first()

    ag_13h_sex = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=6, # Sexta-feira
        hora__gte=time(12, 0),
        hora__lt=time(13, 0)
    ).first()

    ag_13h_sab = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=7, # Sábado-feira
        hora__gte=time(12, 0),
        hora__lt=time(13, 0)
    ).first()

    #14pm - 15pm
    ag_14h_seg = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=2, # Segunda-feira
        hora__gte=time(13, 0),
        hora__lt=time(14, 0)
    ).first()  # Pega apenas o primeiro, se houver

    ag_14h_ter = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=3, # Terça-feira
        hora__gte=time(13, 0),
        hora__lt=time(14, 0)
    ).first()  # Pega apenas o primeiro, se houver

    ag_14h_qua = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=4, # Quarta-feira
        hora__gte=time(13, 0),
        hora__lt=time(14, 0)
    ).first()

    ag_14h_qui = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=5, # Quinta-feira
        hora__gte=time(13, 0),
        hora__lt=time(14, 0)
    ).first()

    ag_14h_sex = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=6, # Sexta-feira
        hora__gte=time(13, 0),
        hora__lt=time(14, 0)
    ).first()

    ag_14h_sab = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=7, # Sábado-feira
        hora__gte=time(13, 0),
        hora__lt=time(14, 0)
    ).first()

    #15pm - 16pm
    ag_15h_seg = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=2, # Segunda-feira
        hora__gte=time(14, 0),
        hora__lt=time(15, 0)
    ).first()  # Pega apenas o primeiro, se houver

    ag_15h_ter = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=3, # Terça-feira
        hora__gte=time(14, 0),
        hora__lt=time(15, 0)
    ).first()  # Pega apenas o primeiro, se houver

    ag_15h_qua = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=4, # Quarta-feira
        hora__gte=time(14, 0),
        hora__lt=time(15, 0)
    ).first()

    ag_15h_qui = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=5, # Quinta-feira
        hora__gte=time(14, 0),
        hora__lt=time(15, 0)
    ).first()

    ag_15h_sex = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=6, # Sexta-feira
        hora__gte=time(14, 0),
        hora__lt=time(15, 0)
    ).first()

    ag_15h_sab = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=7, # Sábado-feira
        hora__gte=time(14, 0),
        hora__lt=time(15, 0)
    ).first()

    #16pm - 17pm
    ag_16h_seg = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=2, # Segunda-feira
        hora__gte=time(15, 0),
        hora__lt=time(16, 0)
    ).first()  # Pega apenas o primeiro, se houver

    ag_16h_ter = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=3, # Terça-feira
        hora__gte=time(15, 0),
        hora__lt=time(16, 0)
    ).first()  # Pega apenas o primeiro, se houver

    ag_16h_qua = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=4, # Quarta-feira
        hora__gte=time(15, 0),
        hora__lt=time(16, 0)
    ).first()

    ag_16h_qui = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=5, # Quinta-feira
        hora__gte=time(15, 0),
        hora__lt=time(16, 0)
    ).first()

    ag_16h_sex = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=6, # Sexta-feira
        hora__gte=time(15, 0),
        hora__lt=time(16, 0)
    ).first()

    ag_16h_sab = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=7, # Sábado-feira
        hora__gte=time(15, 0),
        hora__lt=time(16, 0)
    ).first()
    
    #17pm - 18pm
    ag_17h_seg = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=2, # Segunda-feira
        hora__gte=time(16, 0),
        hora__lt=time(17, 0)
    ).first()  # Pega apenas o primeiro, se houver

    ag_17h_ter = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=3, # Terça-feira
        hora__gte=time(16, 0),
        hora__lt=time(17, 0)
    ).first()  # Pega apenas o primeiro, se houver

    ag_17h_qua = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=4, # Quarta-feira
        hora__gte=time(16, 0),
        hora__lt=time(17, 0)
    ).first()

    ag_17h_qui = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=5, # Quinta-feira
        hora__gte=time(16, 0),
        hora__lt=time(17, 0)
    ).first()

    ag_17h_sex = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=6, # Sexta-feira
        hora__gte=time(16, 0),
        hora__lt=time(17, 0)
    ).first()

    ag_17h_sab = agendamento_de_aula.objects.filter(
        data_agendamento__week_day=7, # Sábado-feira
        hora__gte=time(16, 0),
        hora__lt=time(17, 0)
    ).first()

    return render(request, 'tela_principal.html', {
        'ag_8h_seg': ag_8h_seg, 'ag_8h_ter': ag_8h_ter,
        'ag_8h_qua': ag_8h_qua, 'ag_8h_qui': ag_8h_qui,
        'ag_8h_sex': ag_8h_sex, 'ag_8h_sab': ag_8h_sab,

        'ag_9h_seg': ag_9h_seg, 'ag_9h_ter': ag_9h_ter,
        'ag_9h_qua': ag_9h_qua, 'ag_9h_qui': ag_9h_qui,
        'ag_9h_sex': ag_9h_sex, 'ag_9h_sab': ag_9h_sab,

        'ag_10h_seg': ag_10h_seg, 'ag_10h_ter': ag_10h_ter,
        'ag_10h_qua': ag_10h_qua, 'ag_10h_qui': ag_10h_qui,
        'ag_10h_sex': ag_10h_sex, 'ag_10h_sab': ag_10h_sab,

        'ag_11h_seg': ag_11h_seg, 'ag_11h_ter': ag_11h_ter,
        'ag_11h_qua': ag_11h_qua, 'ag_11h_qui': ag_11h_qui,
        'ag_11h_sex': ag_11h_sex, 'ag_11h_sab': ag_11h_sab,

        'ag_12h_seg': ag_12h_seg, 'ag_12h_ter': ag_12h_ter,
        'ag_12h_qua': ag_12h_qua, 'ag_12h_qui': ag_12h_qui,
        'ag_12h_sex': ag_12h_sex, 'ag_12h_sab': ag_12h_sab,

        'ag_13h_seg': ag_13h_seg, 'ag_13h_ter': ag_13h_ter,
        'ag_13h_qua': ag_13h_qua, 'ag_13h_qui': ag_13h_qui,
        'ag_13h_sex': ag_13h_sex, 'ag_13h_sab': ag_13h_sab,

        'ag_14h_seg': ag_14h_seg, 'ag_14h_ter': ag_14h_ter,
        'ag_14h_qua': ag_14h_qua, 'ag_14h_qui': ag_14h_qui,
        'ag_14h_sex': ag_14h_sex, 'ag_14h_sab': ag_14h_sab,

        'ag_15h_seg': ag_15h_seg, 'ag_15h_ter': ag_15h_ter,
        'ag_15h_qua': ag_15h_qua, 'ag_15h_qui': ag_15h_qui,
        'ag_15h_sex': ag_15h_sex, 'ag_15h_sab': ag_15h_sab,

        'ag_16h_seg': ag_16h_seg, 'ag_16h_ter': ag_16h_ter,
        'ag_16h_qua': ag_16h_qua, 'ag_16h_qui': ag_16h_qui,
        'ag_16h_sex': ag_16h_sex, 'ag_16h_sab': ag_16h_sab,

        'ag_17h_seg': ag_17h_seg, 'ag_17h_ter': ag_17h_ter,
        'ag_17h_qua': ag_17h_qua, 'ag_17h_qui': ag_17h_qui,
        'ag_17h_sex': ag_17h_sex, 'ag_17h_sab': ag_17h_sab, 
    })

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