from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models.animais import Animal
from .models.vacinas import Vacina
from django.forms import DateField
from django.contrib.auth import get_user_model


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




User = get_user_model()

class AddAnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = [
            'ani_nome',
            'ani_raça',
            'ani_cor',
            'ani_castr',
            'ani_espec',
            'ani_sexo',
            'ani_porte',
            'ani_peso',
            'ani_dnasc',
            'ani_foto',
            'ani_rga',
            'ani_anilha',
            'ani_nmchip',
            'ani_idade',
            'ani_obs',
        ]
        labels = {
            'ani_nome': 'Nome do animal',
            'ani_raça': 'Raça do animal',
            'ani_cor': 'Cor',
            'ani_castr': 'Castrado',
            'ani_espec': 'Espécie',
            'ani_sexo': 'Sexo',
            'ani_porte': 'Porte',
            'ani_peso': 'Peso do animal',
            'ani_dnasc': 'Data de nascimento do animal',
            'ani_foto': 'Fotografia do animal',
            'ani_rga': 'Registro Geral',
            'ani_anilha': 'Número de identificação da anilha (no caso de aves)',
            'ani_nmchip': 'Número de identificação do microchip (se houver)',
            'ani_idade': 'Idade do animal em anos',
            'ani_obs': 'Observações',
        }
        widgets = {
            'ani_nome': forms.TextInput(attrs={'class': 'form-control'}),
            'ani_raça': forms.TextInput(attrs={'class': 'form-control'}),
            'ani_cor': forms.TextInput(attrs={'class': 'form-control'}),
            'ani_castr': forms.Select(attrs={'class': 'form-select'}),
            'ani_espec': forms.Select(attrs={'class': 'form-select'}),
            'ani_sexo': forms.Select(attrs={'class': 'form-select'}),
            'ani_porte': forms.Select(attrs={'class': 'form-select'}),
            'ani_peso': forms.NumberInput(attrs={'class': 'form-control'}),
            'ani_dnasc': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'ani_foto': forms.FileInput(attrs={'class': 'form-control', 'multiple': False}),
            'ani_rga': forms.TextInput(attrs={'class': 'form-control'}),
            'ani_anilha': forms.TextInput(attrs={'class': 'form-control'}),
            'ani_nmchip': forms.TextInput(attrs={'class': 'form-control'}),
            'ani_idade': forms.NumberInput(attrs={'class': 'form-control'}),
            'ani_obs': forms.Textarea(attrs={'class': 'form-control', 'rows': 9}),
        }

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

    ani_castr = forms.ChoiceField(
        choices=CASTRADO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Castrado'
    )

    ani_espec = forms.ChoiceField(
        choices=ESPECIE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Espécie'
    )

    ani_sexo = forms.ChoiceField(
        choices=SEXO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Sexo'
    )

    ani_porte = forms.ChoiceField(
        choices=PORTE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Porte'
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        animal = super().save(commit=False)
        animal.tutor = self._get_current_user()
        if commit:
            animal.save()
        return animal

    def _get_current_user(self):
        if self.request and self.request.user.is_authenticated:
            return self.request.user
        return None

    


class UpdateAnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = [
            'ani_nome',
            'ani_raça',
            'ani_cor',
            'ani_castr',
            'ani_espec',
            'ani_sexo',
            'ani_porte',
            'ani_peso',
            'ani_dnasc',
            'ani_foto',
            'ani_rga',
            'ani_anilha',
            'ani_nmchip',
            'ani_idade',
            'ani_obs',
        ]
        labels = {
            'ani_nome': 'Nome do animal',
            'ani_raça': 'Raça do animal',
            'ani_cor': 'Cor',
            'ani_castr': 'Castrado',
            'ani_espec': 'Espécie',
            'ani_sexo': 'Sexo',
            'ani_porte': 'Porte',
            'ani_peso': 'Peso do animal',
            'ani_dnasc': 'Data de nascimento do animal',
            'ani_foto': 'Fotografia do animal',
            'ani_rga': 'Registro Geral',
            'ani_anilha': 'Número de identificação da anilha (no caso de aves)',
            'ani_nmchip': 'Número de identificação do microchip (se houver)',
            'ani_idade': 'Idade do animal em anos',
            'ani_obs': 'Observações',
        }
        widgets = {
            'ani_nome': forms.TextInput(attrs={'class': 'form-control'}),
            'ani_raça': forms.TextInput(attrs={'class': 'form-control'}),
            'ani_cor': forms.TextInput(attrs={'class': 'form-control'}),
            'ani_castr': forms.Select(attrs={'class': 'form-select'}),
            'ani_espec': forms.Select(attrs={'class': 'form-select'}),
            'ani_sexo': forms.Select(attrs={'class': 'form-select'}),
            'ani_porte': forms.Select(attrs={'class': 'form-select'}),
            'ani_peso': forms.NumberInput(attrs={'class': 'form-control'}),
            'ani_dnasc': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'ani_foto': forms.FileInput(attrs={'class': 'form-control', 'multiple': False}),
            'ani_rga': forms.TextInput(attrs={'class': 'form-control'}),
            'ani_anilha': forms.TextInput(attrs={'class': 'form-control'}),
            'ani_nmchip': forms.TextInput(attrs={'class': 'form-control'}),
            'ani_idade': forms.NumberInput(attrs={'class': 'form-control'}),
            'ani_obs': forms.Textarea(attrs={'class': 'form-control', 'rows': 9}),
        }

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

    ani_castr = forms.ChoiceField(
        choices=CASTRADO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Castrado'
    )

    ani_espec = forms.ChoiceField(
        choices=ESPECIE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Espécie'
    )

    ani_sexo = forms.ChoiceField(
        choices=SEXO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Sexo'
    )

    ani_porte = forms.ChoiceField(
        choices=PORTE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Porte'
    )
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.animal_instance = kwargs.pop('animal_instance', None)
        super(UpdateAnimalForm, self).__init__(*args, **kwargs)



class AddVacinaForm(forms.ModelForm):
    VAC_TIPO_CHOICES = [
        ('V8 ou V10', 'V8 ou V10'),
        ('Antirrábica', 'Antirrábica'),
        ('Contra giárdia', 'Contra giárdia'),
        ('Contra tosse dos canis', 'Contra tosse dos canis'),
        ('Vermífugo', 'Vermífugo'),
        ('Antipulgas e Carrapaticidas', 'Antipulgas e Carrapaticidas'),
        ('Exame de sangue', 'Exame de sangue'),
        ("Exame de urina ou fezes", "Exame de urina ou fezes"),
        ('Testes de diagnóstico por imagem', 'Testes de diagnóstico por imagem'),
        ('Outros', 'Outros'),
    ]

    vac_tipo = forms.ChoiceField(choices=VAC_TIPO_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}), label='Tipo')

    class Meta:
        model = Vacina
        fields = ['vac_nome', 'vac_tipo', 'vac_data_admin', 'vac_validade', 'vac_num_dose', 'vac_fabricante', 'vac_anexo']
        labels = {
            'vac_nome': 'Nome',
            'vac_data_admin': 'Data de Aplicação/Exame',
            'vac_validade': 'Validade',
            'vac_num_dose': 'Doses',
            'vac_fabricante': 'Fabricante/Laboratório',
            'vac_anexo': 'Anexo',
        }
        widgets = {
            'vac_nome': forms.TextInput(attrs={'class': 'form-control'}),
            'vac_data_admin': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'vac_validade': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'vac_num_dose': forms.NumberInput(attrs={'class': 'form-control'}),
            'vac_fabricante': forms.TextInput(attrs={'class': 'form-control'}),
            'vac_anexo': forms.FileInput(attrs={'class': 'form-control'}),
        }

class UpdateVacinaForm(forms.ModelForm):
    VAC_TIPO_CHOICES = [
        ('V8 ou V10', 'V8 ou V10'),
        ('Antirrábica', 'Antirrábica'),
        ('Contra giárdia', 'Contra giárdia'),
        ('Contra tosse dos canis', 'Contra tosse dos canis'),
        ('Vermífugo', 'Vermífugo'),
        ('Antipulgas e Carrapaticidas', 'Antipulgas e Carrapaticidas'),
        ('Exame de sangue', 'Exame de sangue'),
        ("Exame de urina ou fezes", "Exame de urina ou fezes"),
        ('Testes de diagnóstico por imagem', 'Testes de diagnóstico por imagem'),
        ('Outros', 'Outros'),
    ]

    vac_tipo = forms.ChoiceField(choices=VAC_TIPO_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}), label='Tipo')

    class Meta:
        model = Vacina
        fields = ['vac_nome', 'vac_tipo', 'vac_data_admin', 'vac_validade', 'vac_num_dose', 'vac_fabricante', 'vac_anexo']
        labels = {
            'vac_nome': 'Nome',
            'vac_data_admin': 'Data de Aplicação/Exame',
            'vac_validade': 'Validade',
            'vac_num_dose': 'Doses',
            'vac_fabricante': 'Fabricante/Laboratório',
            'vac_anexo': 'Anexo',
        }
        widgets = {
            'vac_nome': forms.TextInput(attrs={'class': 'form-control'}),
            'vac_data_admin': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'vac_validade': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'vac_num_dose': forms.NumberInput(attrs={'class': 'form-control'}),
            'vac_fabricante': forms.TextInput(attrs={'class': 'form-control'}),
            'vac_anexo': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vac_anexo'].required = False

    def clean_vac_anexo(self):
        vac_anexo = self.cleaned_data['vac_anexo']
        if not vac_anexo and self.instance:
            return self.instance.vac_anexo
        return vac_anexo