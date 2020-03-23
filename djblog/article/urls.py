from django.urls import path

from . import views as v

app_name = 'article'

urlpatterns = [
    path('', v.article_list, name='article_list'),
    path('painel/', v.article_admin_list, name='article_admin_list'),
]
