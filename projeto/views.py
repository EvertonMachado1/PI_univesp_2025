from django.shortcuts import render, redirect
from .forms import CadastroUsuarioForm


# cadastarar usuario

def cadastro_usuario(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # redireciona para login após cadastro
    else:
        form = CadastroUsuarioForm()
    return render(request, 'cadastro.html', {'form': form})

def tela_principal(request):
    return render(request, 'tela_principal.html')

def tabelaagd(request):
    return render(request, 'tabelaagd.html')