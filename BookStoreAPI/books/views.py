import imp
from pickle import FRAME
from xmlrpc.client import ResponseError
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

from .models import Books, Authors, Comments, Ratings
from .serializers import BooksSerializers, AuthorsSerializers, CommentsSerializers, RatingsSerializers

# Create your views here.
def welcomePage(request):
    if request.method == 'GET':
        return JsonResponse('Welcome to Group 10\'s bookstore API!', safe = False)

@api_view(['GET', 'POST'])
def getBooks(request):
    if request.method == 'GET':
        books = Books.objects.all()
        books_serializer = BooksSerializers(books, many = True)
        return JsonResponse(books_serializer.data, safe= False)
    elif request.method == 'POST':
        print(request.data)
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
        
    
@api_view(['GET', 'POST'])
def getAuthors(request):
    if request.method == 'GET':
        authors = Authors.objects.all()
        authors_serializer = AuthorsSerializers(authors, many = True)
        return JsonResponse(authors_serializer.data, safe= False)
    if request.method == 'POST':
        print(request.data)
        authors_serializer = AuthorsSerializers(data = request.data)
        if authors_serializer.is_valid():
            authors_serializer.save()
            return Response(authors_serializer.data, status = status.HTTP_201_CREATED)
   
@api_view(['GET'])     
def booksByAuthor(request, author):
    try:
        books = Books.objects.all()
    except Books.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    
    if request.method == 'GET':
        books_serializer = BooksSerializers(books)
        return Response(books_serializer.data)

@api_view(['GET'])
def getRateBook(request):

    if request.method == 'GET':
        book_ISBN = JSONParser().parse(request)
        ratings_book = Ratings.objects.all().filter(ISBN = book_ISBN['ISBN'])
        rating_serializer = RatingsSerializers(data=ratings_book, many=True)
        return JsonResponse(JSONParser().parse(rating_serializer))

@api_view(['GET'])
def ge(request):

    if request.method == 'GET':
        book_ISBN = JSONParser().parse(request)
        ratings_book = Ratings.objects.filter(ISBN = book_ISBN)
        rating_serializer = RatingsSerializers(data=ratings_book)
        return JsonResponse(JSONParser().parse(rating_serializer))

@api_view(['POST'])
def rateBook(request):

    if request.method == 'POST':
        rating_data = JSONParser().parse(request)
        rating_serializer = RatingsSerializers(data=rating_data)

        if rating_serializer.is_valid():
            rating_serializer.save()
            return JsonResponse('Rating added successfully')

@api_view(['POST'])
def commentBook(request):
    
    if request.method == 'POST':
        comment_data = JSONParser().parse(request)
        comment_serializer = CommentsSerializers(data=comment_data)

        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse('Rating added successfully')