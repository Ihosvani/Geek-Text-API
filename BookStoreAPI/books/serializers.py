from rest_framework import serializers
from .models import Books, Authors

class BooksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('ISBN', 'bookTitle', 'bookDescription', 'bookPrice', 'bookAuthor', 'bookGenre', 'publisher', 'publishYear', 'bookCopiesSold')
        
class AuthorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ('id', 'authorFirstName', 'authorLastName', 'authorBiography', 'publisher')