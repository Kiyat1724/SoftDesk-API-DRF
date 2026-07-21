from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Project, Contributor
from .permissions import IsProjectAuthorOrReadOnly
from .serializers import (
    ProjectListSerializer,
    ProjectDetailSerializer,
    ContributorSerializer,
)


class ProjectViewSet(ModelViewSet):
   
    permission_classes = [
        IsAuthenticated,
        IsProjectAuthorOrReadOnly,
    ]

    def get_serializer_class(self):
        if self.action == "list":
            return ProjectListSerializer
        return ProjectDetailSerializer

    def get_queryset(self):
        return Project.objects.filter(
            contributors__user=self.request.user
        ).distinct()

    def perform_create(self, serializer):
        project = serializer.save(
            author_user=self.request.user
        )

        Contributor.objects.create(
            user=self.request.user,
            project=project,
            role="AUTHOR",
            permission="WRITE",
        )


class ContributorViewSet(ModelViewSet):

    serializer_class = ContributorSerializer
    permission_classes = [
        IsAuthenticated,
        IsProjectAuthorOrReadOnly,
    ]

    def get_queryset(self):
        return Contributor.objects.filter(
            project__contributors__user=self.request.user
        ).distinct()
