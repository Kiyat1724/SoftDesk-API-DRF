from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsIssueContributor(BasePermission):
    """
    Seuls les contributeurs du projet auquel appartient l'issue
    peuvent accéder aux commentaires.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


class IsCommentAuthorOrReadOnly(BasePermission):
    """
    Seul l'auteur d'un commentaire peut le modifier.
    """

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.author_user == request.user
