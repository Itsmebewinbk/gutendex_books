from django.urls import path
from books.views import BooksListView, LanguageListView, MimeTypeListView

urlpatterns = [
    path("books/", BooksListView.as_view()),
    path("languages/", LanguageListView.as_view()),
    path("mime_types/", MimeTypeListView.as_view()),
]
