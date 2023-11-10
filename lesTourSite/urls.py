from django.contrib import admin
from django.urls import path,  include
from lesTourWeb import views

urlpatterns = [
    path("admin/", admin.site.urls),
    #path("",include("lesTourApp.urls")),
    path("", views.home, name="home"),
    path("signup/", views.signUp, name="signup"),
    path("reservation/", views.reservation, name="reservation"),
    path("logout/", views.signOut, name="logout"),
    path("signin/", views.signIn, name="signin"),
    path("reservation/create/", views.createReservation, name="createReservation"),


    ## inicio segunda parcial ##
    path("hoteles/", views.Hoteles, name="hoteles"),
    path("personal/", views.Personal, name="personal"),
    path("usuarios/", views.Usuarios, name="usuarios")
    
]