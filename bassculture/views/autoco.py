from rest_framework.generics import GenericAPIView
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.reverse import reverse
import json
from django.http import HttpResponse
from bassculture.renderers.custom_html_renderer import CustomHTMLRenderer
from bassculture.models.author import Author


def json_response_view(request):
    q = request.GET.get('q', '')
    response_data = Author.objects.filter(surname__startswith=q).values("surname")
    return HttpResponse(json.dumps(response_data), content_type="application/json")


class AutocoView(GenericAPIView):
    renderer_classes = (JSONRenderer, renderers.BrowsableAPIRenderer)

    def get(self, request, *args, **kwargs):
        return Response({
            })
