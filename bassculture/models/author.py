from django.db import models


class Author(models.Model):
    class Meta:
        app_label = 'bassculture'

    name = models.CharField(max_length=255)
    short_title = models.ManyToManyField("bassculture.Item", blank=True, related_name="items")

    def __str__(self):
        return u"{0}".format(self.name)