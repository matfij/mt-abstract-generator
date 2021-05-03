from rest_framework.serializers import ModelSerializer

from polls.models import PollModel


class PollSerializer(ModelSerializer):

    class Meta:
        model = PollModel
        fields = '__all__'
