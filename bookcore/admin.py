from django.contrib import admin
from .models import Author, Book, Category, Language, ListaLectura
# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Language)
admin.site.register(ListaLectura)