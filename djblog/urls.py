from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('djblog.core.urls', namespace='core')),
    path('postagens/', include('djblog.article.urls', namespace='article')),
    path('conta/', include('djblog.account.urls', namespace='accounts')),
    path('admin/', admin.site.urls),
]
