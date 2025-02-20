from django.urls import path
from .views import *

urlpatterns = [
    path('', student_list, name='student_list'),
    path('<int:pk>/edit/', student_update, name='student_update'),
    path('<int:pk>/delete/', student_delete, name='student_delete')
]
