from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category,Review
from product.serializers import ProductSerializer,CategorySerializer,ReviewSerializer
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from api.permissions import IsAdminOrReadOnly
from rest_framework.permissions import DjangoModelPermissions
# Create your views here.

class ProductViewSet(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # permission_classes = [IsAdminOrReadOnly]
    permission_classes = [DjangoModelPermissions]


    def destroy(self,request,*args,**kwargs):
       product=self.get_object()
       if product.stock > 10 :
           return Response({'message': "Eta delete kora jabe na."})
       self.perform_destroy(product)
       return Response (status=status.HTTP_204_NO_CONTENT)
    
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
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}

