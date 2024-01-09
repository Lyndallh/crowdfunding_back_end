from django.urls import path
from . import views

urlpatterns = [    
    path('projects/', views.ProjectList.as_view()),
    
    ]
