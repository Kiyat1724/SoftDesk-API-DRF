from rest_framework import serializers
from .models import Project, Contributor
from.models import Issue   
from. models import Comment


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ["author_user", "created_time"]


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = "__all__"


class IssueSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Issue
        fields = "__all__"
        read_only_fields = ["author_user", "created_time"]


class CommentSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["author_user", "created_time"]