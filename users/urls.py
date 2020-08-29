from django.urls import path
from users import views

urlpatterns = [
    path('', views.index, name='users-index'),
    path('form', views.userForm_view, name='users-form'),
]
