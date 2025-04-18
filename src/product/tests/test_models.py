from django.test import TestCase
from django.core.exceptions import ValidationError
from product.models import Product, ProductView, ProductImage
from catigory.models import Region, Category, Brand
from user.models import Profile
from django.contrib.auth.models import User


class ProductModelTest(TestCase):
    def test_create_product(self):
        user = User.objects.create(username="testuser", password="testpass")
        profile = Profile.objects.create(user=user)  
        region = Region.objects.create(name="Toshkent", sorting=1)
        category = Category.objects.create(name="Elektronika", slug="elektronika")
        brand = Brand.objects.create(name="Samsung")

        product = Product.objects.create(
            title="Test Product",
            description="This is a test product",
            location=region,
            category=category,
            user=profile,
            condition=1,  
            status=1,     
            price=100,
            price_on_call=False,
            brand=brand
        )

        self.assertEqual(product.title, "Test Product")
        self.assertEqual(product.description, "This is a test product")
        self.assertEqual(product.location, region)
        self.assertEqual(product.category, category)
        self.assertEqual(product.user, profile)
        self.assertEqual(product.condition, 1)
        self.assertEqual(product.status, 1)
        self.assertEqual(product.price, 100)
        self.assertEqual(product.price_on_call, False)
        self.assertEqual(product.brand, brand)
        self.assertEqual(str(product), "Test Product")

    def test_product_default_values(self):
        user = User.objects.create(username="testuser", password="testpass")
        profile = Profile.objects.create(user=user)  
        region = Region.objects.create(name="Toshkent", sorting=1)
        category = Category.objects.create(name="Elektronika", slug="elektronika")

        product = Product.objects.create(
            title="Default Product",
            description="Default description",
            location=region,
            category=category,
            user=profile
        )

        self.assertEqual(product.condition, 1) 
        self.assertEqual(product.status, 1)     
        self.assertEqual(product.price_on_call, False)
        self.assertIsNone(product.price)
        self.assertIsNone(product.brand)
        self.assertIsNotNone(product.created_at)
        self.assertIsNotNone(product.updated_at)

    def test_product_invalid_condition(self):
        user = User.objects.create(username="testuser", password="testpass")
        profile = Profile.objects.create(user=user) 
        region = Region.objects.create(name="Toshkent", sorting=1)
        category = Category.objects.create(name="Elektronika", slug="elektronika")

        product = Product(
            title="Invalid Product",
            description="Invalid condition",
            location=region,
            category=category,
            user=profile,
            condition=999 
        )

        with self.assertRaises(ValidationError):
            product.full_clean()


class ProductViewModelTest(TestCase):
    def test_create_product_view(self):
        user = User.objects.create(username="testuser", password="testpass")
        profile = Profile.objects.create(user=user) 
        region = Region.objects.create(name="Toshkent", sorting=1)
        category = Category.objects.create(name="Elektronika", slug="elektronika")
        product = Product.objects.create(
            title="Test Product",
            description="This is a test product",
            location=region,
            category=category,
            user=profile
        )

        product_view = ProductView.objects.create(
            product=product,
            view_count=10
        )

        self.assertEqual(product_view.product, product)
        self.assertEqual(product_view.view_count, 10)

    def test_product_view_default_value(self):
        user = User.objects.create(username="testuser", password="testpass")
        profile = Profile.objects.create(user=user)  
        region = Region.objects.create(name="Toshkent", sorting=1)
        category = Category.objects.create(name="Elektronika", slug="elektronika")
        product = Product.objects.create(
            title="Test Product",
            description="This is a test product",
            location=region,
            category=category,
            user=profile
        )

        product_view = ProductView.objects.create(product=product)

        self.assertEqual(product_view.view_count, 0)  


class ProductImageModelTest(TestCase):
    def test_create_product_image(self):
        user = User.objects.create(username="testuser", password="testpass")
        profile = Profile.objects.create(user=user) 
        region = Region.objects.create(name="Toshkent", sorting=1)
        category = Category.objects.create(name="Elektronika", slug="elektronika")
        product = Product.objects.create(
            title="Test Product",
            description="This is a test product",
            location=region,
            category=category,
            user=profile
        )

        product_image = ProductImage.objects.create(
            product=product,
            image="path/to/image.jpg",
            is_main=True
        )

        self.assertEqual(product_image.product, product)
        self.assertEqual(product_image.image, "path/to/image.jpg")
        self.assertEqual(product_image.is_main, True)

    def test_product_image_default_value(self):
        user = User.objects.create(username="testuser", password="testpass")
        profile = Profile.objects.create(user=user) 
        region = Region.objects.create(name="Toshkent", sorting=1)
        category = Category.objects.create(name="Elektronika", slug="elektronika")
        product = Product.objects.create(
            title="Test Product",
            description="This is a test product",
            location=region,
            category=category,
            user=profile
        )

        product_image = ProductImage.objects.create(
            product=product,
            image="path/to/image.jpg"
        )

        self.assertEqual(product_image.is_main, False)  

    def test_product_image_related_name(self):
        user = User.objects.create(username="testuser", password="testpass")
        profile = Profile.objects.create(user=user)  
        region = Region.objects.create(name="Toshkent", sorting=1)
        category = Category.objects.create(name="Elektronika", slug="elektronika")
        product = Product.objects.create(
            title="Test Product",
            description="This is a test product",
            location=region,
            category=category,
            user=profile
        )

        product_image1 = ProductImage.objects.create(
            product=product,
            image="path/to/image1.jpg"
        )
        product_image2 = ProductImage.objects.create(
            product=product,
            image="path/to/image2.jpg"
        )

        self.assertEqual(product.images.count(), 2)