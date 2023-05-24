from django.contrib import admin

# Register your models here.
from .models.animais import Animal
from .models.vacinas import Vacina



admin.site.register(Animal)

admin.site.register(Vacina)
