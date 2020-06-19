from unittest import TestCase
from src.legendary_item import LegendaryItem

class TestLegendaryItem(TestCase):

    def test_update_sell_in(self):
        """
        LegendaryItem's sell_in never changes
        """
        legendary_item = LegendaryItem("Sulfuras, Hand of Ragnaros", 10, 10)
        legendary_item.update_sell_in()
        self.assertEqual(legendary_item.sell_in, 10)

    def test_update_quality(self):
        """
        LegendaryItem's quality never changes
        """
        legendary_item = LegendaryItem("Sulfuras, Hand of Ragnaros", 10, 10)
        legendary_item.update_quality()
        self.assertEqual(legendary_item.sell_in, 10)