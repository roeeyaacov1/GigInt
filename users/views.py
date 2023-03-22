from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from Gigint.settings import logger
from reviews.Serializer import ReviewSerializer
from reviews.models import Review
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # specify serializer to be used
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def get_user_summary(self, request, pk=None):
        user = get_object_or_404(User, id=pk)
        serializer = self.get_serializer(user)
        data = serializer.data
        logger.info(f"User:  {user}")

        reviews = Review.objects.all() # filter(user=user)
        review_serializer = ReviewSerializer(reviews)
        data += review_serializer.data
        logger.info(f"Reviews:  {review_serializer.data}")

        return Response(data)
