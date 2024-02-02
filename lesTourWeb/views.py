from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ReservaForm
from django.contrib.auth.decorators import login_required
from lesTourApp.models import Hoteles, Habitacion, Reservas, TipoHabitacion, Empleados, Clientes
from datetime import datetime



#CONSTANTES TEMPLATE
SIGNUP_HTML_TEMPLATE = "signUp.html"
CREATE_RESERVATION_HTML_TEMPLATE = "CreateReservation.html"

def home(request):  #Home view
    return render(request, "Home.html")

def signUp(request):    #Register view
    if request.method == "GET":
        return render(
            request, 
            SIGNUP_HTML_TEMPLATE, 
            {"form": UserCreationForm})
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
                    SIGNUP_HTML_TEMPLATE,
                    {"form": UserCreationForm, "error": "El usuario ya existe"},
                )
        else:
            return render(
                request,
                SIGNUP_HTML_TEMPLATE,
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
        return render(request, CREATE_RESERVATION_HTML_TEMPLATE, {"form":ReservaForm})
    else:
        try:
            form = ReservaForm(request.POST) #Recover template data
            if form.is_valid(): #Validate with ReservaForm from forms.py
                new_reservation = form.save(commit=False) #"commit=false" to save the recovered data without committing to the DB
                new_reservation.cliente = request.user   #Assign the user who created the reservation, obtained from the login
                new_reservation.save()   #finally, commit to the DB
            return render(request, CREATE_RESERVATION_HTML_TEMPLATE, {"form":ReservaForm})
        except ValueError:
            return render(request, CREATE_RESERVATION_HTML_TEMPLATE, {"form":ReservaForm, "error":"Ingrese datos validos porfavor"})

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

# Decorador para restringir el acceso a administradores
def es_admin(user):
    return user.is_authenticated and user.is_staff  # Suponiendo que el admin es un staff

def dashboard(request):
    # Obtener recuentos de información
    total_hoteles = Hoteles.objects.count()
    total_habitaciones = Habitacion.objects.count()
    total_reservas = Reservas.objects.count()
    total_empleados = Empleados.objects.count()
    total_clientes = Clientes.objects.count()

    # Obtener información adicional si es necesario...

    return render(request, 'dashboard.html', {
        'total_hoteles': total_hoteles,
        'total_habitaciones': total_habitaciones,
        'total_reservas': total_reservas,
        'total_empleados': total_empleados,
        'total_clientes': total_clientes,
        # Otros datos que quieras mostrar en el dashboard
    })
    
def nosotros(request):
    # Puedes agregar lógica para obtener la información de la empresa aquí
    informacion_empresa = {
        'mision': 'Proporcionar experiencias de viaje inolvidables al ofrecer servicios de reserva de hoteles de alta calidad y en tiempo real.',
        'vision': 'Convertirnos en la principal plataforma de reservas de hoteles, reconocida por la excelencia en el servicio y la satisfacción del cliente.',
        'valores': ['Compromiso con la calidad', 'Atención al cliente excepcional', 'Innovación continua'],
        'historia': 'Fundada en el año 2023, LesTour ha estado comprometida con brindar a los viajeros opciones de hospedaje excepcionales desde nuestros inicios.',
        'equipo': [
            {'nombre': 'Micaela Lugo', 'puesto': 'Presidenta de LesTour'},
            {'nombre': 'Matias Arias', 'puesto': 'Director de Operaciones'},
            {'nombre': 'Marcela Dresler', 'puesto': 'Lic. Hoteleria y Turismo'},
        ],
        'contactos': {'telefono': '+595992 986-754', 'correo': 'reservaslestour@turismo.edu.py'},
    }

    return render(request, 'nosotros.html', {'informacion_empresa': informacion_empresa})
