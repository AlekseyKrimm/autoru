# main/urls.py
from django.urls import path
from . import views

app_name = 'main'  # Это важно для использования namespace

urlpatterns = [
    path('', views.home, name='home'),
    path('creators_list', views.creators_list, name='creators_list'),
    path('creators/<str:creator>/', views.creators_page, name='creators_page'),
    path('cars/<str:car>/', views.car_page, name='car_page'),  # Маршрут для страниц автомобилей
    path('catalog/', views.catalog, name='catalog'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('add-listing/', views.add_listing, name='add_listing'),
    path('validate-field/', views.validate_field, name='validate_field'),
]