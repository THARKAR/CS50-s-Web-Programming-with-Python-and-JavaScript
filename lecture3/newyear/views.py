from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def index(req):
    now = datetime.now()
    return render(req, 'newyear/index.html',{
        'newyear': now.day == 1 and now.month == 1
    })

