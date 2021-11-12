from rest_framework import authentication
from cart.models import Contents, Product
from .serializers import ContentsSerializer, ProductSerializer
from rest_framework import viewsets


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Product.objects.all()


class ContentsViewSet(viewsets.ModelViewSet):
    serializer_class = ContentsSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Contents.objects.all()
