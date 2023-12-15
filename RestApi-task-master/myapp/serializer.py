from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'is_active')

class CategorySerializer(serializers.ModelSerializer):
    sub = serializers.SerializerMethodField()

    def get_sub(self, obj):
        mydata = Category.objects.filter(subcategory=obj)
        serializer = self.__class__(mydata, many=True)
        return serializer.data

    class Meta:
        model = Category
        fields = ('id', 'category_name', 'subcategory', 'sub')

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True,read_only = True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'category')
