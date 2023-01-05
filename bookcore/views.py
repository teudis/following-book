from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.contrib import messages

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import View

from .models import Book, ListaLectura
# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = "book/list.html"
    context_object_name = "books"
    paginate_by = 9
    
    
class BookDetailView(LoginRequiredMixin,DetailView):
    model = Book    
    template_name = 'book/detail.html'
    context_object_name = 'book'  

class ListReadView(ListView):
    model = ListaLectura
    template_name =  'book/list_read.html'
    context_object_name = 'my_list'  
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
    
        
@login_required
def add_book(request, pk):
    book= get_object_or_404(Book, id=pk)
    user = request.user
    list_reading, created = ListaLectura.objects.get_or_create(user=user)       
    list_reading.books.add(book)
    my_list = ListaLectura.objects.filter(user=user)
    messages.success(request, 'Updated List successfully' )
    return render(request,'book/list_read.html',{'my_list': my_list})

@login_required
def remove_book(request, pk):
    book= get_object_or_404(Book, id=pk)
    user = request.user
    list_reading = ListaLectura.objects.get(user=user) 
    list_reading.books.remove(book)
    my_list = ListaLectura.objects.filter(user=user)
    messages.success(request, 'Removed Book successfully' )
    return render(request,'book/list_read.html',{'my_list': my_list})