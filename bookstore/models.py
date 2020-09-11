from django.db import models


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
