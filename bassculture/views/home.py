from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from bassculture.renderers.custom_html_renderer import CustomHTMLRenderer
from bassculture.serializers.search import SearchSerializer


class HomeViewHTMLRenderer(CustomHTMLRenderer):
    template_name = "main/home.html"


class HomeView(GenericAPIView):
    serializer_class = SearchSerializer
    renderer_classes = (JSONRenderer, HomeViewHTMLRenderer)

    def get(self, request, *args, **kwargs):
        return Response({})
