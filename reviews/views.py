from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def reviews(request):
    return HttpResponse("Hello, world. You're at the reviews index.")

