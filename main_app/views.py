from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Wacky Wish Widget</h1>')
