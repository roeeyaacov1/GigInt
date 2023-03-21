from rest_framework import serializers
from .models import Review, Comment, Like


class ReviewSerializer(serializers.ModelSerializer):
    num_likes = serializers.IntegerField()
    class Meta:
        model = Review
        exclude = ('pub_date', )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
