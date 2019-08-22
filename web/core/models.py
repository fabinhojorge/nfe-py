from django.db import models


class Nfe(models.Model):
    access_key = models.CharField('Access Key', max_length=44, null=False, blank=False, unique=True)
    xml = models.CharField('XML', max_length=4000, null=False, blank=False)
    value = models.CharField('Value', max_length=20, null=True, blank=True)

    def __str__(self):
        return "{0}-{1}".format(self.id, self.access_key)
