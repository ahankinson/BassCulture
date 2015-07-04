from rest_framework import generics
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from bassculture.renderers.custom_html_renderer import CustomHTMLRenderer
from bassculture.models.tune import Tune
from bassculture.serializers.tune import TuneDetailSerializer
from bassculture.serializers.tune import TuneListSerializer


class TuneListHTMLRenderer(CustomHTMLRenderer):
    template_name = "tune/tune_list.html"


class TuneDetailHTMLRenderer(CustomHTMLRenderer):
    template_name = "tune/tune_detail.html"


class TuneList(generics.ListCreateAPIView):
    model = Tune
    queryset = Tune.objects.all()
    serializer_class = TuneListSerializer
    renderer_classes = (JSONRenderer, TuneListHTMLRenderer, BrowsableAPIRenderer)


class TuneDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Tune
    queryset = Tune.objects.all()
    serializer_class = TuneDetailSerializer
    renderer_classes = (JSONRenderer, TuneDetailHTMLRenderer, BrowsableAPIRenderer)