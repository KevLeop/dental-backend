

# FINAL-BACKEND-G5-CODIGO

## Integrantes:
 - Kevin Valverde
 - Mateo Quispe

## Proyecto Final de BackEnd - CodiGo - TECSUP

_La aplicación consiste en el una base de datos para el registro de diferentes pacientes según el usuario final quien es el Doctor de la Clínica Dental,
no solo registrando al paciente sino que también creando una historia clínica de lo que le han ido realizando, y a su vez también
poder programar su correspondiente cita. El usuario podrá registrar al paciente y tenerlo guardado en su base de datos para agilizar
su registro de cita para el futuro, de igual manera podrá ver su información como su edad o su número de celular según sea la necesidad,
tendrá la opción de editar la información si ocurriera algún error en los datos del paciente y podrá registrar la fotografía del correspondiente paciente._

## Enlace de la documentación

Documentacion con swagger:
https://dental-app-final.herokuapp.com/

## Ejecutando las pruebas ⚙️

_Verificar la conexion con el BACKEND que se encuentra en HEROKU_

```
export const URL_BACKEND = "http://dental-app-final.herokuapp.com";
```

![image](https://user-images.githubusercontent.com/73620785/115120422-080c2080-9f73-11eb-9f2d-c4b5ea33cbde.png)

## Consumo de servicios ⚙️

_Consumo del BACKEND_ **LOGIN** _Promesa para la autenticacion del usuario_

```
import { URL_BACKEND } from "../environments/environments";

export const postLogin = async (objAuth) => {
  const peticion = await fetch(`${URL_BACKEND}/login-custom`, {
    method: "POST",
    headers: {
      "Content-type": "application/json",
    },
    body: JSON.stringify(objAuth),
  });
  let data = await peticion.json();
  return data;
};

```

![image](https://user-images.githubusercontent.com/73620785/115120592-e495a580-9f73-11eb-9eca-532504892165.png)

_Consumo del BACKEND_ **GET Y POST CITAS** _Crud de datos para las citas_

```
import { URL_BACKEND } from "../environments/environments";

export const getCitas = async () => {
  const peticion = await fetch(`${URL_BACKEND}/citas`);
  const data = await peticion.json();
  return data;
};

export const postCitas = async (objCita) => {
  const peticion = await fetch(`${URL_BACKEND}/citas`, {
    method: "POST",
    body: JSON.stringify(objCita),
    headers: {
      "Content-type": "application/json",
    },
  });
  const data = await peticion.json();
  return data;
};

```

![image](https://user-images.githubusercontent.com/73620785/115120633-21fa3300-9f74-11eb-9dae-41cbdc945a4c.png)

_Consumo del BACKEND_ **GET, POST, PUT, DELETE HISTORIAS CLINICAS** _Crud de datos para las historias clinicas_

```
import { URL_BACKEND } from "../environments/environments";

export const getHistoriasClinicas = async () => {
  const peticion = await fetch(`${URL_BACKEND}/hclinicas`);
  const data = await peticion.json();
  return data;
};

export const posthClinica = async (objhClinica) => {
  const peticion = await fetch(`${URL_BACKEND}/hclinicas`, {
    method: "POST",
    body: JSON.stringify(objhClinica),
    headers: {
      "Content-type": "application/json",
    },
  });
  const data = await peticion.json();
  return data;
};

export const putHclinica = async (objHClinica) => {
  const peticion = await fetch(
    `${URL_BACKEND}/hclinicas/${objHClinica.paciente}`,
    {
      method: "PUT",
      body: JSON.stringify(objHClinica),
      headers: {
        "Content-type": "application/json",
      },
    }
  );
  const data = await peticion.json();
  return data;
};

export const deleteHclinica = async (id_hclinica) => {
  const peticion = await fetch(`${URL_BACKEND}/hclinicas/${id_hclinica}`, {
    method: "DELETE",
  });
  const data = await peticion.json();
  return data;
};

```

![image](https://user-images.githubusercontent.com/73620785/115120650-33dbd600-9f74-11eb-8b12-c13f592768c3.png)
![image](https://user-images.githubusercontent.com/73620785/115120652-376f5d00-9f74-11eb-8c65-61489ca20249.png)

_Consumo del BACKEND_ **GET, POST, PUT, DELETE HISTORIAS CLINICAS** _Crud de datos para los pacientes_

```
import { URL_BACKEND } from "../environments/environments";

export const getPacientes = async () => {
  const peticion = await fetch(`${URL_BACKEND}/pacientes`);
  const data = await peticion.json();
  return data;
};

export const searchPaciente = async (nombrePaciente) => {
  const peticion = await fetch(`${URL_BACKEND}/pacientes?=${nombrePaciente}`);
  const data = await peticion.json();
  return data;
};

export const postPacientes = async (formData) => {
  const peticion = await fetch(`${URL_BACKEND}/pacientes`, {
    method: "POST",
    body: formData,
  });
  const data = await peticion.json();
  return data;
};

export const putPacientes = async (objPaciente) => {
  const peticion = await fetch(
    `${URL_BACKEND}/pacientes/${objPaciente.pacienteDni}`,
    {
      method: "PUT",
      body: JSON.stringify(objPaciente),
      headers: {
        "Content-type": "application/json",
      },
    }
  );
  const data = await peticion.json();
  return data;
};

export const deletePaciente = async (pacienteId) => {
  const peticion = await fetch(`${URL_BACKEND}/pacientes/${pacienteId}`, {
    method: "DELETE",
  });
  const data = await peticion.json();
  return data;
};
```

![image](https://user-images.githubusercontent.com/73620785/115120676-540b9500-9f74-11eb-9b6f-0e123a7a4352.png)
![image](https://user-images.githubusercontent.com/73620785/115120682-579f1c00-9f74-11eb-8cca-17d2b1be8858.png)

_Consumo del BACKEND_ **GET, POST, PUT, DELETE HISTORIAS CLINICAS** _Crud de datos para los tratamientos_

```
import { URL_BACKEND } from "../environments/environments";

export const getTratamientos = async () => {
  const peticion = await fetch(`${URL_BACKEND}/tratamientos`);
  const data = await peticion.json();
  return data;
};

export const postTratamientos = async (objTratamiento) => {
  const peticion = await fetch(`${URL_BACKEND}/tratamientos`, {
    method: "POST",
    body: JSON.stringify(objTratamiento),
    headers: {
      "Content-type": "application/json",
    },
  });
  const data = await peticion.json();
  return data;
};

export const putTratamientos = async (objTratamiento) => {
  const peticion = await fetch(
    `${URL_BACKEND}/tratamientos/${objTratamiento.paciente}`,
    {
      method: "PUT",
      body: JSON.stringify(objTratamiento),
      headers: {
        "Content-type": "application/json",
      },
    }
  );
  const data = await peticion.json();
  return data;
};

export const deleteTratamiento = async (trat_id) => {
  const peticion = await fetch(`${URL_BACKEND}/tratamientos/${trat_id}`, {
    method: "DELETE",
  });
  const data = await peticion.json();
  return data;
};
```

![image](https://user-images.githubusercontent.com/73620785/115120693-6554a180-9f74-11eb-91ca-63cfa7d0eb56.png)
![image](https://user-images.githubusercontent.com/73620785/115120695-6980bf00-9f74-11eb-8234-d9134643b65e.png)
=======

# dental-backend

## Modelos

### REGISTRO DE PERSONAL VALORES

```
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
```

### Activar Activididad

```
  is_active = models.BooleanField(
    default=True
  )

  is_staff = models.BooleanField(
    default=False
  )
```

### Asignamos el comportamiento con el modelo

```
  objects = UsuarioManager()
```

### ahora definimos que columna será la encagada del login

```
  USERNAME_FIELD = 'personalCorreo'
```

### para solicitar los campos al momento de crear superusuario por consola

```
  REQUIRED_FIELDS = ['personalNombre', 'personalApellido', 'personalTipo']

  class Meta:
    db_table='t_personal'
    verbose_name = 'personal'
    verbose_name_plural = 'personales'
```

### Modelos de TRATAMIENTOS

```
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

```

### Modelos de PACIENTES

```
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
    null=False,
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

```

### Modelos de HOJA HISTORIAL CLINICO

```
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

```

### Modelos de CITAS

````
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

  )
```
