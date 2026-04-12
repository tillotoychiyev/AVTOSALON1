from django.shortcuts import render, redirect

from django.http import HttpRequest, HttpResponse

from .models import Car, Category
from .forms import CarForm

def home(request: HttpRequest):
    categories = Category.objects.all()
    cars = Car.objects.all()

    context = {
        'cars':cars,
        'categories':categories,
        'title': 'INOMARKA AVTOSALON'
    }
    return render(request, 'main/index.html', context)

def car_by_category(request, category_id):
    categories = Category.objects.all()
    category = Category.objects.get(id=category_id)
    cars = Car.objects.filter(category=category)
    context = {
        'cars':cars,
        'categories':categories,
        'title':category.name
    }
    return render(request, 'main/index.html', context)

def car_detail(request, car_id: int):
    categories = Category.objects.all()
    car = Car.objects.get(id=car_id)
    context = {
        'categories':categories,
        'car':car,
        'title':car.name
    }
    return render(request, 'main/detail.html', context)

def add_car(request: HttpRequest):
    if request.method == 'POST':
        form = CarForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            car = form.save()
            return redirect('detail', car_id=car.id)
    form = CarForm()
    context = {
        'form':form
    }
    return render(request, 'main/add_car.html', context)

def about(request: HttpRequest):
    return render(request, 'main/about.html')
