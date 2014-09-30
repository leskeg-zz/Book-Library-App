from django.contrib import admin
from myapp.models import *

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publisher', 'year')

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname')

admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)