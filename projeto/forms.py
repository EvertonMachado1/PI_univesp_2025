from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, AulaAgendada, Sala, Instrumento

# Formulário para cadastro de usuário
class CadastroUsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirmar senha')
    nome = forms.CharField(max_length=100)
    cpf = forms.CharField(max_length=14)
    telefone = forms.CharField(max_length=20)
    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('As senhas não coincidem.')
        return password2

    def save(self, commit=True):
        # Cria o usuário
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_superuser = False
        user.is_staff = False
        
        if commit:
            user.save()

        # Cria o perfil do usuário (UserProfile)
        user_profile = UserProfile(
            user=user,
            cpf=self.cleaned_data['cpf'],
            telefone=self.cleaned_data['telefone'],
            data_nascimento=self.cleaned_data['data_nascimento'],
        )
        user_profile.save()

        return user
    
# agendamento de aula
class AgendamentoAulaForm(forms.ModelForm):
    ano = forms.IntegerField(initial=2025, widget=forms.HiddenInput())  # pode ser alterado conforme necessario
    mes = forms.ChoiceField(choices=[(i, f'{i:02d}') for i in range(1, 13)], label="Mês")
    dia = forms.IntegerField(min_value=1, max_value=31, label="Dia")
    hora = forms.ChoiceField(choices=[(f"{h:02d}:00", f"{h:02d}:00") for h in range(8, 21)], label="Hora")
    sala = forms.ModelChoiceField(queryset=Sala.objects.all(), label="Sala")
    instrumento = forms.ModelChoiceField(queryset=Instrumento.objects.all(), required=False, label="Instrumento")
    
    class Meta:
        model = AulaAgendada
        fields = ['ano', 'mes', 'dia', 'hora', 'sala', 'instrumento']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # busca salas disponiveis no horario selecionado
        self.fields['sala'].queryset = self.get_salas_disponiveis()
        #retorna as salas disponiveis
    def get_salas_disponiveis(self):
        ano = self.cleaned_data.get('ano') if 'ano' in self.cleaned_data else None
        mes = self.cleaned_data.get('mes') if 'mes' in self.cleaned_data else None
        dia = self.cleaned_data.get('dia') if 'dia' in self.cleaned_data else None
        hora = self.cleaned_data.get('hora') if 'hora' in self.cleaned_data else None
        
        # se faltar informações para o filtro retorna todas as salas
        if not ano or not mes or not dia or not hora:
            return Sala.objects.all()

        # retorna salas que NÃO estão ocupadas no horario selecionado
        return Sala.objects.exclude(id__in=AulaAgendada.objects.filter(
            ano=ano,
            mes=mes,
            dia=dia,
            hora=hora
        ).values_list('sala', flat=True))
  