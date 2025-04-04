from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# tela de login
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tela_inicial')
        else:
            return render(request, 'index.html', {'error': 'Usuário ou senha inválidos'})

    return render(request, 'index.html')

# redirect do login
@login_required
def tela_inicial(request):
    return render(request, 'tela_inicial.html')