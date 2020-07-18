from django.test import TestCase
from .services.location_search import LocationSearchService
from .models import Location
from .utils.bulk_manager import BulkCreateManager
from django.utils import timezone

import json
import os


class LocationSearchTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")

        bulk_mgr = BulkCreateManager(chunk_size=20)
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file = open(base_dir + '/main/data/test_data.csv', 'r')

        counter = 0
        for each_line in file:
            popularity, name = each_line.split(" ")
            name = name.strip()
            bulk_mgr.add(Location(name=name, popularity=int(popularity), display_name=' '.join(name.split("_")),
                                  created_at=timezone.now(), updated_at=timezone.now()))
            if counter == 10:
                break

            counter += 1

        bulk_mgr.done()
        print("setUpTestData:finished \n")


    def test_check_results_for_empty_query(self):
        print("test_check_results_for_empty_query: Running test to check the response for expty query")

        locations = LocationSearchService().get_locations('')
        desired_response = {
            "data": "",
            "code": 400,
            "error": "Invalid Request!! Query Parameter term should have some value"
        }
        self.assertJSONEqual(
            json.dumps(locations),
            json.dumps(desired_response)
        )

        print("test_check_results_for_empty_query: finished \n")

    def test_limit_results(self):
        print("test_limit_results: Running test to limit the response")

        locations = LocationSearchService().get_locations(term='a', limit='10')
        desired_response_length = 10
        self.assertEqual(len(locations["data"]), desired_response_length)

        print("test_limit_results: finished \n")

    def test_results_starts_with(self):
        print("test_results_starts_with: Running test to check that the response is starting with a given query")

        response = LocationSearchService().get_locations(term='a', limit='10')
        locations = response["data"]

        for location in locations:
            self.assertEqual(location["name"][0], 'a')

        print("test_results_starts_with: finished \n")

    def test_where_no_results_come(self):
        print("test_where_no_results_come: Running test to check for empty response when data is not in DB")

        response = LocationSearchService().get_locations(term='b', limit=10)
        locations = response["data"]
        desired_response_length = 0

        self.assertEqual(len(locations), desired_response_length)

        print("test_where_no_results_come: finished \n")

    def test_results_order_by_popularity(self):
        print("test_results_order_by_popularity: Running test to check the response is ordered by popularity descending")

        response = LocationSearchService().get_locations(term='b', limit=10, order_by='-popularity')
        locations = response["data"]
        popularities = [location.popularity for location in locations]

        for counter in range(len(popularities)-1):
            self.assertGreaterEqual(popularities[counter], popularities[counter+1])

        print("test_results_order_by_popularity: finished \n")
