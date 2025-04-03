from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.product_list, name='home'),
    path('shop/create', views.product_create, name='product_create'),
    path('shop/<int:product_id>/', views.product_detail, name='product_detail'),
    path('shop/<int:product_id>/edit', views.product_update, name='product_update'),
    path('shop/<int:product_id>/delete', views.product_delete, name='product_delete'),
]