from django.conf import settings
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.pagination import PageNumberPagination
from rest_framework.compat import OrderedDict
from haystack.query import SearchQuerySet

from bassculture.renderers.custom_html_renderer import CustomHTMLRenderer
from bassculture.serializers.search import SearchSerializer


class FacetedQueryPagination(PageNumberPagination):
    page_size = 20

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))


class SearchViewHTMLRenderer(CustomHTMLRenderer):
    template_name = "search/search.html"


class SearchView(GenericAPIView):
    serializer_class = SearchSerializer
    renderer_classes = (JSONRenderer, SearchViewHTMLRenderer)
    queryset = SearchQuerySet()
    pagination_class = FacetedQueryPagination

    def get(self, request, *args, **kwargs):
        q = self.queryset.filter(text=request.GET.get('q', None)).facet('author', mincount=1).facet('source_title', mincount=1)
        page = self.paginate_queryset(q)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            resp = self.get_paginated_response(serializer.data)
            resp.data['facets'] = q.facet_counts()
            return resp

        serializer = self.get_serializer(q, many=True)
        return Response(serializer.data)
