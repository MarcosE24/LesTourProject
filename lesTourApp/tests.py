from django.test import TestCase
from django.urls import reverse

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
