from django.urls import path

from .views import BookListView, AuthorListView

urlpatterns = [
    path('books/', BookListView.as_view()),
    path('authors/', AuthorListView.as_view()),
]