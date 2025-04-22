from django.contrib.auth.models import User
from django.db import models

# cadastro dos usuarios
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.user.username
    
# salas
class Sala(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True) # pra poder por os instrumentos nas salas

    def __str__(self):
        return self.nome
    

# instrumetos
class Instrumento(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    

# aulas
class Aula(models.Model):
    professor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='aulas_ministradas')
    alunos = models.ManyToManyField(User, blank=True)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    instrumento = models.ForeignKey(Instrumento, on_delete=models.SET_NULL, null=True)
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()

    def __str__(self):
        return f'{self.professor.username} - {self.instrumento.nome if self.instrumento else "Sem instrumento"} - {self.sala.nome} em {self.data} das {self.hora_inicio} às {self.hora_fim}'


# agendamento
class AulaAgendada(models.Model):
    ano = models.IntegerField()
    mes = models.IntegerField()
    dia = models.IntegerField()
    hora = models.CharField(max_length=5)
    
    # relacionamento com as salas
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)

    # relacionamento com os instrumentos
    instrumento = models.ForeignKey(Instrumento, on_delete=models.SET_NULL, null=True, blank=True)

    # dados do professor
    professor = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Aula agendada na sala {self.sala} - {self.dia}/{self.mes}/{self.ano} às {self.hora}"

    class Meta:
        unique_together = ('ano', 'mes', 'dia', 'hora', 'sala')  # garante que a sala não seja duplicada no mesmo horario

    professor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='aulas_agendadas')
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    instrumento = models.ForeignKey(Instrumento, on_delete=models.SET_NULL, null=True)
    ano = models.IntegerField()
    mes = models.IntegerField()  # 1 = janeiro, ..., 12 = dezembro
    dia = models.IntegerField()  # dia do mes
    hora = models.TimeField()  # ex: 08:00
    
    alunos = models.ManyToManyField(User, blank=True)
    data_agendamento = models.DateTimeField(auto_now_add=True)  # data e hora do agendamento

    def __str__(self):
        return f"Aula de {self.professor.username} na {self.sala.nome} ({self.instrumento.nome if self.instrumento else 'Sem instrumento'}) em {self.dia}/{self.mes}/{self.ano} às {self.hora}"

    class Meta:
        unique_together = ('sala', 'ano', 'mes', 'dia', 'hora')  # Impede agendar mais de uma aula no mesmo horario na mesma sala