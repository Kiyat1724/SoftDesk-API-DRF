from rest_framework import serializers
from .models import Project, Contributor


class ProjectListSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour afficher la liste des projets.
    """

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "type",
        ]


class ProjectDetailSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour afficher le détail d'un projet
    et pour les créations/modifications.
    """

    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = [
            "author_user",
            "created_time",
        ]


class ContributorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        fields = "__all__"
