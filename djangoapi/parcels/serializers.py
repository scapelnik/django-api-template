from rest_framework import serializers
from core.myLib.geoModelSerializer import GeoModelSerializer
from .models import Parcels, Parcels_Owners 

class ParcelsSerializer(GeoModelSerializer):                 # ← Deduje od GeoModelSerializer 
    """
    Serializer za parcele z geometrijsko validacijo.
    Parent class (GeoModelSerializer) že izvaja:
    - Snap to grid (WkbConversor)
    - ST_IsValid preverjanje
    - ST_Relate preverjanje prekrivanja
    """
    check_geometry_is_valid = True
    check_st_relation = True
    matrix9IM = 'T********'
    
    class Meta:
        model = Parcels
        fields = GeoModelSerializer.Meta.fields + ['parc_st', 'sifko', 'area']


class ParcelsOwnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcels_Owners
        fields = ['id', 'name', 'dni']
    
    def validate_name(self, value):
        if 'bad' in value.lower():
            raise serializers.ValidationError("The name can't contain 'bad'.")
        return value
