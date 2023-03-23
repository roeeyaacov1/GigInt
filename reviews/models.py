from datetime import datetime
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from food.models import Food


#class Like(models.Model):
#    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
#    object_id = models.PositiveIntegerField()
#    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#    content_object = GenericForeignKey('content_type', 'object_id')


# Create your models here.
class Review(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, blank=True, help_text="Food Review", null=True,
                             default=None)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True,
                             help_text="User that wrote this review")
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=datetime.now)
    likes = models.ManyToManyField(get_user_model(), related_name='review_likes', blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, db_constraint=False)
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=datetime.now)
    likes = models.ManyToManyField(get_user_model(), related_name='comment_likes', blank=True)
