from django.db.models import Count
from rest_framework import serializers

from .models import Review, Comment
from food.serializers import FoodBasicSerializer


class ReviewSerializer(serializers.ModelSerializer):
    num_comment = serializers.IntegerField()
    num_likes = serializers.IntegerField()
    food = FoodBasicSerializer()

    # def get_food(self, obj):
    #     queryset = Food.objects.filter(name=obj.food).annotate(num_reviews=Count('review'))
    #     food_serializer = FoodSerializer(queryset, many=True)
    #
    #     return food_serializer.data

    class Meta:
        model = Review
        fields = ['food', 'user', 'title', 'description', 'likes', 'num_comment', 'num_likes']


class CommentSerializer(serializers.ModelSerializer):
    review = serializers.SerializerMethodField()

    def get_review(self, obj):
        queryset = Review.objects.filter(id=obj['review_id']).annotate(num_comment=Count('comment'),
                                                                       num_likes=Count('likes'))
        review_serializer = ReviewSerializer(queryset, many=True)

        return review_serializer.data

    class Meta:
        model = Comment
        fields = ['user', 'review', 'text', 'pub_date', 'likes']


class CommentBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'text', 'pub_date', 'likes']
