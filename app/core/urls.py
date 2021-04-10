from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import AbstractViewSet, get_related_urls


router = DefaultRouter()
router.register('abstract', AbstractViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('core/', get_related_urls),  # /api/core/
]
