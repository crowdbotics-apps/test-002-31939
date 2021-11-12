from rest_framework import serializers
from cart.models import Contents, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ContentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contents
        fields = "__all__"
