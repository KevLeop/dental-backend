# Generated by Django 3.1.7 on 2021-04-06 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0003_auto_20210406_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacientemodel',
            name='pacienteImagen',
            field=models.ImageField(db_column='pac_imagen', default='', upload_to='platos/'),
            preserve_default=False,
        ),
    ]