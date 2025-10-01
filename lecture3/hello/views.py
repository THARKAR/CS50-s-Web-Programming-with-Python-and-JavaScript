from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # when we render something we need the http request and the name of the template. templates folder is already understood.
    return render(request, 'hello/index.html')


# Only Request Parameter is Mandatory, Other Parameters are Optional. Here are the available parameters:
# request: The HttpRequest object.

def brain(request):
    return HttpResponse('What the hell, brain?')


def david(req):
    return HttpResponse('Hello, David')


def greet(req, name):
    return render(req,'hello/greet.html', {
        'name': name.capitalize()
    })






