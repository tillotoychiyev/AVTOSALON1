from tkinter.constants import CASCADE

from django.db import models
from django.core.validators import ValidationError, FileExtensionValidator
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"PK: {self.pk}. {self.name}"

class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    video = models.FileField('videos/', null=True, blank=True,
                             validators=[FileExtensionValidator(['mp4', 'avi','mov'])])
    text = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"PK: {self.pk}. {self.name}"


class Comment(models.Model):
    text = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username

    def __repr__(self):
        return f"PK: {self.pk}. {self.text}"


    # def clean(self):
    #     if self.price <= 0:
    #         raise ValidationError("Avtomobil narxi '0' dan katta bo'lishi shart!!!")
    #     if not self.name.islower():
    #         raise ValidationError("Avtomobil nomi kichik haflardan iborat bo'lishi kerak!!!")

