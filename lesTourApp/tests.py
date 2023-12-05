from django.test import TestCase
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from .models import Ciudades, Hoteles, Areas, Cargo, Empleados, Clientes, Tipo_Habitacion, Habitacion, Reservas, Reserva_Huesped

#PRUEBAS PARA LAS URLS
class TestUrls(TestCase):
    def test_url_home(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_url_signup(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_url_reservation(self):
        url = reverse('reservation')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_url_signin(self):
        url = reverse('signin')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

#PRUEBAS PARA LOS MODELS
class TestModels(TestCase):
    def test_hoteles(self):
        # Crear un Hotel con todos los campos, incluyendo el nombre
        hotel = Hoteles.objects.create(
            nombre='Hotel',
            ciudad='Villarrica',
            barrio='Barrio San Juan',
            direccion='San Juan',
            telefono=123456789,
            email='test@gmail.com',
            pisos=5,
            habitaciones=50
        )
        # Verificar si se creó el hotel exitosamente
        self.assertIsNotNone(hotel)
        
    def test_ciudades(self):
        ciudad = Ciudades.objects.create(nombre='Iturbe')
        self.assertEqual(ciudad.nombre, 'Iturbe')

#PRUEBAS PARA LAS VISTAS
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')  # Crea un usuario para las pruebas

    def test_home_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Home.html')

    def test_signUp_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'SignUp.html')

    def test_reservation_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('reservation'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Reservation.html')

    def test_signOut_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirección después del cierre de sesión

    def test_signIn_view(self):
        response = self.client.get(reverse('signin'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'SignIn.html')

    def test_createReservation_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('createReservation'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'CreateReservation.html')

    def test_hoteles_view(self):
        response = self.client.get(reverse('hotels'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Hoteles.html')
