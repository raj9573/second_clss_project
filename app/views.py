from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):

    return HttpResponse("Welcome to our website")


def first(request):
    data = {'name':'Merida!!!'}

    return render(request,'first.html',data)
