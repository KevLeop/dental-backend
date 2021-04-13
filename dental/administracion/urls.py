from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="API - Sistema de Control Dental",
      default_version='v1',
      description="API para el manejo de citas e historias clinicas de un consultorio dental",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(name="Kevin Valverde", email='kevnleo93@gmail.com'),
      license=openapi.License(name='MIT', url="https://es.wikipedia.org/wiki/Licencia_MIT"),

   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


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