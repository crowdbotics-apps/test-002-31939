from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ContentsViewSet, ProductViewSet

router = DefaultRouter()
router.register("product", ProductViewSet)
router.register("contents", ContentsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
