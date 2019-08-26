from django.db import models
import base64
from bs4 import BeautifulSoup


class Nfe(models.Model):
    access_key = models.CharField('Access Key', max_length=44, null=False, blank=False, unique=True)
    xml = models.CharField('XML', max_length=50000, null=False, blank=False)
    value = models.CharField('Value', max_length=20, null=True, blank=True)

    create_at = models.DateTimeField("Create at", auto_now_add=True)
    update_at = models.DateTimeField("Update at", auto_now=True)

    def __str__(self):
        return "{0}-{1}".format(self.id, self.access_key)

    @staticmethod
    def prepare_nfe_and_save(data):
        access_key = data['access_key']
        xml = base64.b64decode(data['xml'])
        soup = BeautifulSoup(xml, "html.parser")
        vnf = soup.select('total ICMSTot vNF')
        if len(vnf) > 0:
            value = vnf[0].text
        else:
            value = None

        nfe = Nfe(access_key=access_key, xml=xml, value=value)

        r = {'access_key': nfe.access_key, 'activity': '', }

        if Nfe.objects.filter(access_key=nfe.access_key).exists():
            r['activity'] = 'no_change'
        else:
            nfe.save()
            r['activity'] = 'new'

        return r
