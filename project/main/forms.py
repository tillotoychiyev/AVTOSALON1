from django import forms

from .models import Car, Category

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'