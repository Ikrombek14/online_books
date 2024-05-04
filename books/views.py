from django.shortcuts import render, redirect
from .models import Authors, Books
from .forms import BooksForm


# Create your views here.
def get_authors(request):
    authors = Authors.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'index.html', context)

def get_books(request, pk):
    books = Books.objects.filter(author_id=pk)
    context = {
        'books': books
    }
    return render(request, 'books.html', context)

def get_book(request, pk):
    book = Books.objects.get(id=pk)
    context = {
        'book': book
    }
    return render(request, 'detail.html', context)

def add_book(request):
    form=BooksForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('get_authors')
    context = {
        'form': form
    }
    return render(request, 'create.html', context)

def update_book(request, pk):
    book=Books.objects.get(id=pk)
    form=BooksForm(instance=book)
    if request.method == 'POST':
        form=BooksForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("get_authors")
    context = {
        'book': book,
        'form': form
    }
    return render(request, 'update.html', context)

def delete_book(request, pk):
    book=Books.objects.get(id=pk)
    if request.method == 'POST':
        book.delete()
        return redirect("get_authors")
    context = {
        'book': book
    }
    return render(request, 'delete.html', context)


