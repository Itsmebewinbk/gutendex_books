from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=128)
    birth_year = models.SmallIntegerField(blank=True, null=True)
    death_year = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class BookAuthor(models.Model):
    book = models.ForeignKey(
        "Book",
        on_delete=models.CASCADE,
        related_name="authors",
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        db_table = "books_book_authors"
