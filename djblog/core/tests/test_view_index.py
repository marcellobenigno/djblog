from django.shortcuts import resolve_url as r
from django.test import TestCase


class TestViewIndex(TestCase):
    def setUp(self):
        self.response = self.client.get(r('core:index'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.response, 'core/index.html')

    def test_login_link(self):
        expected = 'href="{}"'.format(r('account:login'))
        self.assertContains(self.response, expected)
