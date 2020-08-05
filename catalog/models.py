from django.db import models
from django.urls import reverse # Used to generate URLS by reversing the URL pattrens
import uuid # required book instances


class Genre(models.Model):
    # models representing a book genre
    name = models.CharField(max_length=200, help_text='Enter a book genre')

    def __str__(self):
        return self.name
        # string representing the model object


class Book(models.Model):
    # representing a book (but not a specific copy of book)
    title = models.CharField(max_length=200)

    # Foreign key is used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    # ManyToMANYField used because nre can contain many books. BoOks can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null = True)

    def display_genre(self):
        return ','.join([genre.name for genre in self.genre.all()[:3]])
        # required to display Genre in Admin because genre cant be directly displayed

    display_genre.short_description = 'Genre'

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class BookInstance(models.Model):# Model representing the specific copy of the book that can be borrowed.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='unique ID for this book')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved')
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank= True,
        default= 'm',
        help_text='Book Availability',
    )

    class Meta:
        ordering = ['due_back'] # to order the records when they are returned in a query

    def __str__(self):# Shown in output in admin panel
        return f'{self.id} ({self.book.title})'


class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self): # view on site option on website
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'


class Language(models.Model):
    name = models.CharField(max_length=30,help_text='Enter the language of the book (ex.  French, Hindi)')

    def __str__(self):
        return self.name
