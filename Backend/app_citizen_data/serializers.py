from rest_framework import serializers
from .models import *

class CitizenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citizen
        fields = ('name', 'surname', 'dob', 'email', 'address')