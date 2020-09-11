from django.test import TestCase
from ..models import *
from django.contrib.auth.models import User


class TestModelsDefaults(TestCase):
    def setUp(self):
        User.objects.create_user(
            first_name="Rogers",
            last_name="Macharia",
            password="1234",
            username="rogers",
            email="rogersmacharia@gmail.com"
        )
        Book.objects.create(title="Atomic Habits", price=100.00, genre="PG", description="Small habits, big difference")
        Author.objects.create(first_name="James", last_name="Clear")
        self.user = User.objects.get(pk=1)
        self.author = Author.objects.get(pk=1)
        self.book = Book.objects.get(pk=1)
        self.book.author.add(self.author)
        Order.objects.create(user=self.user)


class TestAuthorModel(TestModelsDefaults):
    def setUp(self):
        super().setUp()

    def test_object_saved(self):
        author = Author.objects.get(pk=1)
        self.assertEquals(author.first_name, self.author.first_name)
        self.assertEquals(author.last_name, self.author.last_name)
        self.assertEquals(author.pk, 1)


class TestBookModel(TestModelsDefaults):
    def setUp(self):
        super().setUp()
        self.book.author.add(self.author)

    def test_object_saved(self):
        self.assertEquals(self.book.title, "Atomic Habits")
        self.assertEquals(self.book.get_genre_display(), "Personal Growth")
        self.assertEquals(list(self.book.get_authors()), [self.author])


class TestOrderAndOrderItemModel(TestModelsDefaults):
    def setUp(self):
        super().setUp()
        self.order, created = Order.objects.get_or_create(user=self.user, complete=False)
        self.order_item, created = OrderItem.objects.get_or_create(user=self.user, order=self.order, book=self.book)
        self.order_item.quantity += 10
        self.order_item.save()

    def test_object_saved(self):
        self.assertEquals(self.order.user.first_name, "Rogers")
        self.assertEquals(self.order.complete, False)
        self.assertEquals(list(self.order.orderitem_set.all()), [self.order_item])
        self.assertEquals(self.order_item.quantity, 10)
        self.assertEquals(self.order_item.order, self.order)
        self.assertEquals(self.order_item.book, self.book)
        self.assertEquals(self.order_item.user.username, "rogers")
        self.assertEquals(self.order_item.book, self.book)
