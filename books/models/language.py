from django.db import models


class Language(models.Model):
    code = models.CharField(max_length=4)


class BookLanguages(models.Model):
    book = models.ForeignKey(
        "Book",
        on_delete=models.CASCADE,
        related_name="languages",
    )
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    class Meta:
        db_table = "books_book_languages"
