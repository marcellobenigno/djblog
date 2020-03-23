from django.db import models
from django.urls import reverse

from ..account.models import User
from ..core.models import BaseModel


class Article(BaseModel):
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.PROTECT)
    title = models.CharField('título', max_length=40)
    slug = models.SlugField('slug')
    body = models.TextField('texto da postagem')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:article_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'
        ordering = ('-created',)
