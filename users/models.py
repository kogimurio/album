from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    STATUS = (
        ('author', 'author'),
        ('family', 'family'),
        ('friends', 'friends'),
        ('public', 'public')
    )
    email = models.EmailField(unique=True)
    description = models.TextField(max_length=600, blank=True, default='')
    status = models.CharField(max_length=100, choices=STATUS, default='author')

    def __str__(self):
        return self.username
