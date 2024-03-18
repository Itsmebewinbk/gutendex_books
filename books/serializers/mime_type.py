from rest_framework import serializers
from books.models import Format


class MimeTypeListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Format
        fields = ("id", "mime_type")
