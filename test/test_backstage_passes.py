from unittest import TestCase
from unittest import mock

from src.gilded_rose import GildedRose

class TestBackstagePasses(TestCase):

    def setUp(self):
        self.backstage_pass = mock.Mock()
        self.backstage_pass.name = "Backstage passes to a TAFKAL80ETC concert"
        items = [self.backstage_pass]
        self.gilded_rose = GildedRose(items)

class GreaterThanTenDays(TestBackstagePasses):
    
    def setUp(self):
        super().setUp()
        self.backstage_pass.sell_in = 11

    def test_update_item_quality(self):
        """
        backstage pass quality increases by 1
        each cycle
        when sell_in is great than 10
        """
        self.backstage_pass.quality = 10
        self.gilded_rose.update_quality()
        self.assertEqual(self.backstage_pass.quality, 11)
    
    def test_update_item_quality_capped(self):
        """
        backstage pass item quality cannot go
        above 50
        """
        self.backstage_pass.quality = 50
        self.gilded_rose.update_quality()
        self.assertEqual(self.backstage_pass.quality, 50)


class BetweenTenAndSixDays(TestBackstagePasses):

    def setUp(self):
        super().setUp()
        self.backstage_pass.sell_in = 9

    def test_update_item_quality(self):
        """
        backstage pass quality increases by 1
        each cycle
        when sell_in is less than 10
        and sell_in is greater than 5
        """
        self.backstage_pass.quality = 10
        self.gilded_rose.update_quality()
        self.assertEqual(self.backstage_pass.quality, 12)

    def test_update_item_quality_capped(self):
        """
        backstage pass item quality cannot go
        above 50
        """
        self.backstage_pass.quality = 50
        self.gilded_rose.update_quality()
        self.assertEqual(self.backstage_pass.quality, 50)

class LessThanSixDays(TestBackstagePasses):

    def setUp(self):
        super().setUp()
        self.backstage_pass.sell_in = 4

    def test_update_item_quality(self):
        """
        backstage pass quality increases by 1
        each cycle
        when sell_in is less than 6
        """
        self.backstage_pass.quality = 10
        self.gilded_rose.update_quality()
        self.assertEqual(self.backstage_pass.quality, 13)

    def test_update_item_quality_capped(self):
        """
        backstage pass item quality cannot go
        above 50
        """
        self.backstage_pass.quality = 50
        self.gilded_rose.update_quality()
        self.assertEqual(self.backstage_pass.quality, 50)
