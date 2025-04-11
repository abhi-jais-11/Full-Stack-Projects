from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=500, unique=True)
    content = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    user_name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_name"
    )

    def __str__(self):
        return f"{self.title} | {self.user_name}"