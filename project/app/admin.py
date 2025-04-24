from django.contrib import admin
from .models import Doctor, Patient, Appointment
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization')
    search_fields = ('name', 'specialization')
    prepopulated_fields = {'slug': ('name',)}
    
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'disease')
    search_fields = ('name', 'disease')
    prepopulated_fields = {'slug': ('name',)}