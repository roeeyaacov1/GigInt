from rest_framework import serializers
from .models import Review, Comment
from food.serializers import FoodSerializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    pk = serializers.SerializerMethodField(method_name="get_id")
    num_comment = serializers.IntegerField()
    num_likes = serializers.IntegerField()
    food = FoodSerializer()

    #def get_id(self, object):
    #    return object.pk

    class Meta:
        model = Review
        fields = ['pk', 'food', 'user', 'title', 'description', 'likes', 'num_comment', 'num_likes']

