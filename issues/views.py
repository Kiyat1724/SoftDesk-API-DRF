from rest_framework.viewsets import ModelViewSet
from .models import Issue
from .serializers import IssueSerializer
# Create your views here.


class IssueViewSet(ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
