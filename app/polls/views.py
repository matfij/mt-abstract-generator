from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin

from core.wrappers import is_authorized, key_required
from polls.models import PollModel
from polls.serializers import PollSerializer


class PollPublicView(GenericAPIView, CreateModelMixin):
    serializer_class = PollSerializer
    queryset = PollModel.objects.all()

    @key_required
    def post(self, request):
        return self.create(request)


class PollAdminView(GenericAPIView, ListModelMixin):
    serializer_class = PollSerializer
    queryset = PollModel.objects.all()

    @is_authorized
    def get(self, request):
        return self.list(None)
