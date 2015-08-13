from django.conf import settings
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.pagination import PageNumberPagination
from rest_framework.compat import OrderedDict
import scorched
# from haystack.query import SearchQuerySet

from bassculture.renderers.custom_html_renderer import CustomHTMLRenderer
from bassculture.serializers.search import SearchSerializer


# [haystack leftover]
# class FacetedQueryPagination(PageNumberPagination):
#    page_size = 20

#   def get_paginated_response(self, data):
#        return Response(OrderedDict([
#            ('count', self.page.paginator.count),
#            ('next', self.get_next_link()),
#            ('previous', self.get_previous_link()),
#            ('results', data)
#        ]))


class SearchViewHTMLRenderer(CustomHTMLRenderer):
    template_name = "search/search.html"


class SearchView(GenericAPIView):
    serializer_class = SearchSerializer
    renderer_classes = (JSONRenderer, SearchViewHTMLRenderer)


# [haystack leftover]
#    queryset = SearchQuerySet()
#    pagination_class = FacetedQueryPagination

    # def get(self, request, *args, **kwargs):
    #     q = request.GET.get('q', None)
    #     if not q:

    #         return Response()

    #     q = self.queryset.filter(text=q)
    #     page = self.paginate_queryset(q)

    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         resp = self.get_paginated_response(serializer.data)
    #         resp.data['facets'] = q.facet_counts()
    #         return resp

    #     serializer = self.get_serializer(q, many=True)
    #     return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        querydict = request.GET
        if not querydict:
            return Response({"results": []})
        si = scorched.SolrInterface(settings.SOLR_SERVER)
        resp = si.query("Gow").execute()
        records = [r for r in resp]
        s = self.get_serializer(records, many=True)

        return Response(s.data)
