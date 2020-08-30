from django.urls import path
from app1 import views

app_name = 'app1'

urlpatterns = [
    path('app1/test', views.test, name='test'),
    path('app1/', views.index, name='index'),
    path('app1/form', views.form, name='form'),
    path('app1/topics', views.topics, name='topics'),
    path('', views.home, name='home'),
]
