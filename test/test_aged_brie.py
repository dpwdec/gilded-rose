from unittest import TestCase
from unittest import mock

from src.gilded_rose import GildedRose
from src.item import Item

class TestGildedRose(TestCase):
    pass

class TestAgedBrieBeforeSellBy(TestGildedRose):

    def setUp(self):
        self.aged_brie = mock.Mock()
        self.aged_brie.quality = 10
        self.aged_brie.sell_in = 10
        self.aged_brie.name = "Aged Brie"
        items = [self.aged_brie]
        self.gilded_rose = GildedRose(items)

    def test_update_quality(self):
        """
        Aged brie increases in quality
        over time
        """
        self.gilded_rose.update_quality()
        self.assertEqual(self.aged_brie.quality, 11)
    
    def test_item_sell_in_lowered(self):
        """
        sell in drops by one 
        each update cycle
        """
        self.gilded_rose.update_quality()
        self.assertEqual(self.aged_brie.sell_in, 9)

class TestAgedBrieAfterSellBy(TestGildedRose):

    def setUp(self):
        self.aged_brie = mock.Mock()
        self.aged_brie.quality = 10
        self.aged_brie.sell_in = 0
        self.aged_brie.name = "Aged Brie"
        items = [self.aged_brie]
        self.gilded_rose = GildedRose(items)

    def test_update_quality_after_sell_in(self):
        """
        Aged brie increases by double quality
        after sell in is passed
        """
        self.gilded_rose.update_quality()
        self.assertEqual(self.aged_brie.quality, 12)