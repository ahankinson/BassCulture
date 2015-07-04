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
                if os.path.splitext(subfile)[-1] != '.mei':
                    continue
                print('Importing: ' + subfile)
                # fparse = re.compile(r'(?P<src>[a-zA-Z0-9\-_\.]+)__(?P<pnum>[0-9]+)\.(?P<name>[a-zA-Z0-9])\.mei')
                filepath = os.path.join(td, subfile)
                page = subfile.split("__")[1].split('.')[0]
                tree = etree.parse(filepath)
                itemStmt_el = tree.findall('.//mei:fileDesc/mei:titleStmt/mei:title[@type="subtitle"]', ns)
                itemStmt = None
                if itemStmt_el:
                    itemStmt = itemStmt_el[0].text

                title = tree.findall('.//mei:work/mei:titleStmt/mei:title', ns)[0].text
                alt_spelling_el = tree.findall('.//mei:work/mei:notesStmt/annot', ns)
                alt_spelling = None
                if alt_spelling_el:
                    alt_spelling = alt_spelling_el[0].text

                item = Item.objects.get(folder=os.path.basename(td))
                print(os.path.basename(td), " ", item)

                t = Tune()
                t.item = item
                t.start_page = int(page)
                t.name = title
                if alt_spelling:
                    t.alternate_spellings = alt_spelling

                # save now before adding the meifiles so that we can get the item's shelfmark for the file saving path.
                t.save()

                with open(filepath, encoding='utf-16') as meifile:
                    mfile = File(meifile)
                    t.mei_file.save(subfile, mfile)
                t.save()
