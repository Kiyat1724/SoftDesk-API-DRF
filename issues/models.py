from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

# Create your models here.


class Issue(models.Model):
    
    TAG_CHOICES = [
        ("BUG", "Bug"),
        ("FEATURE", "Feature"),
        ("TASK", "Task"),
    ]

    PRIORITY_CHOICES = [
        ("LOW", "Low"),
        ("MEDIUM", "Medium"),
        ("HIGH", "High"),
    ]

    STATUS_CHOICES = [
        ("TODO", "To Do"),
        ("IN_PROGRESS", "In Progress"),
        ("FINISHED", "Finished"),
    ]

    title = models.CharField(max_length=128)

    description = models.TextField()

    tag = models.CharField(
        max_length=20,
        choices=TAG_CHOICES
    )

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="issues"
    )

    author_user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="created_issues"
    )

    assignee_user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="assigned_issues"
    )
    
    created_time = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title