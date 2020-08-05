from django.shortcuts import render
from . models import Book, BookInstance, Author, Genre, Language


def index(request):
    num_books = Book.objects.all().count() # genrate thee counts of the some of the main objects
    num_instances = BookInstance.objects.all().count()

    # Available books (status ='a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    context={
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    } # Render the HTMl template index.html with the data in the context(python dictionary) variable
    return render(request, 'index.html', context=context)