from rest_framework import serializers
from .models import Issue


class IssueListSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour afficher la liste des issues.
    """

    class Meta:
        model = Issue
        fields = [
            "id",
            "title",
            "status",
            "priority",
        ]


class IssueDetailSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour afficher le détail
    d'une issue et pour les créations/modifications.
    """

    class Meta:
        model = Issue
        fields = "__all__"
        read_only_fields = [
            "author_user",
            "project",
            "created_time",
        ]