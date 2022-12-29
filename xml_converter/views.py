from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.request import Request

from xml_converter.api import ConverterViewSet

@api_view(['POST', 'GET'])
def upload_page(request: Request) -> HttpResponse:
    """
    The api_view decorator allows us to modify the WSGI request
    so that it can be handled by Django REST framework.
    It also ensures that the response is properly formatted according
    to the Django REST framework standards.

    In this case, the decorator allows us to use the ConverterViewSet().convert method to handle the POST request
    """
    if request.method == "POST":
        return ConverterViewSet().convert(request)
    return render(request, "upload_page.html")
