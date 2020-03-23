from django.urls import path

from . import views as v

app_name = 'account'

urlpatterns = [
    path('entrar/', v.login, name='login'),
    path('sair/', v.logout, name='logout'),
    path('registrar-se/', v.signin, name='signin'),
    path('sucesso/', v.success, name='success'),
]
