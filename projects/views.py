from rest_framework.viewsets import ModelViewSet
from .models import Project, Contributor
from .serializers import ProjectSerializer, ContributorSerializer
# Create your views here.


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ContributorViewSet(ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer