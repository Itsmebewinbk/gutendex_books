from rest_framework.generics import ListAPIView
from books.serializers import (
    Book,
    Language,
    Format,
    LanguageListSerializers,
    BooksListSerializers,
    MimeTypeListSerializers,
)
from rest_framework.filters import SearchFilter
from books.filters import BooksFilterBackend


class BooksListView(ListAPIView):
    serializer_class = BooksListSerializers
    filter_backends = (SearchFilter, BooksFilterBackend)
    search_fields = ("title", "gutenberg_id")

    def get_queryset(self):
        return Book.objects.prefetch_related(
            "authors", "languages", "subjects", "genres", "shelves", "formats"
        ).order_by("-id")


class LanguageListView(ListAPIView):
    serializer_class = LanguageListSerializers
    filter_backends = (SearchFilter,)
    search_fields = ("code",)
    queryset = Language.objects.all()


class MimeTypeListView(ListAPIView):
    serializer_class = MimeTypeListSerializers
    filter_backends = (SearchFilter,)
    search_fields = ("mime_type",)
    queryset = Format.objects.all()
