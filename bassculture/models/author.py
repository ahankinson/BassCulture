from django.db import models


class Author(models.Model):
    class Meta:
        app_label = 'bassculture'

    name = models.TextField(max_length=255)
    biographical_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return u"{0}".format(self.name)
