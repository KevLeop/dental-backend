from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# AbstractBaseUser solo modificar, agregar campos al modelo Usuario
from .authmanager import UsuarioManager

class PersonalModel(AbstractBaseUser, PermissionsMixin):
  TIPO_PERSONAL=[(1,"ADMIN"),(2,"DOCTOR"),(3,'PACIENTE')]
  personalId = models.AutoField(
    primary_key=True,
    unique=True,
    db_column='personal_id'
  )

  personalCorreo = models.EmailField(
    db_column='personal_correo',
    max_length=50,
    verbose_name='Correo del usuario',
    unique=True
  )

  personalTipo = models.IntegerField(
    db_column='personal_tipo',
    choices=TIPO_PERSONAL,
    verbose_name='Tipo del usuario'
  )

  personalNombre=models.CharField(
    max_length=45,
    null=False,
    db_column='personal_nombre',
    verbose_name='Nombre del Personal',
  )
  personalApellido=models.CharField(
    max_length=45,
    null=False,
    db_column='personal_apellido',
    verbose_name='Apellido del Personal',
  )

  password = models.TextField(
    db_column='personal_password',
    verbose_name='Contraseña del usuario',
  )

  is_active = models.BooleanField(
    default=True
  )

  is_staff = models.BooleanField(
    default=False
  )
  # asignamos el comportamiento con el modelo
  objects = UsuarioManager()

  # ahora definimos que columna será la encagada dle login
  #esto ahce que esa columna sea unica y null=false
  USERNAME_FIELD = 'personalCorreo'
  # para solicitar los campos al momento de crear superusuario por consola
  REQUIRED_FIELDS = ['personalNombre', 'personalApellido', 'personalTipo']

  class Meta:
    db_table='t_personal'
    verbose_name = 'personal'
    verbose_name_plural = 'personales'

class TratamientoModel(models.Model):
  tratamientoId = models.AutoField(
    primary_key=True,
    auto_created=True,
    null = False,
    unique=True,
    help_text='ID del tratamiento',
    verbose_name='ID del tratamiento',
    db_column='trat_id',
  )
  tratamientoNombre = models.CharField(
    max_length=45,
    null= False,
    help_text='Nombre el tratamiento',
    verbose_name='Nombre del tratamiento',
    db_column='trat_nombre'
  )
  tratamientoDescripcion = models.CharField(
    max_length=100,
    null=True,
    help_text='Descripcion del tratamiento',
    verbose_name='Descripcion del tratamiento',
    db_column='trat_descripcion'
  )

  tratamientoEstado = models.BooleanField(
    default=True,
    null=False,
    db_column='trat_estado'
  )


  def __str__(self):
    return self.tratamientoNombre

  class Meta:
    db_table='t_tratamiento'
    verbose_name='Tratamiento'
    verbose_name_plural = 'Tratamientos'


class PacienteModel(models.Model):
  pacienteDni=models.CharField(
    max_length=9,
    primary_key=True,
    null = False,
    unique=True,
    help_text='ID del paciente',
    verbose_name='ID del paciente',
    db_column='pac_id',
  )
  pacienteNombre=models.CharField(
    max_length=40,
    null= False,
    help_text='Nombre del paciente',
    verbose_name='Nombre del paciente',
    db_column='pac_nombre'
  )
  pacienteApellido=models.CharField(
    max_length=40,
    null= False,
    help_text='Apellido del paciente',
    verbose_name='Apellido del paciente',
    db_column='pac_apellido'
  )
  pacienteFnacimiento = models.DateField(
    null=False,
    help_text='Fecha de Nacimiento del paciente',
    verbose_name='Fecha de Nacimiento del paciente',
    db_column='pac_fnacimiento',
  )
  SEXO_CHOICES=[('M','Masculino'),('F','Femenino'),('O','Otro')]
  pacienteSexo = models.CharField(
    max_length=1,
    choices=SEXO_CHOICES,
    null=False,
    db_column='pac_sexo'
  )
  pacienteTelefono = models.CharField(
    max_length=15,
    null=False,
    db_column='pac_telefono'
  )
  pacienteEmail = models.EmailField(
    max_length=45,
    null=False,
    db_column='pac_email'
  )
  SANGRE_CHOICES=[('O-','O-'),('O+','O+'),('A-','A-'),('A+','A+'),('B-','B-'),('B+','B+'),('AB-','AB-'),('AB+','AB+'),]
  pacienteGSanguineo = models.CharField(
    max_length=3,
    choices=SANGRE_CHOICES,
    null=True,
    db_column='pac_gsang'
  )
  # Clase 43-44
  pacienteImagen = models.ImageField(
    # pic = models.ImageField(upload_to='blah', default='path/to/my/default/image.jpg')
    upload_to='pacientes',
    # default = 'default-image.jpg',
    db_column='pac_imagen',
    null=True,
  )

  pacienteEstado = models.BooleanField(
    default=True,
    null=False,
    db_column='pac_estado'
  )
  
  class Meta:
    db_table='t_paciente'
    verbose_name='Paciente'
    verbose_name_plural = 'Pacientes'


class HClinicaModel(models.Model):
  hclinicaId=models.AutoField(
    primary_key=True,
    auto_created=True,
    null = False,
    unique=True,
    help_text='ID de la Historia Clinica',
    verbose_name='ID de la Historia Clinica',
    db_column='hclinica_id',
  )
  hclinicaFecha=models.DateField(
    null=False,
    help_text='Fecha de la Historia Clinica',
    verbose_name='Fecha de la Historia Clinica',
    db_column='hclinica_fecha',
  )
  hclinicaProblema = models.CharField(
    max_length=50,
    null=True,
    help_text='Problema',
    verbose_name='Problema',
    db_column='hclinica_problema'
  )
  hclinicaDiagnostico=models.CharField(
    max_length=50,
    null= False,
    help_text='Diagnostico',
    verbose_name='Diagnostico',
    db_column='hclinica_diagnostico'
  )
  hclinicaPrecio = models.DecimalField(
    max_digits=6,
    decimal_places=2,
    help_text='Precio de la HClinica',
    verbose_name='Precio de la HClinica',
    db_column='hclinica_precio'
  )
  hclinicaPagado = models.BooleanField(
    default=False,
    db_column='hclinica_pagado'
  )


  paciente = models.ForeignKey(
    to=PacienteModel,
    on_delete=models.PROTECT,
    null=False,
    related_name='hcPaciente',
    db_column='paciente_dni'
  )

  tratamiento = models.ForeignKey(
    to=TratamientoModel,
    on_delete=models.PROTECT,
    null=False,
    related_name='hcTratamiento',
    db_column='tratamiento_id'
  )

  class Meta:
    db_table='t_hclinica'
    verbose_name='Historia Clinica'
    verbose_name_plural = 'Historias Clinicas'


class CitaModel(models.Model):
  citaId=models.AutoField(
    primary_key=True,
    auto_created=True,
    null = False,
    unique=True,
    help_text='ID de la Cita',
    verbose_name='ID de la Cita',
    db_column='cita_id',
  )
  citaTitulo=models.CharField(
    max_length=40,
    null= False,
    help_text='Cita',
    verbose_name='Cita',
    db_column='cita_titulo'
  )
  citaFechaInicio=models.DateTimeField(
    null=False,
    help_text='Fecha y hora de inicio',
    verbose_name='Fecha y hora de inicio',
    db_column='cita_finicio'
  )
  citaFechaFin=models.DateTimeField(
    null=False,
    help_text='Fecha y hora de fin',
    verbose_name='Fecha y hora de fin',
    db_column='cita_ffin'
  )
  CITA_ESTADO_CHOICES=[('PEND','Pendiente'),('ATEN','Atendido'),('CANC','Cancelado')]
  citaEstado = models.CharField(
    max_length=4,
    choices=CITA_ESTADO_CHOICES,
    default='PEND',
    db_column='cita_estado'
  )

  paciente = models.ForeignKey(
    to=PacienteModel,
    on_delete=models.PROTECT,
    null=False,
    related_name='citaPaciente',
    db_column='paciente_id'
  )

  class Meta:
    db_table='t_cita'
    verbose_name='Cita'
    verbose_name_plural = 'Citas'



  

  



