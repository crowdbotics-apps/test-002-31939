from rest_framework import authentication
from cart.models import Content, Product
from .serializers import ContentSerializer, ProductSerializer
from rest_framework import viewsets


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Product.objects.all()


class ContentViewSet(viewsets.ModelViewSet):
    serializer_class = ContentSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Content.objects.all()
