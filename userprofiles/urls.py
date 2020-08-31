from django.urls import path
from userprofiles import views

app_name = 'userprofiles'

urlpatterns = [
    path('register', views.register, name='register'),
    path('thank_you', views.thank_you, name='thank_you'),
    path('login', views.user_login, name='user_login'),
    path('logout', views.user_logout, name='user_logout'),
    path('', views.index, name='index'),
]
