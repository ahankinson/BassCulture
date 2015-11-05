from rest_framework import generics
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from django.http import HttpResponse
import csv
import json
from bassculture.models.author import Author
from bassculture.models.tune import Tune
from bassculture.models.source import Source


def load_author(file_path):
    "this loads drugs from pipe delimited file with headers"
    reader = csv.DictReader(open(file_path))
    for row in reader:
        author = Author(firstname=row['firstname'], surname=row['surname'])
        author.save()


def autocomplete(request):
#    if request.is_ajax():
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
            results.append(tune_JSON)
        #list(set) removes duplicate items from the list (e.g. 8 N. Gows)
        results = list(set(results))
        data = json.dumps(results)
#    else:
#        data = 'fail'
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)