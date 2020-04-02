from django.shortcuts import resolve_url as r
from django.test import TestCase

from ...account.models import User


class TestLogout(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            name='fred',
            email='test@test.com',
            password='secret.123'
        )
        self.client.login(
            username='test@test.com',
            password='secret.123'
        )
        self.resp = self.client.get(r('account:logout'), follow=True)

    def test_logout_redirect(self):
        """Logout should redirect to / """
        self.assertRedirects(self.resp, r('core:index'))

    def test_user_logged_out(self):
        """User should be authenticated"""
        self.assertFalse(self.resp.context['user'].is_authenticated)
