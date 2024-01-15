# myroot/urls.py
from django.urls import path
from .views import welcome_view

app_name = 'myroot'

urlpatterns = [
    path('', welcome_view, name='welcome'),

]
