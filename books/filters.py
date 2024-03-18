from django.db.models import Q
from coreapi import Field
from rest_framework.filters import BaseFilterBackend
from rest_framework.compat import coreschema


class BooksFilterBackend(BaseFilterBackend):
    def get_schema_fields(self, view):
        return [
            Field(
                name="gutenberg_id",
                location="query",
                required=False,
                schema=coreschema.Integer(),
            ),
            Field(
                name="topic",
                location="query",
                required=False,
                schema=coreschema.String(),
            ),
            Field(
                name="language_id",
                location="query",
                required=False,
                schema=coreschema.Integer(),
            ),
            Field(
                name="format_id",
                location="query",
                required=False,
                schema=coreschema.Integer(),
            ),
        ]

    def filter_queryset(self, request, queryset, view):
        topic = request.query_params.get("topic", None)
        gutenberg_id = request.query_params.get("gutenberg_id", None)
        language_id = request.query_params.get("language_id")
        format_id = request.query_params.get("format_id")

        if topic:
            queryset = queryset.filter(
                Q(subjects__subject__name__icontains=topic)
                | Q(
                    shelves__bookshelf__name__icontains=topic,
                )
            )
        if gutenberg_id:
            queryset = queryset.filter(gutenberg_id=gutenberg_id)
        if language_id:
            queryset = queryset.filter(languages__language_id=language_id)

        if format_id:
            queryset = queryset.filter(formats__id=format_id)
        return queryset
