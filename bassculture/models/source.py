from django.db import models


class Source(models.Model):
    class Meta:
        app_label = "bassculture"

    ORIENTATION_CHOICES = (
        ('l', 'Landscape'),
        ('p', 'Portrait'),
    )

    source_id = models.CharField(max_length=128, blank=True, null=True)
    full_title = models.CharField(max_length=500)
    short_title = models.CharField(max_length=255)
    author = models.ForeignKey("bassculture.Author", blank=True, related_name="sources")
    description = models.TextField(blank=True, null=True)
    source_notes = models.TextField(blank=True, null=True)
    publisher = models.TextField(blank=True, null=True)
    printer = models.TextField(blank=True, null=True)
    edition = models.CharField(max_length=64)
    orientation = models.CharField(max_length=16, blank=True, null=True, choices=ORIENTATION_CHOICES)
    date = models.CharField(max_length=128)
    link = models.URLField(blank=True, null=True)
    link_label = models.TextField(blank=True, null=True)
    rism = models.CharField(max_length=32, blank=True, null=True)
    gore = models.CharField(max_length=16, blank=True, null=True)
    locations = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.short_title:
            return "{0}".format(self.short_title)
        else:
            return "{0}".format(self.id)
