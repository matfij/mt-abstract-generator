import json
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin

from core.models import GenerateAbstractParams, KeyModel
from core.serializers import AbstractSerializer, KeySerializer
from core.services import CoreService
from core.wrappers import is_authorized, key_required


class AbstractView(GenericAPIView, CreateModelMixin):

    # @key_required
    def post(self, request):
        body = json.loads(request.body)
        params = GenerateAbstractParams(body)

        service = CoreService()
        abstract = service.generate_abstract(params)

        serializer = AbstractSerializer(abstract)
        return Response(serializer.data)


class KeyView(GenericAPIView, CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin):
    serializer_class = KeySerializer
    queryset = KeyModel.objects.all()
    lookup_field = 'id'

    @is_authorized
    def post(self, request):
        return self.create(request)

    @is_authorized
    def get(self, request, id=None):
        if id:
            return self.retrieve(None, id=id)
        else:
            return self.list(None)

    @is_authorized
    def put(self, request, id=None):
        return self.update(request, id)

    @is_authorized
    def delete(self, request, id):
        return self.destroy(request, id)
