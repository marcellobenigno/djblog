from django.shortcuts import resolve_url as r
from django.test import TestCase


class TestGetSuccessView(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('account:success'))

    def test_status_code(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'account/success.html')

    def test_subscription_link(self):
        expected = 'href="{}"'.format(r('account:login'))
        self.assertContains(self.resp, expected)
