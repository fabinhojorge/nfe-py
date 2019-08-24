from rest_framework import serializers
from .models import Nfe


class NfeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nfe
        fields = ('access_key', 'xml', 'value', 'create_at', 'update_at', )
