from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('general/', views.general, name='general'),
    path('patient/', views.patient, name='patient'),
    path('doctor/', views.doctor, name='doctor'),
    path('allgroups/', views.allGroups, name='allGroups')
]
