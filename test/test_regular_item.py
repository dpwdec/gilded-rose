# -*- coding: utf-8 -*-
from unittest import TestCase
from unittest import mock

from src.gilded_rose import GildedRose

class TestRegularItem(TestCase):

    def setUp(self):
        self.foo_item = mock.Mock()
        self.foo_item.name = "Foo"
        items = [self.foo_item]
        self.gilded_rose = GildedRose(items)

class BeforeSellBy(TestRegularItem):

    def setUp(self):
        super().setUp()
        self.foo_item.sell_in = 10

    def test_item_quality_lowered(self):
        """
        regular item quality degrades by 1
        each update cycle
        when sell in is above 0
        """
        self.foo_item.quality = 10
        self.gilded_rose.update_quality()
        self.assertEqual(self.foo_item.quality, 9)

    def test_item_sell_in_lowered(self):
        """
        sell in drops by one 
        each update cycle
        """
        self.foo_item.quality = 10
        self.gilded_rose.update_quality()
        self.assertEqual(self.foo_item.sell_in, 9)

    def test_item_quality_floor_capped(self):
        """
        regular item quality cannot drop below zero 
        """
        self.foo_item.quality = 0
        self.gilded_rose.update_quality()
        self.assertEqual(self.foo_item.quality, 0)


class AfterSellBy(TestRegularItem):

    def setUp(self):
        super().setUp()
        self.foo_item.sell_in = 0

    def test_item_quality_lowered(self):
        """
        regular item quality degrades by 2
        each update cycle
        when sell in is above 0
        """
        self.foo_item.quality = 10
        self.gilded_rose.update_quality()
        self.assertEqual(self.foo_item.quality, 8)

    def test_item_quality_floor_capped(self):
        """
        regular item quality cannot drop below zero 
        """
        self.foo_item.quality = 0
        self.gilded_rose.update_quality()
        self.assertEqual(self.foo_item.quality, 0)