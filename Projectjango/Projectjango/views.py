from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("hello, world, . home page")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("hello, world, . about page")

def contact(request):
    return HttpResponse("hello, world, . Contact")