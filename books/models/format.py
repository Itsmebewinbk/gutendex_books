from django.db import models


class Format(models.Model):
    mime_type = models.CharField(max_length=32)
    url = models.URLField(max_length=256)
    book = models.ForeignKey(
        "Book",
        on_delete=models.CASCADE,
        related_name="formats",
    )
    charset = models.CharField(max_length=50, blank=True, null=True)
