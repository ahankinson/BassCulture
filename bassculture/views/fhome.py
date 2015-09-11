from rest_framework.generics import GenericAPIView
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.reverse import reverse

from bassculture.renderers.custom_html_renderer import CustomHTMLRenderer


class FhomeViewHTMLRenderer(CustomHTMLRenderer):
    template_name = "findex.html"


class FhomeView(GenericAPIView):
    renderer_classes = (JSONRenderer, FhomeViewHTMLRenderer,
                        renderers.BrowsableAPIRenderer)

    def get(self, request, *args, **kwargs):
        return Response({
            'sources': reverse('source-list', request=request),
            'items': reverse('item-list', request=request),
            'authors': reverse('author-list', request=request)
            })
