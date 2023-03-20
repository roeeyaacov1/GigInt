from food.serializers import FoodSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Food


# Create your views here.

class FoodViewSet(viewsets.ViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def create(self, request, *args, **kwargs):
        pass

    def retrieve(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        pass

    def list(self, request, *args, **kwargs):
        pass

    def partial_update(self, request, *args, **kwargs):
        pass
