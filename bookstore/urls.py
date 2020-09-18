from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path("", views.HomepageView.as_view(), name="home"),
    path("book/<int:pk>/", views.BookDetailView.as_view(), name="book-detail")
]
