# Generated by Django 3.1.7 on 2021-03-19 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PacienteModel',
            fields=[
                ('pacienteDni', models.CharField(db_column='pac_id', help_text='ID del paciente', max_length=9, primary_key=True, serialize=False, unique=True, verbose_name='ID del paciente')),
                ('pacienteNombre', models.CharField(db_column='pac_nombre', help_text='Nombre del paciente', max_length=40, verbose_name='Nombre del paciente')),
                ('pacienteApellido', models.CharField(db_column='pac_apellido', help_text='Apellido del paciente', max_length=40, verbose_name='Apellido del paciente')),
                ('pacienteFnacimiento', models.DateField(db_column='pac_fnacimiento', help_text='Fecha de Nacimiento del paciente', verbose_name='Fecha de Nacimiento del paciente')),
                ('pacienteSexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], db_column='pac_sexo', max_length=1)),
                ('pacienteTelefono', models.CharField(db_column='pac_telefono', max_length=15)),
                ('pacienteEmail', models.EmailField(db_column='pac_email', max_length=45)),
                ('pacienteGSanguineo', models.CharField(choices=[('O-', 'O-'), ('O+', 'O+'), ('A-', 'A-'), ('A+', 'A+'), ('B-', 'B-'), ('B+', 'B+'), ('AB-', 'AB-'), ('AB+', 'AB+')], db_column='pac_gsang', max_length=3, null=True)),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
                'db_table': 't_paciente',
            },
        ),
        migrations.CreateModel(
            name='TratamientoModel',
            fields=[
                ('tratamientoId', models.AutoField(auto_created=True, db_column='trat_id', help_text='ID del tratamiento', primary_key=True, serialize=False, unique=True, verbose_name='ID del tratamiento')),
                ('tratamientoNombre', models.CharField(db_column='trat_nombre', help_text='Nombre el tratamiento', max_length=45, verbose_name='Nombre del tratamiento')),
                ('tratamientoDescripcion', models.CharField(db_column='trat_descripcion', help_text='Descripcion del tratamiento', max_length=100, null=True, verbose_name='Descripcion del tratamiento')),
            ],
            options={
                'verbose_name': 'Tratamiento',
                'verbose_name_plural': 'Tratamientos',
                'db_table': 't_tratamiento',
            },
        ),
        migrations.CreateModel(
            name='HClinicaModel',
            fields=[
                ('hclinicaId', models.AutoField(auto_created=True, db_column='hclinica_id', help_text='ID de la Historia Clinica', primary_key=True, serialize=False, unique=True, verbose_name='ID de la Historia Clinica')),
                ('hclinicaFecha', models.DateField(db_column='hclinica_fecha', help_text='Fecha de la Historia Clinica', verbose_name='Fecha de la Historia Clinica')),
                ('hclinicaDiagnostico', models.CharField(db_column='hclinica_diagnostico', help_text='Diagnostico', max_length=50, verbose_name='Diagnostico')),
                ('hclinicaPrecio', models.DecimalField(db_column='hclinica_precio', decimal_places=2, help_text='Precio de la HClinica', max_digits=6, verbose_name='Precio de la HClinica')),
                ('hclinicaPagado', models.BooleanField(db_column='hclinica_pagado', default=False)),
                ('paciente', models.ForeignKey(db_column='paciente_id', on_delete=django.db.models.deletion.PROTECT, related_name='hcPaciente', to='administracion.pacientemodel')),
                ('tratamiento', models.ForeignKey(db_column='hc_id', on_delete=django.db.models.deletion.PROTECT, related_name='hcTratamiento', to='administracion.tratamientomodel')),
            ],
            options={
                'verbose_name': 'Historia Clinica',
                'verbose_name_plural': 'Historias Clinicas',
                'db_table': 't_hclinica',
            },
        ),
        migrations.CreateModel(
            name='CitaModel',
            fields=[
                ('citaId', models.AutoField(auto_created=True, db_column='cita_id', help_text='ID de la Cita', primary_key=True, serialize=False, unique=True, verbose_name='ID de la Cita')),
                ('citaTitulo', models.CharField(db_column='cita_titulo', help_text='Cita', max_length=40, verbose_name='Cita')),
                ('citaFechaInicio', models.DateTimeField(db_column='cita_finicio', help_text='Fecha y hora de inicio', verbose_name='Fecha y hora de inicio')),
                ('citaFechaFin', models.DateTimeField(db_column='cita_ffin', help_text='Fecha y hora de fin', verbose_name='Fecha y hora de fin')),
                ('citaEstado', models.CharField(choices=[('PEND', 'Pendiente'), ('ATEN', 'Atendido'), ('CANC', 'Cancelado')], db_column='cita_estado', default='PEND', max_length=4)),
                ('paciente', models.ForeignKey(db_column='paciente_id', on_delete=django.db.models.deletion.PROTECT, related_name='citaPaciente', to='administracion.pacientemodel')),
            ],
            options={
                'verbose_name': 'Cita',
                'verbose_name_plural': 'Citas',
                'db_table': 't_cita',
            },
        ),
    ]
