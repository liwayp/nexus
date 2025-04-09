from django.test import TestCase
from catigory.models import Category, Region, Brand 

class CategoryModelTest(TestCase):
    def test_create_main_category(self):
        category = Category.objects.create(
            name = 'Car',
            is_main=False,
            slug='Cars'
        )
        self.assertEqual(category.name, "Car")
        self.assertFalse(category.is_main)
        self.assertIsNone(category.parent)

    def test_create_subcategory(self):
        parent = Category.objects.create(name="Car", slug="Cars")
        sub = Category.objects.create(
            name="Malibu",
            slug="Moshinalar",
            parent=parent
        )
        self.assertEqual(sub.parent, parent)



class RegionModelTest(TestCase):
    def test_create_region(self):
        region = Region.objects.create(name="Toshkent", sorting=1)
        self.assertEqual(region.name, "Toshkent")
        self.assertEqual(region.sorting, 1)


class BrandModelTest(TestCase):
    def test_create_brand(self):
        brand = Brand.objects.create(name="Samsung")
        self.assertEqual(brand.name, "Samsung")

