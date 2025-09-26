from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login,logout,update_session_auth_hash
from .models import Patient,Appointment,Doctor
from .forms import PatientForm,AppointmentForm,RegisterForm,DoctorForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request,'register_temp.html',context={'form':form,'errors':form.errors})
    form=RegisterForm()
    return render(request,'register_temp.html',context={'form':form})

def login_page(request):
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('dashboard')
        return render(request,'login_temp.html',context={'form':form,'errors':form.errors})
    form=AuthenticationForm()
    return render(request,'login_temp.html',context={'form':form}) 
    
@login_required(login_url='login')
def dashboard(request):
    return render(request,'dashboard.html')

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return render(request,'logout_temp.html')

def add_doctor(request):
    if request.method=='POST':
        form=DoctorForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
        return render(request,'add_doctor.html',content={'form':form,'errors':form.errors})
    form=DoctorForm()
    return render(request,'add_doctor.html',context={'form':form})

def update_doctor(request,id):
    data=Doctor.objects.get(id=id)
    if request.method=='POST':
        form=DoctorForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
        return render(request,'update_doctor.html',{'form':form,'errors':form.errors})
    form=DoctorForm(instance=data)
    return render(request,'update_doctor.html',{'form':form,'data':data})

def delete_doctor(request,id):
    data=Doctor.objects.get(id=id)
    data.delete()
    return redirect('doctor_list')
    
def view_doctor(request):
    qs=Doctor.objects.all()
    return render(request,'doctor_view.html',{'qs':qs})

def doctor_search(request):
    dname=request.GET.get('name')
    rec=Doctor.objects.filter(name__icontains=dname) if dname else Doctor.objects.all()
    return render(request,'doctor_view.html',{'qs':rec})

def add_patient(request):
    if request.method=='POST':
        form=PatientForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
        return render(request,'add_patient.html',content={'form':form,'errors':form.errors})
    form=PatientForm()
    return render(request,'add_patient.html',context={'form':form})

def update_patient(request,id):
    data=Patient.objects.get(id=id)
    if request.method=='POST':
        form=PatientForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
        return render(request,'update_patient.html',{'form':form,'errors':form.errors})
    form=PatientForm(instance=data)
    return render(request,'update_patient.html',{'form':form,'data':data})

def delete_patient(request,id):
    data=Patient.objects.get(id=id)
    data.delete()
    return redirect('patient_list')

def view_patient(request):
    qs=Patient.objects.all()
    return render(request,'patient_view.html',{'qs':qs})

def patient_search(request):
    dname=request.GET.get('name')
    qs=Patient.objects.filter(name__icontains=dname) if dname else Patient.objects.all()
    return render(request,'patient_view.html',{'qs':qs})

def add_appointment(request):
    qs=Doctor.objects.all()
    data=Patient.objects.all()
    if request.method=='POST':
        form=AppointmentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_appoint')
        return render(request,'add_appointment.html',{'form':form,'errors':form.errors})
    form=AppointmentForm()
    return render(request,'add_appointment.html',{'form':form,'qs':qs,'data':data})

def update_appointment(request,id):
    qs=Doctor.objects.all()
    data=Patient.objects.all()
    data1=Appointment.objects.get(id=id)
    if request.method=='POST':
        form=AppointmentForm(request.POST,request.FILES,instance=data1)
        if form.is_valid():
            form.save()
            return redirect('view_appoint')
        return render(request,'update_appointment.html',{'form':form,'errors':form.errors})
    form=AppointmentForm(instance=data1)
    return render(request,'update_appointment.html',{'form':form,'data1':data1,'qs':qs,'data':data})

def delete_appointment(request,id):
    data=Appointment.objects.get(id=id)
    data.delete()
    return redirect('view_appoint')

def view_appointment(request):
    qs=Appointment.objects.all()
    return render(request,'appointment_view.html',{'qs':qs})