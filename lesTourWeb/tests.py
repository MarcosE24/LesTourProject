from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from . import views 
from .views import createReservation

class TestViews(TestCase):

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Home.html')

    def test_signUp_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
     #  self.assertTemplateUsed(response, 'signUp.html')

