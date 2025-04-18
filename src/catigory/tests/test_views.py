# from django.test import TestCase
# from django.urls import reverse
# from catigory.models import Category
# from catigory.views import Region

# class RegionViewTests(TestCase):
#     def setUp(self):
#         self.region = Region.objects.create(
#             name = "Xorazm", sorting = "2"
#         )

#     def test_region_list_status(self):
#         response = self.client.get(reverse('region'))
#         self.assertEqual(response.status_code, 200)

#     def test_region_view_template_used(self):
#         response = self.client.get(reverse('region'))
#         self.assertTemplateUsed(response, 'region.html')

#     def test_region_view_context_contains_form(self):
#         response = self.client.get(reverse('region'))
