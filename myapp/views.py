# Create your views here.
from django.http import HttpResponse
import datetime
# from myapp.models import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
