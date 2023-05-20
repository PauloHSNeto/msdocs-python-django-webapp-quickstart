from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models.animais import Animal
from .models.vacinas import Vacina
from django.forms import DateField

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Endereço de Email'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sobrenome'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Nome de Usuário'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Obrigatório. 150 caracteres ou menos. Letras, dígitos e apenas @/./+/-/_.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Sua senha não pode ser muito parecida com suas outras informações pessoais.</li><li>Sua senha deve conter pelo menos 8 caracteres.</li><li>Sua senha não pode ser uma senha comumente usada.</li><li>Sua senha não pode ser totalmente numérica.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar Senha'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Digite a mesma senha de antes, para verificação.</small></span>'	


class AddAnimalForm(forms.ModelForm):
    CASTRADO_CHOICES = [
        ('Sim', 'Sim'),
        ('Não', 'Não'),
        ('Não sei', 'Não sei'),
    ]
    
    ESPECIE_CHOICES = [
        ('Cachorro', 'Cachorro'),
        ('Gato', 'Gato'),
        ('Ave', 'Ave'),
        ('Outro', 'Outro'),
    ]
    
    SEXO_CHOICES = [
        ('Macho', 'Macho'),
        ('Fêmea', 'Fêmea'),
        ('Indefinido', 'Indefinido'),
    ]
    
    PORTE_CHOICES = [
        ('Pequeno', 'Pequeno'),
        ('Médio', 'Médio'),
        ('Grande', 'Grande'),
    ]
    
    ani_castr = forms.ChoiceField(choices=CASTRADO_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}), label='Castrado')
    ani_espec = forms.ChoiceField(choices=ESPECIE_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}), label='Espécie')
    ani_sexo = forms.ChoiceField(choices=SEXO_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}), label='Sexo')
    ani_porte = forms.ChoiceField(choices=PORTE_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}), label='Porte')
    ani_dnasc = DateField(widget=forms.TextInput(attrs={'class': 'form-control datepicker'}), label='Data de nascimento do animal')
    
    class Meta:
        model = Animal
        fields = '__all__'
        labels = {
            'tutor': 'Tutor',
            'ani_nome': 'Nome do animal',
            'ani_raça': 'Raça do animal',
            'ani_cor': 'Cor da pelagem ou plumagem',
            'ani_foto': 'Fotografia do animal',
            'ani_rga': 'Registro Geral',
            'ani_anilha': 'Número de identificação da anilha (no caso de aves)',
            'ani_nmchip': 'Número de identificação do microchip (se houver)',
            'ani_idade': 'Idade do animal em anos',
            'ani_vacinado': 'Vacinado',
            'ani_vermifugado': 'Vermifugado',
            'ani_obs': 'Observações',
        }
        widgets = {
            'tutor': forms.TextInput(attrs={'class': 'form-control', 'blank': True}),
            'ani_foto': forms.FileInput(attrs={'multiple': False, 'class': 'form-control', 'blank': True}),
            'ani_nome': forms.TextInput(attrs={'class': 'form-control'}),
            'ani_raça': forms.TextInput(attrs={'class': 'form-control'}),
            'ani_sexo': forms.Select(attrs={'class': 'form-select'}),
            'ani_cor': forms.TextInput(attrs={'class': 'form-control'}),
            'ani_porte': forms.Select(attrs={'class': 'form-select'}),
            'ani_rga': forms.TextInput(attrs={'class': 'form-control', 'blank': True}),
            'ani_anilha': forms.TextInput(attrs={'class': 'form-control', 'blank': True}),
            'ani_nmchip': forms.TextInput(attrs={'class': 'form-control', 'blank': True}),
            'ani_dnasc': forms.DateInput(attrs={'type': 'date', 'class': 'form-control datepicker', 'blank': True}),
            'ani_idade': forms.NumberInput(attrs={'class': 'form-control', 'blank': True}),
            'ani_vacinado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'ani_vermifugado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'ani_obs': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'blank': True}),
        }

class UpdateAnimalForm(forms.ModelForm):
    CASTRADO_CHOICES = [
        ('Sim', 'Sim'),
        ('Não', 'Não'),
        ('Não sei', 'Não sei'),
    ]
    
    ESPECIE_CHOICES = [
        ('Cachorro', 'Cachorro'),
        ('Gato', 'Gato'),
        ('Ave', 'Ave'),
        ('Outro', 'Outro'),
    ]
    
    SEXO_CHOICES = [
        ('Macho', 'Macho'),
        ('Fêmea', 'Fêmea'),
        ('Indefinido', 'Indefinido'),
    ]
    
    PORTE_CHOICES = [
        ('Pequeno', 'Pequeno'),
        ('Médio', 'Médio'),
        ('Grande', 'Grande'),
    ]
    
    ani_castr = forms.ChoiceField(choices=CASTRADO_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}), label='Castrado')
    ani_espec = forms.ChoiceField(choices=ESPECIE_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}), label='Espécie')
    ani_sexo = forms.ChoiceField(choices=SEXO_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}), label='Sexo')
    ani_porte = forms.ChoiceField(choices=PORTE_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}), label='Porte')
    ani_dnasc = DateField(widget=forms.TextInput(attrs={'class': 'form-control datepicker'}), label='Data de nascimento do animal')
    
    class Meta:
        model = Animal
        fields = '__all__'
        labels = {
            'tutor': 'Tutor',
            'ani_nome': 'Nome do animal',
            'ani_raça': 'Raça do animal',
            'ani_cor': 'Cor da pelagem ou plumagem',
            'ani_foto': 'Fotografia do animal',
            'ani_rga': 'Registro Geral',
            'ani_anilha': 'Número de identificação da anilha (no caso de aves)',
            'ani_nmchip': 'Número de identificação do microchip (se houver)',
            'ani_idade': 'Idade do animal em anos',
            'ani_vacinado': 'Vacinado',
            'ani_vermifugado': 'Vermifugado',
            'ani_obs': 'Observações',
        }
        widgets = {
            'tutor': forms.TextInput(attrs={'class': 'form-control', 'blank': True}),
            'ani_foto': forms.FileInput(attrs={'multiple': False, 'class': 'form-control', 'blank': True}),
            'ani_nome': forms.TextInput(attrs={'class': 'form-control'}),
            'ani_raça': forms.TextInput(attrs={'class': 'form-control'}),
            'ani_sexo': forms.Select(attrs={'class': 'form-select'}),
            'ani_cor': forms.TextInput(attrs={'class': 'form-control'}),
            'ani_porte': forms.Select(attrs={'class': 'form-select'}),
            'ani_rga': forms.TextInput(attrs={'class': 'form-control', 'blank': True}),
            'ani_anilha': forms.TextInput(attrs={'class': 'form-control', 'blank': True}),
            'ani_nmchip': forms.TextInput(attrs={'class': 'form-control', 'blank': True}),
            'ani_dnasc': forms.DateInput(attrs={'type': 'date', 'class': 'form-control datepicker', 'blank': True}),
            'ani_idade': forms.NumberInput(attrs={'class': 'form-control', 'blank': True}),
            'ani_vacinado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'ani_vermifugado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'ani_obs': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'blank': True}),
        }
