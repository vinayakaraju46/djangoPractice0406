from django.urls import path
from . import views

urlpatterns = [
    path('getUser/', views.get_user),
    path('getStudent/', views.student_list),
    path('student/', views.student_details)
]