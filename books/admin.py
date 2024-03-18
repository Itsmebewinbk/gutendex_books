from django.contrib import admin
from books.models import (
    Author,
    Book,
    BookAuthor,
    BookLanguages,
    BookSubject,
    Language,
    Format,
    Subject,
    Genre,
    Shelf,
    BookShelf,
    BookGenre,
)

# admin.site.register(Author)
# admin.site.register(BookLanguages)
# admin.site.register(BookAuthor)
# admin.site.register(BookSubject)
# admin.site.register(Language)
# admin.site.register(Format)
# admin.site.register(Subject)
# admin.site.register(Genre)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "gutenberg_id", "media_type", "download_count")
    search_fields = ("title", "gutenberg_id")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "birth_year", "death_year")
    search_fields = ("name",)


@admin.register(Format)
class FormatAdmin(admin.ModelAdmin):
    list_display = ("mime_type", "url", "book", "charset")
    search_fields = ("mime_type", "url", "book__title")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("code",)
    search_fields = ("code",)


@admin.register(Shelf)
class ShelfAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(BookShelf)
class BookShelfAdmin(admin.ModelAdmin):
    list_display = ("book", "bookshelf")


@admin.register(BookGenre)
class BookGenreAdmin(admin.ModelAdmin):
    list_display = ("book", "genre")


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(BookAuthor)
class BookGenreAdmin(admin.ModelAdmin):
    list_display = ("book", "author")


@admin.register(BookLanguages)
class BookLanguageAdmin(admin.ModelAdmin):
    list_display = ("book", "language")


@admin.register(BookSubject)
class BookSubjectAdmin(admin.ModelAdmin):
    list_display = ("book", "subject")
