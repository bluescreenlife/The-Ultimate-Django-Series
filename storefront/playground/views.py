from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# view function takes a request, returns response
# aka request handler, or action

# def say_hello(request):
#     # pull data from db,
#     # transform data, send emails etc

#     return HttpResponse('Hello World')

def calculate():
    x = 1
    y = 2
    return x

def say_hello(request):
    # pull data from db,
    # transform data, send emails etc

    x = calculate()

    return render(request, 'hello.html', {'name':'Andrew'})