from django.contrib import admin
from .models import TratamientoModel,PacienteModel,HClinicaModel,CitaModel

admin.site.register(TratamientoModel)
admin.site.register(PacienteModel)
admin.site.register(HClinicaModel)
admin.site.register(CitaModel)

# Register your models here.

