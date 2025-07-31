from django.test import TestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView


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


class AboutPageTest(TestCase):
    def setUp(self):
        url = reverse("about")
        self.response = self.client.get(url)

    def test_about_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_about_page_template(self):
        self.assertTemplateUsed(self.response, "base.html")
        self.assertTemplateUsed(self.response, "about.html")
        self.assertTemplateNotUsed(self.response, "login.html")
        self.assertContains(self.response, "About Page")

    def test_aboutpage_url_resolve_aboutpageview(self):
        view = resolve("/about/")
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)


# Chapter 6 completed
