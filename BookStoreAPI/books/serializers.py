from rest_framework import serializers
from .models import Books, Authors, Comments, Ratings

class BooksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('ISBN', 'bookTitle', 'bookDescription', 'bookPrice', 'bookAuthor', 'bookGenre', 'publisher', 'publishYear', 'bookCopiesSold')
        
class AuthorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ('id', 'authorFirstName', 'authorLastName', 'authorBiography', 'publisher')

class CommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('ISBN_COMMENT', 'bookComment', 'userName')

class RatingsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ('ISBN_RATING', 'rating', 'userName')

        