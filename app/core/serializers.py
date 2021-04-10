from rest_framework.serializers import ModelSerializer
from core.models import AbstractModel


class AbstractSerializer(ModelSerializer):
    
    class Meta:
        model = AbstractModel
        fields = ('id', 'urls')
        read_only_fields = ('id',)
