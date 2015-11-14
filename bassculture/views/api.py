from rest_framework import generics
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from django.http import HttpResponse
import csv
import json
from bassculture.models.author import Author
from bassculture.models.tune import Tune
from bassculture.models.source import Source


def autocomplete(request):
        q = request.GET.get('term', '')
        authors = Author.objects.filter(surname__istartswith=q)[:400]
        results = []
        for author in authors:
            author_JSON = {}
            author_JSON = author.firstname + " " + author.surname
            results.append(author_JSON)

        sources = Source.objects.filter(short_title__icontains=q)[:400]
        for source in sources:
            source_JSON = {}
            source_JSON = source.short_title
            results.append(source_JSON)

        tunes = Tune.objects.filter(name__icontains=q)[:2000]
        for tune in tunes:
            tune_JSON = {}
            tune_JSON = tune.name
        # .split() removes extra white spaces in the title of the tunes
            " ".join(tune_JSON.split())
            results.append(tune_JSON)
        # list(set) removes duplicate items from the list (e.g. 8 N. Gows)
        results = list(set(results))
        data = json.dumps(results)
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)