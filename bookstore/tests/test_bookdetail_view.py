from django.test import TestCase

from ..models import Book, Author
from django.urls import reverse, resolve
from ..views import BookDetailView


class BookDetailViewTests(TestCase):
    def setUp(self):
        Book.objects.create(title="Atomic Habits", price=100)
        Author.objects.create(first_name="rogers", last_name="macharia")
        self.author = Author.objects.get(pk=1)
        self.book = Book.objects.get(pk=1)
        self.book.author.add(self.author)
        self.book.save()
        self.url = reverse("book-detail", kwargs={"pk": self.book.pk})
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_page_not_found(self):
        url = reverse("book-detail", kwargs={"pk": 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_resolves_correct_view(self):
        view = resolve(self.url)
        self.assertEquals(view.func.view_class, BookDetailView)

    def test_template_used(self):
        template = "book_detail.html"
        self.assertTemplateUsed(self.response, template)