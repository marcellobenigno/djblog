from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import LoginForm, SignInForm


class Login(SuccessMessageMixin, LoginView):
    template_name = 'account/login.html'
    form_class = LoginForm
    redirect_authenticated_user = True
    success_message = "Seja bem vindo ao DjBlog!"


class SignInView(CreateView):
    form_class = SignInForm
    template_name = 'account/signin.html'
    success_url = reverse_lazy('account:success')


class SucessView(TemplateView):
    template_name = 'account/success.html'


class Logout(LogoutView):
    next_page = 'core:index'


login = Login.as_view()
logout = Logout.as_view()
signin = SignInView.as_view()
success = SucessView.as_view()
