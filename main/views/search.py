from django.http import HttpResponse
import json
from ..models import Location
from ..utils import APIResponse

def index(request):
    return HttpResponse('You are at KHOJ')

def search(request):

    term = request.GET.get('term')
    if term:
        try:

            location_list = Location.objects.filter(name__startswith=term).order_by('-popularity')
            locations = location_list.all()
            response = []
            for location in locations:
                response.append({'name': location.name, 'popularity': location.popularity})

            return APIResponse.send(json.dumps(response))

        except Exception as e:

            return APIResponse.send("", code=500, error=e)

    else:
        return APIResponse.send("", code=400, error='Invalid request!! Query parameter term should have some value')
