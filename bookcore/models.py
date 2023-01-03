from django.db import models
from django.urls import reverse
from django. contrib. auth import get_user_model

# Create your models here.
class Genre(models.Model):   
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        """String for representing the Model object."""
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        """String for representing the Model object."""
        return self.name
    
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    
    def __str__(self):
        """String for representing the Model object."""
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self):     
        """Returns the url to access a particular author instance."""   
        return reverse('author-detail', kwargs={'pk': self.pk})
    
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True) 
    summary = models.TextField(max_length=1000, help_text="Insert description about book")
    isbn = models.CharField('ISBN', unique=True, max_length=13, help_text='13 Characters <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="Seleccione un genero para este libro")
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='book/%Y/%m/%d')
    
    class Meta:
        ordering = ['title', 'author']
        
    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('book-detail', kwargs={'pk': self.pk})

    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    
class ListaLectura(models.Model):
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE,)
    books = models.ManyToManyField(Book)
