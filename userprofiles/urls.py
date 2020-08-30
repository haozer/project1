from django.urls import path
from userprofiles import views

app_name = 'userprofiles'

urlpatterns = [
    path('register', views.register, name='register'),
    path('thank_you', views.thank_you, name='thank_you'),
    path('', views.index, name='index'),
]
