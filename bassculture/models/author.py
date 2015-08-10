from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


class Author(models.Model):
    class Meta:
        app_label = 'bassculture'

    author = models.CharField(max_length=255)
#    author_firstname = models.CharField(max_length=255)
#    extra_info = models.CharField(max_length=16)
    biographical_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return u"{0}".format(self.author)

    # @property
    # def full_name(self):
    #     if self.name:
    #         return u"{0}, {1}, {2}".format(self.surname, self.name,
    #                                        self.extra_info)
    #     else:
    #         return u"{0}".format(self.surname)

@receiver(post_save, sender=Author)
def solr_index(sender, instance, created, **kwargs):
    import uuid
    from django.conf import settings
    import scorched

    si = scorched.SolrInterface("localhost:8983/solr/")
    record = si.query(type="author", author_id="{0}".format(instance.author_id)
                      ).execute()  # checks if the record exists in solr

    if record:  # if it exists
        si.delete_by_ids([x['id'] for x in record])

    d = {
        'pk': '{0}'.format(instance.pk),
        'type': 'author',
        'id': str(uuid.uuid4()),
        'author_id': instance.id,
#        'name': instance.author_firstname,
        'author': instance.author,
#        'extra_info': instance.author_extra_info,
    }

    si.add(d)
    si.commit()
