from django.contrib import admin

# Register your models here.
from .models.animais import *
from .models.vacinas import *

admin.site.register(Tutor)
admin.site.register(Especie)
admin.site.register(Sexo)
admin.site.register(Porte)
admin.site.register(Raça)
admin.site.register(Animal)

admin.site.register(Vacina)
