from django.shortcuts import render
from django.http import HttpResponse


def home(request):  # must take the response argument
    return HttpResponse('<h1> Blog Home </h1>')


def about(request):
    return HttpResponse('<h1> About us </h1>')
