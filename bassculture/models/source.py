from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.conf import settings


class Source(models.Model):
    class Meta:
        app_label = "bassculture"

    ORIENTATION_CHOICES = (
        ('l', 'Landscape'),
        ('p', 'Portrait'),
        )

    source_id = models.CharField(max_length=128, blank=True, null=True)
    full_title = models.TextField()
    short_title = models.CharField(max_length=255)
    author = models.ForeignKey("bassculture.Author", blank=True, null=True,
                               related_name="sources")
    description = models.TextField(blank=True, null=True)
    source_notes = models.TextField(blank=True, null=True)
    publisher = models.TextField(blank=True, null=True)
    printer = models.TextField(blank=True, null=True)
    edition = models.CharField(max_length=64)
    orientation = models.CharField(max_length=16, blank=True, null=True,
                                   choices=ORIENTATION_CHOICES)
    date = models.CharField(max_length=128)
    link = models.URLField(max_length=255, blank=True, null=True)
    link_label = models.TextField(blank=True, null=True)
    rism = models.CharField(max_length=128, blank=True, null=True)
    gore = models.CharField(max_length=128, blank=True, null=True)
    locations = models.TextField(blank=True, null=True)
    variants = models.CharField(max_length=256, blank=True,
                                null=True)

    def __str__(self):
            if self.short_title:
                return "{0}".format(self.short_title)
            else:
                return "{0}".format(self.id)

    @property
    def source_biographicalinfo(self):
        return "{0}".format(self.author.biographical_info)

    @property
    def the_author(self):
            return u"{0} {1} {2}".format(self.author.firstname,
                                         self.author.surname,
                                         self.author.extrainfo)

    @property
    def source_authorid(self):
        return "{0}".format(self.author.id)


@receiver(post_save, sender=Source)
def solr_index(sender, instance, created, **kwargs):
    import uuid
    from django.conf import settings
    import scorched

    si = scorched.SolrInterface(settings.SOLR_SERVER)
    record = si.query(type="source", pk="{0}".format(instance.pk)).execute()  # checks if the record exists in solr

    if record:  # if it does
        si.delete_by_ids([x['id'] for x in record])

    d = {
        # 'pk': '{0}'.format(instance.pk),
        'pk': str(instance.pk),
        'type': 'source',
        'id': str(uuid.uuid4()),
        'description': instance.description,
        'short_title': instance.short_title,
        'full_title': instance.full_title,
        'author': instance.author.full_name,
        'description': instance.description,
        'publisher': instance.publisher,
        'variants': instance.variants,
    }

    si.add(d)
    si.commit()
