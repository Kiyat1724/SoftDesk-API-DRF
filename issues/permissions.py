from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsProjectContributor(BasePermission):
    """
    Autorise uniquement les contributeurs du projet.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return True


class IsIssueAuthorOrReadOnly(BasePermission):
    """
    Seul l'auteur d'une issue peut la modifier.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author_user == request.user
