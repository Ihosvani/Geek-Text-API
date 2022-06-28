from django.db import models

# Create your models here.
class Books(models.Model):
    ISBN = models.CharField(primary_key=True, max_length=13)
    bookTitle = models.CharField(max_length=500)
    bookDescription = models.TextField()
    bookPrice = models.CharField(max_length=7)
    bookAuthor = models.CharField(max_length=500)
    bookGenre = models.CharField(max_length=500)
    publisher = models.CharField(max_length=500)
    publishYear = models.CharField(max_length=4)
    bookCopiesSold = models.CharField(max_length=500)
    
    def __str__(self):
        return self.ISBN
    
class Comments(models.Model):
    ISBN_COMMENT= models.ManyToManyField(Books)
    bookComment = models.CharField(max_length=10000)
    commentDate = models.DateField(auto_now_add=True, blank=True)
    userName = models.CharField(max_length=50)

    def __str__(self):
        return self.ISBN

class Ratings(models.Model):
    ISBN_RATING = models.ManyToManyField(Books)
    rating = models.CharField(max_length=1)
    ratingDate = models.DateField(auto_now_add=True, blank=True)
    userName = models.CharField(max_length=50)

    def __str__(self):
        return self.ISBN

class Authors(models.Model):
    id = models.AutoField(primary_key=True)
    authorFirstName = models.CharField(max_length=500)
    authorLastName = models.CharField(max_length=500)
    authorBiography = models.TextField()
    publisher = models.CharField(max_length=500)
    
    def __str__(self):
        return self.authorFirstName + ' ' + self.authorLastName
    
