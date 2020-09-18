from django.shortcuts import render
from .models import Book, Author, Order, OrderItem
from django.views import generic
from django.shortcuts import get_object_or_404


def auto_complete(request):
    pass


class HomepageView(generic.View):
    def get(self, request):
        """
        Lists all the books
        :return: books dict
        """
        books = Book.objects.all()
        context = {
            "books": books,
        }
        return render(request, "home.html", context)

    def post(self, request):
        pass


class BookDetailView(generic.View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)

        related_books = Book.objects.filter(genre=book.genre)[:5]

        context = {
            "book": book,
            "related_books": related_books,
        }

        return render(request, "book_detail.html", context)
