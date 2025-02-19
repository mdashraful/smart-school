from django.contrib import admin
from django.urls import path, include
from smart_school.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('students/', include('students.urls'))
]
