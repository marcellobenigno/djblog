from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import LoginForm


class Login(SuccessMessageMixin, LoginView):
    template_name = 'account/login.html'
    form_class = LoginForm
    redirect_authenticated_user = True
    success_message = "Seja bem vindo ao DjBlog!"


class Logout(LogoutView):
    next_page = 'core:index'


login = Login.as_view()
logout = Logout.as_view()
