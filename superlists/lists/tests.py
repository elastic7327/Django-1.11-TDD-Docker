from django.test import TestCase

from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.http import HttpRequest

from lists.views import home_page

import ipdb as br


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        expected_html = render_to_string('lists/home.html')
        self.assertEqual(expected_html, html)
# Create your tests here.
