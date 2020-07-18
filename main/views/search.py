from django.http import HttpResponse
import json
from ..models import Location

def index(request):
    return HttpResponse('You are at KHOJ')

def search(request):

    location_list = Location.objects.filter(name__startswith='a').order_by('-count')

    return HttpResponse(location_list)

