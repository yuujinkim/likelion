from operator import mod
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=5, null=True)
    email = models.EmailField(default='')

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]
