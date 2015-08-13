import os
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


class Tune(models.Model):
    class Meta:
        app_label = "bassculture"

    def upload_to(instance, filename):
        # this will work when we get the item stuff sorted out.
        return "{0}".format(os.path.join(instance.item.shelfmark, 'mei',
                            filename))

    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    mei_file = models.FileField(upload_to=upload_to, blank=True, null=True)
    start_page = models.IntegerField(blank=True, null=True)
    alternate_spellings = models.CharField(max_length=256, blank=True,
                                           null=True)
    item = models.ForeignKey("bassculture.Item", blank=True, null=True,
                             related_name="tunes")

    def __str__(self):
        return "{0}".format(self.name)


@receiver(post_save, sender=Tune)
def solr_index(sender, instance, created, **kwargs):
    import uuid
    from django.conf import settings
    import scorched

    si = scorched.SolrInterface(settings.SOLR_SERVER)
    record = si.query(type="tune", id="{0}".format(instance.id)
                      ).execute()  # checks if the record exists in solr

    if record:  # if it does
        si.delete_by_ids([x['id'] for x in record])

    d = {
        'pk': '{0}'.format(instance.pk),
        'type': 'tune',
        'id': str(uuid.uuid4()),
        'alternate_spellings': instance.alternate_spellings,
        'name': instance.name,
    }

    si.add(d)
    si.commit()
