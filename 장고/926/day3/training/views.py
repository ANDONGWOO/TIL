from multiprocessing import context
from unicodedata import name
from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, "index.html")


def is_odd_even(request, _number):
    context = {
        "name": _number,
    }
    return render(request, "is_odd_even.html", context)
