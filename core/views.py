from agenda import urls
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import agendamento_de_aula


#render tela inicial
@login_required
def tela_principal(request):
    return render(request, 'tela_principal.html', {'agendamentos': agendamento_de_aula})