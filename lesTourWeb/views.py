from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ReservaForm
from django.contrib.auth.decorators import login_required
from lesTourApp.models import Hoteles, Habitacion, Reservas, Tipo_Habitacion
from datetime import datetime

def home(request):  #Home view
    return render(request, "Home.html")

def signUp(request):    #Register view
    if request.method == "GET":
        return render(request, "SignUp.html", {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            # Register user
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                return redirect("reservation")
            except IntegrityError:
                return render(
                    request,
                    "SignUp.html",
                    {"form": UserCreationForm, "error": "El usuario ya existe"},
                )
        else:
            return render(
                request,
                "SignUp.html",
                {"form": UserCreationForm, "error": "Las contraseñas no coinciden"},
            )

def reservation(request):   #hay que ver que hacer con esta vista, si mostrar las reservas y el historial o quitarla
    return render(request, "Reservation.html")

@login_required
def signOut(request):   #Logout function and show home view
    logout(request)
    return redirect("home")

def signIn(request):    #Login view
    if request.method == "GET":
        return render(request, "SignIn.html", {"form":AuthenticationForm})
    else:
        user= authenticate(request, username=request.POST["username"], password=request.POST["password"])
        print(request.POST)
        if user is None:
            return render(request, "SignIn.html",{"form":AuthenticationForm, "error":"Usuario o Contraseña Incorrectos"})
        else:
            login(request, user)
            return redirect("reservation")

@login_required
def createReservation(request): #View that renders the page in "GET" and saves the reservation data in "POST"
    if request.method == "GET":
        return render(request, "CreateReservation.html", {"form":ReservaForm})
    else:
        try:
            form = ReservaForm(request.POST) #Recover template data
            if form.is_valid(): #Validate with ReservaForm from forms.py
                newReservation = form.save(commit=False) #"commit=false" to save the recovered data without committing to the DB
                newReservation.cliente = request.user   #Assign the user who created the reservation, obtained from the login
                newReservation.save()   #finally, commit to the DB
            return render(request, "CreateReservation.html", {"form":ReservaForm})
        except ValueError:
            return render(request, "CreateReservation.html", {"form":ReservaForm, "error":"Ingrese datos validos porfavor"})

def hoteles(request):
    hoteles = Hoteles.objects.all()  # Recupera todos los registros de la tabla Hoteles
    return render(request, 'Hoteles.html', {'hoteles': hoteles})




def habitaciones_hotel(request):
    hoteles = Hoteles.objects.all()
    hotel_id = request.GET.get('hotel', None)
    habitaciones = Habitacion.objects.all()

    if hotel_id:
        habitaciones = habitaciones.filter(id_hotel=hotel_id)

    return render(request, 'habitaciones_hotel.html', {'habitaciones': habitaciones, 'hoteles': hoteles})

