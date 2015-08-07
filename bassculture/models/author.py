from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


class Author(models.Model):
    class Meta:
        app_label = 'bassculture'

    name = models.TextField(max_length=255)
    biographical_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return u"{0}".format(self.name)


@receiver(post_save, sender=Author)
def solr_index(sender, instance, created, **kwargs):
    import uuid
    from django.conf import settings
    import scorched

    si = scorched.SolrInterface(settings.SOLR_SERVER)
    record = si.query(type="author", author_id="{0}".format(instance.author_id)
                      ).execute()  # checks if the record exists in solr

    if record:  # if it does
        si.delete_by_ids([x['id'] for x in record])

    d = {
        'pk': '{0}'.format(instance.pk),
        'type': 'author',
        'id': str(uuid.uuid4()),
        'author_id': instance.author_id,
        'name': instance.name,
        'surname': instance.surname
    }

    si.add(d)
    si.commit()