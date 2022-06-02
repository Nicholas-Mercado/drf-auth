from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from unittest import skip
from .models import Book


class BookTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_thing = Book.objects.create(
            title="rake",
            owner=testuser1,
            description="Better for collecting leaves than a shovel.",
        )
        test_thing.save()
     
    def setUp(self):
        self.client.login(username="testuser1", password="pass")
            
    def test_books_model(self):
        book = Book.objects.get(id=1)
        actual_owner = str(book.owner)
        actual_name = str(book.title)
        actual_description = str(book.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(
            actual_description, "Better for collecting leaves than a shovel."
        )
    # @skip('not yet')
    def test_get_book_list(self):
        url = reverse("book_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        books = response.data
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]["title"], "rake")
        
    # @skip('not yet')
    def test_get_title_by_id(self):
        url = reverse("book_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        books = response.data
        self.assertEqual(books["title"], "rake")
        
    # @skip('not yet')
    def test_create_book(self):
        url = reverse("book_list")
        data = {"owner": 1, "title": "spoon", "author": "ME!", "description": "good for cereal and soup"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        books = Book.objects.all()
        self.assertEqual(len(books), 2)
        self.assertEqual(Book.objects.get(id=2).title, "spoon")

    # @skip('not yet')
    def test_update_book(self):
        url = reverse("book_detail", args=(1,))
        data = {
            "owner": 1,
            "title": "rake",
            "author": "ME!",
            "description": "pole with a crossbar toothed like a comb.",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        books = Book.objects.get(id=1)
        self.assertEqual(books.title, data["title"])
        self.assertEqual(books.owner.id, data["owner"])
        self.assertEqual(books.description, data["description"])
        
    # @skip('not yet')
    def test_delete_book(self):
        url = reverse("book_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        books = Book.objects.all()
        self.assertEqual(len(books), 0)
        
    def test_authentication_required(self):
        self.client.logout()
        url = reverse("book_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
