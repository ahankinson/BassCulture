from rest_framework.generics import GenericAPIView
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.reverse import reverse

from bassculture.renderers.custom_html_renderer import CustomHTMLRenderer


class SiglaViewHTMLRenderer(CustomHTMLRenderer):
    template_name = "sigla.html"


class SiglaView(GenericAPIView):
    renderer_classes = (JSONRenderer, SiglaViewHTMLRenderer,
                        renderers.BrowsableAPIRenderer)

    def get(self, request, *args, **kwargs):
        return Response({
            })
