from rest_framework.serializers import ModelSerializer
from core.models import ResultPageModel, AbstractModel


class ResultPageSerializer(ModelSerializer):
    
    class Meta:
        model = ResultPageModel
        fields = ['url', 'references', 'content', 'quality']


class AbstractSerializer(ModelSerializer):

    class Meta:
        model = AbstractModel
        fields = ['answer', 'summary']
