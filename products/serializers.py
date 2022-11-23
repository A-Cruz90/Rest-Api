from rest_framework import serializers
from . import Product

class ProductSerializer(serializers.ModelSerializer):
   class Meta:
    model = Product 
    fields = [ 'id', 'title', 'description', 'price', 'inventory_quantity' ]