from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, FormView, UpdateView

from .forms import LoginForm, SignInForm, UpdateUserForm
from .models import User


class Login(SuccessMessageMixin, LoginView):
    template_name = 'account/login.html'
    form_class = LoginForm
    redirect_authenticated_user = True
    success_message = "Seja bem-vindo(a) ao DjBlog!"


class SignInView(CreateView):
    form_class = SignInForm
    template_name = 'account/signin.html'
    success_url = reverse_lazy('account:success')


class SucessView(TemplateView):
    template_name = 'account/success.html'


class Logout(LogoutView):
    next_page = 'core:index'


class AccountView(LoginRequiredMixin, TemplateView):
    template_name = 'account/account.html'


class UpdateUserView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'account/update_user.html'
    form_class = UpdateUserForm
    success_message = 'Dados pessoais editados com sucesso!'
    success_url = reverse_lazy('accounts:account')

    def get_object(self):
        return self.request.user


class UpdatePasswordView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    template_name = 'account/update_password.html'
    form_class = PasswordChangeForm
    success_message = 'Senha editada com sucesso!'
    success_url = reverse_lazy('accounts:account')

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


login = Login.as_view()
logout = Logout.as_view()
signin = SignInView.as_view()
success = SucessView.as_view()
account = AccountView.as_view()
update_user = UpdateUserView.as_view()
update_password = UpdatePasswordView.as_view()
