from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import BookListView, BookDetailView

urlpatterns = [
    path("", BookListView.as_view(), name="home"),
    path("book/detail/<int:pk>", BookDetailView.as_view(), name="book-detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
