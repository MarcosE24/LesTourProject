from django import forms
from lesTourApp.models import Reservas

class ReservaForm(forms.ModelForm):
    class Meta:
        model= Reservas
        fields= ["checkin_date", "checkout_date", "room", "hotel", "observation", "cost"]
        widgets = {
            "checkin_date": forms.DateInput(attrs={
                "placeholder":"DD/MM/AAAA",
                "class":"w-full bg-gray-300 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 text-gray-900 dark:text-white sm:text-sm rounded-lg focus:ring-primary-600 block p-2.5"}),
            "checkout_date": forms.DateInput(attrs={
                "placeholder":"DD/MM/AAAA",
                "class":"w-full bg-gray-300 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 text-gray-900 dark:text-white sm:text-sm rounded-lg focus:ring-primary-600 block p-2.5"}),
            "room": forms.Select(attrs={
                "class":"w-full bg-gray-300 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 text-gray-900 dark:text-white sm:text-sm rounded-lg focus:ring-primary-600 block p-2.5"}),
            "hotel": forms.Select(attrs={
                "class":"w-full bg-gray-300 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 text-gray-900 dark:text-white sm:text-sm rounded-lg focus:ring-primary-600 block p-2.5"}),
            "observation": forms.Textarea(attrs={
                "class":"w-full h-20 bg-gray-300 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 text-gray-900 dark:text-white sm:text-sm rounded-lg focus:ring-primary-600 block p-2.5"}),
            "cost": forms.TextInput(attrs={
                "class":"w-full bg-gray-300 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 text-gray-900 dark:text-white sm:text-sm rounded-lg focus:ring-primary-600 block p-2.5"})
        }