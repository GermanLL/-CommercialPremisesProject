from rest_framework import viewsets
# from rest_framework.decorators import action
# from rest_framework.response import Response
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Filtrado por Categoría
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)

        # Filtrado por nombre de producto
        search = self.request.query_params.get('search', None)
        if search is not None:
            queryset = queryset.filter(name__icontains=search) | queryset.filter(description__icontains=search)

        return queryset
    # @action(detail=False)
    # def by_category(self, request):
    #     category = self.request.query_params.get('category', None)
    #     products = Product.objects.filter(category=category)
    #     serializer = ProductSerializer(products, many=True)
    #     return Response(serializer.data)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


#class Productlist(generics.ListCreateAPIView):
#    queryset = Product.objects.all ()
#    serializer_class = ProductSerializer

#class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Product.objects.all()
#    serializer_class = ProductSerializer

