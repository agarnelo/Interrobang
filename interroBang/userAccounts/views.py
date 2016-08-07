from allauth.accounts.views import SignupView
from allauth.accounts.forms import LoginForm
from django.shortcuts import render

class denoeSignUpView(SignupView):
    def getContext(self, **kwargs):
        context = super(denoeSignUpView, self).getContext(**kwargs)
        context['login_form'] = LoginForm()
        return context

