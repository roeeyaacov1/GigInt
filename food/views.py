from food.serializers import FoodSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Food


# Create your views here.

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

