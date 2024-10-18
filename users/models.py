from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lesson_price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Vocabulary(models.Model):
    phrase = models.CharField(max_length=100, unique=True)
    translate = models.CharField(max_length=200, blank=True, null=True)
    examples = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.phrase
