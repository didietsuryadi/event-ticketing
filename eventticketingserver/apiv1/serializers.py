from rest_framework import serializers
from .models import *

class LocationSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Location

class TicketSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Ticket

class TicketTransactionSerializer(serializers.ModelSerializer):
    tiket = TicketSerializer(read_only=True)
    class Meta(object):
        model = TicketTransaction

class CustomerSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Customer

class TransactionSerializer(serializers.ModelSerializer):
    ticket_transaction = TicketTransactionSerializer(many=True, read_only=True)
    customer = CustomerSerializer(read_only=True)
    class Meta(object):
        model = Transaction

class EventSerializer(serializers.ModelSerializer):
    ticket = TicketSerializer(many=True, read_only=True)
    location = LocationSerializer(read_only=True)
    class Meta(object):
        model = Event
