from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': "Email ou senha inválidos",
        'inactive': 'Está conta está inativa',
    }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].label = 'Código do Imóvel'


# class UserAdminForm(forms.ModelForm):
#     new_password = forms.CharField(
#         label='Nova Senha', widget=forms.PasswordInput,
#         required=False,
#         help_text='Informe uma senha caso deseje alterar, caso contrário deixa esse campo em branco'
#     )
#
#     def save(self, commit=True):
#         new_password = self.cleaned_data.get('new_password', '')
#         if new_password:
#             self.instance.set_password(new_password)
#         return super().save(commit=commit)
#
#     class Meta:
#         model = Usuario
#         exclude = ['password']
