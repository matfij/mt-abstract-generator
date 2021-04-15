import json
from rest_framework.decorators import api_view
from rest_framework.response import Response

from common import repository as R
from core.models import ResultPageModel, AbstractModel
from core.serializers import ResultPageSerializer, AbstractSerializer
from core.services import CoreService


@api_view(['GET', 'POST'])
def generate_abstract(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    phrase = body['searchPhrase']
    page_number = body['pageNumber']
    answer_model = body['answerModel']
    summary_model = body['summaryModel']

    service = CoreService()
    abstract = service.generate_abstract(phrase, page_number, answer_model, summary_model)

    serializer = AbstractSerializer(abstract)
    return Response(serializer.data)
