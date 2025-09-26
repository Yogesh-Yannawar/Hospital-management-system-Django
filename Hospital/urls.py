"""
URL configuration for Hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from . import settings
from django.conf.urls.static import static
from hospitalApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.register,name='register'),
    path('login/',views.login_page,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.logout_view,name='logout'),
    path('add_doctor/',views.add_doctor,name='add_doctor'),
    path('update_doctor/<id>/',views.update_doctor,name='update_doctor'),
    path('delete_doctor/<id>/',views.delete_doctor,name='delete_doctor'),
    path('doctor_list/',views.view_doctor,name='doctor_list'),
    path('doctor_search/',views.doctor_search,name='doctor_search'),
    path('add_patient/',views.add_patient,name='add_patient'),
    path('update_patient/<id>/',views.update_patient,name='update_patient'),
    path('delete_patient/<id>/',views.delete_patient,name='delete_patient'),
    path('patient_list/',views.view_patient,name='patient_list'),
    path('patient_search/',views.patient_search,name='patient_search'),
    path('add_appoint/',views.add_appointment,name='add_appoint'),
    path('update_appoint/<id>/',views.update_appointment,name='update_appoint'),
    path('delete_appoint/<id>/',views.delete_appointment,name='delete_appoint'),
    path('view_appoint/',views.view_appointment,name='view_appoint'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
