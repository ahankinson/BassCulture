from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


class Printer(models.Model):
    class Meta:
        app_label = 'bassculture'

    name = models.CharField("Printer", max_length=255)

    def __str__(self):
        return "{0}".format(self.name)