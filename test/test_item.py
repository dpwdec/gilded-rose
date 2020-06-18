from unittest import TestCase
from src.item import Item

class TestItem(TestCase):
    
    def test_has_name(self):
        item = Item("foo", 0, 0)
        self.assertTrue(hasattr(item, "name"))