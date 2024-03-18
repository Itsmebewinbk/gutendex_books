from django.db import models


class Shelf(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "books_bookshelf"


class BookShelf(models.Model):
    book = models.ForeignKey(
        "Book", on_delete=models.CASCADE, related_name="shelves"
    )
    bookshelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)

    class Meta:
        db_table = "books_book_bookshelves"
