from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def products(request):
    return HttpResponse('Esta es la vista para los prodcutos')