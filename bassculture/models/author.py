from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.conf import settings


class Author(models.Model):
    class Meta:
        app_label = 'bassculture'
        # unique_together = ("author_surname", "author_firstname", "author_extrainfo")

    author_surname = models.CharField(max_length=255)
    author_firstname = models.CharField(max_length=255)
    author_extrainfo = models.CharField(max_length=16)
    biographical_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return u"{0} {1} {2}".format(self.author_firstname,
                                     self.author_surname,
                                     self.author_extrainfo)

    @property
    def full_name(self):
        if self.author_firstname:
            return u"{0} {1} {2}".format(self.author_firstname,
                                         self.author_surname,
                                         self.author_extrainfo)
        else:
            return u"{0}".format(self.author_surname)


@receiver(post_save, sender=Author)
def solr_index(sender, instance, created, **kwargs):
    import uuid
    from django.conf import settings
    import scorched

    si = scorched.SolrInterface(settings.SOLR_SERVER)
    record = si.query(type="author", id="{0}".format(instance.id)
                      ).execute()  # checks if the record exists in solr

    if record:  # if it exists
        si.delete_by_ids([x['id'] for x in record])

    d = {
        'pk': '{0}'.format(instance.id),
        'type': 'author',
        'id': str(uuid.uuid4()),
        'author_surname': instance.author_surname,
        'author_firstname': instance.author_firstname,
        'author_extrainfo': instance.author_extrainfo,
        'biographical_info': instance.biographical_info,
    }

    si.add(d)
    si.commit()
