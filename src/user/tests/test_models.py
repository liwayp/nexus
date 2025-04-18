from django.test import TestCase
from django.contrib.auth.models import User
from user.models import Profile  

class ProfileModelTest(TestCase):
    def test_create_profile(self):
        """Тест создания профиля с заполненными полями"""
        user = User.objects.create(username="testuser", password="testpass")
        profile = Profile.objects.create(
            user=user,
            first_name="John",
            last_name="Doe",
            phone_number="1234567890",
            image="path/to/image.jpg"
        )

        self.assertEqual(profile.user, user)
        self.assertEqual(profile.first_name, "John")
        self.assertEqual(profile.last_name, "Doe")
        self.assertEqual(profile.phone_number, "1234567890")
        self.assertEqual(profile.image.name, "path/to/image.jpg")
        self.assertEqual(str(profile), "John Doe")

    def test_profile_default_values(self):
        """Тест значений по умолчанию для необязательных полей"""
        user = User.objects.create(username="testuser", password="testpass")
        profile = Profile.objects.create(
            user=user,
            first_name="Jane"
        )

        self.assertEqual(profile.first_name, "Jane")
        self.assertIsNone(profile.last_name)
        self.assertIsNone(profile.phone_number)
        self.assertIsNone(profile.image.name)  
        self.assertEqual(str(profile), "Jane None")  
    def test_profile_str_method(self):
        """Тест метода __str__"""
        user = User.objects.create(username="testuser", password="testpass")
        profile = Profile.objects.create(
            user=user,
            first_name="Alice",
            last_name="Smith"
        )

        self.assertEqual(str(profile), "Alice Smith")

    def test_profile_user_relationship(self):
        """Тест связи профиля с пользователем"""
        user = User.objects.create(username="testuser", password="testpass")
        profile = Profile.objects.create(
            user=user,
            first_name="Bob"
        )

        self.assertEqual(profile.user, user)
        self.assertEqual(user.profile, profile) 