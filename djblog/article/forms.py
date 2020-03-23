from django import forms
from django.utils.text import slugify

from .models import Article


class ArticleForm(forms.ModelForm):

    def __init__(self, author, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.author = author

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.author = self.author
        obj.slug = slugify(obj.title)
        if commit:
            obj.save()
        return obj

    class Meta:
        model = Article
        fields = ['active', 'title', 'body']
