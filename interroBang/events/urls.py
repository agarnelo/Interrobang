from django.conf.urls import url
from .views import (
    event_create,
    event_list,
    event_detail,
    event_delete,
    event_update
)

urlpatterns = [
    url(r'^create/$', event_create),
    url(r'^(?P<slug>[\w-]+)/$', event_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', event_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', event_delete),
    url(r'^$', event_list, name='list'),

]
