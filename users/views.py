from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from Gigint.settings import logger
from reviews.serializers import ReviewSerializer, CommentSerializer
from reviews.models import Review, Comment
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # specify serializer to be used
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def get_user_summary(self, request, pk=None):
        user = get_object_or_404(User, id=pk)
        serializer = self.get_serializer(user)
        user_data = serializer.data
        logger.info(f"User1:  {user}")

        reviews = Review.objects.filter(user=user).annotate(num_comment=Count('comment'), num_likes=Count('likes'))
        review_serializer = ReviewSerializer(reviews, many=True)
        reviews_data = review_serializer.data

        comments = Comment.objects.filter(user=user).values()
        logger.info(comments)
        logger.warning(comments)
        comment_serializer = CommentSerializer(comments, many=True)
        comments_data = comment_serializer.data

        json_data = {'user': user_data, 'reviews': reviews_data, 'comments': comments_data}
        return Response(json_data)
