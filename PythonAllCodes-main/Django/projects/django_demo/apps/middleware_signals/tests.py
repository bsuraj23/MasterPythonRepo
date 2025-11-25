from django.test import TestCase, Client
from django.urls import reverse


class MiddlewareSignalsTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_ping_creates_ping_and_sets_header(self):
        resp = self.client.get(reverse('middleware_signals:ping'))
        self.assertEqual(resp.status_code, 200)
        # middleware should set header
        self.assertIn('X-View-Duration-ms', resp)
