from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class HomepageTest(TestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_home_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_url(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template_used(self):
        self.assertTemplateUsed(self.response, "base.html")
        self.assertTemplateUsed(self.response, "home.html")
        self.assertContains(self.response, "<h1>Homepage</h1>")
