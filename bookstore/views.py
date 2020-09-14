from django.shortcuts import render
from .models import Book, Author, Order, OrderItem
from django.views import generic


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
