from django.db.models import Count
from rest_framework import serializers

from .models import Review, Comment
from food.serializers import FoodBasicSerializer


class CommentBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'text', 'pub_date', 'likes']


class ReviewSerializer(serializers.ModelSerializer):
    comments = CommentBasicSerializer(many=True, read_only=True)
    num_comment = serializers.IntegerField()
    num_likes = serializers.IntegerField()
    food = FoodBasicSerializer()

    class Meta:
        model = Review
        fields = ['food', 'user', 'title', 'description', 'comments', 'likes', 'num_comment', 'num_likes']


class CommentSerializer(serializers.ModelSerializer):

    review = serializers.SerializerMethodField()

    def get_review(self, obj):
        queryset = Review.objects.filter(id=obj['review_id']).annotate(num_comment=Count('comments'),
                                                                       num_likes=Count('likes'))
        review_serializer = ReviewSerializer(queryset, many=True)

        return review_serializer.data

    class Meta:
        model = Comment
        fields = ['user', 'review', 'text', 'pub_date', 'likes']
