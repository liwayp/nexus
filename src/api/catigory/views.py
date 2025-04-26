from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import CategorySerializer 
from catigory.models import Category



@api_view(['GET', 'POST'])
def get_list_ctg(request):
    if request.method == "GET":
        categories = Category.objects.all()
        result = CategorySerializer(categories, many=True)
        return Response({"data": result.data})

    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            result = serializer.save()
            return Response({'data': "success"}, status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def detail_ctg(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({'error': 'Could not found'}, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(category, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'Could not edit'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response({'status': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    


class GetCategoryView(APIView):
    def get(self, request):
        category = Category.objects.all()
        result = CategorySerializer(category, many=True)
        return Response({"data": result.data})
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            result = serializer.save()
            return Response({'data': "OK"})
        else:
            return Response(serializer.errors)


class DetailCategoryView(APIView):
    
    def get_object(self,pk):
        category = get_object_or_404(Category, pk=pk)
        return category


    def get(self,request, pk ):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return Response({'data':'deleted'})