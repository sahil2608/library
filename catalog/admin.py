from django.contrib import admin
from .models import Author, Genre, Language, Book, BookInstance

# admin.site.register(BookInstance)
# admin.site.register(Book)
admin.site.register(Language)
# admin.site.register(Author)
admin.site.register(Genre)


class BooksInline(admin.TabularInline):
    model = Book


# Define admin class list displayed so that when we have many author we can easily identify
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')] # show in same row
    inlines = [BooksInline]


admin.site.register(Author, AuthorAdmin)


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


# register the admin classes for Book Using the Decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    # can't directly specify the genre filed in list_display because it is ManyToManyField
    inlines = [BooksInstanceInline]

# Register the admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back') # list_filter will show option on side.
    fieldsets = (
        (None,{
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availablity', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
# Fieldsets None and Availability are titles, None because we don't want to give a title

