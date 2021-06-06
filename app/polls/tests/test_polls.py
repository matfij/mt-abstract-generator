from django.urls import reverse
from unittest.case import skipIf
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from polls.models import PollModel
from polls.serializers import PollSerializer
from core.models import KeyModel


class PollsTests(APITestCase):

    def setUp(self):
        self.key = 'auth'
        self.client = APIClient()
        # self.client.headers.update({'key': self.key})
        KeyModel.objects.create(
            key = self.key,
            tester_name = 'tester'
        )

        self.submit_poll_url = reverse('polls:submit-poll')
        self.get_polls_url = reverse('polls:get-polls')

    @skipIf(True, 'Django API client bug')
    def test_submit_poll(self):
        payload = {
            'key': self.key,
            'phrase': 'Is cofee healthy?',
            'answer_model': 0,
            'summary_model': 0,
            'page_number':30,
            'answer_score_logical':5.0,
            'answer_score_grammatical':5.0,
            'summary_score_logical':5.0,
            'summary_score_grammatical':5.0,
            'time_score':5.0,
            'answer': 'Coffee and tea are incredibly healthy beverages.',
            'summary': 'Coffee cherries grow on coffee trees from a genus of plants calledA plain \"black\" cup of coffee is a very low calorie drink8 ounces only contains 2 calories! Caffeine is naturally found in the fruit, leaves, and beans of coffee, cacao, and guarana plants. Caffeine in coffee can stay in your system for several hours after your last sip. We do not endorse non-Cleveland Clinic products or services. It could be, for example, that coffee drinkers are more active and social.'
        }

        response = self.client.post(self.submit_poll_url, payload)
        exists = PollModel.objects.filter(
            key=self.key
        ).exists()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(exists)

    @skipIf(True, 'Django API client bug')
    def test_submit_poll(self):
        PollModel.objects.create(
            key = self.key,
            phrase = 'Is coffee healthy?',
            answer_model = 0,
            summary_model = 0,
            page_number = 25,
            time_score = 5.0
        )
        PollModel.objects.create(
            key = self.key,
            phrase = 'How to prepare for a marathon?',
            answer_model = 1,
            summary_model = 1,
            page_number = 50,
            time_score = 5.0
        )

        response = self.client.get(self.get_polls_url)
        tags = PollModel.objects.all()
        serializer = PollSerializer(tags, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
