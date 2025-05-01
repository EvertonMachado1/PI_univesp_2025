from agenda import urls
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from core.models import agendamento_de_aula,Matricula
from datetime import time


#render tela inicial
@login_required
def tela_principal(request):
    #08am - 09am
    agendamento_8h = agendamento_de_aula.objects.filter(
        hora__gte=time(8, 0),
        hora__lt=time(9, 0)
    ).first()  # Pega apenas o primeiro, se houver

    #09am - 10am
    agendamento_9h = agendamento_de_aula.objects.filter(
        hora__gte=time(9, 0),
        hora__lt=time(10, 0)
    ).first()  # Pega apenas o primeiro, se houver

        #010am - 11am
    agendamento_10h = agendamento_de_aula.objects.filter(
        hora__gte=time(10, 0),
        hora__lt=time(11, 0)
    ).first()  # Pega apenas o primeiro, se houver

        #11am - 12pm
    agendamento_11h = agendamento_de_aula.objects.filter(
        hora__gte=time(11, 0),
        hora__lt=time(12, 0)
    ).first()  # Pega apenas o primeiro, se houver

        #12pm - 13pm
    agendamento_12h = agendamento_de_aula.objects.filter(
        hora__gte=time(12, 0),
        hora__lt=time(13, 0)
    ).first()  # Pega apenas o primeiro, se houver

        #13pm - 14pm
    agendamento_13h = agendamento_de_aula.objects.filter(
        hora__gte=time(13, 0),
        hora__lt=time(14, 0)
    ).first()  # Pega apenas o primeiro, se houver

        #14pm - 15pm
    agendamento_14h = agendamento_de_aula.objects.filter(
        hora__gte=time(14, 0),
        hora__lt=time(15, 0)
    ).first()  # Pega apenas o primeiro, se houver

        #15pm - 16pm
    agendamento_15h = agendamento_de_aula.objects.filter(
        hora__gte=time(15, 0),
        hora__lt=time(16, 0)
    ).first()  # Pega apenas o primeiro, se houver

        #16pm - 17pm
    agendamento_16h = agendamento_de_aula.objects.filter(
        hora__gte=time(16, 0),
        hora__lt=time(17, 0)
    ).first()  # Pega apenas o primeiro, se houver
    
        #17pm - 18pm
    agendamento_17h = agendamento_de_aula.objects.filter(
        hora__gte=time(17, 0),
        hora__lt=time(18, 0)
    ).first()  # Pega apenas o primeiro, se houver

    return render(request, 'tela_principal.html', {
        'agendamento_8h': agendamento_8h, 'agendamento_9h': agendamento_9h,
        'agendamento_10h': agendamento_10h,'agendamento_11h': agendamento_11h,
        'agendamento_12h': agendamento_12h,'agendamento_13h': agendamento_13h,
        'agendamento_14h': agendamento_14h,'agendamento_15h': agendamento_15h,
        'agendamento_16h': agendamento_16h,'agendamento_17h': agendamento_17h,
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