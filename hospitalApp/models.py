from django.db import models

# Create your models here.

# Doctor Table
class Doctor(models.Model):
    name=models.CharField(max_length=100)
    specialization=models.CharField(max_length=100)
    contact=models.CharField(max_length=15)
    profile=models.ImageField(upload_to='doctorimage/',blank=True)

    class Meta:
        db_table="doctor"

    def __str__(self):
        return f'{self.name}[{self.specialization}]'

# Patient Table
class Patient(models.Model):
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=10)
    contact=models.CharField(max_length=15)
    profile=models.ImageField(upload_to='patientimage/',blank=True)

    class Meta:
        db_table='patient'

    def __str__(self):
        return self.name

# Appoint Table
class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    description=models.TextField(blank=True)

    class Meta:
        unique_together=['doctor','date','time']

    
