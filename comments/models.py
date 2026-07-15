from django.db import models
from django.contrib.auth.models import User
from issues.models import Issue
# Create your models here.


class Comment(models.Model):
    description = models.TextField()
    author_user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="created_comments"
    )
    issue = models.ForeignKey(
        Issue,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    created_time = models.DateTimeField(
        auto_now_add=True
    )
  
    def __str__(self):
        return f"Comment by {self.author_user.username}"