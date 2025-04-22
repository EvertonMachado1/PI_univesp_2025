from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from projeto.forms import CadastroUsuarioForm
from django.http import JsonResponse
from .models import AulaAgendada, Sala, Instrumento


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

# agendamento
def agendar_aula(request):
    if request.method == 'POST':
        ano = request.POST.get('ano')
        mes = request.POST.get('mes')
        dia = request.POST.get('dia')
        hora = request.POST.get('hora')
        sala_id = request.POST.get('sala')
        instrumento_id = request.POST.get('instrumento')
        
        # Recuperando a sala e o instrumento pelo ID
        sala = Sala.objects.get(id=sala_id)
        instrumento = Instrumento.objects.get(id=instrumento_id)
        
        # Criando o agendamento
        aula_agendada = AulaAgendada.objects.create(
            ano=ano, mes=mes, dia=dia, hora=hora, sala=sala, instrumento=instrumento
        )
        
        return JsonResponse({'status': 'sucesso', 'message': 'Aula agendada com sucesso!'})
    
    return JsonResponse({'status': 'erro', 'message': 'Método não permitido'})