import logging
import datetime

from django.db import transaction

# Create your views here.

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

logger = logging.getLogger(__name__)

class CreateEventView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):

        return Response(status=HTTP_200_OK, data={'status': 'mantapss'})


class CreateTicketEventView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):

        return Response(status=HTTP_200_OK, data={'status': 'mantapss'})


class GetEventInfoView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request):

        return Response(status=HTTP_200_OK, data={'status': 'mantapss'})


class CreateLocationView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):

        return Response(status=HTTP_200_OK, data={'status': 'mantapss'})


class CreateTransactionView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):

        return Response(status=HTTP_200_OK, data={'status': 'mantapss'})

class GetTransactionInfoView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request):

        return Response(status=HTTP_200_OK, data={'status': 'mantapss'})
