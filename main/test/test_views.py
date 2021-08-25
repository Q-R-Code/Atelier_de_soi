from django.test import TestCase
from django.urls import reverse



class TestViews(TestCase):
    """Test some views"""

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/home.html')

    def test_legal_view(self):
        response = self.client.get(reverse('main:legal_notice'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/legal_notice.html')
