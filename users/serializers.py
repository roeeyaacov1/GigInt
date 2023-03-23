from rest_framework import serializers
from django.contrib.auth.models import User

from Gigint.settings import logger
from reviews.models import Review
from reviews.serializers import ReviewSerializer


class UserSerializer(serializers.ModelSerializer):
    #review = serializers.SerializerMethodField()
#
    #def get_review(self, obj):
    #    logger.info(obj['review_id'])
    #    queryset = Review.objects.filter(id=obj['review_id']).annotate(num_comment=Count('comment'),
    #                                                                   num_likes=Count('likes'))
    #    review_serializer = ReviewSerializer(queryset, many=True)
#
    #    return review_serializer.data
    class Meta:
        model = User
        fields = '__all__'
