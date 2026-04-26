from django import forms
from django.core.validators import ValidationError
from .models import Car, Category, Comment



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
        labels = {
            'name':'Nomi: ✏️',
            'price':'Narxi: 💵',
            'text':'Batafsil ma\'lumot ✏️',
            'image':'Avtomobil rasmi 🖼',
            'video':'Avtomobil haqida qisqa obzor🎬'
        }

    def clean_price(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('price')
        if price <= 0:
            raise ValidationError("Avtomobil narxi '0' dan katta bo'lishi shart!!!")
        return price

    def clean_name(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        if not name.islower():
            raise ValidationError("Avtomobil nomi kichik haflardan iborat bo'lishi kerak!!!")
        return name

class CommentForm(forms.Form):
    text = forms.CharField(max_length=500)