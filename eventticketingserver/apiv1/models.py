from __future__ import unicode_literals

from django.core import exceptions
from django.db import models
from django.db.models import Sum
from django.db.utils import IntegrityError
from django.db.models import Q
from django.db.models import Max
from django.db import transaction

from django.utils import timezone

# Create your models here.

class TimeStampedModel(models.Model):

    class Meta(object):
        abstract = True

    cdate = models.DateTimeField(auto_now_add=True)
    udate = models.DateTimeField(auto_now=True)

class Location(TimeStampedModel):
    id = models.AutoField(db_column='location_id', primary_key=True)

    location_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    is_active = models.BooleanField()

    class Meta:
        db_table = 'location'

class Event(TimeStampedModel):
    id = models.AutoField(db_column='event_id', primary_key=True)

    location = models.ForeignKey(
        'Location', models.DO_NOTHING, db_column='location_id', null=True, blank=True)

    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    event_name = models.CharField(max_length=200)
    event_organizer = models.CharField(max_length=200)

    class Meta:
        db_table = 'event'

class Ticket(TimeStampedModel):
    id = models.AutoField(db_column='ticket_id', primary_key=True)

    event = models.ForeignKey(
        'Event', models.DO_NOTHING, db_column='event_id', related_name='ticket',
        blank=True, null=True)

    name = models.CharField(max_length=200)
    ticket_type = models.CharField(max_length=200)
    price = models.BigIntegerField(default=0, blank=True, null=True)
    is_active = models.BooleanField()
    quota = models.BigIntegerField(default=0, blank=True, null=True)

    class Meta:
        db_table = 'ticket'

class TicketTransaction(TimeStampedModel):
    id = models.AutoField(db_column='ticket_transaction_id', primary_key=True)

    ticket = models.ForeignKey(
        'Ticket', models.DO_NOTHING, db_column='ticket_id', null=True, blank=True)

    transaction = models.ForeignKey(
        'Transaction', models.DO_NOTHING, db_column='transaction_id', \
        related_name='ticket_transaction', null=True, blank=True)

    quatity = models.IntegerField(default=0)
    total_price = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'ticket_transaction'

class Transaction(TimeStampedModel):
    id = models.AutoField(db_column='transaction_id', primary_key=True)

    customer = models.ForeignKey(
        'Customer', models.DO_NOTHING, db_column='customer_id', null=True, blank=True)

    amount = models.BigIntegerField(default=0)
    payment_method = models.CharField(max_length=200)

    class Meta:
        db_table = 'transaction'

class Customer(TimeStampedModel):
    id = models.AutoField(db_column='customer_id', primary_key=True)

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    dob = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    username = models.CharField(max_length=100)

    class Meta:
        db_table = 'customer'
