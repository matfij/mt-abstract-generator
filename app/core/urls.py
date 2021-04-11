from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import ResultPageViewSet, get_related_pages


router = DefaultRouter()
router.register('abstract', ResultPageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('core/pages/', get_related_pages),
]
