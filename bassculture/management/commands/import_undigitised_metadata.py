import csv
from django.core.management.base import BaseCommand
from bassculture.models import Source
from bassculture.models import Author


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('location', help="Location of the .csv file")

    def handle(self, *args, **kwargs):
        print(kwargs)
        location = kwargs['location']

        with open(location) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.author = None
                self.source = None
                self.create_author(row)
                self.create_source(row)

    def create_author(self, row):
        self.author, auth_created = Author.objects.get_or_create(biographical_info=row['biographical_info'],
                                                                 extrainfo=row['extra_info'],
                                                                 surname=str(row['author_surname']),
                                                                 firstname=row['author_firstname'])
        if auth_created:
            self.author.save()

    def create_source(self, row):
        print("Creating source " + row['short_title'])
        # # author, auth_created = Source.objects.get_or_create(source_id=row["source_id"])

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
            'author': self.author,
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

        self.source = s
