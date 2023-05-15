from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Animal(models.Model):
    tutor = models.CharField(max_length=50)
    ani_nome = models.CharField(max_length=50)
    ani_raça = models.CharField(max_length=50)
    ani_espec = models.CharField(max_length=50)
    ani_sexo = models.CharField(max_length=50)
    ani_cor = models.CharField(max_length=50)
    ani_foto = models.ImageField(blank=True)
    ani_porte = models.CharField(max_length=50)
    ani_rga = models.CharField(max_length=50, blank=True)
    ani_castr = models.CharField(max_length=50)
    ani_anilha = models.CharField(max_length=50, default='não informado', blank=True)
    ani_nmchip = models.CharField(max_length=50, default='não informado', blank=True)
    ani_dnasc = models.DateField(blank=True)
    ani_idade = models.IntegerField(blank=True)
    data_cadastro = models.DateField(auto_now_add=True)
    ani_vacinado = models.BooleanField(blank=True)
    ani_vermifugado = models.BooleanField(blank=True)
    ani_obs = models.CharField(max_length=200, default='não informado', blank=True)

    def __str__(self):
        return self.ani_nome