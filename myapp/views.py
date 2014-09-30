# Create your views here.
from django.http import HttpResponse
import datetime
from myapp.models import *
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def addBook(request):
	data = json.load(request)
	newBook = Book(title=data["title"], publisher=Publisher.objects.get(id=data["publisher"]), year=data["year"])
	newBook.save()
	return HttpResponse('added!')

@csrf_exempt
def editBook(request):
	data = json.load(request)
	editBook = Book.objects.get(id=data["id"])
	editBook.title = data["title"]
	editBook.year = data["year"]
	editBook.publisher = Publisher.objects.get(id=data["publisher"])
	editBook.save()
	return HttpResponse('edited!')

@csrf_exempt
def deleteBook(request):
	data = json.load(request)
	deleteBook = Book.objects.get(id=data["id"])
	deleteBook.delete()
	return HttpResponse('deleted!')