from distutils.command.upload import upload
from operator import mod
from django.db import models
from django.conf import settings
import os


class Blog(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=5, null=True)
    email = models.EmailField(default='')
    image = models.ImageField(upload_to='blog/', blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]

    def delete(self, *args, **kargs):
        if self.image:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
        super(Blog, self).delete(*args, **kargs)
