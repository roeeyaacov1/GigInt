from django.db.models import Count, Max
from django.shortcuts import render
from django.http import HttpResponse
from .Serializer import ReviewSerializer, CommentSerializer
from .models import Review, Comment
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import permissions
from Gigint.settings import logger


# Create your views here.

class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    # specify serializer to be used
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    def get_queryset(self):
        queryset = self.queryset.annotate(num_comment=Count('comment'), num_likes=Count('likes'))
        #count_like = Review.objects.all()
        #queryset = queryset.annotate(num_likes=Count('likes'))
        return queryset

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data

        return Response(data)

    @action(detail=True, methods=["GET"])
    def get_review_comments(self, request, pk):
        """
        Function returns all the comments connected to certain review
        """
        return Response(Comment.objects.filter(review__in=pk).values())

    @action(detail=False, methods=["GET"])
    def most_commented_review(self, request):
        """
        Function returns the review with the most comments
        """
        commented_review = self.get_queryset().order_by('num_comment').last()
        serializer = self.get_serializer_class()(commented_review)
        return Response(serializer.data)

    @action(detail=False, methods=["GET"])
    def max_likes(self, request,):
        all_response = Response.object.all()
        return Response(Review.likes.count())


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().values()

    # specify serializer to be used
    serializer_class = CommentSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        return Response(data)

