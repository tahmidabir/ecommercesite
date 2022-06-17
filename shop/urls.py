from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about/', views.about, name="AboutUS"),
    path('contact/', views.contact, name="ContactUS"),
    path('tracker/', views.tracker, name="TrackingStatus"),
    path('search/', views.search, name="Search"),
    path('productview/', views.prodView, name="ProductView"),
    path('checkout/', views.checkout, name="Checkout"),

]