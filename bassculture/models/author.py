from django.db import models


class Author(models.Model):
    class Meta:
        app_label = 'bassculture'
        ordering = ['surname']

    author_id = models.IntegerField(unique=True, db_index=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return u"{0}, {1}".format(self.surname, self.name)

    @property
    def full_name(self):
        if self.name:
            return u"{0}, {1}".format(self.surname, self.name)
        else:
            return u"{0}".format(self.surname)