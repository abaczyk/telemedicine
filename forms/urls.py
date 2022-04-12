from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('general', views.general),
    path('patient', views.patient),
    path('doctor', views.doctor),
    path('allgroups', views.allGroups)
]
