from django.urls import path

from .views import home, about, car_detail, car_by_category

urlpatterns = [
    path('', home, name='home'),
    path('category/<int:category_id>/', car_by_category, name='car_by_category'),
    path('about/', about, name='about'),
    path('car/<int:car_id>/', car_detail, name='detail'),
]