from django.db import models


class Author(models.Model):
    class Meta:
        app_label = 'bassculture'

    name = models.CharField(max_length=255)

    def __str__(self):
        return u"{0}".format(self.name)