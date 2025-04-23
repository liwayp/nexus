from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import BlogSerializer 
from blog.models import Blog


@api_view(['GET', 'POST'])
def get_list_blog(request):
    if request.method == "GET":
        blog = Blog.objects.all()
        result = BlogSerializer(blog, many=True)
        print(result.data)
        return Response({"data": result.data})

    elif request.method == "POST":
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            result = serializer.save()
            return Response({'data': "success"}, status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def detail_blog(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response({'error': 'Could not found'}, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BlogSerializer(blog, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'Could not edit'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        blog.delete()
        return Response({'status': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)