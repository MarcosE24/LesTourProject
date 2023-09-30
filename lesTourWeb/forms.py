from django.forms import ModelForm
from .models import Reserva

class ReservaForm(ModelForm):
    class Meta:
        model= Reserva
        fields= ["id_user", "checkin_datetime", "checkout_datetime", "total_cost", "id_room", "observation"]