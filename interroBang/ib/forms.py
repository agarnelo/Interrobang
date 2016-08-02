from django import forms
from .models import User

#The user info we need to get from form
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "fname",
            "lname"
        ]