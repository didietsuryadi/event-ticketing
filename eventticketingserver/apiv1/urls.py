from django.conf.urls import include, url
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
    #endpoints related to event
    url(r'^event/create$', CreateEventView.as_view()),
    url(r'^event/ticket/create$', CreateTicketEventView.as_view()),
    url(r'^event/get_info$', GetEventInfoView.as_view()),
    #endpoint related to location
    url(r'^location/create$', CreateLocationView.as_view()),
    #endpoint related to transactions
    url(r'^transaction/purchase$', CreateTransactionView.as_view()),
    url(r'^transaction/get_info$', GetTransactionInfoView.as_view()),
]
