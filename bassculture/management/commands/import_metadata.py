import os
import csv
from django.core.management.base import BaseCommand
from bassculture.models import Item, Source, Author


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('location', help="Location of the .csv file to import")

    def handle(self, *args, **kwargs):
        print(kwargs)
        location = kwargs['location']

        with open(location) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.this_source = None
                self.this_author = None
                self.create_author(row)
                self.create_source(row)
                self.create_item(row)

    def create_author(self, row):
        print("Resetting Authors")
        Author.objects.all().delete()

        d = {
            'name':row['author'],
        }

        a = Author(**d)
        a.save()

        self.this_author = a

    def create_source(self, row):
        print("Cleaning source table")
        Source.objects.all().delete()


        print("Creating source " + row['source_id'])
        author = self.this_author

        if row['orientation'] == "Portrait":
            orientation = "p"
        elif row['orientation'] == "Landscape":
            orientation = "l"
        else:
            orientation = None

        d = {
            'source_id':row['source_id'],
            'full_title':row['full_title'],
            'short_title':row['short_title'],
            'authors':author,
            'description':row['source_description'],
            'source_notes':row['source_detailed_notes'],
            'publisher':row['published'],
            'printer':row['printed'],
            'edition':row['edition'],
            'orientation':row['orientation'],
            'date':row['date'],
            'link':row['link_url'],
            'link_label':row['link_label'],
            'rism':row['rism'],
            'gore':row['gore'],
            'locations':row['locations'],
        }

        s = Source(**d)
        s.save()

        self.this_source = s

    def create_item(self, row):
        print("Resetting Items")
        Item.objects.all().delete()

        source = self.this_source

        d = {
            'pagination':row['pagination'],
            'dimensions':row['dimensions'],
            'library':row['library_name'],
            'shelfmark':row['shelfmark'],
            'item_notes':row['item_notes'],
            'source': source,
            'seller':row['sold'],
        }

        i = Item(**d)
        i.save()