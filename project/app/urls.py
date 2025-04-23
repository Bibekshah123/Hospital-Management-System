from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from .views import signup_view, login_view, logout_view

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    
    path('doctor/', DoctorListView.as_view(), name='doctor-list'),
    path('doctor/add/', DoctorCreateView.as_view(), name='doctor-add'),
    path('doctor/<int:pk>/delete/', DoctorDeleteView.as_view(), name='doctor-delete'),
    path('doctor/<int:pk>/update/', DoctorUpdateView.as_view(), name='doctor-update'),
    
    path('patient/', PatientListView.as_view(), name='patient-list'),
    path('patient/add/', PatientCreateView.as_view(), name='patient-add'),
    path('patient/<int:pk>/delete/', PatientDeleteView.as_view(), name='patient-delete'),
    path('patient/<int:pk>/update/', PatientUpdateView.as_view(), name='patient-update'),
    
    path('appointment/', AppointmentListView.as_view(), name='appointment-list'),
    path('appointment/add/', AppointmentCreateView.as_view(), name='appointment-add'),
    path('appointment/<int:pk>/delete/', AppointmentDeleteView.as_view(), name='appointment-delete'),
    path('appointment/<int:pk>/update/', AppointmentUpdateView.as_view(), name='appointment-update'),
    
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
