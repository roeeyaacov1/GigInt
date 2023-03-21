from django.shortcuts import render
from django.http import HttpResponse
from .Serializer import ReviewSerializer, CommentSerializer, LikeSerializer
from .models import Review
from rest_framework import viewsets
from rest_framework.response import Response


# Create your views here.

class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    # specify serializer to be used
    serializer_class = ReviewSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.only("id")
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    # specify serializer to be used
    serializer_class = ReviewSerializer


class LikesViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    # specify serializer to be used
    serializer_class = ReviewSerializer
