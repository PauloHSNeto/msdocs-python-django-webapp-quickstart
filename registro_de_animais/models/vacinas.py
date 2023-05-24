from django.db import models
from django.contrib.auth import get_user_model
from .animais import Animal

User = get_user_model()

class Vacina(models.Model):
    vac_id = models.AutoField(primary_key=True)
    vac_nome = models.CharField(max_length=50, default=None)
    vac_tipo = models.CharField(default=None, blank=True, max_length=50, null=True)
    vac_data_admin = models.DateField(max_length=11)
    vac_num_dose = models.IntegerField(null=True, blank=True)
    vac_fabricante = models.CharField(max_length=50, null=True, blank=True)
    vac_validade = models.DateField(null=True, blank=True)
    vac_anexo = models.FileField(upload_to='vacinas', null=True, blank=True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='vacinas', default=None)

    def __str__(self):
        return self.vac_nome
