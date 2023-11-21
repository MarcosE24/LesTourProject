from django import forms
from lesTourApp.models import Reservas

class ReservaForm(forms.ModelForm):
    class Meta:
        model= Reservas
        fields= ["checkin_date", "checkout_date", "room", "hotel", "observation", "cost"]
        widgets = {
            "id_user": forms.Select(attrs={"class":"w-full"}),
            "checkin_datetime": forms.DateTimeInput(attrs={"class":"w-full font-bold"}),
            "checkout_datetime": forms.DateTimeInput(attrs={"class":"w-full font-bold"}),
            "total_cost": forms.NumberInput(attrs={"class":"w-full font-bold"}),
            #"id_room": forms.Select(attrs={"class":"w-full font-bold"}),
            "observation": forms.Textarea(attrs={"class":"w-full font-bold"}),
        }