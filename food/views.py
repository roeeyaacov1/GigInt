from django.shortcuts import get_object_or_404
from rest_framework.decorators import action

from Gigint.settings import logger
from food.serializers import FoodSerializer
from rest_framework import viewsets
from rest_framework.response import Response

from reviews.Serializer import ReviewSerializer, CommentSerializer
from reviews.models import Review, Comment
from .models import Food


# Create your views here.

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    @action(detail=True, methods=['get'])
    def get_user_summary(self, request, pk=None):
        food = get_object_or_404(Food, id=pk)
        serializer = self.get_serializer(food)
        user_data = serializer.data
        logger.info(f"Food:  {food}")

        reviews = Review.objects.filter(food=food)
        logger.info(reviews)
        review_serializer = ReviewSerializer(reviews, many=True)
        logger.info(review_serializer.data)
        reviews_data = review_serializer.data

        comments = Comment.objects.filter(food=food)
        logger.info(comments)
        comment_serializer = CommentSerializer(comments, many=True)
        logger.info(comment_serializer.data)
        comments_data = comment_serializer.data

        logger.info(f"Reviews:  {comment_serializer.data}")
        json_data = {'user': user_data, 'reviews': reviews_data, 'comments': comments_data}

        return Response(json_data)
