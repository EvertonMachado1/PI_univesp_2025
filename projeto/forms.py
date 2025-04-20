from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

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