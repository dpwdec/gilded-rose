from unittest import TestCase
from unittest import mock
from src.regular_item import RegularItem

class TestRegularItem(TestCase):

    def test_update_sell_in(self):
        regular_item = RegularItem('foo', 10, 0)
        regular_item.update_sell_in()
        self.assertEqual(regular_item.sell_in, 9)
