from django.conf.urls import url
from .views import (
    event_create,
)

urlpatterns = [
    url(r'^create/$', event_create),
]