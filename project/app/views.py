from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  
from django.views.generic.base import TemplateView
from .mixins import OwnerMixin


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'
    
def signup_view(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home') 
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')


class DoctorListView(LoginRequiredMixin, OwnerMixin, ListView):
    model = Doctor
    template_name = 'doctor_list.html'
    
class DoctorCreateView(LoginRequiredMixin, CreateView):
    model = Doctor
    template_name = 'doctor_form.html'
    fields = ['name', 'specialization']
    success_url = reverse_lazy('doctor-list')
    
class DoctorDeleteView(LoginRequiredMixin, DeleteView):
    model = Doctor
    template_name = 'doctor_delete.html'
    success_url = reverse_lazy('doctor-list')
    
class DoctorDetailView(LoginRequiredMixin,  DetailView):
    model = Doctor
    template_name = 'doctor_detail.html'
    context_object_name = 'doctor'
    
class DoctorUpdateView(LoginRequiredMixin, UpdateView):
    model = Doctor
    template_name = 'doctor_form.html'
    fields = ['name', 'specialization']
    success_url = reverse_lazy('doctor-list')

    
class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = 'patient_list.html'

class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    template_name = 'patient_form.html'
    fields = ['name', 'age', 'disease']
    success_url = reverse_lazy('patient-list')
    
class PatientDeleteView(LoginRequiredMixin, DeleteView):
    model = Patient
    template_name = 'patient_delete.html'
    success_url = reverse_lazy('patient-list')
    
class PatientUpdateView(LoginRequiredMixin, UpdateView):
    model = Patient
    template_name = 'patient_form.html'
    fields = ['name', 'age', 'disease']
    success_url = reverse_lazy('patient-list')

class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient
    template_name = 'patient_detail.html'
    context_object_name = 'patient'

    

class AppointmentListView(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'appointment_list.html'
    
class AppointmentCreateView(LoginRequiredMixin, CreateView):
    model = Appointment
    template_name = 'appointment_form.html'
    fields = ['doctor', 'patient', 'date']
    success_url = reverse_lazy('appointment-list')

class AppointmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Appointment
    template_name = 'appointment_delete.html'
    success_url = reverse_lazy('appointment-list')

class AppointmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Appointment
    template_name = 'appointment_form.html'
    fields = ['doctor', 'patient', 'date']
    success_url = reverse_lazy('appointment-list')
    
class AppointmentDetailView(LoginRequiredMixin, DetailView):
    model = Appointment
    template_name = 'appointment_detail.html'
    context_object_name = 'appointment'
