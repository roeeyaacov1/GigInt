from django.db.models import Count
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from Gigint.settings import logger
from .models import Review, Comment
from .serializers import ReviewSerializer, CommentSerializer


# Create your views here.

class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    # specify serializer to be used
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = self.queryset.annotate(num_comment=Count('comments'), num_likes=Count('likes'))
        return queryset

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
    def max_likes(self, request):
        liked_review = self.get_queryset().order_by('num_likes').last()
        serializer = self.get_serializer_class()(liked_review)
        return Response(serializer.data)


class CommentsViewSet(viewsets.ModelViewSet):  # TODO: add review to create() comment
    queryset = Comment.objects.all().values()
    # specify serializer to be used
    serializer_class = CommentSerializer
