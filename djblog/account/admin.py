from django.contrib import admin

from .forms import UserAdminForm
from .models import User


@admin.register(User)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'is_active', 'is_superuser', ]
    list_filter = ['groups', 'is_active', 'is_superuser', ]
    search_fields = ['name', 'email', 'phone', ]
    exclude = ['password']
    form = UserAdminForm
    filter_horizontal = ('groups', 'user_permissions',)
    fieldsets = (
        (None, {
            'fields': (
                'name', 'email', 'phone',
            )
        }), (
            'Permissões', {
                'fields': ('new_password', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
            }
        ),
    )
