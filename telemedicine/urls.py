"""Anna Baczyk 180849, Bartosz Czapla 181486"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('forms.urls')),
    path('admin/', admin.site.urls),
]
