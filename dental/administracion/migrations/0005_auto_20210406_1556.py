# Generated by Django 3.1.7 on 2021-04-06 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0004_pacientemodel_pacienteimagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientemodel',
            name='pacienteImagen',
            field=models.URLField(db_column='pac_imagen'),
        ),
    ]
