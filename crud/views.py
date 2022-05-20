from django.http import request
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CategorySerializer
from .models import Category
# Create your views here.


"""
apiOverview is a method designed to serve as an index of the urls of this API
"""
@api_view(['GET'])
def apiOverview(request): 
    api_urls = {
        'List': '/category-list',
        'Create': '/category-create/',
        'Update': '/category-update/<str:pk>',
        'Delete': '/category-delete/<str:pk>',
    }
    return Response(api_urls)

# Read
@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

# Create
@api_view(['POST'])
def category_create(request):
    serializer = CategorySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# Update
@api_view(['POST'])
def category_update(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(instance=category, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# Delete

@api_view(['DELETE'])
def category_delete(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    
    return Response('Category Succesfully Deleted')