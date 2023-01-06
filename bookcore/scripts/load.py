import requests
import json
import logging
import environ
from pathlib import Path
from bookcore.models import Author, Category, Language, Book

logger = logging.getLogger(__name__)

#Config Django environ
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
API_KEY = env('API_KEY')

def run():  # sourcery skip: extract-method
    logger.info('Starting Reading books from Google API books')    
    value = 'python'
    
    try:        
        URL_API = f"https://www.googleapis.com/books/v1/volumes?q={value}&maxResults=30&key={API_KEY}"
        result = requests.get(URL_API)
        books = result.json()
        items = books["items"]
        encoded = json.dumps(items)
        decoded = json.loads(encoded) 
        for book in decoded:
            if book.get('volumeInfo', {}).get('authors', {}) is not None and book.get('volumeInfo', {}).get('categories', {}) and book.get('volumeInfo', {}).get('industryIdentifiers', {}) :
                print("URL",book["volumeInfo"]["infoLink"])             
                title = book["volumeInfo"]["title"]
                authors = book["volumeInfo"]["authors"]
                lan = book["volumeInfo"]["language"]
                categories = book["volumeInfo"]["categories"]
                publishedDate = book["volumeInfo"]["publishedDate"]
                description = book["volumeInfo"]["description"]            
                pageCount = book["volumeInfo"]["pageCount"]
                isbn = book["volumeInfo"]["industryIdentifiers"][0]["identifier"]
                image = book["volumeInfo"]["imageLinks"]["thumbnail"]
                addauthor(authors)
                addlanguage(lan)
                addcategories(categories)            
                try:
                    book = Book.objects.get(isbn=isbn) 
                    b = Book.objects.filter(isbn=isbn).update(title=title, summary=description, image= image) 
                    for author in authors:
                        a = Author.objects.get(full_name=author)
                        book.author.add(a)
                    for category in categories:
                        c = Category.objects.get(name=category)
                        book.categories.add(c)             
                except Book.DoesNotExist: 
                    language = Language.objects.get(name=lan)               
                    book = Book(title=title, summary=description, isbn=isbn, image= image)
                    book.language = language                
                    book.save()
                    for author in authors:
                        a = Author.objects.get(full_name=author)
                        book.author.add(a)
                    for category in categories:
                        c = Category.objects.get(name=category)
                        book.categories.add(c)
            
        logger.info('Process finished succefully')   
    
    except requests.exceptions.ConnectionError as err:
        logger.exception(err)
        
        
def addauthor(authors):    
    for author in authors:
        Author.objects.get_or_create(full_name=author)
        
def addcategories(categories):
    for category in categories:
        Category.objects.get_or_create(name=category)        
        
def addlanguage(lan):
    Language.objects.get_or_create(name=lan)