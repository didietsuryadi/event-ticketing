import logging
import datetime
import json

from django.db import transaction
from django.forms.models import model_to_dict
# Create your views here.

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.status import HTTP_201_CREATED
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from .models import *
from .serializers import *

logger = logging.getLogger(__name__)

class CreateEventView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):

        location = Location.objects.filter(pk=request.data['location_id']).last()
        if not location:
            return Response(status=HTTP_400_BAD_REQUEST,
                            data={'messages': 'location_not_available'})
        data = request.data.copy()
        serializer = EventSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(location_id=location.id)
        return Response(status=HTTP_201_CREATED, data=serializer.data)


class CreateTicketEventView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):

        event = Event.objects.filter(pk=request.data['event_id']).last()
        if not event:
            return Response(status=HTTP_400_BAD_REQUEST,
                            data={'messages': 'event_not_available'})
        data = request.data.copy()
        serializer = TicketSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(event_id=event.id)
        return Response(status=HTTP_201_CREATED, data=serializer.data)


class GetEventInfoView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, event_id):

        event_data = Event.objects.filter(pk=event_id).last()
        if not event_data:
            return Response(status=HTTP_400_BAD_REQUEST,
                            data={'messages': 'event data not found'})

        serializer_event = EventSerializer(event_data)
        return Response(status=HTTP_200_OK,
                        data=serializer_event.data)


class CreateLocationView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):

        data = request.data.copy()
        serializer = LocationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=HTTP_201_CREATED, data=serializer.data)


class CreateTransactionView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data.copy()
        serializer = TransactionSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        ticket_transactions = data.pop('ticket_transaction', None)
        if not ticket_transactions:
            return Response(status=HTTP_400_BAD_REQUEST,
                            data={'messages': 'transaction_have_no_ticket'})
        try:
            with transaction.atomic():
                transaction_result = Transaction.objects.create(**data)
                for ticket_transaction in ticket_transactions:
                    detail_ticket = Ticket.objects.filter(pk=ticket_transaction['ticket_id']).last()
                    if not detail_ticket:
                        continue
                    if detail_ticket.quota == 1:
                        continue
                    ticket_transaction['total_price'] = detail_ticket.price \
                        * ticket_transaction['quatity']
                    result = TicketTransaction.objects.create(**ticket_transaction)
                    result.ticket = detail_ticket
                    result.transaction = transaction_result
                    result.save()
                    transaction_result.amount += result.total_price
                    transaction_result.save()
                    detail_ticket.quota -= ticket_transaction['quatity']
                    detail_ticket.save()
                serializer = TransactionSerializer(data=model_to_dict(transaction_result))
                serializer.is_valid(raise_exception=True)
                return Response(status=HTTP_200_OK, data=serializer.data)
        except Exception as e:
            return Response(status=HTTP_400_BAD_REQUEST,
                        data={'messages': e})

class GetTransactionInfoView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, transaction_id):

        transaction_data = Transaction.objects.filter(pk=transaction_id).last()
        if not transaction_data:
            return Response(status=HTTP_400_BAD_REQUEST,
                            data={'messages': 'transaction data not found'})

        serializer_transaction = TransactionSerializer(transaction_data)
        return Response(status=HTTP_200_OK,
                        data=serializer_transaction.data)
