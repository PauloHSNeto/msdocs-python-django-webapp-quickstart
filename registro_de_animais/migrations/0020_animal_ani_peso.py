# Generated by Django 4.2.1 on 2023-05-24 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_de_animais', '0019_alter_vacina_vac_validade'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='ani_peso',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
