from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import status
from catigory.models import Region
from .serializers import RegionSerializer

@api_view(['GET', 'POST'])
def get_list_regions(request):
    if request.method == "GET":
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True)
        return Response({"data": serializer.data})

    elif request.method == "POST":
        serializer = RegionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': "success"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET', 'PUT', 'DELETE'])
def detail_region(request, pk):
    try:
        region = Region.objects.get(pk=pk)
    except Region.DoesNotExist:
        return Response({'error': 'Region not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RegionSerializer(region)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RegionSerializer(region, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'Could not edit'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        region.delete()
        return Response({'status': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    


class GetRegion(APIView):
    def get(self, request):
        region = Region.objects.all()
        result = RegionSerializer(region, many=True)
        return Response({"data": result.data})
    


class DetailRegion(APIView):
    def get_object(self,pk):
        region = get_object_or_404(Region, pk=pk)
        return region


    def get (self, request, pk):
        region = self.get_object(pk)
        serializer = RegionSerializer(region)
        return Response(serializer.data)