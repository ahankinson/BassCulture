import os
import csv
from django.core.management.base import BaseCommand
from bassculture.models import Item, Source, Author


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('location', help="Location of the .csv file")

    def handle(self, *args, **kwargs):
        print(kwargs)
        location = kwargs['location']

        # Author.objects.all().delete()
        # Item.objects.all().delete()
        # Source.objects.all().delete()

        with open(location) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.this_source = None
                self.this_author = None
                self.create_source(row)
                self.create_item(row)

    def create_source(self, row):
        print("Cleaning source table")

        print("Creating source " + row['source_id'])
        author, auth_created = Author.objects.get_or_create(id=Source.author)
        if auth_created:
                # author.author_surname = row['author_surname'],
                author.author_firstname = row['author_firstname'],
                author.author_extrainfo = row['extra_info'],
                author.biographical_info = row['biographical_info'],
                author.save()

        if row['orientation'] == "Portrait":
            orientation = "p"
        elif row['orientation'] == "Landscape":
            orientation = "l"
        else:
            orientation = None

        d = {
            'source_id': row['source_id'],
            'full_title': row['full_title'],
            'short_title': row['short_title'].strip(),
            'author': author,
            'description': row['source_description'],
            'source_notes': row['source_detailed_notes'],
            'publisher': row['published'],
            'printer': row['printed'],
            'edition': row['edition'],
            'orientation': row['orientation'],
            'date': row['date'],
            'link': row['link_url'],
            'link_label': row['link_label'],
            'rism': row['rism'],
            'gore': row['gore'],
            'locations': row['locations'],
        }

        s = Source(**d)
        s.save()

        self.this_source = s

    def create_item(self, row):
        print("Resetting Items")

        source = self.this_source

        d = {
            'folder': row['folder'],
            'pagination': row['pagination'],
            'dimensions': row['dimensions'],
            'library': row['library_name'],
            'shelfmark': row['shelfmark'],
            'item_notes': row['item_notes'],
            'source': source,
            'seller': row['sold'],
        }

        i = Item(**d)
        i.save()
