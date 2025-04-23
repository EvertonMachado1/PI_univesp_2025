from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
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
    horarios = [
        "08:00", "09:00", "10:00", "11:00", "12:00",
        "13:00", "14:00", "15:00", "16:00", "17:00",
        "18:00", "19:00", "20:00"
    ]

    context = {
        'horarios': horarios,
        # da pra adicionar mais dados ao contexto aqui se precisar
    }

    return render(request, 'tela_principal.html', context)

@csrf_exempt
def agendar_aula(request):
    if request.method == 'POST':
        try:
            ano = int(request.POST.get('ano'))
            mes = int(request.POST.get('mes'))
            dia = int(request.POST.get('dia'))
            hora = request.POST.get('hora')
            sala_id = request.POST.get('sala')
            instrumento_id = request.POST.get('instrumento') or None
            professor_id = request.POST.get('professor')
            alunos_ids = request.POST.getlist('alunos')

            sala = Sala.objects.get(id=sala_id)
            instrumento = Instrumento.objects.get(id=instrumento_id) if instrumento_id else None
            professor = User.objects.get(id=professor_id)

            agendamento = AulaAgendada.objects.create(
                ano=ano, mes=mes, dia=dia, hora=hora,
                sala=sala, instrumento=instrumento, professor=professor
            )
            
            for aluno_id in alunos_ids:
                aluno = User.objects.get(id=aluno_id)
                agendamento.alunos.add(aluno)

            return JsonResponse({'status': 'sucesso', 'message': 'Aula agendada com sucesso!'})
        except Exception as e:
            return JsonResponse({'status': 'erro', 'message': str(e)})

    return JsonResponse({'status': 'erro', 'message': 'Método não permitido'})