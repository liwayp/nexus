from django import forms 
from .models import Region

class RegionForm(forms.ModelField):
    class Meta:
        model = Region
        fields = '__all__'
