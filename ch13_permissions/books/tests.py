from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Book, Review
from django.urls import reverse
# Create your tests here.


class BookTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Atomic habits",
            author="James Clear",
            price="25.00",
        )
        self.user = get_user_model().objects.create_user(
            email="testuser@example.com",
            username="testuser",
            password="testpass123",
        )
        self.review = Review.objects.create(
            book=self.book, author=self.user, review="Great book"
        )

    def test_book_listing(self):
        self.assertEqual(f"{self.book.title}", "Atomic habits")
        self.assertEqual(f"{self.book.author}", "James Clear")
        self.assertEqual(f"{self.book.price}", "25.00")

    def test_book_list_view(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Atomic habits")
        self.assertTemplateUsed(response, "books/book_list.html")

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("/book/125")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, "books/book_detail.html")
        self.assertContains(response, "Great book")
        self.assertContains(response, "Atomic habits")
