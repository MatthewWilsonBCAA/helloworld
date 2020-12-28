# from django.shortcuts import render

# Create your views here.
import random
from django.http import HttpResponse


def homePageView(request):
    return HttpResponse(random.randint(0, 100))
