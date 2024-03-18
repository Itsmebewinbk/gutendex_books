from rest_framework import serializers
from books.models import Book


class BooksListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        authors = instance.authors.select_related(
            "author",
        )
        languages = instance.languages.values_list(
            "language__code",
            flat=True,
        )
        subjects = instance.subjects.values_list(
            "subject__name",
            flat=True,
        )
        genres = instance.genres.values_list(
            "genre__name",
            flat=True,
        )
        bookshelves = instance.shelves.values_list(
            "bookshelf__name",
            flat=True,
        )
        formats = instance.formats.all()

        data["author_details"] = [
            {
                "name": author.author.name,
                "birth_year": author.author.birth_year,
                "death_year": author.author.death_year,
            }
            for author in authors
            if authors
        ]
        data["languages"] = list(languages)
        data["subjects"] = list(subjects)
        data["bookshelves"] = list(bookshelves)
        data["genres"] = list(genres)
        data["formats"] = [
            {
                "mime-type": format.mime_type,
                "charset": format.charset,
                "url": format.url,
            }
            for format in formats
            if formats
        ]

        return data
