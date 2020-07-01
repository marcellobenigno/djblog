from django.urls import path

from . import views as v

app_name = 'book'

urlpatterns = [
    path('lista/', v.book_list, name='book_list'),
    path('criar/', v.book_create, name='book_create'),
    path('<int:pk>/atualizar/', v.book_update, name='book_update'),
    path('<int:pk>/remover/', v.book_delete, name='book_delete'),
]
