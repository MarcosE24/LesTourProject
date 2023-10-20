from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ReservaForm
from django.contrib.auth.decorators import login_required

def home(request):  #home view
    return render(request, "Home.html")

def signUp(request):    #register view
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
def signOut(request):   #logout function and show home view
    logout(request)
    return redirect("home")

def signIn(request):    #login view
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
def createReservation(request):
    if request.method == "GET":
        return render(request, "CreateReservation.html", {"form":ReservaForm})
    else:
        try:
            form= ReservaForm(request.POST)
            newReservation= form.save(commit= False)
            newReservation.save()
            #newReservation.user= request.user
            #print(newReservation)
            return render(request, "CreateReservation.html", {"form":ReservaForm})
        except ValueError:
            return render(request, "CreateReservation.html", {"form":ReservaForm, "error":"Ingrese datos validos porfavor"})