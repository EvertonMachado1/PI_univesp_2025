from agenda import urls
from django.shortcuts import render


#render tela inicial
def tela_inicial(request):
    return render(request, 'tela_inicial.html')