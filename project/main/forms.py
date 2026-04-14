from django import forms

from .models import Car, Category

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        # fields = '__all__'
        # fields = ['name', 'text', 'price', 'image', 'category', 'published']
        exclude = ['views']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'published': forms.CheckboxInput(attrs={
                'class': 'checkbox-inline'
            })

        }