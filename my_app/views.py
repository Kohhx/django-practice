from django.http import HttpResponse
from django.shortcuts import render

# Create your views here (Function based).
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def about(request):
    return HttpResponse("My ABout page")


def hello(request, first_name):
    return HttpResponse(f"Hello {first_name}")
