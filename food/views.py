from django.db.models import Count
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from food.serializers import FoodSerializer, FoodBasicSerializer
from reviews.models import Review, Comment
from reviews.serializers import ReviewSerializer, CommentBasicSerializer
from .models import Food


# Create your views here.


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return FoodBasicSerializer
        return FoodSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(num_reviews=Count('review'))
        return queryset

    @action(detail=True, methods=['get'])
    def get_food_summary(self, request, pk=None):  # TODO: add user to comments response
        food = self.get_queryset().filter(id=pk).get()
        serializer = self.get_serializer(food)
        food_data = serializer.data

        reviews = Review.objects.filter(food=food).annotate(num_comment=Count('comments'), num_likes=Count('likes'))
        review_serializer = ReviewSerializer(reviews, many=True)
        reviews_data = review_serializer.data

        for index, review in enumerate(reviews):
            comments = Comment.objects.filter(review=review).values()
            comment_serializer = CommentBasicSerializer(comments, many=True)
            comments_data = comment_serializer.data
            reviews_data[index]['comments'] = comments_data

        json_data = {'food': food_data, 'reviews': reviews_data}
        return Response(json_data)
