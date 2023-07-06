from django.urls import path
from book.views import BookListView, BookDetailView


urlpatterns = [
    path('books/', BookListView.as_view()),
    path('books/<int:id>/', BookDetailView.as_view()),

]
