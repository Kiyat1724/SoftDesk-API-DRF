from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Project(models.Model):
    PROJECT_TYPES = [
        ("BACKEND", "Backend"),
        ("FRONTEND", "Frontend"),
        ("IOS", "iOS"),
        ("ANDROID", "Android"),
    ]
    title = models.CharField(
        max_length=128
    )
    description = models.TextField()

    type = models.CharField(
        max_length=20,
        choices=PROJECT_TYPES
    )
    author_user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="created_projects"
    )
    created_time = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class Contributor(models.Model):
    
    ROLE_CHOICES = [
        ("AUTHOR", "Author"),
        ("CONTRIBUTOR", "Contributor"),
    ]

    PERMISSION_CHOICES = [
        ("READ", "Read"),
        ("WRITE", "Write"),
    ]
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="contributions"
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="contributors"
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )
    permission = models.CharField(
        max_length=20,
        choices=PERMISSION_CHOICES
    )
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "project"],
                name="unique_contributor_per_project"
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.project.title}"