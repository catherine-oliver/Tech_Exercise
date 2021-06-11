# pages/urls.py
from django.urls import path
from .views import addPage
from .views import addTask

urlpatterns = [
    path('', addPage, name='addPage'),
    path('add-task/', addTask, name="addTask")
]