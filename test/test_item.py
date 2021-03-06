from unittest import TestCase
from src.item import Item

class TestItem(TestCase):

    def setUp(self):
        self.item = Item("foo", 0, 0)
    
    def test_has_name(self):
        self.assertTrue(hasattr(self.item, "name"))

    def test_name_initialized(self):
        self.assertEqual(self.item.name, "foo")

    def test_has_quality(self):
        self.assertTrue(hasattr(self.item, "quality"))

    def test_quality_initialized(self):
        self.assertEqual(self.item.quality, 0)

    def test_has_sell_in(self):
        self.assertTrue(hasattr(self.item, "sell_in"))

    def test_sell_in_initialized(self):
        self.assertEqual(self.item.sell_in, 0)