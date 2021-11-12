from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ContentViewSet, ProductViewSet

router = DefaultRouter()
router.register("product", ProductViewSet)
router.register("content", ContentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
