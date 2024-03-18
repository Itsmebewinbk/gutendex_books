from django.test import TestCase

from .models import Author, Book, Format, Genre, Language, Shelf, Subject


class BookTestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            name="Test Author", birth_year=1980, death_year=2020
        )
        self.format = Format.objects.create(
            mime_type="text/plain", url="https://www.linkedin.com/"
        )
        self.genre = Genre.objects.create(name="Test Genre")
        self.language = Language.objects.create(code="en")
        self.shelf = Shelf.objects.create(name="Test Shelf")
        self.subject = Subject.objects.create(name="Test Subject")

        self.book = Book.objects.create(
            title="Test Book",
            gutenberg_id="123456",
            media_type="text",
            download_count=100,
        )
        self.book.authors.add(self.author)
        self.book.formats.add(self.format)
        self.book.genres.add(self.genre)
        self.book.languages.add(self.language)
        self.book.shelves.add(self.shelf)
        self.book.subjects.add(self.subject)
