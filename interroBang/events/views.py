from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils import timezone

from .forms import EventForm
from .models import Event


# Create your views here.
def event_create(request):
    if not request.user.is_authenticated():
        raise Http404
    form = EventForm(request.POST or None, request.FILES or None)
    title = "Post Event"
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # message success
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect("/")
    context = {
        "form": form,
        "title": title,
    }
    return render(request, "event_form.html", context)

def event_list(request):
    queryset_list = Event.objects.active()
    if request.user.is_authenticated():
        queryset_list = Event.objects.filter(user=request.user)
    context = {
        "object_list": queryset_list,
        "title": "Event List",
        "id": id,
    }
    return render(request, "event_list.html", context)

def event_detail(request):
    #Send title as "update event"
    return render(request, "event_list.html", {})

def event_delete(request):
    return render(request, "event_list.html", {})