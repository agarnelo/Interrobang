from django.conf.urls import url
from .views import (
    event_create,
    event_list
)

urlpatterns = [
    url(r'^create/$', event_create),
    url(r'^$', event_list, name='list'),

]
