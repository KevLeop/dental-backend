# Generated by Django 3.1.7 on 2021-04-16 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0021_auto_20210415_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientemodel',
            name='pacienteImagen',
            field=models.ImageField(db_column='pac_imagen', default='paciente_default.jpg', null=True, upload_to='pacientes'),
        ),
    ]
