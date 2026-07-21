from django.urls import path, include

from issues.urls import issues_router
from .views import CommentViewSet

issues_router.register(
    r'comments',
    CommentViewSet,
    basename='issue-comments'
)

urlpatterns = [
    path("", include(issues_router.urls)),
]