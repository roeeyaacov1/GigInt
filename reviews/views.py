from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponse
from .Serializer import ReviewSerializer, CommentSerializer, LikeSerializer
from .models import Review, Comment, Like
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import permissions


# Create your views here.

class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    # specify serializer to be used
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.annotate(num_likes=Count('comment'))

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data

        # Include related fields for author and publisher
        # data['comment'] = CommentSerializer(instance.comment).data
        # data['comment']['like'] = LikeSerializer(instance.comment.like).data
        return Response(data)

    @action(detail=True, methods=["GET"])
    def get_review_comments(self, request, pk):
        """
        Function returns all the comments connected to certain review
        """
        return Response(Comment.objects.filter(review__in=pk).values())


class CommentsViewSet(viewsets.ModelViewSet):
    #permission_classes = (permissions.AllowAny,)
    queryset = Comment.objects.all()

    # specify serializer to be used
    serializer_class = CommentSerializer


class LikesViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    # specify serializer to be used
    serializer_class = LikeSerializer
