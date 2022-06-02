from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from .permissions import IsOwnerOrReadOnly

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
