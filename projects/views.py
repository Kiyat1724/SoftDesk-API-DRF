from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Project, Contributor
from .permissions import IsProjectAuthorOrReadOnly
from .serializers import ProjectSerializer, ContributorSerializer


class ProjectViewSet(ModelViewSet):

    serializer_class = ProjectSerializer
    permission_classes = [
        IsAuthenticated,
        IsProjectAuthorOrReadOnly,
    ]

    def get_queryset(self):
        return Project.objects.filter(
            contributors__user=self.request.user
        ).distinct()

    def perform_create(self, serializer):
        serializer.save(author_user=self.request.user)


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
