from django.db import models


class Printer(models.Model):
    class Meta:
        app_label = 'bassculture'

    printer_id = models.IntegerField(unique=True, db_index=True)
    name = models.CharField("Printer", max_length=255)

    def __str__(self):
        return "{0}".format(self.name)
