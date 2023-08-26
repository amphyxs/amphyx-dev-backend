from rest_framework.routers import DefaultRouter

from apps.projects import views

router = DefaultRouter()
router.register(r'', views.ProjectViewSet)

urlpatterns = router.urls
