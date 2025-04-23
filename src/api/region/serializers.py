from rest_framework import serializers 
from catigory.models import Region


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id','name', 'sorting']