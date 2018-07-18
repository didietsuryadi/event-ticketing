from django.contrib import admin
from .apiv1.models import *

admin.site.register(Event)
admin.site.register(Customer)
admin.site.register(Transaction)
