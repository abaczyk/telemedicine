"""Anna Baczyk 180849
Plik umozliwiajacy utworzenie strony glownej i podstron"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('statistics/', views.statistics, name='statistics'),
    path('data_exploration/', views.data_exploration, name='data_exploration'),
    path('general/', views.general, name='general'),
    path('patient/', views.patient, name='patient'),
    path('doctor/', views.doctor, name='doctor'),
    path('allgroups/', views.allGroups, name='allGroups'),
    path('thankYou/', views.thankYou, name='thankYou')
]
