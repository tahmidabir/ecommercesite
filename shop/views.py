from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


# path('about/', views.about, name="AboutUS"),
# path('contact/', views.contact, name="ContactUS"),
# path('tracker/', views.tracker, name="TrackingStatus"),
# path('search/', views.search, name="Search"),
# path('productview/', views.prodView, name="Product"),
# path('checkout/', views.checkout, name="Checkout"),


def index(request):
    return render(request, 'shop/index.html')


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("contact")


def tracker(request):
    return HttpResponse("tracker")


def search(request):
    return HttpResponse("search")


def prodView(request):
    return HttpResponse("product view")


def checkout(request):
    return HttpResponse("checkout")
