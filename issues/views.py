from rest_framework.viewsets import ModelViewSet
from .models import Issue
from .serializers import IssueSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class IssueViewSet(ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]
    serializer_class = IssueSerializer
