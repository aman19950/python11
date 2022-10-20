import re
from django.shortcuts import render
from .models import *


def index(request):

    fetch_obj = Registration.objects.get(first_name='sonudfg')
    # name = "sonu"
    return render(request, 'home.html', {'a': fetch_obj})


def contact(request):
    return render(request, 'contact.html')
