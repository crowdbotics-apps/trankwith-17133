from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import TypeViewSet

router = DefaultRouter()
router.register("type", TypeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
