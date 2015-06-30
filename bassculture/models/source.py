from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


class Source(models.Model):
    class Meta:
        app_label = "bassculture"


    ORIENTATION_CHOICES = (
        ('l', 'landscape'),
        ('p', 'portrait'),
    )

    source_id = models.IntegerField(unique=True, db_index=True)
    full_title = models.CharField(max_length=255)
    short_title = models.CharField(max_length=255)
    authors = models.ManyToManyField("bassculture.Author", blank=True, related_name="sources")
    description = models.TextField(blank=True, null=True)
    source_notes = models.TextField(blank=True, null=True)
    publisher = models.ForeignKey("bassculture.Publisher", related_name="sources", blank=True, null=True)
    printer = models.ForeignKey("bassculture.Printer", related_name="sources", blank=True, null=True)
    edition = models.CharField(max_length=16)
    orientation = models.CharField(max_length=16, blank=True, null=True, choices=ORIENTATION_CHOICES)
    date = models.CharField(max_length=16)
    link = models.URLField(blank=True, null=True)
    link_label = models.TextField(blank=True, null=True)
    rism = models.CharField(max_length=16)
    gore = models.CharField(max_length=16)
    locations = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{0}".format(self.short_title)