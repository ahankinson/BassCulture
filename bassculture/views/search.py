import os
from django.conf import settings
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.compat import OrderedDict
from rest_framework.settings import api_settings
import scorched

from bassculture.renderers.custom_html_renderer import CustomHTMLRenderer


class SearchResultsPagination(LimitOffsetPagination):
    def get_paginated_response(self, data):
        """
        :param data: serialized data
        :param solr_response: the raw Solr response
        :return: Response object
        """
        self.solr_response = data['solr_response']
        self.offset = self.solr_response.result.start
        self.limit = len(data['records'])
        self.count = self.solr_response.result.numFound
        self.request = data['request']

        resp = Response(OrderedDict([
            ('count', self.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data['records']),
            ('facets', self.solr_response.facet_counts.facet_fields),
            ('params', self.solr_response.params),
            ('highlighting', self.solr_response.highlighting),

        ]))

        return resp


class SearchViewHTMLRenderer(CustomHTMLRenderer):
    template_name = "search/search.html"


class SearchView(GenericAPIView):
    renderer_classes = (JSONRenderer, SearchViewHTMLRenderer)
    pagination_class = SearchResultsPagination

    def get(self, request, *args, **kwargs):
        querydict = request.GET
        offset = querydict.get('offset', 0)

        fq = {}
        for f in settings.SEARCH_FACETS:
            if querydict.get(f, None):
                fq[f] = querydict.get(f)

        si = scorched.SolrInterface(settings.SOLR_SERVER)
        response = si.query(querydict.get('q')) \
                     .filter(**fq)\
                     .highlight('*')\
                     .paginate(start=int(offset), rows=api_settings.PAGE_SIZE)\
                     .facet_by(fields=settings.SEARCH_FACETS, mincount=1)\
                     .execute()

        records = []
        for result in response:
            type = result['type']
            pk = result['pk']
            # # This should always be relative to the root, not the current path.
            result['url'] = request.build_absolute_uri(os.path.join('/fiddle/', type, pk))
            records.append(result)

        d = {
            'records': records,
            'solr_response': response,
            'request': request,
        }
        resp = self.get_paginated_response(d)

        return resp
