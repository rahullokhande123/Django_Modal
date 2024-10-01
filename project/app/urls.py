from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('first/', views.first, name='first'),
    path('last/', views.last, name='last'),
    path('letest/', views.letest, name='letest'),
    path('earliast/', views.earliast, name='earliast')
]