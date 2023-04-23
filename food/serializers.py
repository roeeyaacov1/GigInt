from rest_framework import serializers
from .models import Food


class FoodSerializer(serializers.ModelSerializer):
    num_reviews = serializers.IntegerField()
    pk = Food.pk

    class Meta:
        model = Food
        fields = ['pk', 'name', 'num_reviews', 'image']


class FoodBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['name', 'image']
