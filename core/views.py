from agenda import urls
from django.shortcuts import render


#render tela inicial
def tela_principal(request):
    return render(request, 'tela_principal.html')