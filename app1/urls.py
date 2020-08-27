from django.urls import path
from app1 import views

urlpatterns = [
    path('app1/test', views.test, name='app1-test'),
    path('app1/', views.index, name='app1-index'),
    path('', views.home, name='app1-home'),
]
