from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import Book, ListaLectura
# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = "book/list.html"
    context_object_name = "books"
    
    
class BookDetailView(DetailView):
    model = Book    
    template_name = 'book/detail.html'
    context_object_name = 'book'
    
    
class AddListReadView(CreateView):
    pass
    