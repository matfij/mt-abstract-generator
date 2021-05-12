from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import AbstractView, KeyView


router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('core/abstract/', AbstractView.as_view()),
    path('core/key/', KeyView.as_view()),
    path('core/key/<int:id>/', KeyView.as_view()),
]
