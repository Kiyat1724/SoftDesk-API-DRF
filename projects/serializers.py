from rest_framework import serializers
from .models import Project, Contributor


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ["author_user", "created_time"]


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = "__all__"