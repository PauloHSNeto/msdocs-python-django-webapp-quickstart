# Generated by Django 4.2.1 on 2023-05-20 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_de_animais', '0008_alter_animal_ani_anilha_alter_animal_ani_dnasc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='ani_foto',
            field=models.ImageField(blank=True, null=True, upload_to='pet_photos'),
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]