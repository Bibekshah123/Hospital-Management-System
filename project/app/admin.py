from django.contrib import admin
from .models import Doctor, Patient, Appointment
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization')
    search_fields = ('name', 'specialization')
    
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'disease')
    search_fields = ('name', 'disease')
