from django.contrib.auth.backends import ModelBackend as BaseModelBackend

from .models import User


class ModelBackend(BaseModelBackend):

    def authenticate(self, request, username=None, password=None):
        if username is not None:
            try:
                user = User.objects.get(email=username)
                if user.check_password(password) and user.is_active:
                    return user
            except User.DoesNotExist:
                pass
