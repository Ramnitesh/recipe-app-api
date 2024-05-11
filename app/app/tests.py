"""
Sample tests
"""

from django.test import TestCase

from app import calc


class CalcTests(TestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(5, 2)
        self.assertEqual(res, 7)

    def test_sub_numbers(self):
        """Test subtracting numbers."""
        res = calc.sub(10, 15)
        self.assertEqual(res, 5)
