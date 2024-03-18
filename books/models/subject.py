from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class BookSubject(models.Model):
    book = models.ForeignKey(
        "Book",
        on_delete=models.CASCADE,
        related_name="subjects",
    )
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        db_table = "books_book_subjects"
