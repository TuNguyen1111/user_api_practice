from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.list_api, name='list-api'),
    path('create/', views.create_product, name='create-product'),
    path('update/<str:pk>/', views.update_product, name='update-product'),
]
