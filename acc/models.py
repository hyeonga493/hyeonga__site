from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pic = models.ImageField(upload_to="user")
    comment = models.TextField()

    def getpic(self):
        if self.pic:
            return self.pic.url
        return "/media/noimage.png"
