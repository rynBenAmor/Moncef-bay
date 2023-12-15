# myroot/urls.py
from django.urls import path
from .views import welcome_view

urlpatterns = [
    path('', welcome_view, name='welcome'),
    # Additional URL patterns can be added here
]
