from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView

from .forms import ArticleForm
from .mixins import SearchPanelMixin
from .models import Article


class ArticlePublicListView(SearchPanelMixin, ListView):
    model = Article
    paginate_by = 2


class ArticlePanelListView(LoginRequiredMixin, SearchPanelMixin, ListView):
    model = Article
    template_name = 'article/article_panel_list.html'
    paginate_by = 5


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
    success_url = reverse_lazy('article:article_panel_list')
    success_message = "Postagem apagada com sucesso!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ArticleDelete, self).delete(request, *args, **kwargs)


article_panel_list = ArticlePanelListView.as_view()

article_detail = ArticleDetailView.as_view()

article_create = ArticleCreateView.as_view()

article_update = ArticleUpdateView.as_view()

article_public_list = ArticlePublicListView.as_view()

article_delete = ArticleDelete.as_view()
