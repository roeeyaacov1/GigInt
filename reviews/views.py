from django.shortcuts import render
from django.http import HttpResponse
from .Serializer import ReviewSerializer, CommentSerializer, LikeSerializer
from .models import Review
from rest_framework import viewsets


# Create your views here.

class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    # specify serializer to be used
    serializer_class = ReviewSerializer

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    # specify serializer to be used
    serializer_class = ReviewSerializer


class LikesViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    # specify serializer to be used
    serializer_class = ReviewSerializer
