from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from issues.models import Issue
from .models import Comment
from .serializers import (
    CommentListSerializer,
    CommentDetailSerializer,
)
from .permissions import (
    IsIssueContributor,
    IsCommentAuthorOrReadOnly,
)


class CommentViewSet(ModelViewSet):
    permission_classes = [
        IsAuthenticated,
        IsIssueContributor,
        IsCommentAuthorOrReadOnly,
    ]

    def get_serializer_class(self):
        if self.action == "list":
            return CommentListSerializer
        return CommentDetailSerializer

    def get_queryset(self):
        return Comment.objects.filter(
            issue_id=self.kwargs["issue_pk"],
            issue__project__contributors__user=self.request.user,
        ).distinct()

    def perform_create(self, serializer):
        issue = Issue.objects.get(
            pk=self.kwargs["issue_pk"]
        )
        serializer.save(
            author_user=self.request.user,
            issue=issue,
        )
