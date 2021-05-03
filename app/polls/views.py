from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin

from polls.models import PollModel
from polls.serializers import PollSerializer


class PollPublicView(GenericAPIView, CreateModelMixin):
    serializer_class = PollSerializer
    queryset = PollModel.objects.all()

    def post(self, request):
        return self.create(request)


class PollAdminView(GenericAPIView, ListModelMixin):
    serializer_class = PollSerializer
    queryset = PollModel.objects.all()

    def get(self, request):
        return self.list(None)
