from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Author,Book
from .serializers import AuthorSerializer,BookSerializer
from rest_framework.generics import ListAPIView,ListCreateAPIView


# Create your views here.

def index_view(request):
    """
    Ensure the user can only see their own profiles.
    """
    response = {
        'authors': Author.objects.all(),
        # 'books': Book.objects.all(),
    }
    return render(request, 'bookreview/index.html', response)


class AuthorView(ListCreateAPIView):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer



class BookView(ListAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorInstanceView(generics.RetrieveAPIView):
    """
    Returns a single author.
    Also allows updating and deleting
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer



# class AuthorView(ListAPIView):

#     def get(self, request):
#         authors = Author.objects.all()
        
#         serializer = AuthorSerializer(authors, many=True)
#         return Response(serializer.data)

