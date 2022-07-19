from rest_framework import serializers
from .models import Books, Authors, Comments, Ratings, Profile, Payment

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

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'password', 'firstName', 'lastName', 'email', 'homeAddress')

        extra_kwargs = {
            'username': {'read_only': True},
            'email': {'read_only': True}
        }

class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('username_creditCard', 'bankName', 'creditCard')

        extra_kwargs = {
            'username_creditCard': {'read_only': True}
        }