from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import BlogSerializer 
from blog.models import Blog
from rest_framework.generics import GenericAPIView
from rest_framework import mixins


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
    



class BlogGenericAPIView(GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get(self, request):
        blogs = self.get_queryset()
        serializer = self.get_serializer(blogs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"data": 'uje est'}, status=status.HTTP_400_BAD_REQUEST)


class BlogGenericAPIViewPk(GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get(self, request, *args, **kwargs):
        blog = self.get_object()
        serializer = self.get_serializer(blog)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        blog = self.get_object()
        serializer = self.get_serializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"Error":" not edited"})

    def delete(self, request, *args, **kwargs):
        blog = self.get_object()
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class BlogMixinAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)   


class BlogMixinAPIViewPk(mixins.ListModelMixin, mixins.CreateModelMixin,  mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    





