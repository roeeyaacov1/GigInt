from django.db import models


# Create your models here.
class User(models.Model):  # add user
    username = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
