from rest_framework.viewsets import ModelViewSet
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]