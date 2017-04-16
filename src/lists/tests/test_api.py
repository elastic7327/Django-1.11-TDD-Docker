import json

from django.core.urlresolvers import reverse
from django.test import TestCase


class TestListViewSet(TestCase):

    def test_viewset(self):
        basse_url = reverse('api:list-list')
        import ipdb;ipdb.set_trace();
