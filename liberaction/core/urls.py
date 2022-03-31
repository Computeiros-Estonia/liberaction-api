from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('redirection/', views.service_vs_product_redirection, name='sp_redirection'),
    path('create_product/', views.create_product, name='create_product'),
    path('create_service/', views.create_service, name='create_service'),
    path('product/<int:pk>/', views.product_details, name='product'),
    path('edit_product/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),
]
