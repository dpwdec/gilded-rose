from unittest import TestCase
from unittest import mock

from src.gilded_rose import GildedRose

class TestGildedRose(TestCase):
    pass

class TestBackstagePasses(TestGildedRose):
    
    def setUp(self):
        self.backstage_pass = mock.Mock()
        self.backstage_pass.quality = 10
        self.backstage_pass.sell_in = 11
        self.backstage_pass.name = "Backstage passes to a TAFKAL80ETC concert"
        items = [self.backstage_pass]
        self.gilded_rose = GildedRose(items)

    def test_update_item_quality(self):
        """
        backstage pass quality increases by 1
        each cycle
        when sell_in is great than 10
        """
        self.gilded_rose.update_quality()
        self.assertEqual(self.backstage_pass.quality, 11)
