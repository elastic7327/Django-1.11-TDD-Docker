from django.db import models
from django.core.urlresolvers import reverse


class List(models.Model):
    """
    DOC STRING
    """

    def get_absolute_url(self):
        """
        DOC STRING
        """
        return reverse('view_list', args=[self.id])


class Item(models.Model):
    """
    DOC STRING
    """

    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
