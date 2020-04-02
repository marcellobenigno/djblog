from django.shortcuts import resolve_url as r
from django.test import TestCase

from ...account.forms import LoginForm
from ...account.models import User


class TestGetLoginView(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('account:login'))

    def test_status_code(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'account/login.html')

    def test_has_form(self):
        """Context must have a form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, LoginForm)


class TestPostValidLoginView(TestCase):
    def setUp(self):
        self.credentials = {
            'email': 'jhon.doe@gmail.com',
            'password': 'ThisIsaTest.123'
        }
        User.objects.create_user(**self.credentials)
        self.resp = self.client.post(
            r('account:login'), {
                'username': 'jhon.doe@gmail.com',
                'password': 'ThisIsaTest.123'
            },
            follow=True
        )

    def test_create_valid_user(self):
        """User should be created with valid credentials"""
        self.assertTrue(User.objects.exists())

    def test_user_logged_in(self):
        """User should be authenticated"""
        self.assertTrue(self.resp.context['user'].is_authenticated)

    def test_redirect(self):
        """valid login should be redirected"""
        self.assertRedirects(self.resp, r('article:article_panel_list'))

    def test_template(self):
        """valid login should be shown: article_panel_list.html"""
        self.assertTemplateUsed('article/article_panel_list.html')


class TestPostInvalidLoginView(TestCase):
    def setUp(self):
        data = {
            'email': 'some@email.com',
            'password': 'ThisUserWasNotCreated'
        }
        self.resp = self.client.post(r('account:login'), data)

    def test_user_doesnt_exists(self):
        """User doesnt exists in database"""
        self.assertFalse(User.objects.exists())

    def test_post(self):
        """Invalid login should not redirect"""
        self.assertEqual(200, self.resp.status_code)

    def test_has_form(self):
        """Invalid POST must have a form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, LoginForm)

    def test_has_errors(self):
        """Invalid POST must have a form with errors"""
        form = self.resp.context['form']
        self.assertTrue(form.errors)
