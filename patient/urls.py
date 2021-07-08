from django.urls import path
from .views import *

urlpatterns=[
    path('',Home , name='home'),
    path('listpatient/' , PatientList.as_view() , name='listpatient1'),
    path('addpatient/', AddPatient.as_view(), name='addpatient'),
    path('updatepatient/',UpdatePatient.as_view(),name='updatepatient'),
    path('updatepatient/<pk>/',UpdatePatientpk.as_view(),name='updatepatientpk'),
    path('deletepatient/',DeletePatient.as_view(),name='deletepatient'),
    path('deletepatient/<pk>/',DeletePatientpk.as_view(),name='deletepatientpk'),



]