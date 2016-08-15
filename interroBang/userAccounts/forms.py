from django import forms
from .models import Profile

class SignupForm(forms.ModelForm):
    first_name = forms.CharField(max_length=35, label = 'First Name', widget = forms.TextInput(attrs={'required': True, 'placeholder':'First Name', 'autofocus':'autofocus'}))
    last_name = forms.CharField(max_length=35, label = 'Last Name', widget = forms.TextInput(attrs={'required': True, 'placeholder':'Last Name'}))
    trip = forms.CharField(max_length=35, label = 'Trip', widget = forms.TextInput(attrs={'required': True, 'placeholder':'Trip'}))
    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'trip')

    # A custom method required to work with django-allauth, see https://stackoverflow.com/questions/12303478/how-to-customize-user-profile-when-using-django-allauth
    def signup(self, request, user):
        # Save your user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        # Save your profile
        profile = Profile()
        profile.trip = self.cleaned_data['trip']
        profile.user = user
        profile.save()