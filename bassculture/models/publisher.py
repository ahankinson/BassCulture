from django.db import models


class Publisher(models.Model):
    class Meta:
        app_label = 'bassculture'

    publisher_id = models.IntegerField(unique=True, db_index=True)
    name = models.CharField("Publisher", max_length=255)

    def __str__(self):
        return "{0}".format(self.name)
