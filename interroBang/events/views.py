from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404

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

