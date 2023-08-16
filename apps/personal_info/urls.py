from rest_framework.routers import DefaultRouter

from apps.personal_info import views

router = DefaultRouter()
router.register(r'contact-links', views.ContactLinkViewSet)
router.register(r'hire-links', views.HireLinkViewSet)

urlpatterns = router.urls
