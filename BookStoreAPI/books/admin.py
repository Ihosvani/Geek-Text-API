from django.contrib import admin

# Register your models here.
from .models import Books
from .models import Authors

admin.site.register(Books)
admin.site.register(Authors)