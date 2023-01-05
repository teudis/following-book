import requests
import json
import logging
from bookcore.models import Author, Category, Language, Book

logger = logging.getLogger(__name__)

def run():  # sourcery skip: extract-method
    logger.info('Starting Reading books from Google API books')
    value = 'python'
    apikey = 'AIzaSyD_mV_JDpR_EmXEEjnfceEt6-Xxflg-rV4'
    try:        
        URL_API = f"https://www.googleapis.com/books/v1/volumes?q={value}&maxResults=10&key={apikey}"
        result = requests.get(URL_API)
        books = result.json()
        items = books["items"]
        encoded = json.dumps(items)
        decoded = json.loads(encoded) 
        for book in decoded:
            
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
    listauthors = []
    for author in authors:
        Author.objects.get_or_create(full_name=author)
        
def addcategories(categories):
    for category in categories:
        Category.objects.get_or_create(name=category)        
        
def addlanguage(lan):
    Language.objects.get_or_create(name=lan)