from rest_framework.viewsets import ModelViewSet
from .models import Project, Contributor
from .serializers import ProjectSerializer, ContributorSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer


class ContributorViewSet(ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]