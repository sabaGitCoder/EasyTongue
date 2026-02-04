from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def wellcome(request) :
    return render(request, 'wellcome.html')