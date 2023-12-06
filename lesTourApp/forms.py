from django import forms

#CONSTANTES

NOMBRE_LABEL = "Nombre:"
CORREO_LABEL = "Correo:"
DIRECCION_LABEL = "Direccion:"
TELEFONO_LABEL = "Telefono:"
CI_LABEL= "N° C.I.:"
CIUDAD_LABEL = "Ciudad:"
BARRIO_LABEL = "Barrio:"
NUM_PISOS_LABEL = "N° Pisos:"
NUM_HABITACIONES_LABEL = "N° Habitaciones:"

class RegisterCustomerForm(forms.Form):
    ci_numero=forms.IntegerField(label=CI_LABEL)
    nombre=forms.CharField(label=NOMBRE_LABEL)
    email=forms.CharField(label=CORREO_LABEL)
    direccion=forms.CharField(label=DIRECCION_LABEL)
    telefono=forms.IntegerField(label=TELEFONO_LABEL)

class RegisterEmployesForm(forms.Form):
    ci_numero=forms.IntegerField(label=CI_LABEL)
    nombre=forms.CharField(label=NOMBRE_LABEL)
    email=forms.CharField(label=CORREO_LABEL)
    direccion=forms.CharField(label=DIRECCION_LABEL)
    telefono=forms.IntegerField(label=TELEFONO_LABEL)

class RegisterHotelForm(forms.Form):
    nombre=forms.CharField(label=NOMBRE_LABEL)
    ciudad=forms.CharField(label=CIUDAD_LABEL)
    barrio=forms.CharField(label=BARRIO_LABEL)
    direccion=forms.CharField(label=DIRECCION_LABEL)
    telefono=forms.IntegerField(label=TELEFONO_LABEL)
    email=forms.CharField(label=CORREO_LABEL)
    pisos=forms.IntegerField(label=NUM_PISOS_LABEL)
    habitaciones=forms.IntegerField(label=NUM_HABITACIONES_LABEL)