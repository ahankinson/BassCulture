import os
import re
import xml.etree.ElementTree as etree
from django.core.management.base import BaseCommand
from django.core.files import File
from bassculture.models.tune import Tune
from bassculture.models.item import Item


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('location', help="Location of the MEI files to import")

    def handle(self, *args, **kwargs):
        print('Emptying Tunes DB')
        Tune.objects.all().delete()

        ns = {'mei': 'http://www.music-encoding.org/ns/mei'}

        for td, sd, f in os.walk(kwargs['location']):
            for subfile in f:
                if subfile.startswith('.'):
                    continue
                print('Importing: ' + subfile)
                # fparse = re.compile(r'(?P<src>[a-zA-Z0-9]+)_(?P<pnum>[0-9]+)\.(?P<name>[a-zA-Z0-9])\.mei')
                filepath = os.path.join(td, subfile)
                tree = etree.parse(filepath)
                itemStmt = tree.findall('.//mei:fileDesc/mei:titleStmt/mei:title[@type="subtitle"]', ns)[0].text
                shelfmark, page = itemStmt.split('_')
                title = tree.findall('.//mei:work/mei:titleStmt/mei:title', ns)[0].text
                alt_spelling = tree.findall('.//mei:work/mei:notesStmt', ns)[0].text

                t = Tune()
                # t.item = Item.objects.get(shelfmark=shelfmark)
                t.start_page = int(page)
                t.title = title
                t.alternate_spellings = alt_spelling

                f = open(filepath, 'r')
                mfile = File(f)
                t.mei_file = mfile

                t.save()
