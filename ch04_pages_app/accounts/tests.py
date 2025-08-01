from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
        )

        self.assertTrue(user.email, "test@example.com")
        self.assertTrue(user.username, "testuser")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username="testuser",
            email="test@example.com",
            password="testpass123",
        )
        self.assertTrue(user.email, "test@example.com")
        self.assertTrue(user.username, "testuser")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
