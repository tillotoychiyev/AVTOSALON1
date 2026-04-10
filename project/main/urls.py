from django.urls import path

from .views import home, about, car_detail

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('car/<int:car_id>/', car_detail, name='detail'),
]