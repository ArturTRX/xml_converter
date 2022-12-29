from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet
from rest_framework.renderers import JSONRenderer

from xml_converter.utils.xml_utils import xml_to_dict, parse_xml


class ConverterViewSet(ViewSet):
    # Note this is not a restful API
    # We still use DRF to assess how well you know the framework
    parser_classes = [MultiPartParser]
    renderer_classes = [JSONRenderer]

    @action(methods=["POST"], detail=False, url_path="convert", url_name="convert")
    def convert(self, request: Request, **kwargs) -> Response:
        if "file" not in request.data:
            return Response({"error": "No file provided"}, status=400)

        root = parse_xml(request.data["file"])
        if root is None:
            # XML file could not be parsed
            return Response({"error": "Invalid XML file"}, status=400)

        # Convert the Python dictionary to a JSON object

        json_data = xml_to_dict(root)

        return Response(json_data, content_type="application/json")
