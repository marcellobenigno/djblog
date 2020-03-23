from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView

from .forms import ArticleForm
from .models import Article


class ArticleSiteListView(ListView):
    paginate_by = 2

    def get_queryset(self):
        return Article.objects.filter(
            active=True
        )


class ArticleAdminListView(LoginRequiredMixin, ListView):
    template_name = 'article/articleadmin_list.html'
    paginate_by = 5

    def get_queryset(self):
        return Article.objects.filter(
            author=self.request.user
        )


class ArticleCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = ArticleForm
    model = Article
    success_message = 'Postagem criada com sucesso!'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['author'] = self.request.user
        return kwargs


class ArticleUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = ArticleForm
    model = Article
    success_message = 'Postagem editada com sucesso!'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['author'] = self.request.user
        return kwargs


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        return Article.objects.get(
            slug=self.kwargs['slug']
        )


class ArticleDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('article:article_admin_list')
    success_message = "Postagem apagada com sucesso!"

    def delete(self, request, *args, **kwargs):
        obj = Article.objects.get(
            author=self.request.user,
            slug=self.kwargs['slug']
        )
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(ArticleDelete, self).delete(request, *args, **kwargs)


article_admin_list = ArticleAdminListView.as_view()

article_detail = ArticleDetailView.as_view()

article_create = ArticleCreateView.as_view()

article_update = ArticleUpdateView.as_view()

article_list = ArticleSiteListView.as_view()

article_delete = ArticleDelete.as_view()
