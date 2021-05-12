from rest_framework.serializers import ModelSerializer

from core.models import ResultPageModel, AbstractModel, KeyModel


class ResultPageSerializer(ModelSerializer):
    
    class Meta:
        model = ResultPageModel
        fields = ['url', 'references', 'content', 'quality']


class AbstractSerializer(ModelSerializer):

    class Meta:
        model = AbstractModel
        fields = ['answer', 'summary']


class KeySerializer(ModelSerializer):

    class Meta:
        model = KeyModel
        fields = '__all__'
