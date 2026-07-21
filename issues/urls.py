from django.urls import path, include
from rest_framework_nested import routers

from projects.urls import projects_router
from .views import IssueViewSet

projects_router.register(
    r'issues',
    IssueViewSet,
    basename='project-issues'
)

# Router imbriqué pour les commentaires
issues_router = routers.NestedDefaultRouter(
    projects_router,
    r'issues',
    lookup='issue'
)

urlpatterns = [
    path("", include(projects_router.urls)),
    path("", include(issues_router.urls)),
]