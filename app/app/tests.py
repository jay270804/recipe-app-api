"""
Sample Tests
"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """ Test the calc module """

    def test_add_module(self):
        """ Test adding numbers together """
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_sub_module(self):
        """ Test substracting numbers together """
        res = calc.sub(10, 15)

        self.assertEqual(res, 5)
