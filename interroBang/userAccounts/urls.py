from django.conf.urls import url
from django.views.generic.simple import direct_to_template
urlpatterns = [
    url(r'^accounts/profile', direct_to_template, {'template': 'profile.html'}),
]
