from rest_framework import serializers
from .models import Books, Authors, Comments, Ratings, Profile, Payment

class BooksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('ISBN', 'bookTitle', 'bookDescription', 'bookPrice', 'bookAuthor', 'bookGenre', 'publisher', 'publishYear', 'bookCopiesSold')
        
class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model: Profile
        fields = ('profileID', 'username', 'password', 'firstName', 'lastName', 'email', 'homeAddress')
        
class AuthorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ('id', 'authorFirstName', 'authorLastName', 'authorBiography', 'publisher')

class CommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('ISBN_COMMENT', 'bookComment', 'userId')

class RatingsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ('ISBN_RATING', 'rating', 'userId')

class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('username_creditCard', 'bankName', 'creditCard')

        