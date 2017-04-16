import json

from django.core.urlresolvers import reverse
from django.test import TestCase


class TestListViewSet(TestCase):

    def test_viewset(self):
        import ipdb;ipdb.set_trace();
        basse_url = reverse('api:list-list')
