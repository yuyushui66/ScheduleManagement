from django.urls import path
from . import views

urlpatterns = [
    path('helloApi/', views.HelloView.as_view()),
]

