from django.db import models
from django.contrib.auth.models import User

class Reserva(models.Model):
    id_user= models.ForeignKey(User, on_delete=models.CASCADE)
    checkin_datetime= models.DateTimeField()
    checkout_datetime= models.DateTimeField()
    total_cost= models.IntegerField(default=0)
    request_datetime= models.DateTimeField(auto_now_add=True)
    id_room= models.IntegerField(default=0)
    observation= models.TextField(blank=True, max_length=500)