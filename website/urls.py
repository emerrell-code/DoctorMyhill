from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('mypractice/', views.mypractice, name="mypractice"),
    path('myteam/', views.myteam, name="myteam"),
    path('find_us/', views.find_us, name="find_us"),
]