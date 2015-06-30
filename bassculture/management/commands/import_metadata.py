import os
import csv
from django.core.management.base import BaseCommand
from bassculture.models.item import Item
from bassculture.models.tune import Source
from bassculture.models.tune import Publisher
from bassculture.models.tune import Printer
from bassculture.models.tune import Author


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('location', help="Location of the .csv file to import")

    def handle(self, *args, **kwargs):
        f = open(location)
        csv_f = csv.reader(f, delimiter=',')
        for row in csv_f
        target_model = Source
            for b in row
            setattr(target_model, target_model._meta.fields[i].name, y)

        target_model.save() 
