from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= "Home"),
    path('single_product/', views.single_product, name = "single_product"),
    path('about/', views.about, name = "about"),
    path('checkout/', views.checkout, name = "checkout"),
    path('contact/', views.contact, name = "contact"),
    path('products/', views.products, name = "products"),
    path('cart/', views.cart, name = "cart"),
    path('update_item/', views.UpdateItem, name = "update_item"),
    path('register/', views.register, name = "register"),
    path('login/', views.loginPage, name = "login"),
    path('logout/', views.logoutPage, name = "logout"),
]

