import json
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from common import repository as R
from core.models import ResultPageModel
from core.serializers import ResultPageSerializer
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

    while len(R.RESULT_PAGES) < R.TARGET_PAGE_NUMBER:
        pass

    pages = []
    for page in R.RESULT_PAGES:
        result_page = ResultPageModel(
            url=page['url'], 
            references=page['references']
        )
        pages.append(result_page)

    serializer = ResultPageSerializer(pages, many=True)
    return Response(serializer.data)
