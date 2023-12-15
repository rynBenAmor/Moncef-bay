from django.urls import path
from . import views  # Import your views module


app_name = 'products1'
urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
 ]