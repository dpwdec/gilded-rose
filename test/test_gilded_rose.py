# -*- coding: utf-8 -*-
from unittest import TestCase
from unittest import mock

from src.gilded_rose import GildedRose
from src.item import Item
from src.regular_item import RegularItem

class GildedRoseTest(TestCase):
    pass
    # what should I testing
    # if I pass in a an item with a name foo
    # and a quality > 0
    # i expect that that mock will have its quality
    # reduced by -1 at some point in the execution of updating
    # I could extend the item class, wh

class TestRegularItemBeforeSellBy(GildedRoseTest):

    def setUp(self):
        self.foo_item = mock.Mock()
        self.foo_item.quality = 10
        self.foo_item.sell_in = 10
        self.foo_item.name = "Foo"
        items = [self.foo_item]
        self.gilded_rose = GildedRose(items)

    def test_item_quality_lowered(self):
        self.gilded_rose.update_quality()
        self.assertEqual(self.foo_item.quality, 9)

    def test_item_sell_in_lowered(self):
        self.gilded_rose.update_quality()
        self.assertEqual(self.foo_item.sell_in, 9)

class TestRegularItemAfterSellBY(GildedRoseTest):

        def setUp(self):
            self.foo_item = mock.Mock()
            self.foo_item.quality = 10
            self.foo_item.sell_in = 0
            self.foo_item.name = "Foo"
            items = [self.foo_item]
            self.gilded_rose = GildedRose(items)

        def test_item_quality_lowered(self):
            self.gilded_rose.update_quality()
            self.assertEqual(self.foo_item.quality, 8)

class LegacyItemTests(GildedRoseTest):

    def _item_comparison(self):
        old_foo_item = Item("Foo", 10, 10)
        old_items = [old_foo_item]
        new_foo_item = RegularItem("Foo", 10, 10)
        gilded_rose = GildedRose(old_items)
        gilded_rose.update_quality()
        new_foo_item.update_quality()
        self.assertEqual(old_items[0].quality, new_foo_item.quality)

    def _item_quality_lowered_by_one(self):
        pass
        foo_item = mock.Mock()
        foo_item.name = "foo"

        number_mock = mock.MagicMock()

        __mock_gt__ = mock.Mock()
        __mock_gt__.return_value = True
        
        __mock_sub__ = mock.MagicMock()
        __mock_sub__.return_value = number_mock

        __mock_lt_ = mock.MagicMock()
        __mock_lt_.return_value = False
        
        number_mock.__gt__ = __mock_gt__
        number_mock.__lt__ = __mock_lt_
        number_mock.__sub__ = __mock_sub__

        foo_item.quality = number_mock
        foo_item.sell_in = number_mock

        items = [foo_item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        foo_item.quality.__sub__.assert_called_with(1)


    
