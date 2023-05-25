from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models.animais import Animal
from .models.vacinas import Vacina
from django.forms import DateField
from django.contrib.auth import get_user_model
from decimal import Decimal

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

class AddAnimalForm(forms.Form):
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

    ani_nome = forms.CharField(
        label='Nome do animal',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50
    )

    ani_raça = forms.CharField(
        label='Raça do animal',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50
    )

    ani_cor = forms.CharField(
        label='Cor da pelagem ou plumagem',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50
    )

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

    ani_peso = forms.CharField(
        label='Peso do animal',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=10,
        required=False
    )

    ani_dnasc = forms.DateField(
        widget=forms.TextInput(attrs={'class': 'form-control datepicker'}),
        label='Data de nascimento do animal',
        required=False
    )

    ani_foto = forms.FileField(
        label='Fotografia do animal',
        widget=forms.FileInput(attrs={'multiple': False, 'class': 'form-control', 'blank': True}),
        required=False
    )

    ani_rga = forms.CharField(
        label='Registro Geral',
        widget=forms.TextInput(attrs={'class': 'form-control', 'blank': True}),
        required=False,
        max_length=50
    )

    ani_anilha = forms.CharField(
        label='Número de identificação da anilha (no caso de aves)',
        widget=forms.TextInput(attrs={'class': 'form-control', 'blank': True}),
        required=False,
        max_length=50
    )

    ani_nmchip = forms.CharField(
        label='Número de identificação do microchip (se houver)',
        widget=forms.TextInput(attrs={'class': 'form-control', 'blank': True}),
        required=False,
        max_length=50
    )

    ani_idade = forms.IntegerField(
        label='Idade do animal em anos',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'blank': True}),
        required=False
    )

    ani_obs = forms.CharField(
        label='Observações',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 9, 'blank': True}),
        required=False,
        max_length=1000
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def save(self):
        animal = Animal(
            tutor=self._get_current_user(),
            ani_nome=self.cleaned_data['ani_nome'],
            ani_raça=self.cleaned_data['ani_raça'],
            ani_cor=self.cleaned_data['ani_cor'],
            ani_castr=self.cleaned_data['ani_castr'],
            ani_espec=self.cleaned_data['ani_espec'],
            ani_sexo=self.cleaned_data['ani_sexo'],
            ani_porte=self.cleaned_data['ani_porte'],
            ani_peso=self.cleaned_data['ani_peso'],
            ani_dnasc=self.cleaned_data['ani_dnasc'],
            ani_foto=self.cleaned_data['ani_foto'],
            ani_rga=self.cleaned_data['ani_rga'],
            ani_anilha=self.cleaned_data['ani_anilha'],
            ani_nmchip=self.cleaned_data['ani_nmchip'],
            ani_idade=self.cleaned_data['ani_idade'],
            ani_obs=self.cleaned_data['ani_obs'],
        )

        animal.save()

    def _get_current_user(self):
        if self.request and self.request.user.is_authenticated:
            return self.request.user
        return None

    def clean_ani_peso(self):
        ani_peso = self.cleaned_data['ani_peso']
        try:
            # Substituir vírgula por ponto
            ani_peso = ani_peso.replace(',', '.')
            # Converter para Decimal
            ani_peso = Decimal(ani_peso)
        except (ValueError, TypeError):
            raise forms.ValidationError('Por favor, insira um número decimal válido.')

        return ani_peso


class UpdateAnimalForm(forms.Form):
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
    
    ani_nome = forms.CharField(
        label='Nome do animal',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50
    )
    
    ani_raça = forms.CharField(
        label='Raça do animal',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50
    )
    
    ani_cor = forms.CharField(
        label='Cor da pelagem ou plumagem',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50
    )
    
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
    
    ani_peso = forms.CharField(
        label='Peso do animal',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=5,
        required=False
    )
    
    ani_dnasc = forms.DateField(
        widget=forms.TextInput(attrs={'class': 'form-control datepicker'}),
        label='Data de nascimento do animal',
        required=False
    )
    
    ani_foto = forms.FileField(
        label='Fotografia do animal',
        widget=forms.FileInput(attrs={'multiple': False, 'class': 'form-control', 'blank': True}),
        required=False
    )
    
    ani_rga = forms.CharField(
        label='Registro Geral',
        widget=forms.TextInput(attrs={'class': 'form-control', 'blank': True}),
        required=False,
        max_length=50
    )
    
    ani_anilha = forms.CharField(
        label='Número de identificação da anilha (no caso de aves)',
        widget=forms.TextInput(attrs={'class': 'form-control', 'blank': True}),
        required=False,
        max_length=50
    )
    
    ani_nmchip = forms.CharField(
        label='Número de identificação do microchip (se houver)',
        widget=forms.TextInput(attrs={'class': 'form-control', 'blank': True}),
        required=False,
        max_length=50
    )
    
    ani_idade = forms.IntegerField(
        label='Idade do animal em anos',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'blank': True}),
        required=False
    )
    
    ani_obs = forms.CharField(
        label='Observações',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 9, 'blank': True}),
        required=False,
        max_length=1000
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.animal_instance = kwargs.pop('animal_instance')
        super().__init__(*args, **kwargs)
        self.populate_form_fields()

    def populate_form_fields(self):
        self.fields['ani_nome'].initial = self.animal_instance.ani_nome
        self.fields['ani_raça'].initial = self.animal_instance.ani_raça
        self.fields['ani_cor'].initial = self.animal_instance.ani_cor
        self.fields['ani_castr'].initial = self.animal_instance.ani_castr
        self.fields['ani_espec'].initial = self.animal_instance.ani_espec
        self.fields['ani_sexo'].initial = self.animal_instance.ani_sexo
        self.fields['ani_porte'].initial = self.animal_instance.ani_porte
        self.fields['ani_peso'].initial = self.animal_instance.ani_peso
        self.fields['ani_dnasc'].initial = self.animal_instance.ani_dnasc
        self.fields['ani_rga'].initial = self.animal_instance.ani_rga
        self.fields['ani_anilha'].initial = self.animal_instance.ani_anilha
        self.fields['ani_nmchip'].initial = self.animal_instance.ani_nmchip
        self.fields['ani_idade'].initial = self.animal_instance.ani_idade
        self.fields['ani_obs'].initial = self.animal_instance.ani_obs


    def save(self, commit=True):
        self.animal_instance.ani_nome = self.cleaned_data['ani_nome']
        self.animal_instance.ani_raça = self.cleaned_data['ani_raça']
        self.animal_instance.ani_cor = self.cleaned_data['ani_cor']
        self.animal_instance.ani_castr = self.cleaned_data['ani_castr']
        self.animal_instance.ani_espec = self.cleaned_data['ani_espec']
        self.animal_instance.ani_sexo = self.cleaned_data['ani_sexo']
        self.animal_instance.ani_porte = self.cleaned_data['ani_porte']
        self.animal_instance.ani_peso = self.cleaned_data['ani_peso']
        self.animal_instance.ani_dnasc = self.cleaned_data['ani_dnasc']
        self.animal_instance.ani_rga = self.cleaned_data['ani_rga']
        self.animal_instance.ani_anilha = self.cleaned_data['ani_anilha']
        self.animal_instance.ani_nmchip = self.cleaned_data['ani_nmchip']
        self.animal_instance.ani_idade = self.cleaned_data['ani_idade']
        self.animal_instance.ani_obs = self.cleaned_data['ani_obs']

        # Verifica se um novo arquivo de foto foi fornecido
        if 'ani_foto' in self.files:
            new_photo = self.files['ani_foto']
            self.animal_instance.ani_foto = new_photo

        self.animal_instance.save()

        
    def _get_current_user(self):
        if self.request and self.request.user.is_authenticated:
            return self.request.user
        return None



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