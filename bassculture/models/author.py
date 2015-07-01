from django.db import models


class Author(models.Model):
    class Meta:
        app_label = 'bassculture'

    name = models.CharField(max_length=255)
    biographical_info = models.TextField(blank=True, null=True)
    short_title = models.ManyToManyField("bassculture.Source", blank=True, related_name="sources")

    def __str__(self):
        return u"{0}".format(self.name)