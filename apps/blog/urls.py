from rest_framework.routers import DefaultRouter

from apps.blog import views

router = DefaultRouter()
router.register(r'posts', views.BlogPostViewSet)

urlpatterns = router.urls
