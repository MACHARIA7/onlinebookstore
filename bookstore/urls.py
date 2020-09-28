from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path("", views.HomepageView.as_view(), name="home"),
    path("book/<int:pk>/", views.BookDetailView.as_view(), name="book-detail"),
    path("autocomplete/", views.auto_complete, name="autocomplete"),
    path("categories/technology/", views.TechnologyBooksView.as_view(), name="tech-books"),
    path("categories/personal-growth/", views.PersonalGrowthBooksView.as_view(), name="pg-books"),
    path("categories/science-fiction/", views.SciFiBooksView.as_view(), name="sci-fi-books"),
    path("categories/programming/", views.ProgrammingBooksView.as_view(), name="programming-books"),
    path("search/", views.SearchResultsView.as_view(), name="search"),
]
