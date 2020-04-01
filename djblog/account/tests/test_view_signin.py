from django.shortcuts import resolve_url as r
from django.test import TestCase

from ...account.forms import SignInForm
from ...account.models import User


class TestSignInView(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('account:signin'))

    def test_status_code(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'account/signin.html')

    def test_has_form(self):
        """ Context must have a form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, SignInForm)


class TestValidPostSignInView(TestCase):
    def setUp(self):
        data = {
            'name': 'Jhon Doe',
            'email': 'user@test.com',
            'phone': 99999999999,
            'password': 'test123',
            'confirm_password': 'test123',
        }
        self.register_url = r('account:signin')
        self.resp = self.client.post(self.register_url, data)

    def test_post(self):
        """Valid POST should redirect to /conta/sucesso/"""
        self.assertRedirects(self.resp, r('account:success'))

    def test_user_created(self):
        """Valid POST should create an object"""
        self.assertTrue(User.objects.exists())


class TestInvalidPostSignInView(TestCase):
    def setUp(self):
        data = {
            'name': 'Jhon Doe',
            'email': 'user@test.com',
            'phone': 99999999999,
            'password': 'test123',
            'confirm_password': '123.ABC',
        }
        self.register_url = r('account:signin')
        self.resp = self.client.post(self.register_url, data)

    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(self.resp.status_code, 200)

    def test_has_form(self):
        """Invalid POST must have a form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, SignInForm)
