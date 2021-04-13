from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns=[
  path('pacientes', PacientesController.as_view()),
  path('pacientes/<str:dni>', PacienteController.as_view()),
  path('pacienteHclinicas/<str:dni>',PacienteHClinicasController.as_view()),
  path('tratamientos',TratamientosController.as_view()),
  path('tratamientos/<int:id>',TratamientoController.as_view()),
  path('hclinicas', HClinicasController.as_view()),
  path('hclinicas/<int:id>',HClinicaController.as_view()),
  path('pendientePago', HClinicasSinPagarController.as_view()),
  path('citas', CitasController.as_view()),
  path('citas/<int:id>', CitaController.as_view()),
  path('registro',RegistrarPersonalController.as_view()),
  path('login', TokenObtainPairView.as_view()),
  path('refresh-token',TokenRefreshView.as_view()),
  path('login-custom', CustomPayloadController.as_view()),
] 