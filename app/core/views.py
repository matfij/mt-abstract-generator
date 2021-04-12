import json
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from common import repository as R
from core.models import ResultPageModel, AbstractModel
from core.serializers import ResultPageSerializer, AbstractSerializer
from core.services import CoreService


class ResultPageViewSet(viewsets.ModelViewSet):
    serializer_class = ResultPageSerializer
    queryset = ResultPageModel.objects.all()


@api_view(['GET', 'POST'])
def get_related_pages(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    phrase = body['searchPhrase']

    service = CoreService()
    service.get_related_urls(phrase)

    while R.SPIDER_FINISHED == False:
        pass

    pages = []
    for page in R.RESULT_PAGES:
        result_page = ResultPageModel(
            url=page['url'], 
            references=page['references'],
            content=page['content'],
            quality=page['quality']
        )
        pages.append(result_page)

    serializer = ResultPageSerializer(pages, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def generate_abstract(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    phrase = body['searchPhrase']
    answer_model = body['answerModel']
    summary_model = body['summaryModel']

    service = CoreService()
    service.generate_abstract(phrase, answer_model, summary_model)

    while R.GENERATOR_FINISHED == False:
        pass

    abstract = AbstractModel(
        answer=R.GENERATOR_ANSWER,
        summary=R.GENERATOR_SUMMARY
    )

    serializer = AbstractSerializer(abstract)
    return Response(serializer.data)
