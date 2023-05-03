from django.urls import path
from . import views

urlpatterns = [
    path('scheduleApi/', views.ScheduleView.as_view()),
]

