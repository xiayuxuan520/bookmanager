from django.urls import path
from book.views import BookListView


urlpatterns = [
    path('books/', BookListView.as_view()),

]
