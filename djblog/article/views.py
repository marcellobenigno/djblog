from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, UpdateView, DetailView

from .forms import ArticleForm
from .models import Article


class ArticleListView(ListView):
    paginate_by = 5

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


article_admin_list = ArticleAdminListView.as_view()

article_detail = ArticleDetailView.as_view()

article_update = ArticleUpdateView.as_view()

article_list = ArticleListView.as_view()
