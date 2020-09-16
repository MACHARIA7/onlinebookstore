from django.db import models
from django.contrib.auth.models import User


GENRE = [
    ("PF", "Personal Finance"),
    ("Sci-Fi", "Science Fiction"),
    ("Tech", "Technology"),
    ("Prog", "Computer Programming"),
    ("PG", "Personal Growth")
]


class Author(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Book(models.Model):
    author = models.ManyToManyField(Author, related_name="books")
    title = models.CharField(max_length=100, blank=True, null=True)
    genre = models.CharField(choices=GENRE, max_length=100, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_authors(self):
        return self.author.all()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, blank=True, null=True)
    transaction_id = models.CharField(max_length=50, blank=True, null=True)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, blank=True, null=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0, blank=True, null=True)
