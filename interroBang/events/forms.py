from django import forms

from .models import Event

class EventForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    publish = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Event
        fields = [
            'title',
            'content',
            'image',
            'draft',
            'publish',

        ]