from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import SignUpForm

class SignUp(CreateView):
    form_class = SignUpForm
    success_url = '/accounts/login/'
    template_name = 'registration/signup.html'
