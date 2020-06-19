from unittest import TestCase
from unittest import mock
from src.regular_item import RegularItem

class TestRegularItem(TestCase):

    def test_update_sell_in(self):
        regular_item = RegularItem('foo', 10, 10)
        regular_item.update_sell_in()
        self.assertEqual(regular_item.sell_in, 9)

    def test_update_quality(self):
        regular_item = RegularItem('foo', 10, 10)
        regular_item.update_quality()
        self.assertEqual(regular_item.quality, 9)

    def test_update_quality_capped_at_zero(self):
        """
        a regular items quality cannot go below 0
        """
        regular_item = RegularItem('foo', 10, 0)
        regular_item.update_quality()
        self.assertEqual(regular_item.quality, 0)

    def test_update_quality_after_sell_in(self):
        """
        a regular items quality degrades twice as fast
        when sell_in is < 0
        """
        regular_item = RegularItem('foo', 0, 10)
        regular_item.update_quality()
        self.assertEqual(regular_item.quality, 8)
