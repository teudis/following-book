from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import BookListView, BookDetailView, ListReadView
from .views import add_book, remove_book

urlpatterns = [
    path("", BookListView.as_view(), name="home"),
    path("book/detail/<int:pk>", BookDetailView.as_view(), name="book-detail"),
    path("listread/", ListReadView.as_view(), name="list-reading"),
    path("add_book/<int:pk>", add_book, name="book-add"),
    path("remove_book/<int:pk>", remove_book, name="book-remove"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
