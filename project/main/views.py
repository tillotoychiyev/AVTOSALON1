from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

from .models import Car, Category

def home(request: HttpRequest):
    categories = Category.objects.all()
    cars = Car.objects.all()

    context = {
        'cars':cars,
        'categories':categories
    }
    return render(request, 'main/index.html', context)

def car_by_category(request, category_id):
    categories = Category.objects.all()
    cars = Car.objects.filter(category_id=category_id)
    context = {
           'cars':cars,
           'categories':categories
    }
    return render(request, 'main/index.html', context)

def car_detail(request, car_id: int):
    car = Car.objects.get(id=car_id)
    context = {
        'car':car
    }
    return render(request, 'main/detail.html', context)

def about(request: HttpRequest):
    return render(request, 'main/about.html')
