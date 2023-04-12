from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(null=True, blank=True)
    username = models.CharField(null=True,max_length=100, unique=True)
    following = models.IntegerField(null=True,)
    follower = models.IntegerField(null=True,)
    post = models.IntegerField(null=True,)

    def __str__(self):
        return f"{self.username}"