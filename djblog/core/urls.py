from django.urls import path

from . import views as v

app_name = 'core'

urlpatterns = [
    path('', v.index, name='index'),
    path('inicio/', v.home, name='home'),
]
