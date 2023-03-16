from unittest import TestCase
from pantry.main import add, subtract


class TestMath(TestCase):
    def test_add(self):
        self.assertEqual(2, add(1, 1))

    def test_subtract(self):
        self.assertEqual(0, subtract(1, 1))
