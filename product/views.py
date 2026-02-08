from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import *
from product.serializers import *
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from api.permissions import IsAdminOrReadOnly
from rest_framework.permissions import DjangoModelPermissions
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

class ProductViewSet(ModelViewSet):
    """Api Endpoint For managing products in the PhiMart"""
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    @swagger_auto_schema(
        operation_summary = 'Retrive a list of products'  
    )
    def list(self, request, *args, **kwargs):
        """Retrive All the products"""
        return super().list(request, *args, **kwargs)

class ProductImageViewSet(ModelViewSet):
    serializer_class = ProductImageSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        if getattr(self,'swagger_fake_view',False):
            return ProductImage.objects.none()
        return ProductImage.objects.filter(product_id=self.kwargs['product_pk'])
    
    def perform_create(self, serializer):
        serializer.save(product_id=self.kwargs.get('product_pk'))
class CategoryViewSet(ModelViewSet):
    permission_classes= [IsAdminOrReadOnly]
    queryset=Category.objects.annotate(
        product_count=Count('products')).all()
    serializer_class=CategorySerializer
    

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if getattr(self,'swagger_fake_view',False):
            return Review.objects.none()
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        if getattr(self,'swagger_fake_view',False):
            return super().get_serializer_context()
        return {'product_id': self.kwargs['product_pk']}

