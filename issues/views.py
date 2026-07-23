from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Issue
from .serializers import (
    IssueListSerializer,
    IssueDetailSerializer,
)

from .permissions import IsProjectContributor, IsIssueAuthorOrReadOnly


# create a viewset


class IssueViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.action == "list":
            return IssueListSerializer
        return IssueDetailSerializer

    permission_classes = [
        IsAuthenticated,
        IsProjectContributor,
        IsIssueAuthorOrReadOnly,
    ]

    def get_queryset(self):
        return Issue.objects.filter(
            project_id=self.kwargs["project_pk"],
            project__contributors__user=self.request.user
        ).distinct()

    def perform_create(self, serializer):
        serializer.save(
            author_user=self.request.user,
            project_id=self.kwargs["project_pk"]
        )
