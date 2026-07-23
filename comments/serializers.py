from rest_framework import serializers
from .models import Comment


class CommentListSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour afficher la liste des commentaires.
    """

    class Meta:
        model = Comment
        fields = [
            "id",
            "description",
            "created_time",
        ]


class CommentDetailSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour afficher le détail d'un commentaire
    et pour les créations/modifications.
    """

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = [
            "author_user",
            "issue",
            "created_time",
        ]
