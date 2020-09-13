from django.shortcuts import render
from .models import *
from django.views import generic


class HomepageView(generic.View):
    def get(self):
        """
        Lists all the books
        :return: books dict
        """
