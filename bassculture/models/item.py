from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.conf import settings


class Item(models.Model):
    class Meta:
        app_label = 'bassculture'

    folder = models.CharField(max_length=128, blank=True, null=True)
    pagination = models.CharField(max_length=255)
    dimensions = models.CharField(max_length=128)
    library = models.CharField(max_length=128, blank=True, null=True)
    shelfmark = models.CharField(max_length=128)
    item_notes = models.TextField(blank=True, null=True)
    source = models.ForeignKey("bassculture.Source", related_name="items")
    seller = models.TextField(blank=True, null=True)

    @property
    def source_title(self):
        return "{0}".format(self.source.short_title)

    @property
    def item_biographicalinfo(self):
        return "{0}".format(self.source.source_biographicalinfo)

    @property
    def item_authorid(self):
        return "{0}".format(self.source.source_authorid)

    @property
    def source_locations(self):
        return "{0}".format(self.source.locations)

    @property
    def source_author(self):
        return "{0}".format(self.source.the_author)

    @property
    def source_date(self):
        return "{0}".format(self.source.date)

    @property
    def source_publisher(self):
        return "{0}".format(self.source.publisher)

    @property
    def source_edition(self):
        return "{0}".format(self.source.edition)

    @property
    def source_description(self):
        return "{0}".format(self.source.description)

    @property
    def source_printer(self):
        return "{0}".format(self.source.printer)

    @property
    def source_rism(self):
        return "{0}".format(self.source.rism)

    @property
    def source_orientation(self):
        return "{0}".format(self.source.orientation)

    @property
    def source_gore(self):
        return "{0}".format(self.source.gore)

    def __str__(self):
        return "{0} {1}".format(self.library, self.shelfmark)


@receiver(post_save, sender=Item)
def solr_index(sender, instance, created, **kwargs):
    import uuid
    from django.conf import settings
    import scorched

    si = scorched.SolrInterface(settings.SOLR_SERVER)
    record = si.query(type="copy", pk="{0}".format(instance.pk)).execute()  # checks if the record already exists in solr

    if record:  # if it does
        si.delete_by_ids([x['id'] for x in record])

    d = {
        'pk': str(instance.pk),
        'type': 'copy',
        'id': str(uuid.uuid4()),
        'item_notes': instance.item_notes,
        'seller': instance.seller,
        'source_title': instance.source_title,
        'source_author': instance.source_author
    }

    si.add(d)
    si.commit()
