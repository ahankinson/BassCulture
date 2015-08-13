from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.reverse import reverse

from bassculture.renderers.custom_html_renderer import CustomHTMLRenderer
from bassculture.serializers.search import SearchSerializer


class HomeViewHTMLRenderer(CustomHTMLRenderer):
    template_name = "index.html"


class HomeView(GenericAPIView):
    serializer_class = SearchSerializer
    renderer_classes = (JSONRenderer, HomeViewHTMLRenderer)

    def get(self, request, *args, **kwargs):
        return Response({
            'sources': reverse('source-list', request=request),
            'items': reverse('item-list', request=request),
            'authors': reverse('author-list', request=request)
            })
