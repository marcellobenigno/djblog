from django.urls import path

from . import views as v

app_name = 'article'

urlpatterns = [
    path('', v.article_list, name='article_list'),
    path('painel/', v.article_admin_list, name='article_admin_list'),
    path('<slug:slug>/editar/', v.article_update, name='article_update'),
    path('<slug:slug>/', v.article_detail, name='article_detail'),
]