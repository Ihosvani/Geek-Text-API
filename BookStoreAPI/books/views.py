from dataclasses import field
from email import message
import imp
from os import stat
from pickle import FRAME
from xmlrpc.client import ResponseError
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

from .models import Books, Authors, Comments, Payment, Profile, Ratings
from .serializers import BooksSerializers, AuthorsSerializers, CommentsSerializers, RatingsSerializers, ProfileSerializers, PaymentSerializers

# Create your views here.
def welcomePage(request):
    if request.method == 'GET':
        return JsonResponse('Welcome to Group 10\'s bookstore API!', safe = False)

@api_view(['GET'])
def getBooks(request):
    if request.method == 'GET':
        books = Books.objects.all()
        books_serializer = BooksSerializers(books, many = True)
        return JsonResponse(books_serializer.data, safe= False)

        
@api_view(['POST'])
def createBook(request):
    if request.method == 'POST':
        books_serializer = BooksSerializers(data = request.data)
        if books_serializer.is_valid():
            books_serializer.save()
            return Response(books_serializer.data, status = status.HTTP_201_CREATED)
        
@api_view(['GET'])     
def bookISBN(request, ISBN):
    try:
        book = Books.objects.get(pk=ISBN)
    except Books.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        books_serializer = BooksSerializers(book)
        return Response(books_serializer.data)

@api_view(['GET'])     
def getBookGenre(request, genre):
    try:
        book = Books.objects.all().filter(bookGenre = genre)
    except Books.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        books_serializer = BooksSerializers(book , many = True)
        return JsonResponse(books_serializer.data, safe= False)


@api_view(['GET'])
def getTopTenBooks(request):
    try:
        book = Books.objects.all().order_by('bookCopiesSold')[:10]
    except:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        books_serializer = BooksSerializers(book , many = True)
        return JsonResponse(books_serializer.data, safe= False)
    

        
    
@api_view(['GET'])
def getAuthors(request):
    if request.method == 'GET':
        authors = Authors.objects.all()
        authors_serializer = AuthorsSerializers(authors, many = True)
        return JsonResponse(authors_serializer.data, safe= False)
    
        
@api_view(['POST'])
def createAuthor(request):
    if request.method == 'POST':
        authors_serializer = AuthorsSerializers(data = request.data)
        print(authors_serializer)
        if authors_serializer.is_valid():
            authors_serializer.save()
            return Response(authors_serializer.data, status = status.HTTP_201_CREATED)
   
@api_view(['GET'])     
# not finished
def booksByAuthor(request, author):
    try:
        books = Books.objects.all().filter(bookAuthor=author)
    except Books.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        books_serializer = BooksSerializers(books, many=True)
        return Response(books_serializer.data)

@api_view(['POST'])
def rateBook(request):

    if(request.data['rating'] > 5 or request.data['rating'] < 0):
        return Response(status=status.HTTP_400_BAD_REQUEST, data='Rating must be between 0 and 5 inclusive')

    rating_serializer = RatingsSerializers(data=request.data)
    if rating_serializer.is_valid():
        rating_serializer.save()
        return Response(rating_serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND, data=rating_serializer.errors)

@api_view(['POST'])
def commentBook(request):
    
    comment_serializer = CommentsSerializers(data=request.data)
    if comment_serializer.is_valid():
        comment_serializer.save()
        return Response(comment_serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND, data=comment_serializer.errors)

@api_view(['GET'])
def getAverageRating(request, ISBN):

    ratings = Ratings.objects.all().filter(ISBN_RATING=ISBN)
    try:
        Books.objects.get(pk=ISBN)
    except Books.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data='Book with ISBN ' + str(ISBN) + ' does not exist')
    if(ratings.count() == 0):
        return Response(status=status.HTTP_404_NOT_FOUND, data='Book with ISBN ' + str(ISBN) + ' does not have any ratings')
    rating_serializer = RatingsSerializers(ratings, many=True)
    counter = 0
    ratingTotal = 0
    for rating in rating_serializer.data:
        counter+= 1
        ratingTotal += int(rating['rating'])
    return Response(ratingTotal/float(counter))

@api_view(['Get'])
def getCommentsAndRatings(request, ISBN):
    
    comments = Comments.objects.all().filter(ISBN_COMMENT = ISBN)
    ratings = Ratings.objects.all().filter(ISBN_RATING = ISBN).order_by('rating')

    try:
        Books.objects.get(pk=ISBN)
    except Books.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data='Book with ISBN ' + str(ISBN) + ' does not exist')
    if(ratings.count() == 0 and comments.count() == 0):
        return Response(status=status.HTTP_404_NOT_FOUND, data='Book with ISBN ' + str(ISBN) + ' does not have any ratings or comments')

    comments_serializer = CommentsSerializers(comments, many=True)
    rating_serializer = RatingsSerializers(ratings, many=True)

    return Response([comments_serializer.data, rating_serializer.data])

@api_view(['POST'])
def createProfile(request):
    if request.method == 'POST':

        profile_serializer = ProfileSerializers(data=request.data)
        print(profile_serializer.is_valid())
        print(profile_serializer.errors)
        if profile_serializer.is_valid():
            print('Profile has been made for this user')
            profile_serializer.save()
            return Response(profile_serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET'])     
def getProfile(request, username):
    try:
        profile = Profile.objects.get(pk=username)
    except Profile.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        profile_serializer = ProfileSerializers(profile)
        return Response(profile_serializer.data)

@api_view(['POST'])
def createPayment(request):
    if request.method == 'POST':
        print(request.data)
        payment_serializer = PaymentSerializers(data=request.data)
        print(payment_serializer)
        payment_serializer.is_valid()
        print(payment_serializer.errors)
        if payment_serializer.is_valid():
            print('Payment method has been added to this user')
            payment_serializer.save()
            return Response(payment_serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET'])     
def paymentByUser(request, username):
    try:
        payment = Payment.objects.filter(username_creditCard=username)
    except Payment.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        payment_serializer = PaymentSerializers(payment, many=True)
        return Response(payment_serializer.data)

@api_view(['PUT'])
def updateProfile(request, username):
    try:
        profile = Profile.objects.get(pk=username)
    except Profile.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
         profile_details = JSONParser().parse(request)
         profile_serializer = ProfileSerializers(profile, data=profile_details)
         
         if profile_serializer.is_valid():
            profile_serializer.save()
            return JsonResponse(profile_serializer.data)
    return JsonResponse(profile_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
