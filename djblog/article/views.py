from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

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


article_list = ArticleListView.as_view()
article_admin_list = ArticleAdminListView.as_view()
