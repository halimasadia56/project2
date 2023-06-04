from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def sample2(request):
    return HttpResponse('this is the second app')