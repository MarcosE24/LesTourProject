from . import models
from django.contrib import admin
from .models import Ciudades, Clientes, Hoteles, Habitacion, TipoHabitacion, Cargo, Areas, Empleados, ReservaHuesped, Reservas

@admin.register(Ciudades)
class CiudadesAdmin(admin.ModelAdmin):
    ordering = ['nombre']

@admin.register(Empleados)
class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ('ci_numero', 'nombre', 'email', 'direccion', 'ciudad', 'telefono', 'cargo', 'hotel')
    list_filter = ('ciudad', 'cargo', 'hotel')
    ordering = ['nombre']

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    ordering = ['nombre']

@admin.register(Reservas)
class ReservasAdmin(admin.ModelAdmin):
    ordering = ['cliente']

@admin.register(Hoteles)
class HotelesAdmin(admin.ModelAdmin):
    ordering = ['nombre']

@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    ordering = ['numero']

@admin.register(TipoHabitacion)
class TipoHabitacionAdmin(admin.ModelAdmin):
    ordering = ['nombre']

@admin.register(ReservaHuesped)
class ReservaHuespedAdmin(admin.ModelAdmin):
    ordering = ['id_cliente']

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    ordering = ['nombre']

@admin.register(Areas)
class AreasAdmin(admin.ModelAdmin):
    ordering = ['nombre']
