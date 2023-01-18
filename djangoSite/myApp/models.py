from django.contrib.auth.models import User
from django.db import models



class Fweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="names", null=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.content
