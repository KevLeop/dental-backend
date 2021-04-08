from django.urls import path
from .views import *

urlpatterns=[
  path('pacientes', PacientesController.as_view()),
  path('pacientes/<str:dni>', PacienteController.as_view()),
  path('tratamientos',TratamientosController.as_view()),
  path('tratamientos/<int:id>',TratamientoController.as_view()),
  path('hclinicas', HClinicasController.as_view()),
  path('hclinicas/<int:id>',HClinicaController.as_view())

]