from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, ContributorViewSet

router = DefaultRouter()

router.register(
    r'projects',
    ProjectViewSet,
    basename='project'
)

router.register(
    r'contributors',
    ContributorViewSet,
    basename='contributor'
)

projects_router = routers.NestedDefaultRouter(
    router,
    r'projects',
    lookup='project'
)

urlpatterns = (
    router.urls +
    projects_router.urls
)