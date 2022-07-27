from django.urls import path
from . import views
app_name = 'card'

urlpatterns = [
    path('book_list/', views.BookListView.as_view(), name="book-list"),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name="book-det"),
    path('book_add/', views.BookAddView.as_view(), name="book-add"),
    path('book_delete/<int:pk>/', views.BookDeleteView.as_view(), name="book-del"),
    path('book_edit/<int:pk>/', views.BookUpdateView.as_view(), name="book-edit"),
]
