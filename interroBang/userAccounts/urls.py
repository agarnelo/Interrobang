from django.conf.urls import url

from .views import (
    index,
    profile,
    logout,
)

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^accounts/profile', profile, name="profile"),
]
