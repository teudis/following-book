from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    path("list", BookListView.as_view(), name="list-books"),
    path('detail/<int:pk>', BookDetailView.as_view()),

]
