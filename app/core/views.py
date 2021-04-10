from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import AbstractModel
from core.serializers import AbstractSerializer


class AbstractViewSet(viewsets.ModelViewSet):
    serializer_class = AbstractSerializer
    queryset = AbstractModel.objects.all()


@api_view(['GET', 'POST'])
def get_related_urls(request):
    abstract = AbstractModel(
        urls = ['www.example.com']
    )
    serializer = AbstractSerializer(AbstractSerializer)

    return Response(serializer.data)
