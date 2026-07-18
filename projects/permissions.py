from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsProjectAuthorOrReadOnly(BasePermission):
    """
    Tous les utilisateurs authentifiés peuvent consulter les projets.
    Seul l'auteur du projet peut le modifier ou le supprimer.
    """

    def has_permission(self, request, view):
        """
        Vérifie que l'utilisateur est authentifié.
        """
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Les méthodes de lecture (GET, HEAD, OPTIONS)
        sont autorisées pour tous les utilisateurs authentifiés.
        """
        if request.method in SAFE_METHODS:
            return True

        """
        Pour POST, PUT, PATCH et DELETE,
        seul l'auteur du projet est autorisé.
        """
        return obj.author_user == request.user