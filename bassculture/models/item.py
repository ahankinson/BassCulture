from django.db import models


class Item(models.Model):
    class Meta:
        app_label = 'bassculture'

    folder = models.CharField(max_length=32, blank=True, null=True)
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

    def author_name(self):
        return "{0}".format(self.source.authors)

    def __str__(self):
        return "{0} {1}".format(self.library, self.shelfmark)
