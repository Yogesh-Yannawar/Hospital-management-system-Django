from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
from .models import Doctor,Patient,Appointment


# Doctor Form
class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields="__all__"

# Patient Form
class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields="__all__"

# Appointment Form
class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields="__all__"

# Registration Form
class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        



