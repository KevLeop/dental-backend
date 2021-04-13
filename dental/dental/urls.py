"""dental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
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


urlpatterns = [
    path('',schema_view.with_ui('swagger')),
    path('redoc',schema_view.with_ui('redoc')),
    path('admin/', admin.site.urls),
    path('',include('administracion.urls')),]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
