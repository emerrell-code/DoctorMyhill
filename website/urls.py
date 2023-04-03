from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('mypractice/', views.mypractice, name="mypractice"),
    path('myteam/', views.myteam, name="myteam"),
    path('find_us/', views.find_us, name="find_us"),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('address/', views.address, name="address"),
    path('website/<str:title>', views.entry, name="entry"),
    path('list/', views.list, name="list"),
    path('ecological/', views.ecological, name="ecological"),
    path('books/', views.books, name="books")
]