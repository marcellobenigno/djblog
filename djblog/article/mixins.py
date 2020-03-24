from django.db.models import Q


class SearchPanelMixin:

    def get_queryset(self):
        queryset = super(SearchPanelMixin, self).get_queryset()

        v = self.request.GET.get('v')

        if v:
            queryset = queryset.filter(
                Q(title__icontains=v) | Q(body__icontains=v)
            )

        if self.request.user.is_authenticated:
            queryset = queryset.filter(
                author=self.request.user
            )
        else:
            queryset = queryset.filter(
                active=True
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('v'):
            context['v'] = self.request.GET.get('v')
        else:
            context['v'] = ''

        context['total_itens'] = self.get_queryset().count()
        return context
