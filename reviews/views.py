from django.db.models import Count
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

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
        queryset = self.queryset.annotate(num_comment=Count('comment'), num_likes=Count('likes'))
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

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
    def max_likes(self, request):
        liked_review = self.get_queryset().order_by('num_likes').last()
        serializer = self.get_serializer_class()(liked_review)
        return Response(serializer.data)


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().values()
    # specify serializer to be used
    serializer_class = CommentSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        return Response(data)
