from rest_framework import serializers
from models import *

# Serializers define the API representation.

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('author_firstname', 'author_lastname')

class BooksSerializer(serializers.Serializer):
   book_name = serializers.CharField(max_length=100)
   author = AuthorSerializer()

class StoresSerializer(serializers.Serializer):
    store_name = serializers.CharField(max_length=100)

class SalesSerializer(serializers.Serializer):
    Store = StoresSerializer()
    Book = BooksSerializer()
    sold = serializers.IntegerField()



