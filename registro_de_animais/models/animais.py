from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Animal(models.Model):
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pets', blank=True, null=True)
    ani_nome = models.CharField(max_length=50, default='')
    ani_raça = models.CharField(max_length=50, default='')
    ani_espec = models.CharField(max_length=50, default='')
    ani_sexo = models.CharField(max_length=50, default='')
    ani_cor = models.CharField(max_length=50, default='')
    ani_foto = models.ImageField(upload_to='pet_profile_pics',  null=True, blank=True)
    ani_porte = models.CharField(max_length=50, default='')
    ani_peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ani_rga = models.CharField(max_length=50, blank=True, null=True)
    ani_castr = models.CharField(max_length=50, default='')
    ani_anilha = models.CharField(max_length=50, default='', blank=True, null=True)
    ani_nmchip = models.CharField(max_length=50, default='', blank=True, null=True)
    ani_dnasc = models.DateField(blank=True, null=True)
    ani_idade = models.IntegerField(blank=True, null=True)
    data_cadastro = models.DateField(auto_now_add=True, blank=True, null=True)
    ani_obs = models.CharField(max_length=1000, default='', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:  # Se o objeto ainda não foi salvo no banco de dados
            self.tutor = self._get_current_user()  # Define o tutor como o usuário logado
        super().save(*args, **kwargs)

    def _get_current_user(self):
        from django.contrib.auth import get_user
        user = get_user(self._request)
        if user.is_authenticated:
            return user
        return None

    @property
    def _request(self):
        return getattr(self, '_request_cache', None)

    @_request.setter
    def _request(self, value):
        self._request_cache = value

    def __str__(self):
        return self.ani_nome
    