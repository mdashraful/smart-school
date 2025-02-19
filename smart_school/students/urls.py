from django.urls import path
from .views import *

urlpatterns = [
    path('', student_list, name='student_list')
]
