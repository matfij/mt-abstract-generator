from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import  generate_abstract


router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('core/abstract/', generate_abstract),
]
