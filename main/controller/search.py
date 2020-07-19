from django.http import HttpResponse

from ..models import Location

from ..utils.api_response import APIResponse
from ..utils.bulk_manager import BulkCreateManager
from ..utils.api_filters import ApiFilters

from ..services.location_search import LocationSearchService
from django.utils import timezone

from ..serializers.search_request_serailizer import SearchSerializer
import os

from django.core.cache import cache
from ratelimit.decorators import ratelimit


def index(request):
    return HttpResponse('Welcome to KHOJ')

@ratelimit(key='ip', rate='20/m', method=ratelimit.ALL)
def search(request):

    if request.method == 'GET':

        if SearchSerializer.validate(request=request):

            term = request.GET.get('term')
            count = request.GET.get('count')

            order_by = request.GET.get('sort')

            cache_key = term+count+order_by
            if cache.get(cache_key):

                return APIResponse.send(cache.get(cache_key))
            else:
                try:
                    response = LocationSearchService().get_locations(term=term, order_by=order_by, limit=count)

                    if response["code"] == 200:
                        cache.set(cache_key, response["data"])
                        return APIResponse.send(response["data"])
                    else:
                        return APIResponse.send(data="", code=response["code"], error=response["error"])

                except Exception as e:

                    return APIResponse.send("", code=500, error=e)

        else:

            return APIResponse.send("", code=400, error='Invalid Request')

    else:

        return APIResponse.send("", code=404, error='Request not found')


def data_entry(request):
    bulk_mgr = BulkCreateManager(chunk_size=20)

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file = open(base_dir+'/data/location_data.csv', 'r')

    for each_line in file:
        popularity, name = each_line.split(" ")
        name = name.strip()
        bulk_mgr.add(Location(name=name,popularity=int(popularity),display_name=' '.join(name.split("_")),created_at=timezone.now(),updated_at=timezone.now()))

    bulk_mgr.done()

    return APIResponse.send(data="success", code=200)
