from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"PK: {self.pk}. {self.name}"

class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
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