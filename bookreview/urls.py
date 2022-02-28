from django.urls import path
from .views import index_view, AuthorView,BookView,AuthorInstanceView

urlpatterns = [
    path('home', index_view, name='index_view'),

    path('authors/', AuthorView.as_view(), name='author-list'),
    path('books/', BookView.as_view(), name='book-list'),
    path('authors/<int:pk>', AuthorInstanceView.as_view(), name='author-instance')

]
