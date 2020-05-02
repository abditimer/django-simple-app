from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    # example: /home/
    path('', views.home, name='home'),
]