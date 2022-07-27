import requests
from random import randint

NUMBER_OF_ENTRIES = 1000


urlCreateBooks = 'http://localhost:8000/admin/books/'
urlCreateAuthors = 'http://localhost:8000/admin/authors/'
urlCreateComment = 'http://localhost:8000/books/commentBook/'
urlCreateRatings = 'http://localhost:8000/books/rateBook/'
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}



payloadBook = {
    'ISBN': '',
    'bookTitle': '',
    'bookDescription': '',
    'bookPrice': '',
    'bookAuthor': '',
    'bookGenre': '',
    'publisher': '',
    'publishYear': '',
    'bookCopiesSold': ''
}

for i in range(20):

    fChar = ord('a') + int(i/26)
    sChar = ord('a') + i%26
    ISBN = 1000000000000 + i
    bookTitle = '' + chr(fChar) + chr(sChar)
    bookDescription = '' + chr(fChar) + chr(sChar)
    bookPrice = i
    bookAuthor = '' + chr(fChar) + chr(sChar)
    bookGenre = ['Classic', 'Terror', 'Comedy', 'Action', 'Horror', 'Thrill']
    publisher = '' + chr(fChar) + chr(sChar) + chr(fChar) + chr(sChar)
    publishYear = i + 1500
    bookCopiesSold = i

    payloadBook['ISBN'] = ISBN
    payloadBook['bookTitle'] = bookTitle
    payloadBook['bookDescription'] = bookDescription
    payloadBook['bookPrice'] = bookPrice
    payloadBook['bookAuthor'] = bookAuthor
    payloadBook['bookGenre'] = bookGenre[randint(0,5)]
    payloadBook['publisher'] = publisher
    payloadBook['publishYear'] = publishYear
    payloadBook['bookCopiesSold'] = bookCopiesSold

    r = requests.post(urlCreateBooks, data=payloadBook)
    print('Book: ' + str(i) + ' response: ')
    print(r)

payloadAuthors = {
    'authorFirstName': '',
    'authorLastName': '',
    'authorBiography': '',
    'publisher': ''
}

for i in range(20):

    fChar = ord('a') + int(i/26)
    sChar = ord('a') + i%26
    authorFirstName = '' + chr(fChar) + chr(sChar)
    authorLastName = '' + chr(fChar) + chr(sChar)
    authorBiography = '' + chr(fChar) + chr(sChar) 
    publisher = '' + chr(fChar) + chr(sChar) 

    payloadAuthors['authorFirstName'] = authorFirstName
    payloadAuthors['authorLastName'] = authorLastName
    payloadAuthors['authorBiography'] = authorBiography
    payloadAuthors['publisher'] = publisher

    r = requests.post(urlCreateAuthors, data=payloadAuthors)
    print('Author: ' + str(i) + ' response: ')
    print(r)

payloadComment = {
    'ISBN_COMMENT': '',
    'bookComment': '',
    'userName': ''
}

for i in range(20):

    fChar = ord('a') + int(i/26)
    sChar = ord('a') + i%26
    ISBN = 1000000000000 + i
    bookComment = '' + chr(fChar) + chr(sChar)
    userName = '' + chr(fChar) + chr(sChar)

    payloadComment['ISBN_COMMENT'] = ISBN
    payloadComment['bookComment'] = bookComment
    payloadComment['userName'] = userName

    r = requests.post(urlCreateComment, data=payloadComment)
    print('Comment: ' + str(i) + ' response: ')
    print(r)

payloadRatings = {
    'ISBN_RATING': '',
    'rating': '',
    'userName': ''
}

for i in range(20):

    fChar = ord('a') + int(i/26)
    sChar = ord('a') + i%26
    ISBN = 1000000000000 + i
    rating = i % 6
    userName = '' + chr(fChar) + chr(sChar)

    payloadRatings['ISBN_RATING'] = ISBN
    payloadRatings['rating'] = rating
    payloadRatings['userName'] = userName
    r = requests.post(urlCreateRatings, data=payloadRatings)
    print('Rating: ' + str(i) + ' response: ')
    print(r)