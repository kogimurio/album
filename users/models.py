from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    STATUS = (
        ('regular', 'regular'),
        ('subscriber', 'subscriber'),
        ('modarator', 'modarator')
    )
    email = models.EmailField(unique=True)
    description = models.TextField(max_length=600, blank=True, default='')
    status = models.CharField(max_length=100, choices=STATUS, default='regular')

    def __str__(self):
        return self.username
