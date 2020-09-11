from django.test import TestCase
from ..models import Author, Book


class TestAuthorModel(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_name='Rogers',
            last_name='Macharia',
        )

    def test_object_saved(self):
        author = Author.objects.get(pk=1)
        self.assertEquals(author.first_name, self.author.first_name)
        self.assertEquals(author.last_name, self.author.last_name)
        self.assertEquals(author.pk, 1)


class TestBookModel(TestAuthorModel, TestCase):
    def setUp(self):
        super(TestBookModel, self).setUp()
        self.book = Book.objects.create(
            title="Atomic Habits",
            genre="PG",
            price=100,
        )
        self.book.author.add(self.author)

    def test_object_saved(self):
        book = Book.objects.get(pk=1)
        self.assertEquals(book.title, self.book.title)
        self.assertEquals(book.get_genre_display(), "Personal Growth")
        self.assertEquals(list(book.get_authors()), [self.author])
