from django.contrib import admin

# Register your models here.
from .models import Books, Comments, Ratings, Authors, Profile, Payment

admin.site.register(Books)
admin.site.register(Comments)
admin.site.register(Ratings)
admin.site.register(Authors)
admin.site.register(Profile)
admin.site.register(Payment)