from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


class Author(models.Model):
    class Meta:
        app_label = 'bassculture'

    surname = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    extrainfo = models.CharField(max_length=255, blank=True, null=True)
    biographical_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return u"{0} {1} {2}".format(self.firstname,
                                     self.surname,
                                     self.extrainfo)

    @property
    def full_name(self):
        if self.firstname:
            return u"{0} {1} {2}".format(self.firstname,
                                         self.surname,
                                         self.extrainfo)
        else:
            return u"{0}".format(self.surname)


@receiver(post_save, sender=Author)
def solr_index(sender, instance, created, **kwargs):
    import uuid
    from django.conf import settings
    import scorched

    si = scorched.SolrInterface(settings.SOLR_SERVER)
    # checks if the record exists in solr
    record = si.query(type="author", pk="{0}".format(instance.pk)).execute()

    if record:  # if it exists
        si.delete_by_ids([x['id'] for x in record])
    print("adding: " + instance.surname)

    d = {
        # 'pk': '{0}'.format(instance.pk),
        'pk': str(instance.pk),
        'type': 'author',
        'id': str(uuid.uuid4()),
        'surname': instance.surname,
        'firstname': instance.firstname,
        'extrainfo': instance.extrainfo,
        'biographical_info': instance.biographical_info
    }

    si.add(d)
    si.commit()
