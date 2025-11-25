from django.test import TestCase
from django.urls import reverse


class ModelsDemoTests(TestCase):
    def test_list_posts_view(self):
        url = reverse('models_index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
