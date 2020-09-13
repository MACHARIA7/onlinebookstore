from django.shortcuts import render
from .models import Book, Author, Order, OrderItem
from django.views import generic


class HomepageView(generic.View):
    def get(self):
        """
        Lists all the books
        :return: books dict
        """
