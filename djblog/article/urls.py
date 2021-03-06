from django.urls import path

from . import views as v

app_name = 'article'

urlpatterns = [
    path('', v.article_public_list, name='article_public_list'),
    path('gerenciar/', v.article_panel_list, name='article_panel_list'),
    path('nova/', v.article_create, name='article_create'),
    path('<slug:slug>/editar/', v.article_update, name='article_update'),
    path('<slug:slug>/', v.article_detail, name='article_detail'),
    path('<slug:slug>/apagar/', v.article_delete, name='article_delete'),
]
