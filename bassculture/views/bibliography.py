from rest_framework.generics import GenericAPIView
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.reverse import reverse

from bassculture.renderers.custom_html_renderer import CustomHTMLRenderer


class BibliographyViewHTMLRenderer(CustomHTMLRenderer):
    template_name = "bibliography.html"


class BibliographyView(GenericAPIView):
    renderer_classes = (JSONRenderer, BibliographyViewHTMLRenderer,
                        renderers.BrowsableAPIRenderer)

    def get(self, request, *args, **kwargs):
        return Response({
            })
