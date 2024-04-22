from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from django.template.defaultfilters import slugify


class CustomUser(AbstractUser):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("users", self.username, instance)
        return None

    STATUS = (
        ('author', 'author'),
        ('family', 'family'),
        ('friends', 'friends'),
        ('public', 'public')
    )
    email = models.EmailField(unique=True)
    description = models.TextField(max_length=600, blank=True, default='')
    status = models.CharField(max_length=100, choices=STATUS, default='author')
    image = models.ImageField(default='default/user.jpg', upload_to=image_upload_to)

    def __str__(self):
        return self.username
