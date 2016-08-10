from django.conf.urls import url
from django.views.generic import TemplateView

from .views import (
    index,
    profile,
    logout,
)

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^accounts/profile', profile, name="profile"),
]
