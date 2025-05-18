from django.db import models
from django.contrib.auth.models import User

class Matricula(models.Model):
    nome_completo = models.CharField(max_length=100)
    idade = models.IntegerField()
    instrumento = models.CharField(max_length=50)  # Corrigido
    email = models.EmailField()
    telefone = models.CharField(max_length=20)     # Corrigido
    observacao = models.TextField()
    instrutor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'matricula'

    def __str__(self):
        return self.nome_completo


class agendamento_de_aula(models.Model):
    aluno = models.ForeignKey(Matricula, on_delete=models.CASCADE, null=True, blank=True)
    telefone = models.CharField(max_length=20)
    data_agendamento = models.DateField(verbose_name='Data do agendamento')
    hora = models.TimeField()
    instrutor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'agendamento_de_aula'

    def __str__(self):
        return f'{self.aluno.nome_completo} - {self.data_agendamento} às {self.hora}'


class deletarAgendamento(models.Model):
    aluno = models.ForeignKey(Matricula, on_delete=models.CASCADE, null=True, blank=True)
    telefone = models.CharField(max_length=20)  # Corrigido
    data_agendamento = models.DateField(verbose_name='Data do agendamento')
    hora = models.TimeField()
    instrutor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'deletarAgendamento'

    def __str__(self):
        return f'{self.aluno.nome_completo} - {self.data_agendamento} às {self.hora}'
