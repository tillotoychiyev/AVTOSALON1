from django.urls import path

from .views import home, about, car_detail, car_by_category, add_car, update_car, delete_car

urlpatterns = [
    path('', home, name='home'),
    path('category/<int:category_id>/', car_by_category, name='car_by_category'),
    path('about/', about, name='about'),
    path('car/<int:car_id>/', car_detail, name='detail'),
    path('car/<int:pk>/update/', update_car, name='update_car'),
    path('car/<int:pk>/delete/', delete_car, name='delete_car'),
    path('car/add/', add_car, name="add_car"),
]