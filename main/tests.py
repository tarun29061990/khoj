from django.test import TestCase
from .services.location_search import LocationSearchService

import json


class LocationSearchTestCase(TestCase):

    def test_check_results_for_empty_query(self):
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

    def test_limit_results(self):
        locations = LocationSearchService().get_locations(term='a', limit='10')
        print(locations)
        desired_response_length = 10
        self.assertEqual(len(locations["data"]), desired_response_length)

    def test_results_starts_with(self):
        response = LocationSearchService().get_locations(term='a', limit='10')
        locations = response["data"]

        for location in locations:
            self.assertEqual(location["name"][0], 'a')
