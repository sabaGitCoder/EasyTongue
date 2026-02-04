from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings
import json
import random
# Create your views here.

def wellcome(request) :
    dictpath = os.path.join(settings.BASE_DIR,'dictionary.json')
    try:
        with open(dictpath, 'r', encoding = 'utf-8') as dictfile:
            dict = json.load(dictfile)
    except FileNotFoundError:
        dict = {}
    x = len(dict)   
    ranum = random.randint(0,x - 1)
    dict = list(dict.items())
    word = dict[ranum][0]
    return render(request, 'wellcome.html', {'word': word})