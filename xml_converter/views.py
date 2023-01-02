# pylint: disable=missing-module-docstring
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.request import Request

from xml_converter.api import ConverterViewSet


@api_view(['POST', 'GET'])
def upload_page(request: Request) -> HttpResponse:
    if request.method == "POST":
        return ConverterViewSet().convert(request)
    return render(request, "upload_page.html")
