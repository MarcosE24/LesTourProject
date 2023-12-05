from django.contrib import admin
from django.urls import path,  include
from lesTourWeb import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("signup/", views.signUp, name="signup"),
    path("reservation/", views.reservation, name="reservation"),
    path("logout/", views.signOut, name="logout"),
    path("signin/", views.signIn, name="signin"),
    path("reservation/create/", views.createReservation, name="createReservation"),
    path("hotels/", views.hoteles, name="hotels"),
    path("habitaciones_hotel/", views.habitaciones_hotel, name="habitaciones_hotel"),
    path("dashboard/", views.dashboard, name="dashboard")


]