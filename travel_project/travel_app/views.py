from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def demo(request):
    return render(request, "index.html")


def index(request):
    return render(request, "index.html")


def news(request):
    return render(request, "news.html")


def contact(request):
    return render(request, "index.html")


def home(request):
    return render(request,"index.html")