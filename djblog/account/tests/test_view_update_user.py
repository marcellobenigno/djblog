from django.shortcuts import resolve_url as r
from django.test import TestCase

from ...account.forms import UpdateUserForm
from ...account.models import User


class TestGetUpdateUserView(TestCase):
    def setUp(self):
        self.credentials = {
            'email': 'jhon.doe@gmail.com',
            'password': 'ThisIsaTest.123'
        }
        User.objects.create_user(**self.credentials)
        self.client.post(
            r('account:login'), {
                'username': self.credentials['email'],
                'password': self.credentials['password'],
            },
            follow=True
        )
        self.resp = self.client.get(r('account:update_user'))

    def test_status_code(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'account/update_user.html')

    def test_has_form(self):
        """ Context must have a form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, UpdateUserForm)


class TestValidPostUpdateUserView(TestCase):
    def setUp(self):
        self.credentials = {
            'name': 'Jhon Doe',
            'email': 'jhon.doe@gmail.com',
            'phone': 11111111111,
            'password': 'ThisIsaTest.123'
        }
        self.user = User.objects.create_user(**self.credentials)

    def test_update_user(self):
        self.client.post(
            r('account:login'), {
                'username': self.credentials['email'],
                'password': self.credentials['password'],
            }
        )
        data = {
            'name': 'Darth Vadder',
            'email': 'vadder@gmail.com',
            'phone': 22222222222,
        }
        self.resp = self.client.post(
            r('account:update_user'),
            data
        )
        self.assertEqual(self.resp.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.name, 'Darth Vadder')
