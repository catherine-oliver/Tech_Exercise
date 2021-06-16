# pages/urls.py
from django.urls import path
from .views import addPage
from .views import addTask
from .views import ryanBranchView

urlpatterns = [
    path('', addPage, name='addPage'),
    path('add-task/', addTask, name="addTask"),
    path('ryan-branch/', ryanBranchView, name='ryanBranch')
]