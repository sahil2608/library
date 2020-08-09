from django.urls import path
from . import views # . because file in same folder
#from django.contrib.auth.urls import
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    # Implementing view as a class,
    # we access an appropriate view function by calling the class method as_view()
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    # pk = primary key
    path('books/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
]

urlpatterns += [
    path('borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),
    path('mybooks/',views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('book/<uuid:pk>/new/', views.renew_book_librarian, name='renew-book-librarian'),
]

urlpatterns += [
    path('author/', views.AuthorListView.as_view(), name='authors'),
    path('author.<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]
