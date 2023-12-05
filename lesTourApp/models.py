from django.db import models
from django.contrib.auth.models import User

class Ciudades(models.Model): # tabla para registrar las ciudades de los empeados
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Ciudades"

class Hoteles(models.Model): #tabla para registrar hoteles
    nombre=models.CharField(max_length=200)
    ciudad=models.CharField(max_length=200)
    barrio=models.CharField(max_length=200)
    direccion=models.CharField(max_length=100)
    telefono=models.IntegerField()
    email=models.CharField(max_length=100)
    pisos=models.IntegerField()
    habitaciones=models.IntegerField()
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Hoteles"

class Areas(models.Model): #tabla para registrar las areas o departamentos dentro del hotel
    nombre=models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Areas"

class Cargo(models.Model): #tabla para registrar los cargos que se encuentran en cada area
    nombre=models.CharField(max_length=100)
    id_area=models.ForeignKey(Areas, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Cargos"

class Empleados(models.Model): #tabla para registrar empleados
    ci_numero=models.IntegerField()
    nombre=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    ciudad = models.ForeignKey(Ciudades, on_delete=models.CASCADE)
    telefono=models.IntegerField()
    cargo=models.ForeignKey(Cargo,on_delete=models.CASCADE)
    hotel=models.ForeignKey(Hoteles, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Empleados"

class Clientes(models.Model): #tabla para registrar clientes
    ci_numero=models.IntegerField()
    nombre=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    telefono=models.IntegerField()
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Clientes" 

class Tipo_Habitacion(models.Model): #tabla para registrar los tipos de habitaciones
    nombre=models.CharField(max_length=100)
    capacidad=models.IntegerField()
    costo=models.IntegerField()
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Tipo_Habitaciones"

class Habitacion(models.Model): #tabla para registrar las habitaciones
    numero=models.IntegerField()
    piso=models.IntegerField()
    id_tipo_habitacion=models.ForeignKey(Tipo_Habitacion, on_delete=models.CASCADE)
    id_hotel=models.ForeignKey(Hoteles, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id_tipo_habitacion) + ": \"" + str(self.id_hotel) + "\""    #Devuelve el nombre y el hotel
    class Meta:
        verbose_name_plural = "Habitaciones"

class Reservas(models.Model): #tabla para registrar las reservas
    cliente=models.ForeignKey(User, on_delete=models.CASCADE)
    checkin_date=models.DateField(blank=False)
    checkout_date=models.DateField(blank=False)
    room= models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    hotel=models.ForeignKey(Hoteles, on_delete=models.CASCADE)
    observation= models.TextField(blank=True, max_length=500)
    cost=models.CharField(max_length=10, blank=False)
    request_datetime= models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Reservas"

class Reserva_Huesped(models.Model): #tabla para registrar mas de un huesped a una reserva
    id_cliente=models.ForeignKey(Clientes, on_delete=models.CASCADE)
    id_reserva=models.ForeignKey(Reservas, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Reserva_Huespedes"