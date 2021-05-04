import os
import json
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status

from core.models import KeyModel
from core.serializers import KeySerializer


def is_authorized(func):
    def wrapper(*args, **kwargs):
        secret_key = os.getenv('SECRET_KEY')
        headers = args[0].request.headers

        if 'secret-key' in headers and headers['secret-key'] == secret_key:
            return func(*args, **kwargs)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    return wrapper


def key_required(func):
    def wrapper(*args, **kwargs):
        try:
            key_header = args[0].request.headers['key']
            key_object = KeyModel.objects.get(key=key_header)
            serializer = KeySerializer(key_object)
            key = serializer.data

            key['use_count'] = key['use_count'] + 1
            if key['use_count'] > key['use_limit']:
                key['active'] = False

            serializer = KeySerializer(key_object, data=key)
            if serializer.is_valid():
                serializer.save()

            if key['active'] == True:
                return func(*args, **kwargs)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    return wrapper
