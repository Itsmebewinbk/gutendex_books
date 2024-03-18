from rest_framework import serializers
from books.models import Language


class LanguageListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ("id", "code")
