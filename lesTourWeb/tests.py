from django.test import TestCase
from django.urls import reverse
from .models import Usuario

message = "Hola Mundo"
name="Marcos Escobar"
#Test para la vista Hoteles
class HotelesTest(TestCase):
    def test_Hoteles_url(self): #Testea si la url se resuelve correctamente
        url = reverse('hoteles')
        respuesta = self.client.get(url)
        self.assertEqual(respuesta.status_code, 200)

    def test_hoteles_contenido(self): #testea si la vista muestra contenido correcto
        url = reverse('hoteles')
        respuesta = self.client.get(url)
        self.assertContains(respuesta, message)

#Test para la vista Personal
class PersonalTest(TestCase):
    def test_Personal_url(self): #Testea si la url se resuelve correctamente
        url = reverse('personal')
        respuesta = self.client.get(url)
        self.assertEqual(respuesta.status_code, 200)

    def test_personal_contenido(self): #testea si la vista muestra contenido correcto
        url = reverse('personal')
        respuesta = self.client.get(url)
        self.assertContains(respuesta, message)

#Test para la vista Usuarios
class UsuariosTest(TestCase):
    def test_Usuarios_url(self): #Testea si la url se resuelve correctamente
        url = reverse('usuarios')
        respuesta = self.client.get(url)
        self.assertEqual(respuesta.status_code, 200)

    def test_usuarios_contenido(self): #testea si la vista muestra contenido correcto
        url = reverse('usuarios')
        respuesta = self.client.get(url)
        self.assertContains(respuesta, message)

#Test para el modelo Reserva
class UsuarioTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configuración de datos de prueba que se aplican a todas las pruebas en la clase
        Usuario.objects.create(nombre=name, edad=25, telefono=986543682)

    def test_nombre_max_length(self):
        modelo = Usuario.objects.get(id=1)
        max_length = modelo._meta.get_field(name).max_length
        self.assertEquals(max_length, 100)

    def test_str_method(self):
        modelo = Usuario.objects.get(id=1)
        self.assertEquals(str(modelo), name)
