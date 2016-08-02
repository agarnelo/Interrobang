from django.conf.urls import url
from . import views

urlpatterns = [
    #Signup url setup
    url(r'^$', views.signup, name='signup'),
]
