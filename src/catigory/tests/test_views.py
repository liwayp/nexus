from django.test import TestCase
from django.urls import reverse, resolve
from django.template.loader import render_to_string
from catigory.models import Category
from catigory.forms import CategoryForm
from catigory.views import Region

class RegionViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('region')  # prover', chto urlpattern nazvan 'region'

    def test_region_get_request(self):
        """Testiruem GET zapros — forma dolzhna byt' v kontekste."""
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'region.html')
        self.assertIsInstance(response.context['form'], RegionForm)

    def test_region_post_valid_form(self):
        """Testiruem POST s korrektnymi dannymi."""
        data = {'name': 'Test Region'}  # predpolagaem, chto Region imeet pole 'name'
        response = self.client.post(self.url, data)

        # Posle sozdaniya dolzhen byt' redirect
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.url)
        self.assertTrue(Region.objects.filter(name='Test Region').exists())

    def test_region_post_invalid_form(self):
        """Testiruem POST s nekorrektnymi dannymi (pustoe znachenie)."""
        response = self.client.post(self.url, {'name': ''})

        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'name', 'This field is required.')