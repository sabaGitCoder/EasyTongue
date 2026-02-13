from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings
import json
import random
import lexicon_engine
from lexicon.storage import shared_lexicon
# Create your views here.

def wellcome(request) :

    # opening dictionary folder and making a list out of it
    # instead of this I need to make lexicon type 
    # and use lexicon functions here to get the words

    #dictpath = os.path.join(settings.BASE_DIR,'dictionary.json')
    #try:
    #    with open(dictpath, 'r', encoding = 'utf-8') as dictfile:
    #       dict = json.load(dictfile)
    #except FileNotFoundError:
    #    dict = {}
    #x = len(dict)   
    #ranum = random.randint(0,x - 1)
    #dict = list(dict.items())
    #word = dict[ranum][0]

    
    # create lexicon type object
    
    # ask it to give you words

    raword = shared_lexicon.get_random_word()
    romaji = shared_lexicon.get_romaji(raword)
    return render(request, 'wellcome.html', {'word': raword , 'romaji' : romaji})