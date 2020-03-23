from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'author', 'created', 'updated')
    list_filter = ('active', 'updated',)
    search_fields = ('title', 'headline')
    prepopulated_fields = {'slug': ('title',)}
