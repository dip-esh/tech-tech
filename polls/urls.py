from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.members, name="index"),
    path("data", views.get_data, name="getData"),
    path("books", views.BookListView.as_view(), name="books"),
    path("book/<int:pk>", views.BookDetailView.as_view(), name="book"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.get_name, name="signup"),
    path('book_delete/<int:pk>', views.BookDeleteView.as_view(), name="book-delete"),
]
