# Generated by Django 4.2.1 on 2023-05-23 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_de_animais', '0015_alter_animal_tutor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='ani_obs',
            field=models.CharField(blank=True, default='não informado', max_length=1000, null=True),
        ),
    ]
