from django.db.models import query
from rest_framework.response import Response
from .serializers import *
from django.shortcuts import render
from rest_framework import generics, status

from .models import *

class PacientesController(generics.ListCreateAPIView):
  queryset=PacienteModel.objects.all()
  serializer_class = PacienteSerializer

  def get(self, request):
    resultado = self.serializer_class(instance=self.get_queryset(),many=True)
    return Response({
      'success':True,
      'content': resultado.data,
      'message':None
    })


  def post(self, request):
    resultado = self.serializer_class(data=request.data)
    if resultado.is_valid():
      resultado.save()
      return Response({
        'success':True,
        'content': resultado.data,
        'message': 'Paciente creado exitosamente'
      })
    else:
      return Response({
        'success':False,
        'content': resultado.errors,
        'message': 'Error al crear paciente'
      },status.HTTP_400_BAD_REQUEST)

class PacienteController(generics.RetrieveDestroyAPIView):
  queryset = PacienteModel.objects.all()
  serializer_class = PacienteSerializer

  def get_queryset(self,dni):
    return PacienteModel.objects.filter(pacienteDni=dni).first()

  def get(self, request, dni):
    paciente = self.get_queryset(dni)
    respuesta = self.serializer_class(instance=paciente)

    if paciente:
      return Response({
        'success':True,
        'content': respuesta.data,
        'message': 'Consulta exitosa'
      }, status.HTTP_200_OK)
    else:
      return Response({
        'success': False,
        'content':None,
        'message': 'ID de paciente no existe'
      },status.HTTP_400_BAD_REQUEST)

  def put(self, request, dni):
    paciente = self.get_queryset(dni)
    respuesta = self.serializer_class(instance=paciente,data=request.data)
    if respuesta.is_valid():
      resultado = respuesta.update()
      return Response({
        'success':True,
        'content':resultado,
        'message': 'Paciente actualizado exitosamente'
      })

    else:
      return Response({
        'success':False,
        'content': respuesta.errors,
        'message':'Data incorrecta'
      })

  def delete(self,request,dni):
    paciente = self.get_queryset(dni)
    if paciente:
      respuesta=self.serializer_class(instance=paciente)
      respuesta.delete()
      return Response({
        'success':True,
        'content':None,
        'message':'Se inhabilitó Paciente con DNI:%s' %(dni)
      })
    else:
      return Response({
        'success':False,
        'content':None,
        "message": 'Paciente no existe'
      })


class TratamientosController(generics.ListCreateAPIView):
  queryset = TratamientoModel.objects.all()
  serializer_class = TratamientoSerializer
  def get(self, request):
    resultado = self.serializer_class(instance=self.get_queryset(),many=True)
    return Response({
      'success':True,
      'content': resultado.data,
      'message':None
    })

  def post(self, request):
    resultado = self.serializer_class(data=request.data)
    if resultado.is_valid():
      resultado.save()
      return Response({
        'success':True,
        'content': resultado.data,
        'message': 'Tratamiento creado exitosamente'
      })
    else:
      return Response({
        'success':False,
        'content': resultado.errors,
        'message': 'Error al crear tratamiento'
      },status.HTTP_400_BAD_REQUEST)

class TratamientoController(generics.RetrieveUpdateDestroyAPIView):
  queryset = TratamientoModel.objects.all()
  serializer_class = TratamientoSerializer

  def get_queryset(self,id):
    return TratamientoModel.objects.filter(tratamientoId=id).first()

  def get(self,request,id):
    resultado = self.serializer_class(instance=self.get_queryset(id))
    return Response({
      'success':True,
      'content':resultado.data,
      'message': None
    })
  
  def put(self,request,id):
    tratamiento = self.get_queryset(id)
    respuesta = self.serializer_class(instance=tratamiento, data=request.data)
    if respuesta.is_valid():
      resultado = respuesta.update()
      return Response({
        'success':True,
        'content': resultado,
        'message': 'Tratamiento actualizado exitosamente'
      })
    else:
      return Response({
        'success':False,
        'content':respuesta.errors,
        'message': "Error al actualizar tratamiento"
      })
  
  def delete(self, request, id):
    tratamiento = self.get_queryset(id)
    if tratamiento:
      respuesta = self.serializer_class(instance=tratamiento)
      respuesta.delete()
      return Response({
        'success':True,
        'content':None,
        'message':'Se inhabilitó Tratamiento id:%s' %(id)
      })
    else:
      return Response({
        'success':False,
        'content':None,
        'message': 'Tratamiento no existe'
      })

    
class HClinicasController(generics.ListCreateAPIView):
  queryset = HClinicaModel.objects.all()
  serializer_class = HClinicaSerializer
  
  def get(self,request):
    resultado = self.serializer_class(instance=self.get_queryset(),many=True)
    return Response({
      'success':True,
      'content': resultado.data,
      'message':'OK'
    })


  def post(self,request):
    resultado = self.serializer_class(data=request.data)
    
    if resultado.is_valid():
      resultado.save()
      return Response({
        'success':True,
        'content': resultado.data,
        'message': 'Historia Clinica agregada exitosamente'
      })
    else:
      return Response({
        'success':False,
        'content': resultado.errors,
        'message': 'Error al crear historia clinica'
      }, status.HTTP_404_NOT_FOUND)
    

class HClinicaController(generics.RetrieveUpdateDestroyAPIView):
  queryset = HClinicaModel.objects.all()
  serializer_class = HClinicaSerializer

  def get_queryset(self,id):
    return HClinicaModel.objects.filter(hclinicaId=id).first()
    
      

  def get(self,request,id):
    hclinica=self.get_queryset(id)
    resultado = self.serializer_class(instance=hclinica)
    if(hclinica):
      return Response({
        'success':True,
        'content':resultado.data,
        'message':None
      })
    else:
      return Response({
        'success':False,
        'content': None,
        'message': 'ID no existe!'
      },status.HTTP_404_NOT_FOUND)

  def put(self,request,id):
    hclinica = self.get_queryset(id)
    respuesta = self.serializer_class(instance=hclinica,data=request.data)
    print(respuesta)
    if respuesta.is_valid():
      resultado = respuesta.update()
      return Response({
        'success':True,
        'content': resultado,
        'message': 'Historia Clinica actualizada!'
      })
    else:
      return Response({
        'success':False,
        'content':respuesta.errors,
        'message':"Data incorrecta"
      })

  def delete(self,request,id):
    hclinica = self.get_queryset(id)
    if (hclinica):
      hclinica.delete()
      return Response({
      'success':True,
      'content':None,
      'message':'Historia clinica {} eliminada'.format(id) 
      })
    else:
      return Response({
        'success':False,
        'content':None,
        'message':'Error al eliminar HistoriaClinica id: {} no existe'.format(id)
      })

class CitasController(generics.ListCreateAPIView):
  queryset = CitaModel.objects.all()
  serializer_class = CitaSerializer

  def get(self,request):
    resultado = self.serializer_class(instance=self.get_queryset(),many=True)
    return Response({
      'success':True,
      'content':resultado.data,
      'message':None
    })
      
  



      
