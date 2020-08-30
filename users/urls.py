from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
    path('form', views.userForm_view, name='form'),
]
