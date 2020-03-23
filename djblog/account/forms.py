from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import User


class LoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': "Email ou senha inválidos",
        'inactive': 'Está conta está inativa',
    }


class UserAdminForm(forms.ModelForm):
    new_password = forms.CharField(
        label='Nova Senha', widget=forms.PasswordInput,
        required=False,
        help_text='Informe uma senha caso deseje alterar, caso contrário deixa esse campo em branco'
    )

    def save(self, commit=True):
        new_password = self.cleaned_data.get('new_password', '')
        if new_password:
            self.instance.set_password(new_password)
        return super().save(commit=commit)

    class Meta:
        model = User
        exclude = ['password']


class SignInForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput())

    def clean_phone(self):
        """ remove all characters for phone field """
        return ''.join([l for l in self.cleaned_data.get('phone', '') if l.isdigit()])

    def clean(self):
        cleaned_data = super(SignInForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "os campos Senha e Confirme a senha não são iguais."
            )

    def save(self):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'password', 'confirm_password', ]


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'phone', ]
