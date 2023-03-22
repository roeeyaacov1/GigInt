from rest_framework import serializers
from .models import Review, Comment, Like


class ReviewSerializer(serializers.ModelSerializer):
    num_likes = serializers.IntegerField()
    pk = serializers.SerializerMethodField(method_name="get_id")

    def get_id(self, object):
        return object.pk

    class Meta:
        model = Review
        # exclude = ('pub_date', )
        fields = ('pk', 'food', 'user', 'title', 'description', 'num_likes')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
