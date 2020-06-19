from unittest import TestCase
from unittest import mock

from src.gilded_rose import GildedRose

class TestAgedBrie(TestCase):

    def setUp(self):
        self.aged_brie = mock.Mock()
        self.aged_brie.name = "Aged Brie"
        items = [self.aged_brie]
        self.gilded_rose = GildedRose(items)

class BeforeSellBy(TestAgedBrie):

    def setUp(self):
        super().setUp()
        self.aged_brie.sell_in = 10

    def test_update_quality(self):
        """
        Aged brie increases in quality by 1
        each cycle
        when sell in is greater than 0
        """
        self.aged_brie.quality = 10
        self.gilded_rose.update_quality()
        self.assertEqual(self.aged_brie.quality, 11)

    def test_update_quality_capped(self):
        """
        Aged brie quality cannot go above 50
        """
        self.aged_brie.quality = 50
        self.gilded_rose.update_quality()
        self.assertEqual(self.aged_brie.quality, 50)
    
    def test_item_sell_in_lowered(self):
        """
        sell in drops by one 
        each update cycle
        """
        self.aged_brie.quality = 10
        self.gilded_rose.update_quality()
        self.assertEqual(self.aged_brie.sell_in, 9)

class AfterSellBy(TestAgedBrie):

    def setUp(self):
        super().setUp()
        self.aged_brie.sell_in = 0

    def test_update_quality_after_sell_in(self):
        """
        Aged brie increases in quality by2
        each cycle
        when sell in is less than 1
        """
        self.aged_brie.quality = 10
        self.gilded_rose.update_quality()
        self.assertEqual(self.aged_brie.quality, 12)
    
    def test_update_quality_capped(self):
        """
        Aged brie quality cannot go above 50
        """
        self.aged_brie.quality = 50
        self.gilded_rose.update_quality()
        self.assertEqual(self.aged_brie.quality, 50)

    def test_item_sell_in_lowered(self):
        """
        sell in drops by one 
        each update cycle
        """
        self.aged_brie.quality = 10
        self.gilded_rose.update_quality()
        self.assertEqual(self.aged_brie.sell_in, -1)

    