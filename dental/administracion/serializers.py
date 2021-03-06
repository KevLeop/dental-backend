from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegistroSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)
  def save (self):
    personalCorreo = self.validated_data.get('personalCorreo')
    personalTipo = self.validated_data.get('personalTipo')
    personalNombre = self.validated_data.get('personalNombre')
    personalApellido = self.validated_data.get('personalApellido')
    password = self.validated_data.get('password')
    is_staff = False

    nuevoPersonal = PersonalModel(
      personalCorreo=personalCorreo,
      personalTipo=personalTipo,
      personalNombre=personalNombre,
      personalApellido=personalApellido,
      is_staff = is_staff
    )
    nuevoPersonal.set_password(password)
    nuevoPersonal.save()
    return nuevoPersonal

  class Meta:
    model = PersonalModel
    exclude = ['groups','user_permissions']


class CustomPayloadSerializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls,user):
    token = super(CustomPayloadSerializer,cls).get_token(user)
    token['personalTipo']=user.personalTipo
    token['personalCorreo'] = user.personalCorreo
    
    return token



class PacienteSerializer(serializers.ModelSerializer):  
  def update(self): 
    self.instance.pacienteNombre = self.validated_data.get('pacienteNombre')
    self.instance.pacienteApellido = self.validated_data.get('pacienteApellido')
    self.instance.pacienteFnacimiento = self.validated_data.get('pacienteFnacimiento')
    self.instance.pacienteSexo = self.validated_data.get('pacienteSexo')
    self.instance.pacienteTelefono = self.validated_data.get('pacienteTelefono')
    self.instance.pacienteEmail = self.validated_data.get('pacienteEmail')
    self.instance.pacienteEstado = self.validated_data.get('pacienteEstado')
    self.instance.pacienteGSanguineo = self.validated_data.get('pacienteGSanguineo')
    # self.instance.pacienteImagen = self.validated_data.get('pacienteImagen')
    
    

    self.instance.save()
    return self.data

  def delete(self):
    # Crear campo estado en modelo paciente
    self.instance.pacienteEstado = False
    self.instance.save()
    return self.data
  
  class Meta:
    model = PacienteModel
    fields = '__all__'


class TratamientoSerializer(serializers.ModelSerializer):
  def update(self):
    self.instance.tratamientoNombre = self.validated_data.get('tratamientoNombre')
    self.instance.tratamientoDescripcion = self.validated_data.get('tratamientoDescripcion')
    self.instance.tratamientoEstado = self.validated_data.get('tratamientoEstado')

    self.instance.save()
    return self.data
  
  def delete(self):
    self.instance.tratamientoEstado = False
    self.instance.save()
    return self.data

  class Meta:
    model = TratamientoModel
    fields= '__all__'

class HClinicaSinPagar(serializers.ModelSerializer):
  
  class Meta:
    model = HClinicaModel
    fields = '__all__'

class HClinicaSerializer(serializers.ModelSerializer):
  # paciente = PacienteSerializer()
  # tratamiento = TratamientoSerializer()
  def update(self):
    self.instance.hclinicaFecha = self.validated_data.get('hclinicaFecha')
    self.instance.hclinicaDiagnostico = self.validated_data.get('hclinicaDiagnostico')
    self.instance.hclinicaProblema = self.validated_data.get('hclinicaProblema')
    self.instance.hclinicaPrecio = self.validated_data.get('hclinicaPrecio')
    self.instance.hclinicaPagado = self.validated_data.get('hclinicaPagado')
    self.instance.paciente = self.validated_data.get('paciente')
    self.instance.tratamiento = self.validated_data.get('tratamiento')
    self.instance.save()
    return self.data

  class Meta:
    model= HClinicaModel
    fields='__all__'

class PacienteHClinicasSerializer(serializers.ModelSerializer):
  hClinicas = HClinicaSerializer(source = 'hcPaciente', many=True )
  class Meta:
    model = PacienteModel
    fields = ["pacienteDni","hClinicas"]

class CitaSerializer(serializers.ModelSerializer):
  def update(self):
    self.instance.citaTitulo = self.validated_data.get('citaTitulo')
    self.instance.citaFechaInicio = self.validated_data.get('citaFechaInicio')
    self.instance.citaFechaFin = self.validated_data.get('citaFechaFin')
    self.instance.citaEstado = self.validated_data.get('citaEstado')
    self.instance.paciente = self.validated_data.get('paciente')
    self.instance.save()
    return self.data
  class Meta:
    model= CitaModel
    fields='__all__'