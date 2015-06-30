import os
from django.core.management.base import BaseCommand
from bassculture.models.item import Item
from bassculture.models.tune import Tune


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('location', help="Location of the MEI files to import")

    def handle(self, *args, **kwargs):
        for td, sd, f in os.walk(kwargs['location']):
            for subfile in f:
                if subfile.startswith('.'):
                    continue
                filepath = os.path.join(td, subfile)
                print(filepath)
