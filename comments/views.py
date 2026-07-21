from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Comment
from .serializers import CommentSerializer
from .permissions import (
    IsIssueContributor,
    IsCommentAuthorOrReadOnly,
)


class CommentViewSet(ModelViewSet):

    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthenticated,
        IsIssueContributor,
        IsCommentAuthorOrReadOnly,
    ]

    def get_queryset(self):
        return Comment.objects.filter(
            issue_id=self.kwargs["issue_pk"],
            issue__project__contributors__user=self.request.user,
        ).distinct()

    def perform_create(self, serializer):
        serializer.save(
            author_user=self.request.user,
            issue_id=self.kwargs["issue_pk"],
        )
