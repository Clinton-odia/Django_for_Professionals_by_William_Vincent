from django.test import TestCase
from django.urls import reverse, resolve
from .views import HomePageView


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

    def test_homepage_url_resolve_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


# Chapter 4 completed
