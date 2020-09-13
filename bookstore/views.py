from django.shortcuts import render
<<<<<<< HEAD
from .models import Book, Author, Order, OrderItem
=======
from .models import Boo
>>>>>>> views
from django.views import generic


class HomepageView(generic.View):
    def get(self):
        """
        Lists all the books
        :return: books dict
        """
