from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "main/home.html")

def about(request):
    return render(request, "main/about.html")

def product(request):
    return render(request, "main/product.html")

def service(request):
    return render(request, "main/service.html") 