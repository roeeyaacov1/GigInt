from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def food(request):
    return HttpResponse("Hello, world. You're at the foods index.")

