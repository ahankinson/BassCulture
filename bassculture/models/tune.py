from django.db import models


class Tune(models.Model):
    class Meta:
        app_label = "bassculture"

    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    mei_file = models.FilePathField(blank=True, null=True)
    start_page = models.IntegerField(blank=True, null=True)
    alternate_spellings = models.CharField(max_length=256, blank=True, null=True)
    item = models.ForeignKey("bassculture.Item", blank=True, null=True)

    def __str__(self):
        return "{0}".format(self.name)
