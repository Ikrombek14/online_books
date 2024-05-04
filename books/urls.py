from django.urls import path

from .views import get_authors, get_books, get_book, add_book, update_book, delete_book

urlpatterns = [
    path('', get_authors, name='get_authors'),
    path('books/<int:pk>', get_books, name='get_books'),
    path('detail/<int:pk>', get_book, name='get_book'),
    path('add_book', add_book, name='add_book'),
    path('update_book/<int:pk>', update_book, name='update_book'),
    path('delete_book/<int:pk>', delete_book, name='delete_book'),


]