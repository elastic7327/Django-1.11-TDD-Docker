"""
    DOC STRING
"""
# !/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from unittest import skip
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    """
    DOC STRING
    """

    @skip
    def test_cannot_add_empty_list_items(self):
        pass


if __name__ == '__main__':
    unittest.main(warnings='ignore')
