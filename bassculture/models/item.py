from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.conf import settings


class Item(models.Model):
    class Meta:
        app_label = 'bassculture'

    folder = models.CharField(max_length=128, blank=True, null=True)
    pagination = models.CharField(max_length=16)
    dimensions = models.CharField(max_length=16)
    library = models.CharField(max_length=40, blank=True, null=True)
    shelfmark = models.CharField(max_length=32)
    item_notes = models.TextField(blank=True, null=True)
    source = models.ForeignKey("bassculture.Source", related_name="items")
    seller = models.TextField()

    @property
    def source_title(self):
        return "{0}".format(self.source.short_title)

    @property
    def source_date(self):
        return "{0}".format(self.source.date)

    @property
    def source_edition(self):
        return "{0}".format(self.source.edition)

    def author_name(self):
        return "{0}".format(self.source.author)

    def __str__(self):
        return "{0} {1}".format(self.library, self.shelfmark)


@receiver(post_save, sender=Item)
def solr_index(sender, instance, created, **kwargs):
    import uuid
    from django.conf import settings
    import scorched

    si = scorched.SolrInterface(settings.SOLR_SERVER)
    record = si.query(type="item", item_id="{0}".format(instance.item_id)).execute()  # checks if the record already exists in solr

    if record:  # if it does
        si.delete_by_ids([x['id'] for x in record])

    d = {
        'type': 'item',
        'id': str(uuid.uuid4()),
        'item_id': instance.item_id,
        'title': instance.short_title,
        'item_notes': instance.item_notes,
        'link': instance.link,
        'link_label': instance.link_label,
    }

    si.add(d)
    si.commit()
