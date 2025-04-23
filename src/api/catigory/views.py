from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import CategorySerializer 
from catigory.models import Category


@api_view(['GET', 'POST'])
def get_list_ctg(request):
    if request.method == "GET":
        categories = Category.objects.all()
        result = CategorySerializer(categories, many=True)
        print(result.data)
        return Response({"data": result.data})

    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            result = serializer.save()
            print(result)
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
            print('serializer.data')
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'Could not edit'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response({'status': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)