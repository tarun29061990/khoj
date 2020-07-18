from rest_framework import status
from django.http import JsonResponse


class APIResponse:

    @staticmethod
    def send(data, code=status.HTTP_200_OK, error=""):
        """Overrides rest_framework response

            :param data: data to be send in response
            :param code: response status code(default has been set to 200)
            :param error: error message(if any, not compulsory)
        """
        res = {"error": error, "response": data}
        return JsonResponse(data=res, status=code)
