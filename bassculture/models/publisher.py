from django.db import models


class Publisher(models.Model):
    class Meta:
        app_label = 'bassculture'

    name = models.CharField("Publisher", max_length=255)

    def __str__(self):
        return "{0}".format(self.name)
