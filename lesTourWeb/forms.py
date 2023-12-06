from django import forms
from lesTourApp.models import Reservas

class ReservaForm(forms.ModelForm):
    class Meta:
        model= Reservas
        fields= ["checkin_date", "checkout_date", "room", "hotel", "observation", "cost"]
        css_classes = "w-full bg-gray-300 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 text-gray-900 dark:text-white sm:text-sm rounded-lg focus:ring-primary-600 block p-2.5"
        widgets = {
            "checkin_date": forms.DateInput(attrs={
            "placeholder": "DD/MM/AAAA",
            "class": css_classes
        }),
            "checkout_date": forms.DateInput(attrs={
                "placeholder":"DD/MM/AAAA",
                "class":"w-full bg-gray-300 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 text-gray-900 dark:text-white sm:text-sm rounded-lg focus:ring-primary-600 block p-2.5"}),
            "room": forms.Select(attrs={
                "class":css_classes}),
            "hotel": forms.Select(attrs={
                "class":css_classes}),            
            "observation": forms.Textarea(attrs={
                "class":css_classes}),
            "cost": forms.TextInput(attrs={
                "class":css_classes}),
        }