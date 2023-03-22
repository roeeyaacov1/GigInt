from django.db.models import Count
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

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(num_reviews=Count('review'))
        return queryset

    @action(detail=True, methods=['get'])
    def get_food_summary(self, request, pk=None):
        food = get_object_or_404(Food, id=pk)
        serializer = self.get_serializer(food)
        food_data = serializer.data
        logger.info(f"Food:  {food}")

        reviews = Review.objects.filter(food=food)
        logger.info(reviews)
        review_serializer = ReviewSerializer(reviews, many=True)
        logger.info(review_serializer.data)
        reviews_data = review_serializer.data

        for review in reviews:
            comments = Comment.objectcs.filter(review=review)
            comment_serializer = CommentSerializer(comments, many=True)
            logger.info(comment_serializer.data)
            comments_data = comment_serializer.data
            reviews_data[review].append('comments': comments_data)


        # logger.info(f"Reviews:  {comment_serializer.data}")
        json_data = {'food': food_data, 'reviews': reviews_data, 'comments': comments_data}
        # json_data = {'food': food_data, 'reviews': reviews_data}
        # json_data = {'food': food_data, 'comments': comments_data}
        return Response(json_data)
