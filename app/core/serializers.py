from rest_framework.serializers import ModelSerializer
from core.models import ResultPageModel


class ResultPageSerializer(ModelSerializer):
    
    class Meta:
        model = ResultPageModel
        fields = ['url', 'references', 'content', 'quality']
