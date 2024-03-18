from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "books_genre"


class BookGenre(models.Model):
    book = models.ForeignKey(
        "Book",
        on_delete=models.CASCADE,
        related_name="genres",
    )
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        db_table = "books_book_genre"
