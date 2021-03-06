from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views import generic
from django.db.models import Q

from .models import Book


def auto_complete(request):
    """
    Adds the auto-complete functionality to the search bar
    :param request:
    :return:
    """
    if "term" in request.GET:
        books = Book.objects.filter(title__icontains=request.GET.get("term"))
        books_list = list()
        for book in books:
            books_list.append(book.title)
        return JsonResponse(books_list, safe=False)


class SearchResultsView(generic.View):
    """
    Adds a search functionality to the app
    """
    def get(self, request):
        query = request.GET.get("q")

        search_results = Book.objects.filter(
            Q(title__icontains=query) | Q(author__first_name__icontains=query) | Q(author__last_name__icontains=query)
        )

        context = {
            "search_results": search_results,
        }

        return render(request, "search_results.html", context)


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


class BookDetailView(generic.View):
    """Displays the book details"""
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)

        related_books = Book.objects.filter(genre=book.genre)[:5]

        context = {
            "book": book,
            "related_books": related_books,
        }

        return render(request, "book_detail.html", context)


class TechnologyBooksView(generic.View):
    """
    Displays books by category ---> Technology
    """
    def get(self, request):
        tech_books = Book.objects.filter(genre="Tech")

        context = {
            "tech_books": tech_books,
        }

        return render(request, "tech_books.html", context)


class PersonalGrowthBooksView(generic.View):
    def get(self, request):
        pg_books = Book.objects.filter(genre="PG")

        context = {
            "pg_books": pg_books,
        }

        return render(request, "pg_books.html", context)


class SciFiBooksView(generic.View):
    def get(self, request):
        sci_fi_books = Book.objects.filter(genre="Sci-Fi")

        context = {
            "sci_fi_books": sci_fi_books,
        }

        return render(request, "sci_fi_books.html", context)


class ProgrammingBooksView(generic.View):
    def get(self, request):
        programming_books = Book.objects.filter(genre="Prog")

        context = {
            "programming_books": programming_books,
        }

        return render(request, "programming_books.html", context)
