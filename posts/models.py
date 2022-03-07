from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=50, null=False)
    code = models.TextField(null=False)
    programming_language = models.CharField(max_length=20, null=False)
    date_posted = models.DateTimeField(default=datetime.now, null=False)
    programmer = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    comments = models.ManyToManyField('Comment', blank=True, related_name='post_comments')

    def __str__(self):
        return f'{self.title[:15]} in {self.programming_language}'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE)
    comment = models.TextField(null=False)

    def __str__(self):
        return f'{self.comment[:10]} - {self.user} - {self.post_}'
