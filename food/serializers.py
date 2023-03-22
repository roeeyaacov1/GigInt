from rest_framework import serializers
from .models import Food


class FoodSerializer(serializers.ModelSerializer):
    num_reviews = serializers.IntegerField()

    class Meta:
        model = Food
        fields = ['name', 'num_reviews']
