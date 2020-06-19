# -*- coding: utf-8 -*-
from unittest import TestCase
from unittest import mock

from src.gilded_rose import GildedRose

class TestRegularItem(TestCase):

    def setUp(self):
        self.sulfuras = mock.Mock()
        self.sulfuras.name = "Sulfuras, Hand of Ragnaros"
        self.sulfuras.quality = 50
        self.sulfuras.sell_in = 50
        items = [self.sulfuras]
        self.gilded_rose = GildedRose(items)
        self.gilded_rose.update_quality()

    def test_quality_does_not_change(self):
        """
        Legendary items do not degrade in quality
        """
        self.assertEqual(self.sulfuras.quality, 50)

    def test_sell_in_does_not_change(self):
        """
        Legendary items never have to be sold
        """
        self.assertEqual(self.sulfuras.sell_in, 50)