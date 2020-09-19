from django.test import TestCase

from ..models import Book, Author
from ..views import HomepageView
from django.urls import reverse, resolve


class HomepageViewTests(TestCase):
    def setUp(self):
        self.url = reverse("home")
        self.response = self.client.get(self.url)
        Author.objects.create(first_name="Rogers", last_name="Macharia")
        self.author = Author.objects.get(pk=1)
        Book.objects.create(title="Atomic Habits", price=100)
        self.book = Book.objects.get(pk=1)
        self.book.author.add(self.author)
        self.book.save()

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_page_not_found(self):
        url = "home/"
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_resolves_correct_view(self):
        view = resolve(self.url)
        self.assertEquals(view.func.view_class, HomepageView)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, "home.html")

    def test_contains_link_details_page(self):
        details_page_link = reverse("book-detail", kwargs={"pk": self.book.pk})
        self.assertContains(self.response, 'href="{0}"'.format(self.url, details_page_link))

