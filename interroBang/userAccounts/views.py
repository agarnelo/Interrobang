from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import logout

def index(request):
    return render(request, "index.html", {})

def profile(request):
    return render(request,"profile.html", {})

def login_required(handler):
    def check_login(self, *args, **kwargs):
        userToken = auth.get_auth().get_user_by_session()
        if not userToken:
            logging.info('No user found for session: login required')
            return self.redirect(LOGIN_URL, abort=False)
        return handler(self, *args, **kwargs) # Call the handler method
    return check_login

@login_required
def logout(request):
    logout(request)
    return redirect('index')

#http://stackoverflow.com/questions/32292769/django-user-logout-fails-to-redirect-homepage