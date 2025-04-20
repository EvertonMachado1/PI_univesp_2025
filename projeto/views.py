from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from projeto.forms import CadastroUsuarioForm


# Tela de login
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tela_principal')
        else:
            return render(request, 'index.html', {'error': 'Usuário ou senha inválidos'})
    return render(request, 'index.html')

# Tela de cadastro de usuário
def cadastro_usuario(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redireciona para a tela de login após o cadastro
    else:
        form = CadastroUsuarioForm()
    return render(request, 'cadastro_usuario.html', {'form': form})

# tela principal
def tela_principal(request):
    return render(request, 'tela_principal.html')